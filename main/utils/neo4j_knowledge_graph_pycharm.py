"""
AI 学术出版社会技术伤害知识图谱
PyCharm 直接运行版

适配你的 Excel：
1. Sheet1：772 条观察记录、19 列
2. 文献名称映射：244 篇文献

使用方法：
1. 把本文件复制到 PyCharm 项目中，或直接在 PyCharm 中打开。
2. 检查 EXCEL_BASE_PATH 是否与你电脑上的 Excel 路径一致。
3. 点击 PyCharm 的绿色运行按钮。
4. 程序会在运行窗口中要求输入 Neo4j 数据库密码。

注意：
- 不要把 Neo4j 密码写进代码。
- AuraDB 的登录邮箱不一定是数据库用户名；默认用户名通常是 neo4j。
- academic-publishing-kg 是你创建的实例名称，默认数据库名通常是 neo4j。
"""

from __future__ import annotations

import hashlib
import os
import re
from pathlib import Path
from typing import Any, Iterable

import pandas as pd
from neo4j import GraphDatabase


# =============================================================================
# 一、只需要检查这里的配置
# =============================================================================

# 你提供的文件位置没有写扩展名，因此程序会自动尝试：
# pdf_Literature_ID、pdf_Literature_ID.xlsx、pdf_Literature_ID.xls
EXCEL_BASE_PATH = Path(
    r"E:\work\experiment\GraphragTest-main\ragtest\utils\pdf_Literature_ID"
)

OBSERVATION_SHEET = "Sheet1"
LITERATURE_SHEET = "文献名称映射"

# 下面三项直接使用你的 AuraDB 正确连接配置。
# 不再读取 PyCharm 中旧的环境变量，避免旧配置覆盖正确值。
# 其中 academic-publishing-kg 是实例名称，不是数据库名称。
NEO4J_URI = "neo4j+s://75847bff.databases.neo4j.io"
NEO4J_USERNAME = "75847bff"
NEO4J_DATABASE = "75847bff"

# 第一次运行时保持 False 即可。只有需要删除当前数据库全部数据时才改为 True。
# 警告：True 会删除当前数据库中的全部节点和关系。
CLEAR_DATABASE = False


# =============================================================================
# 二、Excel 文件定位
# =============================================================================

def locate_excel_file() -> Path:
    """自动寻找用户提供的 Excel 文件。"""
    candidates = [
        EXCEL_BASE_PATH,
        EXCEL_BASE_PATH.with_suffix(".xlsx"),
        EXCEL_BASE_PATH.with_suffix(".xls"),
    ]

    for candidate in candidates:
        if candidate.is_file():
            return candidate

    message = "\n".join(str(item) for item in candidates)
    raise FileNotFoundError(
        "找不到 Excel 文件。程序尝试过以下路径：\n" + message +
        "\n请检查 EXCEL_BASE_PATH 是否与电脑中的文件路径一致。"
    )


# =============================================================================
# 三、通用处理函数
# =============================================================================

def clean_text(value: Any) -> str:
    """清除 Excel 中的空值、换行和多余空格。"""
    if value is None or pd.isna(value):
        return ""
    text = str(value).replace("\r", " ").replace("\n", " ")
    return re.sub(r"\s+", " ", text).strip()


def stable_id(prefix: str, value: str) -> str:
    """根据文本生成稳定 ID，避免重复导入时生成重复节点。"""
    digest = hashlib.sha1(value.encode("utf-8")).hexdigest()[:16]
    return f"{prefix}_{digest}"


def normalize_binary(value: Any) -> bool:
    """兼容 0/1、True/False、Yes/No 和中文是/否。"""
    if value is None or pd.isna(value):
        return False
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return value != 0

    text = clean_text(value).lower()
    return text in {
        "1", "1.0", "true", "yes", "y", "是", "有", "涉及", "included"
    }


def chunks(items: list[dict[str, Any]], size: int) -> Iterable[list[dict[str, Any]]]:
    for start in range(0, len(items), size):
        yield items[start:start + size]


# =============================================================================
# 四、读取你的 Excel
# =============================================================================

