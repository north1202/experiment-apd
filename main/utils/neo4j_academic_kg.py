# -*- coding: utf-8 -*-
"""学术出版 AI 伦理知识图谱：在 PyCharm 中右键 Run 即可。

准备：Python 3.10+；在同一解释器的终端执行 python -m pip install "neo4j>=5.28,<7"
将本脚本与 Literature_Metadata.csv、Summary_Observations.csv 放在同一文件夹。
另外四张拆分表如在同一文件夹，会一并检查是否与总表一致。
确认下方 URI、USERNAME、PASSWORD、DATABASE，再运行。Aura 用户名应使用实例连接凭证中的
用户名，不是 Aura 网站登录邮箱。密码只填在本机。
DATABASE 是连接详情中的数据库名；Aura 常见默认值为 neo4j，实例卡片的显示名称不一定是数据库名。

--dry-run：仅检查数据并生成本地图，不连接数据库。
--data-dir 路径：临时指定 CSV 文件夹。

不删除原数据库节点；使用 AcademicKG 标签及内容版本标识隔离本次图谱。
同样的数据重复运行使用 MERGE，不叠加节点、关系或权重。
数据内容变化会生成新版本，查询时应使用本次输出的 dataset_id。
数量基于所提供记录，重复内容只提示，绝不自动删除。
"""

from pathlib import Path
from collections import Counter, defaultdict
from itertools import combinations
from contextlib import contextmanager
import argparse
import csv
import hashlib
import html
import io
import json
import math
import os
import sys
import threading
import time

# ====================== 只需先修改这里 ======================
DATA_DIR = Path(__file__).resolve().parent

NEO4J_URI = ""  # 核对是否仍为你的实例地址
NEO4J_USERNAME = ""    # 以 Aura 实例连接凭证为准；不是网站登录邮箱
NEO4J_PASSWORD = ""            # 在这里填写数据库密码，或设置 NEO4J_PASSWORD 环境变量
NEO4J_DATABASE = ""       # 以连接详情为准；Aura常见默认值，不一定等于实例显示名称
DRY_RUN = False               # True：仅检查与预览；False：实际导入 Neo4j
BATCH_SIZE = 200
EXPORT_HTML = True
# ==========================================================

HARM_NAMES = {
    "Allocative Harms": "分配伤害",
    "Representational Harms": "表征伤害",
    "Quality-of-Service Harms": "服务质量伤害",
    "Interpersonal Harms": "人际伤害",
    "Social System Harms": "社会系统伤害",
}
DOMAINS = {
    "Scenario_Submission": "写作、投稿与披露",
    "Scenario_Screening": "编辑技术预审",
    "Scenario_PeerReview": "同行评议",
    "Scenario_MacroPolicy": "宏观评价与制度治理",
}
ACTORS = {
    "Stakeholder_Authors": "作者与研究者",
    "Stakeholder_Publishers": "出版者与编辑",
    "Stakeholder_Reviewers": "审稿人",
    "Stakeholder_Institutions": "机构",
    "Stakeholder_AIDevs": "AI开发与工具供给方",
}
# 下面是显示用的主题简称；类别编号与源 CSV 保持一致，可自行调整简称。
TOPICS = {
    "class0": "高校诚信与机构治理", "class1": "科研中LLM的伦理边界",
    "class2": "作者身份与人机协作", "class3": "学术群体的使用与认知",
    "class4": "AI写作与使用披露", "class5": "科研诚信与学术不端",
    "class6": "AI伦理教育", "class7": "不当使用的个体因素",
    "class8": "AI文本检测", "class9": "机构合规与诚信支持",
    "class10": "编辑质检与同行评议", "class11": "教育生态与伦理响应",
}
BIN = list(DOMAINS) + list(ACTORS)
META_FIELDS = ["Literature_ID", "Literature_Title", "Literature_Doi",
               "Publication_Year", "BERTopic_Cluster"]
OBS_FIELDS = ["Record_ID", "Literature_ID", "Social_Harm_Type",
              "Manifestation_Text", "Mitigation_Text"] + BIN
PARTS = {
    "HarmType_Observations": ["Social_Harm_Type"],
    "ProblemsAndSolutions_Observations": ["Manifestation_Text", "Mitigation_Text"],
    "PublishingScenario_Observations": list(DOMAINS),
    "Stakeholder_Observations": list(ACTORS),
}
LABELS = {"Paper", "Observation", "Topic", "HarmType", "GovernanceDomain", "Stakeholder"}
REL_TYPES = {"HAS_OBSERVATION", "IN_TOPIC", "HAS_HARM", "IN_DOMAIN", "INVOLVES", "CO_OCCURS"}


def log(message):
    print(time.strftime("[%H:%M:%S] ") + str(message), flush=True)


@contextmanager
def heartbeat(message):
    """长操作期间显示等待信息，避免误以为程序卡住。"""
    stopped = threading.Event()
    def pulse():
        while not stopped.wait(8):
            log(message + "（仍在等待，尚未报告成功）")
    worker = threading.Thread(target=pulse, daemon=True)
    worker.start()
    try:
        yield
    finally:
        stopped.set()
        worker.join(timeout=1)


def read_csv(path, fields):
    if not path.is_file():
        raise FileNotFoundError(f"找不到 {path}\n请将 CSV 与脚本放在一起，或修改 DATA_DIR。")
    raw = path.read_bytes()
    for encoding in ("utf-8-sig", "gb18030"):
        try:
            text = raw.decode(encoding, errors="strict")
            break
        except UnicodeDecodeError:
            continue
    else:
        raise ValueError(f"{path.name} 无法按 UTF-8 或 GB18030 无损读取。")
    reader = csv.DictReader(io.StringIO(text, newline=""))
    missing = set(fields) - set(reader.fieldnames or [])
    if missing:
        raise ValueError(f"{path.name} 缺少列：{sorted(missing)}")
    rows = list(reader)
    if not rows:
        raise ValueError(f"{path.name} 没有数据行。")
    if any(None in row or any(v is None for v in row.values()) for row in rows):
        raise ValueError(f"{path.name} 有列数不一致的行，请检查 CSV 的引号和分隔符。")
    log(f"读取 {path.name}：{len(rows)} 行，编码 {encoding}")
    return rows


def index_rows(rows, key, filename):
    index = {}
    for line, row in enumerate(rows, 2):
        value = row[key]
        if not value or value != value.strip():
            raise ValueError(f"{filename} 第{line}行 {key} 为空或含首尾空格。")
        if value in index:
            raise ValueError(f"{filename} 有重复主键 {key}={value}，已停止，未合并这些行。")
        index[value] = row
    return index


def load_data(folder):
    papers = read_csv(folder / "Literature_Metadata.csv", META_FIELDS)
    observations = read_csv(folder / "Summary_Observations.csv", OBS_FIELDS)
    pm = index_rows(papers, "Literature_ID", "Literature_Metadata.csv")
    om = index_rows(observations, "Record_ID", "Summary_Observations.csv")
    for p in papers:
        if p["BERTopic_Cluster"] not in TOPICS:
            raise ValueError(f"未知主题：{p['BERTopic_Cluster']}；请更新 TOPICS 对照表。")
        try:
            int(p["Publication_Year"])
        except ValueError:
            raise ValueError(f"{p['Literature_ID']} 的年份不是整数。") from None
    for r in observations:
        if r["Literature_ID"] not in pm:
            raise ValueError(f"{r['Record_ID']} 的文献ID不存在于元数据表。")
        if r["Social_Harm_Type"] not in HARM_NAMES:
            raise ValueError(f"{r['Record_ID']} 的伤害类型不在五类规范名称中。")
        if any(r[k] not in ("0", "1") for k in BIN):
            raise ValueError(f"{r['Record_ID']} 有不是0/1的标签值。")
    for name, fields in PARTS.items():
        path = folder / (name + ".csv")
        if not path.exists():
            log(f"可选分表未提供：{path.name}；继续使用综合观察表。")
            continue
        rows = read_csv(path, ["Record_ID", "Literature_ID"] + fields)
        part = index_rows(rows, "Record_ID", name)
        if set(part) != set(om):
            raise ValueError(f"{name} 的 Record_ID 集合与综合表不同。")
        for rid, r in part.items():
            if any(r[k] != om[rid][k] for k in ["Literature_ID"] + fields):
                raise ValueError(f"{name} 的 {rid} 与综合表不一致，停止导入。")
    duplicates = defaultdict(list)
    for r in observations:
        duplicates[tuple(r[k] for k in OBS_FIELDS if k != "Record_ID")].append(r["Record_ID"])
    groups = [ids for ids in duplicates.values() if len(ids) > 1]
    missing_mitigation = sum(not r["Mitigation_Text"].strip() for r in observations)
    no_obs = sorted(set(pm) - {r["Literature_ID"] for r in observations})
    log(f"内容重复冗余 {sum(len(g)-1 for g in groups)} 条：保留各自 Record_ID，不自动删除。")
    log(f"缓解措施缺失 {missing_mitigation} 条；无观察记录的文献 {len(no_obs)} 篇。")
    return papers, observations, {"duplicate_record_groups": groups,
                                 "missing_mitigation": missing_mitigation,
                                 "papers_without_observations": no_obs}