def read_excel_data(path: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    """读取 Sheet1 和文献名称映射两个 Sheet。"""
    print(f"正在读取 Excel：{path}")
    observations = pd.read_excel(path, sheet_name=OBSERVATION_SHEET)
    literature_map = pd.read_excel(path, sheet_name=LITERATURE_SHEET)

    required_observation_columns = [
        "文献名称",
        "BERTopic聚类",
        "社会系统伤害类型",
        "映射场景具体表现",
        "解决/缓解该对策的措施",
        "Literature_ID",
    ]
    missing = [
        column for column in required_observation_columns
        if column not in observations.columns
    ]
    if missing:
        raise KeyError(
            "Sheet1 缺少以下字段：" + ", ".join(missing) +
            "\n当前字段为：" + ", ".join(str(c) for c in observations.columns)
        )

    required_literature_columns = [
        "Literature_ID",
        "BERTopic_Cluster",
        "标准文献名称",
    ]
    missing_literature = [
        column for column in required_literature_columns
        if column not in literature_map.columns
    ]
    if missing_literature:
        raise KeyError(
            "文献名称映射 Sheet 缺少以下字段：" + ", ".join(missing_literature)
        )

    print(f"观察记录：{len(observations)} 条")
    print(f"文献映射：{len(literature_map)} 篇")
    print(f"观察记录对应的文献数：{observations['Literature_ID'].nunique()} 篇")
    return observations, literature_map


def prepare_papers(literature_map: pd.DataFrame) -> list[dict[str, Any]]:
    """准备 244 篇 Paper 节点。"""
    papers: list[dict[str, Any]] = []

    for _, row in literature_map.iterrows():
        literature_id = clean_text(row["Literature_ID"])
        if not literature_id:
            continue

        papers.append(
            {
                "paper_id": literature_id,
                "paper_title": clean_text(row["标准文献名称"]),
                "topic": clean_text(row["BERTopic_Cluster"]),
                "original_title": clean_text(row.get("原始文献名称", "")),
                "topic_code": clean_text(row.get("Topic_Code", "")),
                "relative_path": clean_text(row.get("相对路径", "")),
            }
        )

    if not papers:
        raise ValueError("文献名称映射 Sheet 没有生成有效 Paper 节点。")
    return papers


def prepare_observations(
    observations: pd.DataFrame,
    literature_map: pd.DataFrame,
) -> list[dict[str, Any]]:
    """准备 772 条 Observation 节点及其属性。"""
    paper_title_map = {
        clean_text(row["Literature_ID"]): clean_text(row["标准文献名称"])
        for _, row in literature_map.iterrows()
        if clean_text(row["Literature_ID"])
    }

    scenario_columns = {
        "Submission": "场景_1. 作者投稿与披露",
        "Screening": "场景_2. 编辑技术预审",
        "Peer Review": "场景_3. 专家同行评议",
        "Macro Policy": "场景_4. 宏观评价与体制",
    }

    stakeholder_columns = {
        "Authors & Researchers": "主体_作者与科研人员",
        "Publishers & Editors": "主体_期刊编辑部与出版商",
        "Reviewers": "主体_同行评议专家",
        "Institutions": "主体_高校与科研院所",
        "AI Developers": "主体_AI技术开发商",
    }

    rows: list[dict[str, Any]] = []
    skipped = 0

    for index, source in observations.iterrows():
        paper_id = clean_text(source["Literature_ID"])
        topic = clean_text(source["BERTopic聚类"])
        harm = clean_text(source["社会系统伤害类型"])
        manifestation = clean_text(source["映射场景具体表现"])
        mitigation = clean_text(source["解决/缓解该对策的措施"])

        if not paper_id or not topic or not harm:
            skipped += 1
            continue

        # 当前 Excel 没有 Record_ID，因此按 Excel 行顺序生成 OBS_0001 等编号。
        record_id = f"OBS_{index + 1:04d}"

        scenarios = [
            name
            for name, column in scenario_columns.items()
            if normalize_binary(source[column])
        ]

        stakeholders = [
            name
            for name, column in stakeholder_columns.items()
            if normalize_binary(source[column])
        ]

        rows.append(
            {
                "paper_id": paper_id,
                "paper_title": paper_title_map.get(
                    paper_id, clean_text(source["文献名称"])
                ),
                "record_id": record_id,
                "topic": topic,
                "harm": harm,
                "manifestation": manifestation,
                "manifestation_id": (
                    stable_id("MAN", manifestation) if manifestation else ""
                ),
                "mitigation": mitigation,
                "mitigation_id": stable_id("MIT", mitigation) if mitigation else "",
                "scenarios": scenarios,
                "stakeholders": stakeholders,
            }
        )

    if skipped:
        print(f"警告：跳过 {skipped} 条缺少 Literature_ID、主题或伤害类型的记录。")
    if not rows:
        raise ValueError("没有生成有效 Observation，请检查 Excel 数据。")

    print(f"准备导入 Observation：{len(rows)} 条")
    return rows


# =============================================================================
# 五、Neo4j 数据结构和 Cypher
# =============================================================================

CONSTRAINTS = [
    "CREATE CONSTRAINT paper_id_unique IF NOT EXISTS FOR (n:Paper) REQUIRE n.id IS UNIQUE",
    "CREATE CONSTRAINT observation_id_unique IF NOT EXISTS FOR (n:Observation) REQUIRE n.id IS UNIQUE",
    "CREATE CONSTRAINT topic_name_unique IF NOT EXISTS FOR (n:Topic) REQUIRE n.name IS UNIQUE",
    "CREATE CONSTRAINT harm_name_unique IF NOT EXISTS FOR (n:Harm) REQUIRE n.name IS UNIQUE",
    "CREATE CONSTRAINT manifestation_id_unique IF NOT EXISTS FOR (n:Manifestation) REQUIRE n.id IS UNIQUE",
    "CREATE CONSTRAINT mitigation_id_unique IF NOT EXISTS FOR (n:Mitigation) REQUIRE n.id IS UNIQUE",
    "CREATE CONSTRAINT scenario_name_unique IF NOT EXISTS FOR (n:Scenario) REQUIRE n.name IS UNIQUE",
    "CREATE CONSTRAINT stakeholder_name_unique IF NOT EXISTS FOR (n:Stakeholder) REQUIRE n.name IS UNIQUE",
]


PAPER_IMPORT_CYPHER = """
UNWIND $rows AS row
MERGE (p:Paper {id: row.paper_id})
SET p.title = row.paper_title,
    p.topic = row.topic,
    p.original_title = row.original_title,
    p.topic_code = row.topic_code,
    p.relative_path = row.relative_path
"""


OBSERVATION_IMPORT_CYPHER = """
UNWIND $rows AS row

MERGE (p:Paper {id: row.paper_id})
SET p.title = CASE
    WHEN coalesce(p.title, '') = '' THEN row.paper_title
    ELSE p.title
END

MERGE (o:Observation {id: row.record_id})
SET o.topic_name = row.topic,
    o.harm_name = row.harm

MERGE (p)-[:HAS_OBSERVATION]->(o)

MERGE (t:Topic {name: row.topic})
MERGE (o)-[:HAS_TOPIC]->(t)

MERGE (h:Harm {name: row.harm})
MERGE (o)-[:HAS_HARM]->(h)

FOREACH (_ IN CASE WHEN row.manifestation_id <> '' THEN [1] ELSE [] END |
    MERGE (m:Manifestation {id: row.manifestation_id})
    SET m.text = row.manifestation
    MERGE (o)-[:HAS_MANIFESTATION]->(m)
)

FOREACH (_ IN CASE WHEN row.mitigation_id <> '' THEN [1] ELSE [] END |
    MERGE (mi:Mitigation {id: row.mitigation_id})
    SET mi.text = row.mitigation
    MERGE (o)-[:HAS_MITIGATION]->(mi)
)
"""


SCENARIO_IMPORT_CYPHER = """
UNWIND $rows AS row
MATCH (o:Observation {id: row.record_id})
FOREACH (scenario_name IN row.scenarios |
    MERGE (s:Scenario {name: scenario_name})
    MERGE (o)-[:OCCURS_IN]->(s)
)
"""


STAKEHOLDER_IMPORT_CYPHER = """
UNWIND $rows AS row
MATCH (o:Observation {id: row.record_id})
FOREACH (stakeholder_name IN row.stakeholders |
    MERGE (st:Stakeholder {name: stakeholder_name})
    MERGE (o)-[:INVOLVES]->(st)
)
"""


FREQUENCY_QUERIES = [
    """
    MATCH (o:Observation)-[:HAS_TOPIC]->(t:Topic)
    WITH t, count(DISTINCT o) AS frequency
    SET t.frequency = frequency
    """,
    """
    MATCH (o:Observation)-[:HAS_HARM]->(h:Harm)
    WITH h, count(DISTINCT o) AS frequency
    SET h.frequency = frequency
    """,
    """
    MATCH (o:Observation)-[:OCCURS_IN]->(s:Scenario)
    WITH s, count(DISTINCT o) AS frequency
    SET s.frequency = frequency
    """,
    """
    MATCH (o:Observation)-[:INVOLVES]->(st:Stakeholder)
    WITH st, count(DISTINCT o) AS frequency
    SET st.frequency = frequency
    """,
]


PROJECTION_QUERIES = [
    (
        "Topic-Harm",
        """
        MATCH (t:Topic)<-[:HAS_TOPIC]-(o:Observation)-[:HAS_HARM]->(h:Harm)
        WITH t, h, count(DISTINCT o) AS frequency
        MERGE (t)-[r:CO_OCCURS_WITH]->(h)
        SET r.frequency = frequency,
            r.relation_type = 'Topic-Harm',
            r.is_causal = false
        """,
    ),
    (
        "Harm-Scenario",
        """
        MATCH (h:Harm)<-[:HAS_HARM]-(o:Observation)-[:OCCURS_IN]->(s:Scenario)
        WITH h, s, count(DISTINCT o) AS frequency
        MERGE (h)-[r:CO_OCCURS_WITH]->(s)
        SET r.frequency = frequency,
            r.relation_type = 'Harm-Scenario',
            r.is_causal = false
        """,
    ),
    (
        "Scenario-Stakeholder",
        """
        MATCH (s:Scenario)<-[:OCCURS_IN]-(o:Observation)-[:INVOLVES]->(st:Stakeholder)
        WITH s, st, count(DISTINCT o) AS frequency
        MERGE (s)-[r:CO_OCCURS_WITH]->(st)
        SET r.frequency = frequency,
            r.relation_type = 'Scenario-Stakeholder',
            r.is_causal = false
        """,
    ),
]


# =============================================================================
# 六、导入 Neo4j
# =============================================================================

def get_password() -> str:
    """使用普通输入，确保 PyCharm 运行窗口能够接收密码。"""
    print("\n程序正在等待输入 Neo4j 数据库密码。")
    print("注意：密码会显示在本机运行窗口中，请不要截图或分享运行窗口。")
    password = input("请输入重置后的密码，然后按 Enter：").strip()
    if not password:
        raise ValueError("密码不能为空，请重新运行程序并输入密码。")
    return password


def create_constraints(session: Any) -> None:
    for statement in CONSTRAINTS:
        session.run(statement).consume()


def clear_database(session: Any) -> None:
    session.run("MATCH (n) DETACH DELETE n").consume()


def import_paper_batch(tx: Any, rows: list[dict[str, Any]]) -> None:
    tx.run(PAPER_IMPORT_CYPHER, rows=rows).consume()


def import_observation_batch(tx: Any, rows: list[dict[str, Any]]) -> None:
    tx.run(OBSERVATION_IMPORT_CYPHER, rows=rows).consume()
    tx.run(SCENARIO_IMPORT_CYPHER, rows=rows).consume()
    tx.run(STAKEHOLDER_IMPORT_CYPHER, rows=rows).consume()


def calculate_frequencies_and_projections(session: Any) -> None:
    for query in FREQUENCY_QUERIES:
        session.run(query).consume()

    for relation_name, query in PROJECTION_QUERIES:
        session.run(query).consume()
        print(f"已生成 {relation_name} 共现关系。")


def print_counts(session: Any) -> None:
    print("\nNeo4j 当前节点数量：")
    labels = [
        "Paper", "Observation", "Topic", "Harm",
        "Manifestation", "Mitigation", "Scenario", "Stakeholder",
    ]
    for label in labels:
        result = session.run(
            f"MATCH (n:{label}) RETURN count(n) AS count"
        ).single()
        print(f"  {label}: {result['count']}")


def import_to_neo4j(
    papers: list[dict[str, Any]],
    observations: list[dict[str, Any]],
) -> None:
    print("\n正在准备 Neo4j 连接信息……")
    print(f"URI：{NEO4J_URI}")
    print(f"用户名：{NEO4J_USERNAME}")
    print(f"数据库：{NEO4J_DATABASE}")
    password = get_password()

    print("正在连接 Neo4j AuraDB……")
    driver = GraphDatabase.driver(
        NEO4J_URI,
        auth=(NEO4J_USERNAME, password),
        connection_timeout=30.0,
    )

    try:
        driver.verify_connectivity()
        print("Neo4j 连接成功。")

        with driver.session(database=NEO4J_DATABASE) as session:
            if CLEAR_DATABASE:
                print("警告：正在清空当前数据库全部数据……")
                clear_database(session)

            print("正在创建唯一约束……")
            create_constraints(session)

            print(f"正在导入 {len(papers)} 篇 Paper……")
            for batch in chunks(papers, 200):
                session.execute_write(import_paper_batch, batch)

            print(f"正在导入 {len(observations)} 条 Observation……")
            for number, batch in enumerate(chunks(observations, 200), start=1):
                session.execute_write(import_observation_batch, batch)
                imported = min(number * 200, len(observations))
                print(f"  已完成 {imported}/{len(observations)} 条")

            print("正在计算节点频次并生成共现关系……")
            calculate_frequencies_and_projections(session)
            print_counts(session)

    except Exception as error:
        print("\n程序运行失败。")
        print(f"错误类型：{type(error).__name__}")
        print(f"错误信息：{error}")
        raise
    finally:
        driver.close()


# =============================================================================
# 七、主程序：PyCharm 点击运行后从这里开始
# =============================================================================

def main() -> None:
    print("=" * 70)
    print("AI 学术出版社会技术伤害知识图谱导入程序")
    print("=" * 70)

    excel_path = locate_excel_file()
    observations_df, literature_df = read_excel_data(excel_path)
    papers = prepare_papers(literature_df)
    observations = prepare_observations(observations_df, literature_df)

    import_to_neo4j(papers, observations)

    print("\n导入完成。请在 Neo4j Query 中运行：")
    print("MATCH (a)-[r:CO_OCCURS_WITH]->(b) RETURN a, r, b LIMIT 200")


if __name__ == "__main__":
    main()