def build_graph(papers, observations):
    # 按ID排序后哈希：文件换编码/改行顺序不产生新版本；内容改变则新建版本。
    canonical = [sorted(papers, key=lambda r: r["Literature_ID"]),
                 sorted(observations, key=lambda r: r["Record_ID"])]
    digest = hashlib.sha256(json.dumps(canonical, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
    dataset = "academic_" + digest[:16]
    def uid(label, code):
        return dataset + "|" + label + "|" + code
    nodes, edges = {}, []
    def node(label, code, name, **props):
        key = uid(label, code)
        nodes[key] = {"uid": key, "label": label, "props": dict(
            uid=key, dataset_id=dataset, kind=label, code=code, name=name, **props)}
        return key
    def edge(source, relation, target, **props):
        edges.append({"source": source, "type": relation, "target": target,
                      "props": dict(dataset_id=dataset, kind="evidence", **props)})
    for label, names in [("Topic", TOPICS), ("HarmType", HARM_NAMES),
                         ("GovernanceDomain", DOMAINS), ("Stakeholder", ACTORS)]:
        for code, name in names.items():
            node(label, code, name, paper_count=0, supporting_paper_count=0, observation_count=0)
    paper_by_id = {p["Literature_ID"]: p for p in papers}
    paper_obs = Counter(r["Literature_ID"] for r in observations)
    topic_papers = defaultdict(set)
    obs_sets, paper_sets = defaultdict(set), defaultdict(set)
    pair_records, pair_papers = defaultdict(set), defaultdict(set)
    for p in papers:
        lid, topic = p["Literature_ID"], p["BERTopic_Cluster"]
        key = node("Paper", lid, p["Literature_Title"], literature_id=lid,
                   title=p["Literature_Title"], doi=p["Literature_Doi"],
                   year=int(p["Publication_Year"]), topic_code=topic,
                   paper_count=1, observation_count=paper_obs[lid])
        edge(key, "IN_TOPIC", uid("Topic", topic), literature_id=lid)
        topic_papers[uid("Topic", topic)].add(lid)
    for r in observations:
        rid, lid = r["Record_ID"], r["Literature_ID"]
        topic = paper_by_id[lid]["BERTopic_Cluster"]
        key = node("Observation", rid, rid, record_id=rid, literature_id=lid,
                   manifestation=r["Manifestation_Text"], mitigation=r["Mitigation_Text"],
                   mitigation_missing=not bool(r["Mitigation_Text"].strip()),
                   harm_type=r["Social_Harm_Type"], topic_code=topic,
                   paper_count=1, observation_count=1,
                   **{k: int(r[k]) for k in BIN})
        edge(uid("Paper", lid), "HAS_OBSERVATION", key, record_id=rid, literature_id=lid)
        tags = [("Topic", topic), ("HarmType", r["Social_Harm_Type"])]
        tags += [("GovernanceDomain", k) for k in DOMAINS if r[k] == "1"]
        tags += [("Stakeholder", k) for k in ACTORS if r[k] == "1"]
        for label, code in tags:
            target = uid(label, code)
            obs_sets[target].add(rid)
            paper_sets[target].add(lid)
            relation = {"HarmType": "HAS_HARM", "GovernanceDomain": "IN_DOMAIN",
                        "Stakeholder": "INVOLVES"}.get(label)
            if relation:
                edge(key, relation, target, record_id=rid, literature_id=lid)
        # 仅计算不同维度之间的共现；每条观察对同一个类别对只计一次。
        for (la, ca), (lb, cb) in combinations(tags, 2):
            if la == lb:
                continue
            pair = tuple(sorted((uid(la, ca), uid(lb, cb))))
            pair_records[pair].add(rid)
            pair_papers[pair].add(lid)
    for key, n in nodes.items():
        if n["label"] not in ("Paper", "Observation"):
            n["props"]["observation_count"] = len(obs_sets[key])
            n["props"]["supporting_paper_count"] = len(paper_sets[key])
            n["props"]["paper_count"] = len(topic_papers[key] if n["label"] == "Topic" else paper_sets[key])
    for (source, target), records in sorted(pair_records.items()):
        edges.append({"source": source, "type": "CO_OCCURS", "target": target,
                      "props": {"dataset_id": dataset, "kind": "cooccurrence",
                                "observation_count": len(records),
                                "paper_count": len(pair_papers[(source, target)]),
                                "record_ids": sorted(records)}})
    return dataset, list(nodes.values()), edges


def local_case(observations):
    rows = [r for r in observations if r["Scenario_PeerReview"] == "1"
            and r["Stakeholder_Publishers"] == "1"]
    return {"observations": len(rows), "papers": len({r["Literature_ID"] for r in rows})}


def import_graph(nodes, edges, dataset, expected_case):
    try:
        from neo4j import GraphDatabase, unit_of_work
    except ImportError:
        raise RuntimeError('请在PyCharm当前解释器的终端运行：python -m pip install "neo4j>=5.28,<7"') from None
    password = NEO4J_PASSWORD or os.environ.get("NEO4J_PASSWORD", "")
    if not password:
        raise ValueError("请在脚本配置区填写 NEO4J_PASSWORD，再运行；不要把密码发到聊天中。")
    if BATCH_SIZE < 1:
        raise ValueError("BATCH_SIZE 必须大于0。")

    @unit_of_work(timeout=45)
    def write(tx, query, batch):
        result = tx.run(query, rows=batch)
        result.consume()

    def batches(session, query, rows, title):
        for start in range(0, len(rows), BATCH_SIZE):
            batch = rows[start:start + BATCH_SIZE]
            with heartbeat(f"正在提交 {title} 批次"):
                session.execute_write(write, query, batch)
            log(f"{title}：{start + len(batch)}/{len(rows)} 已提交")

    log("连接Neo4j并校验认证……")
    with GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, password),
                              connection_timeout=10, connection_acquisition_timeout=20,
                              max_transaction_retry_time=15, max_connection_pool_size=4) as driver:
        with heartbeat("正在验证数据库连接"):
            driver.verify_connectivity()
        with driver.session(database=NEO4J_DATABASE) as session:
            session.run("RETURN 1 AS ok").consume()
            log("连接和数据库访问通过。创建本脚本使用的唯一约束……")
            session.run("CREATE CONSTRAINT academic_kg_uid IF NOT EXISTS "
                        "FOR (n:AcademicKG) REQUIRE n.uid IS UNIQUE").consume()
            by_label, by_type = defaultdict(list), defaultdict(list)
            for row in nodes:
                by_label[row["label"]].append(row)
            for row in edges:
                by_type[row["type"]].append(row)
            for label, rows in by_label.items():
                assert label in LABELS
                query = ("UNWIND $rows AS row MERGE (n:AcademicKG {uid: row.uid}) "
                         f"SET n:{label} SET n += row.props")
                batches(session, query, rows, "节点 " + label)
            for relation, rows in by_type.items():
                assert relation in REL_TYPES
                query = ("UNWIND $rows AS row "
                         "MATCH (a:AcademicKG {uid: row.source}) "
                         "MATCH (b:AcademicKG {uid: row.target}) "
                         f"MERGE (a)-[r:{relation}]->(b) SET r = row.props")
                batches(session, query, rows, "关系 " + relation)
            log("导入批次完成，开始核对当前版本的节点、关系和查询结果……")
            actual_nodes = {r["kind"]: r["n"] for r in session.run(
                "MATCH (n:AcademicKG {dataset_id:$d}) RETURN n.kind AS kind, count(n) AS n", d=dataset)}
            actual_edges = {r["type"]: r["n"] for r in session.run(
                "MATCH (a:AcademicKG {dataset_id:$d})-[r]->(b:AcademicKG {dataset_id:$d}) "
                "RETURN type(r) AS type, count(r) AS n", d=dataset)}
            if actual_nodes != dict(Counter(r["label"] for r in nodes)):
                raise RuntimeError(f"节点核验不一致：{actual_nodes}；未报告导入成功。")
            if actual_edges != dict(Counter(r["type"] for r in edges)):
                raise RuntimeError(f"关系核验不一致：{actual_edges}；未报告导入成功。")
            result = session.run(CASE_QUERY, d=dataset).single()
            actual_case = {"observations": result["observations"], "papers": result["papers"]}
            if actual_case != expected_case:
                raise RuntimeError(f"数据库查询结果 {actual_case} 与本地 {expected_case} 不一致。")
            # 核验所有类别节点和共现边的计数，而不仅仅核验总数。
            wanted = {n["uid"]: (n["props"]["paper_count"], n["props"]["observation_count"])
                      for n in nodes if n["label"] not in ("Paper", "Observation")}
            actual = {r["uid"]: (r["p"], r["o"]) for r in session.run(
                "MATCH (n:AcademicKG {dataset_id:$d}) WHERE NOT n:Paper AND NOT n:Observation "
                "RETURN n.uid AS uid,n.paper_count AS p,n.observation_count AS o", d=dataset)}
            if actual != wanted:
                raise RuntimeError("类别节点的文献/观察数量核验失败。")
            expected_weights = {(e["source"],e["target"]): (e["props"]["paper_count"],e["props"]["observation_count"])
                                for e in edges if e["type"] == "CO_OCCURS"}
            actual_weights = {(r["a"],r["b"]): (r["p"],r["o"]) for r in session.run(
                "MATCH (a:AcademicKG {dataset_id:$d})-[r:CO_OCCURS]->(b:AcademicKG {dataset_id:$d}) "
                "RETURN a.uid AS a,b.uid AS b,r.paper_count AS p,r.observation_count AS o", d=dataset)}
            if actual_weights != expected_weights:
                raise RuntimeError("共现关系权重核验失败。")
            log(f"核验通过！同行评议＋出版者/编辑：{actual_case['observations']} 条观察，{actual_case['papers']} 篇文献。")
            return {"status": "verified", "node_counts": actual_nodes,
                    "relationship_counts": actual_edges, "case_query": actual_case}


CASE_QUERY = """MATCH (p:AcademicKG:Paper {dataset_id:$d})-[:HAS_OBSERVATION]->(o:AcademicKG:Observation)
WHERE EXISTS { MATCH (o)-[:IN_DOMAIN]->(:AcademicKG:GovernanceDomain {code:'Scenario_PeerReview'}) }
  AND EXISTS { MATCH (o)-[:INVOLVES]->(:AcademicKG:Stakeholder {code:'Stakeholder_Publishers'}) }
RETURN count(DISTINCT o) AS observations, count(DISTINCT p) AS papers"""


def write_queries(out, dataset):
    # dataset来自固定前缀和十六进制hash，不含用户提供的查询片段。
    literal = "'" + dataset + "'"
    text = f"""// 每次复制一个查询到 Neo4j 的 Query/Browser 执行。
// 所有查询限定当前数据版本：{dataset}

// 1. 概览：线条上的 paper_count / observation_count 是共现数量。
MATCH (a:AcademicKG {{dataset_id:{literal}}})-[r:CO_OCCURS]->(b:AcademicKG {{dataset_id:{literal}}})
RETURN a,r,b;

// 2. 查回 REC_0001 的来源、主题与标签，可改成其他 Record_ID。
MATCH (p:AcademicKG:Paper {{dataset_id:{literal}}})-[s:HAS_OBSERVATION]->(o:AcademicKG:Observation {{record_id:'REC_0001'}})
MATCH (p)-[pt:IN_TOPIC]->(t:AcademicKG:Topic)
OPTIONAL MATCH (o)-[r:HAS_HARM|IN_DOMAIN|INVOLVES]->(c:AcademicKG)
RETURN p,s,o,pt,t,r,c;

// 3. 查看原始文本和来源 DOI。
MATCH (p:AcademicKG:Paper {{dataset_id:{literal}}})-[:HAS_OBSERVATION]->(o:AcademicKG:Observation)
RETURN o.record_id AS Record_ID,p.literature_id AS Literature_ID,p.title AS title,
       p.doi AS DOI,o.manifestation AS manifestation,o.mitigation AS mitigation
ORDER BY Record_ID LIMIT 50;

// 4. 主题文献数与观察数；Topic的paper_count包括无观察记录的文献。
MATCH (t:AcademicKG:Topic {{dataset_id:{literal}}})
RETURN t.code AS topic,t.name AS name,t.paper_count AS papers,
       t.supporting_paper_count AS papers_with_observations,t.observation_count AS observations
ORDER BY papers DESC;

// 5. 与论文一致的最小应用实例。
{CASE_QUERY.replace('$d',literal)};

// 6. 追溯一个类别对的共现证据，以下以同行评议—出版者/编辑为例。
MATCH (a:AcademicKG:GovernanceDomain {{dataset_id:{literal},code:'Scenario_PeerReview'}})
      -[r:CO_OCCURS]-(b:AcademicKG:Stakeholder {{dataset_id:{literal},code:'Stakeholder_Publishers'}})
UNWIND r.record_ids AS rid
MATCH (p:AcademicKG:Paper {{dataset_id:{literal}}})-[:HAS_OBSERVATION]->
      (o:AcademicKG:Observation {{dataset_id:{literal},record_id:rid}})
RETURN o.record_id AS Record_ID,p.literature_id AS Literature_ID,p.doi AS DOI,
       o.manifestation AS manifestation,o.mitigation AS mitigation
ORDER BY Record_ID;
"""
    (out / "Neo4j_查询示例.cypher").write_text(text, encoding="utf-8")


def export_html(out, nodes, edges, status):
    # 全部资源内嵌；只展示26个类别，完整证据保留在Neo4j及查询示例中。
    groups = ["Topic", "HarmType", "GovernanceDomain", "Stakeholder"]
    colors = {"Topic":"#3b82f6", "HarmType":"#ef8354", "GovernanceDomain":"#36a398", "Stakeholder":"#9666c3"}
    categories = [dict(n["props"], group=n["label"], color=colors[n["label"]])
                  for n in nodes if n["label"] in groups]
    for g in groups:
        members = [n for n in categories if n["group"] == g]
        if g == "Topic":
            members.sort(key=lambda n:int(n["code"][5:]))
        for i,n in enumerate(members):
            n.update(x=130+groups.index(g)*320, y=90+(i+.5)*890/len(members))
    links = [dict(e["props"],source=e["source"],target=e["target"])
             for e in edges if e["type"] == "CO_OCCURS"]
    payload = json.dumps({"nodes":categories,"edges":links}, ensure_ascii=False).replace("<","\\u003c").replace(">","\\u003e").replace("&","\\u0026")
    page = HTML.replace("__DATA__",payload).replace("__STATUS__",html.escape(status))
    (out / "知识图谱_数量概览.html").write_text(page,encoding="utf-8")


HTML = r'''<!doctype html><html lang="zh"><meta charset="utf-8">
<title>学术出版AI伦理：类别共现图</title>
<style>body{margin:24px;background:#f5f7fb;color:#233047;font:15px system-ui,sans-serif}h1{font-size:24px}p{line-height:1.7}select,input,button{padding:7px;margin:4px}svg{background:white;border:1px solid #dbe2ec;max-width:100%;height:auto}#tip{white-space:pre-wrap;line-height:1.6;padding:14px;background:white;border-left:4px solid #3b82f6;min-height:75px}text{pointer-events:none}label{display:inline-block}</style>
<h1>学术出版AI伦理：类别共现图</h1><p>__STATUS__</p>
<p>节点面积随数量增加；线宽随共现数量增加。主题的文献数包含未产生观察记录的文献，其他类别按关联观察的来源文献去重。只绘制不同维度之间的共现；同一文献可同时支持多条边。悬停或点击查看计数，双击边查看对应Record_ID，再到Neo4j查询来源。</p>
<label>节点大小 <select id="nm"><option value="paper_count">文献数量</option><option value="observation_count">观察记录数量</option></select></label>
<label>线条粗细 <select id="em"><option value="observation_count">共现观察数量</option><option value="paper_count">共现文献数量</option></select></label>
<label>至少共现 <input id="min" type="number" value="1" min="1" max="10000" style="width:70px"></label>
<button id="save">保存当前图为SVG</button><div id="tip">蓝色：主题；橙色：伤害；绿色：治理环节；紫色：治理主体。</div>
<svg id="graph" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1250 1040"></svg>
<script>
const data=__DATA__, svg=document.getElementById('graph'),tip=document.getElementById('tip');
const byId=new Map(data.nodes.map(n=>[n.uid,n]));
function el(tag,attrs,text){let x=document.createElementNS('http://www.w3.org/2000/svg',tag);for(let k in attrs)x.setAttribute(k,attrs[k]);if(text!==undefined)x.textContent=text;svg.appendChild(x);return x;}
function render(){svg.replaceChildren();let nm=document.getElementById('nm').value,em=document.getElementById('em').value,min=Math.max(1,Number(document.getElementById('min').value)||1);
let nmTitle=nm==='paper_count'?'文献数量':'观察数量',emTitle=em==='paper_count'?'共现文献':'共现观察';
el('text',{x:25,y:25,'font-size':15,fill:'#233047'},'节点：'+nmTitle+'；线宽：'+emTitle+'；显示阈值 ≥ '+min);
['主题','伤害类型','出版治理环节','治理主体'].forEach((s,i)=>el('text',{x:130+i*320,y:64,'text-anchor':'middle','font-size':19,fill:'#233047'},s));
let visible=data.edges.filter(e=>e[em]>=min), maxE=Math.max(1,...visible.map(e=>e[em])),maxN=Math.max(1,...data.nodes.map(n=>n[nm]));
for(let e of visible){let a=byId.get(e.source),b=byId.get(e.target),line=el('line',{x1:a.x,y1:a.y,x2:b.x,y2:b.y,stroke:'#64748b','stroke-opacity':.14,'stroke-width':.5+7.5*e[em]/maxE});
const show=()=>{line.setAttribute('stroke-opacity',.9);tip.textContent=a.name+' ↔ '+b.name+'\n共现观察：'+e.observation_count+'；去重文献：'+e.paper_count+'\n双击此线查看Record_ID。';};line.addEventListener('mouseenter',show);line.addEventListener('click',show);line.addEventListener('mouseleave',()=>line.setAttribute('stroke-opacity',.14));line.addEventListener('dblclick',()=>tip.textContent=a.name+' ↔ '+b.name+'\nRecord_ID：'+e.record_ids.join(', '));}
for(let n of data.nodes){let radius=Math.max(5,32*Math.sqrt(n[nm]/maxN));let circle=el('circle',{cx:n.x,cy:n.y,r:radius,fill:n.color,stroke:'white','stroke-width':2});
const show=()=>tip.textContent=n.code+'｜'+n.name+'\n文献数量：'+n.paper_count+'；有观察支持的文献：'+n.supporting_paper_count+'；观察数量：'+n.observation_count;circle.addEventListener('mouseenter',show);circle.addEventListener('click',show);
let label=n.group==='Topic'?n.code+' '+n.name:n.name;el('text',{x:n.x,y:n.y+radius+16,'text-anchor':'middle','font-size':12,fill:'#233047'},label);el('text',{x:n.x,y:n.y+4,'text-anchor':'middle','font-size':11,fill:'white'},n[nm]);}
el('text',{x:25,y:1020,'font-size':13,fill:'#475569'},'显示 '+visible.length+' / '+data.edges.length+' 条类别共现边；计数包含源表保留的重复内容记录。');}
['nm','em','min'].forEach(id=>document.getElementById(id).addEventListener('input',render));
document.getElementById('save').onclick=()=>{let b=new Blob([new XMLSerializer().serializeToString(svg)],{type:'image/svg+xml;charset=utf-8'}),u=URL.createObjectURL(b),a=document.createElement('a');a.href=u;a.download='学术出版AI伦理_类别共现图.svg';a.click();setTimeout(()=>URL.revokeObjectURL(u),1000);};render();
</script></html>'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="仅本地核验，不连接Neo4j")
    parser.add_argument("--data-dir", type=Path, default=DATA_DIR)
    args = parser.parse_args()
    dry_run = DRY_RUN or args.dry_run
    log("1/4 读取并核验CSV；源文件不会被修改。")
    papers, observations, audit = load_data(args.data_dir)
    dataset, nodes, edges = build_graph(papers, observations)
    node_counts = dict(Counter(n["label"] for n in nodes))
    edge_counts = dict(Counter(e["type"] for e in edges))
    core = sum(e["type"] != "CO_OCCURS" for e in edges)
    case = local_case(observations)
    log(f"2/4 已生成图结构：{len(nodes)} 节点；{core} 基础关系；{len(edges)-core} 共现关系。")
    log(f"dataset_id = {dataset}")
    log(f"本地应用查询：{case['observations']} 条记录、{case['papers']} 篇文献。")
    out = args.data_dir / "neo4j_output" / dataset
    out.mkdir(parents=True, exist_ok=True)
    report = {"dataset_id": dataset, "status": "local_only", "node_counts": node_counts,
              "relationship_counts": edge_counts, "evidence_relationships": core,
              "case_query": case, "audit": audit}
    report_path = out / "导入核验报告.json"
    report_path.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
    write_queries(out, dataset)
    if EXPORT_HTML:
        export_html(out,nodes,edges,"本地CSV预览；尚未验证Neo4j导入。")
    if not dry_run:
        log("3/4 开始实际导入。每个批次提交后显示进度。")
        try:
            verified = import_graph(nodes,edges,dataset,case)
        except Exception as exc:
            report["status"] = "failed_or_incomplete"
            report["error_type"] = type(exc).__name__  # 不把密码或连接异常全文写入报告
            report_path.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
            raise
        report["status"] = "verified"
        report["database_validation"] = verified
        report_path.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
        if EXPORT_HTML:
            export_html(out,nodes,edges,"来源：本地CSV。Neo4j中当前版本的节点、关系、计数及应用查询已核验通过。")
    else:
        log("3/4 DRY_RUN：跳过数据库连接与导入，仅生成本地结果。")
    log("4/4 完成。输出目录：" + str(out.resolve()))
    log("打开 知识图谱_数量概览.html 查看节点大小和线条粗细；可保存SVG。")
    log("打开 Neo4j_查询示例.cypher，逐个复制查询到网页 Query 查看完整来源关系。")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log("已中断。已提交批次可能保留；相同数据重新运行可继续，不累计权重。")
        sys.exit(130)
    except Exception as exc:
        code = getattr(exc, "code", "") or ""
        kind = type(exc).__name__
        log("运行失败：" + kind)
        if kind == "AuthError" or "Unauthorized" in code:
            log("认证失败：请核对数据库URI、用户名和数据库密码；它们不是Aura网站登录凭证。")
        elif "DatabaseNotFound" in code:
            log("数据库名不存在：检查 NEO4J_DATABASE；Aura通常使用 neo4j，不是实例显示名称。")
        elif kind in ("ServiceUnavailable", "SessionExpired", "ConnectionAcquisitionTimeoutError"):
            log("连接或会话失败：检查实例是否运行、网络是否可达及URI是否正确；稍后可重新运行。")
        elif kind in ("FileNotFoundError", "ValueError", "RuntimeError"):
            log(str(exc))
        else:
            log("数据库错误码：" + (code or "无"))
            log("请检查驱动版本与账号建约束/写入权限。未报告导入成功。")
        sys.exit(1)
