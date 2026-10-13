"""English academic-publishing knowledge graph for Neo4j Desktop.
Python 3.10+. Install: python -m pip install "neo4j>=5.28,<7"
Put Literature_Metadata.csv and Summary_Observations.csv beside this script.
Set the local URI, username, password and database in the configuration below.
Run this Python file in PyCharm; run generated Cypher queries in Desktop Query.
--dry-run validates data and exports a local HTML overview without connecting.
CSV contents are preserved. Chinese source titles/evidence require English input.
Existing graphs are not deleted. English graphs use a separate dataset prefix.
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
# ===== EDIT THESE LOCAL SETTINGS =====
DATA_DIR = Path(__file__).resolve().parent
NEO4J_URI = 'neo4j://127.0.0.1:7687'
NEO4J_USERNAME = 'neo4j'
NEO4J_PASSWORD = 'salt1202'  # Enter the password created in Neo4j Desktop.
NEO4J_DATABASE = 'neo4j'
DRY_RUN = False
BATCH_SIZE = 200
EXPORT_HTML = True
# ===== END OF LOCAL SETTINGS =====
HARM_NAMES = {'Allocative Harms': 'Allocative Harms', 'Representational Harms': 'Representational Harms', 'Quality-of-Service Harms': 'Quality-of-Service Harms', 'Interpersonal Harms': 'Interpersonal Harms', 'Social System Harms': 'Social System Harms'}
DOMAINS = {'Scenario_Submission': 'Writing, Submission and Disclosure', 'Scenario_Screening': 'Editorial Screening', 'Scenario_PeerReview': 'Peer Review', 'Scenario_MacroPolicy': 'Research Evaluation and Institutional Governance'}
ACTORS = {'Stakeholder_Authors': 'Authors and Researchers', 'Stakeholder_Publishers': 'Publishers and Editors', 'Stakeholder_Reviewers': 'Reviewers', 'Stakeholder_Institutions': 'Institutions', 'Stakeholder_AIDevs': 'AI Developers and Tool Providers'}
TOPICS = {'class0': 'Academic Integrity and Institutional Governance', 'class1': 'Ethical Boundaries of LLMs in Research', 'class2': 'Authorship and Human-AI Collaboration', 'class3': 'AI Use and Perceptions in Academic Communities', 'class4': 'AI Writing and Use Disclosure', 'class5': 'Research Integrity and Academic Misconduct', 'class6': 'AI Ethics Education', 'class7': 'Individual Factors in AI Misuse', 'class8': 'AI-Generated Text Detection', 'class9': 'Institutional Compliance and Integrity Support', 'class10': 'Editorial Quality Control and Peer Review', 'class11': 'Educational Ecosystems and Ethical Responses'}
BIN = list(DOMAINS) + list(ACTORS)
META_FIELDS = ['Literature_ID', 'Literature_Title', 'Literature_Doi', 'Publication_Year', 'BERTopic_Cluster']
OBS_FIELDS = ['Record_ID', 'Literature_ID', 'Social_Harm_Type', 'Manifestation_Text', 'Mitigation_Text'] + BIN
PARTS = {'HarmType_Observations': ['Social_Harm_Type'], 'ProblemsAndSolutions_Observations': ['Manifestation_Text', 'Mitigation_Text'], 'PublishingScenario_Observations': list(DOMAINS), 'Stakeholder_Observations': list(ACTORS)}
LABELS = {'Paper', 'Observation', 'Topic', 'HarmType', 'GovernanceDomain', 'Stakeholder'}
REL_TYPES = {'HAS_OBSERVATION', 'IN_TOPIC', 'HAS_HARM', 'IN_DOMAIN', 'INVOLVES', 'CO_OCCURS'}

def log(message):
    print(time.strftime('[%H:%M:%S] ') + str(message), flush=True)

@contextmanager
def heartbeat(message):
    """Report progress while waiting for a long-running operation."""
    stopped = threading.Event()

    def pulse():
        while not stopped.wait(8):
            log(message + ' (still waiting; success has not been reported)')
    worker = threading.Thread(target=pulse, daemon=True)
    worker.start()
    try:
        yield
    finally:
        stopped.set()
        worker.join(timeout=1)

def read_csv(path, fields):
    if not path.is_file():
        raise FileNotFoundError(f'File not found: {path}\nPlace CSV files beside this script or change DATA_DIR.')
    raw = path.read_bytes()
    for encoding in ('utf-8-sig', 'gb18030'):
        try:
            text = raw.decode(encoding, errors='strict')
            break
        except UnicodeDecodeError:
            continue
    else:
        raise ValueError(f'{path.name} cannot be decoded losslessly as UTF-8 or GB18030.')
    reader = csv.DictReader(io.StringIO(text, newline=''))
    missing = set(fields) - set(reader.fieldnames or [])
    if missing:
        raise ValueError(f'{path.name} is missing columns: {sorted(missing)}')
    rows = list(reader)
    if not rows:
        raise ValueError(f'{path.name} has no data rows.')
    if any((None in row or any((v is None for v in row.values())) for row in rows)):
        raise ValueError(f'{path.name} has inconsistent column counts; check CSV quoting and delimiters.')
    log(f'Loaded {path.name}：{len(rows)} rows; encoding: {encoding}')
    return rows

def index_rows(rows, key, filename):
    index = {}
    for line, row in enumerate(rows, 2):
        value = row[key]
        if not value or value != value.strip():
            raise ValueError(f'{filename} row {line}: {key} is empty or contains leading/trailing whitespace.')
        if value in index:
            raise ValueError(f'{filename} has duplicate primary key {key}={value}; stopped without merging duplicate rows.')
        index[value] = row
    return index

def load_data(folder):
    papers = read_csv(folder / 'Literature_Metadata.csv', META_FIELDS)
    observations = read_csv(folder / 'Summary_Observations.csv', OBS_FIELDS)
    pm = index_rows(papers, 'Literature_ID', 'Literature_Metadata.csv')
    om = index_rows(observations, 'Record_ID', 'Summary_Observations.csv')
    for p in papers:
        if p['BERTopic_Cluster'] not in TOPICS:
            raise ValueError(f"Unknown topic: {p['BERTopic_Cluster']}; update the TOPICS mapping.")
        try:
            int(p['Publication_Year'])
        except ValueError:
            raise ValueError(f"{p['Literature_ID']} has a non-integer publication year.") from None
    for r in observations:
        if r['Literature_ID'] not in pm:
            raise ValueError(f"{r['Record_ID']} refers to a Literature_ID missing from metadata.")
        if r['Social_Harm_Type'] not in HARM_NAMES:
            raise ValueError(f"{r['Record_ID']} has an unsupported harm category.")
        if any((r[k] not in ('0', '1') for k in BIN)):
            raise ValueError(f"{r['Record_ID']} has a binary label other than 0 or 1.")
    for name, fields in PARTS.items():
        path = folder / (name + '.csv')
        if not path.exists():
            log(f'Optional dimension table not provided: {path.name}; continuing with Summary_Observations.csv.')
            continue
        rows = read_csv(path, ['Record_ID', 'Literature_ID'] + fields)
        part = index_rows(rows, 'Record_ID', name)
        if set(part) != set(om):
            raise ValueError(f'{name} has a Record_ID set different from the summary table.')
        for rid, r in part.items():
            if any((r[k] != om[rid][k] for k in ['Literature_ID'] + fields)):
                raise ValueError(f'{name} record {rid} differs from the summary table; import stopped.')
    duplicates = defaultdict(list)
    for r in observations:
        duplicates[tuple((r[k] for k in OBS_FIELDS if k != 'Record_ID'))].append(r['Record_ID'])
    groups = [ids for ids in duplicates.values() if len(ids) > 1]
    missing_mitigation = sum((not r['Mitigation_Text'].strip() for r in observations))
    no_obs = sorted(set(pm) - {r['Literature_ID'] for r in observations})
    log(f'Duplicate-content surplus: {sum((len(g) - 1 for g in groups))} records; all Record_ID values are retained.')
    log(f'Missing mitigation: {missing_mitigation} records; papers without observations: {len(no_obs)} papers.')
    return (papers, observations, {'duplicate_record_groups': groups, 'missing_mitigation': missing_mitigation, 'papers_without_observations': no_obs})

def build_graph(papers, observations):
    canonical = [sorted(papers, key=lambda r: r['Literature_ID']), sorted(observations, key=lambda r: r['Record_ID'])]
    digest = hashlib.sha256(json.dumps(canonical, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
    dataset = 'academic_desktop_en_v1_' + digest[:16]

    def uid(label, code):
        return dataset + '|' + label + '|' + code
    nodes, edges = ({}, [])

    def node(label, code, name, **props):
        key = uid(label, code)
        nodes[key] = {'uid': key, 'label': label, 'props': dict(uid=key, dataset_id=dataset, kind=label, code=code, name=name, **props)}
        return key

    def edge(source, relation, target, **props):
        edges.append({'source': source, 'type': relation, 'target': target, 'props': dict(dataset_id=dataset, kind='evidence', **props)})
    for label, names in [('Topic', TOPICS), ('HarmType', HARM_NAMES), ('GovernanceDomain', DOMAINS), ('Stakeholder', ACTORS)]:
        for code, name in names.items():
            node(label, code, name, paper_count=0, supporting_paper_count=0, observation_count=0)
    paper_by_id = {p['Literature_ID']: p for p in papers}
    paper_obs = Counter((r['Literature_ID'] for r in observations))
    topic_papers = defaultdict(set)
    obs_sets, paper_sets = (defaultdict(set), defaultdict(set))
    pair_records, pair_papers = (defaultdict(set), defaultdict(set))
    for p in papers:
        lid, topic = (p['Literature_ID'], p['BERTopic_Cluster'])
        key = node('Paper', lid, p['Literature_Title'], literature_id=lid, title=p['Literature_Title'], doi=p['Literature_Doi'], year=int(p['Publication_Year']), topic_code=topic, paper_count=1, observation_count=paper_obs[lid])
        edge(key, 'IN_TOPIC', uid('Topic', topic), literature_id=lid)
        topic_papers[uid('Topic', topic)].add(lid)
    for r in observations:
        rid, lid = (r['Record_ID'], r['Literature_ID'])
        topic = paper_by_id[lid]['BERTopic_Cluster']
        key = node('Observation', rid, rid, record_id=rid, literature_id=lid, manifestation=r['Manifestation_Text'], mitigation=r['Mitigation_Text'], mitigation_missing=not bool(r['Mitigation_Text'].strip()), harm_type=r['Social_Harm_Type'], topic_code=topic, paper_count=1, observation_count=1, **{k: int(r[k]) for k in BIN})
        edge(uid('Paper', lid), 'HAS_OBSERVATION', key, record_id=rid, literature_id=lid)
        tags = [('Topic', topic), ('HarmType', r['Social_Harm_Type'])]
        tags += [('GovernanceDomain', k) for k in DOMAINS if r[k] == '1']
        tags += [('Stakeholder', k) for k in ACTORS if r[k] == '1']
        for label, code in tags:
            target = uid(label, code)
            obs_sets[target].add(rid)
            paper_sets[target].add(lid)
            relation = {'HarmType': 'HAS_HARM', 'GovernanceDomain': 'IN_DOMAIN', 'Stakeholder': 'INVOLVES'}.get(label)
            if relation:
                edge(key, relation, target, record_id=rid, literature_id=lid)
        for (la, ca), (lb, cb) in combinations(tags, 2):
            if la == lb:
                continue
            pair = tuple(sorted((uid(la, ca), uid(lb, cb))))
            pair_records[pair].add(rid)
            pair_papers[pair].add(lid)
    for key, n in nodes.items():
        if n['label'] not in ('Paper', 'Observation'):
            n['props']['observation_count'] = len(obs_sets[key])
            n['props']['supporting_paper_count'] = len(paper_sets[key])
            n['props']['paper_count'] = len(topic_papers[key] if n['label'] == 'Topic' else paper_sets[key])
    for (source, target), records in sorted(pair_records.items()):
        edges.append({'source': source, 'type': 'CO_OCCURS', 'target': target, 'props': {'dataset_id': dataset, 'kind': 'cooccurrence', 'observation_count': len(records), 'paper_count': len(pair_papers[source, target]), 'record_ids': sorted(records)}})
    return (dataset, list(nodes.values()), edges)

def local_case(observations):
    rows = [r for r in observations if r['Scenario_PeerReview'] == '1' and r['Stakeholder_Publishers'] == '1']
    return {'observations': len(rows), 'papers': len({r['Literature_ID'] for r in rows})}

def import_graph(nodes, edges, dataset, expected_case):
    try:
        from neo4j import GraphDatabase, unit_of_work
    except ImportError:
        raise RuntimeError('Run in the PyCharm terminal: python -m pip install "neo4j>=5.28,<7"') from None
    password = NEO4J_PASSWORD or os.environ.get('NEO4J_PASSWORD', '')
    if not password:
        raise ValueError('Set NEO4J_PASSWORD in the configuration or environment. Use your local database password.')
    if BATCH_SIZE < 1:
        raise ValueError('BATCH_SIZE must be greater than zero.')

    @unit_of_work(timeout=45)
    def write(tx, query, batch):
        result = tx.run(query, rows=batch)
        result.consume()

    def batches(session, query, rows, title):
        for start in range(0, len(rows), BATCH_SIZE):
            batch = rows[start:start + BATCH_SIZE]
            with heartbeat(f'Committing {title} batch'):
                session.execute_write(write, query, batch)
            log(f'{title}：{start + len(batch)}/{len(rows)} committed')
    log('Connecting to Neo4j and checking authentication...')
    with GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, password), connection_timeout=10, connection_acquisition_timeout=20, max_transaction_retry_time=15, max_connection_pool_size=4) as driver:
        with heartbeat('Checking database connectivity'):
            driver.verify_connectivity()
        with driver.session(database=NEO4J_DATABASE) as session:
            session.run('RETURN 1 AS ok').consume()
            log('Connection verified. Creating the graph identifier constraint...')
            session.run('CREATE CONSTRAINT academic_kg_uid IF NOT EXISTS FOR (n:AcademicKG) REQUIRE n.uid IS UNIQUE').consume()
            by_label, by_type = (defaultdict(list), defaultdict(list))
            for row in nodes:
                by_label[row['label']].append(row)
            for row in edges:
                by_type[row['type']].append(row)
            for label, rows in by_label.items():
                assert label in LABELS
                query = f'UNWIND $rows AS row MERGE (n:AcademicKG {{uid: row.uid}}) SET n:{label} SET n += row.props'
                batches(session, query, rows, 'Nodes: ' + label)
            for relation, rows in by_type.items():
                assert relation in REL_TYPES
                query = f'UNWIND $rows AS row MATCH (a:AcademicKG {{uid: row.source}}) MATCH (b:AcademicKG {{uid: row.target}}) MERGE (a)-[r:{relation}]->(b) SET r = row.props'
                batches(session, query, rows, 'Relationships: ' + relation)
            log('Import batches completed. Verifying nodes, relationships, weights and example query...')
            actual_nodes = {r['kind']: r['n'] for r in session.run('MATCH (n:AcademicKG {dataset_id:$d}) RETURN n.kind AS kind, count(n) AS n', d=dataset)}
            actual_edges = {r['type']: r['n'] for r in session.run('MATCH (a:AcademicKG {dataset_id:$d})-[r]->(b:AcademicKG {dataset_id:$d}) RETURN type(r) AS type, count(r) AS n', d=dataset)}
            if actual_nodes != dict(Counter((r['label'] for r in nodes))):
                raise RuntimeError(f'Node count mismatch: {actual_nodes}; import has not been reported as successful.')
            if actual_edges != dict(Counter((r['type'] for r in edges))):
                raise RuntimeError(f'Relationship count mismatch: {actual_edges}; import has not been reported as successful.')
            result = session.run(CASE_QUERY, d=dataset).single()
            actual_case = {'observations': result['observations'], 'papers': result['papers']}
            if actual_case != expected_case:
                raise RuntimeError(f'Database query result {actual_case} differs from local result {expected_case}.')
            wanted = {n['uid']: (n['props']['paper_count'], n['props']['observation_count']) for n in nodes if n['label'] not in ('Paper', 'Observation')}
            actual = {r['uid']: (r['p'], r['o']) for r in session.run('MATCH (n:AcademicKG {dataset_id:$d}) WHERE NOT n:Paper AND NOT n:Observation RETURN n.uid AS uid,n.paper_count AS p,n.observation_count AS o', d=dataset)}
            if actual != wanted:
                raise RuntimeError('Category paper/observation count validation failed.')
            expected_weights = {(e['source'], e['target']): (e['props']['paper_count'], e['props']['observation_count']) for e in edges if e['type'] == 'CO_OCCURS'}
            actual_weights = {(r['a'], r['b']): (r['p'], r['o']) for r in session.run('MATCH (a:AcademicKG {dataset_id:$d})-[r:CO_OCCURS]->(b:AcademicKG {dataset_id:$d}) RETURN a.uid AS a,b.uid AS b,r.paper_count AS p,r.observation_count AS o', d=dataset)}
            if actual_weights != expected_weights:
                raise RuntimeError('Co-occurrence weight validation failed.')
            log(f"Validation passed! Peer Review + Publishers and Editors: {actual_case['observations']} observations, {actual_case['papers']} papers.")
            return {'status': 'verified', 'node_counts': actual_nodes, 'relationship_counts': actual_edges, 'case_query': actual_case}
CASE_QUERY = "MATCH (p:AcademicKG:Paper {dataset_id:$d})-[:HAS_OBSERVATION]->(o:AcademicKG:Observation)\nWHERE EXISTS { MATCH (o)-[:IN_DOMAIN]->(:AcademicKG:GovernanceDomain {code:'Scenario_PeerReview'}) }\n  AND EXISTS { MATCH (o)-[:INVOLVES]->(:AcademicKG:Stakeholder {code:'Stakeholder_Publishers'}) }\nRETURN count(DISTINCT o) AS observations, count(DISTINCT p) AS papers"

def write_queries(out, dataset):
    literal = "'" + dataset + "'"
    text = f"// Query example for this dataset version.\n// Query example for this dataset version.{dataset}\n\n// Query example for this dataset version.\nMATCH (a:AcademicKG {{dataset_id:{literal}}})-[r:CO_OCCURS]->(b:AcademicKG {{dataset_id:{literal}}})\nRETURN a,r,b;\n\n// Query example for this dataset version.\nMATCH (p:AcademicKG:Paper {{dataset_id:{literal}}})-[s:HAS_OBSERVATION]->(o:AcademicKG:Observation {{record_id:'REC_0001'}})\nMATCH (p)-[pt:IN_TOPIC]->(t:AcademicKG:Topic)\nOPTIONAL MATCH (o)-[r:HAS_HARM|IN_DOMAIN|INVOLVES]->(c:AcademicKG)\nRETURN p,s,o,pt,t,r,c;\n\n// Query example for this dataset version.\nMATCH (p:AcademicKG:Paper {{dataset_id:{literal}}})-[:HAS_OBSERVATION]->(o:AcademicKG:Observation)\nRETURN o.record_id AS Record_ID,p.literature_id AS Literature_ID,p.title AS title,\n       p.doi AS DOI,o.manifestation AS manifestation,o.mitigation AS mitigation\nORDER BY Record_ID LIMIT 50;\n\n// Query example for this dataset version.\nMATCH (t:AcademicKG:Topic {{dataset_id:{literal}}})\nRETURN t.code AS topic,t.name AS name,t.paper_count AS papers,\n       t.supporting_paper_count AS papers_with_observations,t.observation_count AS observations\nORDER BY papers DESC;\n\n// Query example for this dataset version.\n{CASE_QUERY.replace('$d', literal)};\n\n// Query example for this dataset version.\nMATCH (a:AcademicKG:GovernanceDomain {{dataset_id:{literal},code:'Scenario_PeerReview'}})\n      -[r:CO_OCCURS]-(b:AcademicKG:Stakeholder {{dataset_id:{literal},code:'Stakeholder_Publishers'}})\nUNWIND r.record_ids AS rid\nMATCH (p:AcademicKG:Paper {{dataset_id:{literal}}})-[:HAS_OBSERVATION]->\n      (o:AcademicKG:Observation {{dataset_id:{literal},record_id:rid}})\nRETURN o.record_id AS Record_ID,p.literature_id AS Literature_ID,p.doi AS DOI,\n       o.manifestation AS manifestation,o.mitigation AS mitigation\nORDER BY Record_ID;\n"
    (out / 'Neo4j_queries.cypher').write_text(text, encoding='utf-8')

def export_html(out, nodes, edges, status):
    groups = ['Topic', 'HarmType', 'GovernanceDomain', 'Stakeholder']
    colors = {'Topic': '#3b82f6', 'HarmType': '#ef8354', 'GovernanceDomain': '#36a398', 'Stakeholder': '#9666c3'}
    categories = [dict(n['props'], group=n['label'], color=colors[n['label']]) for n in nodes if n['label'] in groups]
    for g in groups:
        members = [n for n in categories if n['group'] == g]
        if g == 'Topic':
            members.sort(key=lambda n: int(n['code'][5:]))
        for i, n in enumerate(members):
            n.update(x=130 + groups.index(g) * 320, y=90 + (i + 0.5) * 890 / len(members))
    links = [dict(e['props'], source=e['source'], target=e['target']) for e in edges if e['type'] == 'CO_OCCURS']
    payload = json.dumps({'nodes': categories, 'edges': links}, ensure_ascii=False).replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')
    page = HTML.replace('__DATA__', payload).replace('__STATUS__', html.escape(status))
    (out / 'knowledge_graph_overview.html').write_text(page, encoding='utf-8')
HTML = '<!doctype html><html lang="en"><meta charset="utf-8">\n<title>AI Ethics in Academic Publishing: Knowledge Graph</title>\n<style>body{margin:24px;background:#f5f7fb;color:#233047;font:15px system-ui,sans-serif}h1{font-size:24px}p{line-height:1.7;max-width:1200px}select,input,button{padding:8px;margin:4px}svg{background:white;border:1px solid #dbe2ec;max-width:100%;height:auto}#tip{white-space:pre-wrap;line-height:1.6;padding:14px;background:white;border-left:4px solid #3b82f6;min-height:80px}text{pointer-events:none}label{display:inline-block}</style>\n<h1>AI Ethics in Academic Publishing: Category Co-occurrence</h1><p>__STATUS__</p>\n<p>Node area encodes the selected count (with a minimum visible size). Edge width increases with co-occurrence count. Topic paper counts include papers without observations; other category counts use distinct papers supporting observations. Co-occurrence does not establish causation. Double-click an edge to view its Record_ID values, then use Neo4j to retrieve the source evidence.</p>\n<label>Node size <select id="nm"><option value="paper_count">Distinct papers</option><option value="observation_count">Observations</option></select></label>\n<label>Edge width <select id="em"><option value="observation_count">Co-occurring observations</option><option value="paper_count">Co-occurring papers</option></select></label>\n<label>Minimum count <input id="min" type="number" value="1" min="1" style="width:75px"></label>\n<button id="save">Download SVG</button><div id="tip">Blue: Topics | Orange: Harm types | Green: Governance domains | Purple: Stakeholders</div>\n<svg id="graph" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2200 1700"></svg>\n<script>\nconst data=__DATA__,svg=document.getElementById(\'graph\'),tip=document.getElementById(\'tip\');\nconst groups=[\'Topic\',\'HarmType\',\'GovernanceDomain\',\'Stakeholder\'];\nfor(const [gi,g] of groups.entries()){const members=data.nodes.filter(n=>n.group===g);if(g===\'Topic\')members.sort((a,b)=>Number(a.code.slice(5))-Number(b.code.slice(5)));members.forEach((n,i)=>{n.x=300+gi*520;n.y=150+(i+.5)*1400/members.length;});}\nconst byId=new Map(data.nodes.map(n=>[n.uid,n]));\nfunction el(tag,attrs,text){const e=document.createElementNS(\'http://www.w3.org/2000/svg\',tag);Object.entries(attrs).forEach(([k,v])=>e.setAttribute(k,v));if(text!==undefined)e.textContent=text;svg.appendChild(e);return e;}\nfunction wrap(text,max=34){let out=[],line=\'\';for(const word of text.split(/\\s+/)){if(line.length+word.length+1>max){out.push(line);line=word;}else line+=(line?\' \':\'\')+word;}if(line)out.push(line);return out;}\nfunction render(){svg.replaceChildren();const nm=document.getElementById(\'nm\').value,em=document.getElementById(\'em\').value,min=Math.max(1,Number(document.getElementById(\'min\').value)||1);\nel(\'text\',{x:40,y:36,\'font-size\':22,fill:\'#233047\'},\'Node size: \'+(nm===\'paper_count\'?\'distinct papers\':\'observations\')+\' | Edge width: \'+(em===\'paper_count\'?\'co-occurring papers\':\'co-occurring observations\')+\' | Minimum count: \'+min);\n[\'Topics\',\'Harm Types\',\'Governance Domains\',\'Stakeholders\'].forEach((t,i)=>el(\'text\',{x:300+i*520,y:106,\'text-anchor\':\'middle\',\'font-size\':28,fill:\'#233047\'},t));\nconst visible=data.edges.filter(e=>e[em]>=min),maxE=Math.max(1,...visible.map(e=>e[em])),maxN=Math.max(1,...data.nodes.map(n=>n[nm]));\nfor(const e of visible){const a=byId.get(e.source),b=byId.get(e.target),line=el(\'line\',{x1:a.x,y1:a.y,x2:b.x,y2:b.y,stroke:\'#64748b\',\'stroke-opacity\':.15,\'stroke-width\':.5+8*e[em]/maxE});const show=()=>{line.setAttribute(\'stroke-opacity\',.9);tip.textContent=a.name+\' ↔ \'+b.name+\'\\nObservations: \'+e.observation_count+\' | Distinct papers: \'+e.paper_count+\'\\nDouble-click to view Record_ID values.\';};line.onmouseenter=show;line.onclick=show;line.onmouseleave=()=>line.setAttribute(\'stroke-opacity\',.15);line.ondblclick=()=>tip.textContent=a.name+\' ↔ \'+b.name+\'\\nRecord_ID: \'+e.record_ids.join(\', \');}\nfor(const n of data.nodes){const r=Math.max(5,29*Math.sqrt(n[nm]/maxN)),c=el(\'circle\',{cx:n.x,cy:n.y,r,fill:n.color,stroke:\'white\',\'stroke-width\':2});const show=()=>tip.textContent=n.code+\' | \'+n.name+\'\\nDistinct papers: \'+n.paper_count+\' | Papers with observations: \'+n.supporting_paper_count+\' | Observations: \'+n.observation_count;c.onmouseenter=show;c.onclick=show;wrap((n.group===\'Topic\'?n.code+\' — \':\'\')+n.name).forEach((t,i)=>el(\'text\',{x:n.x,y:n.y+r+21+i*20,\'text-anchor\':\'middle\',\'font-size\':17,fill:\'#233047\'},t));el(\'text\',{x:n.x,y:n.y+5,\'text-anchor\':\'middle\',\'font-size\':14,fill:\'white\'},n[nm]);}\nel(\'text\',{x:40,y:1650,\'font-size\':20,fill:\'#475569\'},\'Displayed co-occurrence edges: \'+visible.length+\' / \'+data.edges.length+\'. Counts retain all source Record_ID values.\');}\n[\'nm\',\'em\',\'min\'].forEach(id=>document.getElementById(id).oninput=render);\ndocument.getElementById(\'save\').onclick=()=>{const blob=new Blob([new XMLSerializer().serializeToString(svg)],{type:\'image/svg+xml;charset=utf-8\'}),url=URL.createObjectURL(blob),a=document.createElement(\'a\');a.href=url;a.download=\'academic_publishing_knowledge_graph.svg\';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);};render();\n</script></html>\n'

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dry-run', action='store_true', help='Validate and export locally without connecting to Neo4j.')
    parser.add_argument('--data-dir', type=Path, default=DATA_DIR)
    args = parser.parse_args()
    dry_run = DRY_RUN or args.dry_run
    log('1/4 Loading and validating CSV files; source files are not modified.')
    papers, observations, audit = load_data(args.data_dir)
    dataset, nodes, edges = build_graph(papers, observations)
    node_counts = dict(Counter((n['label'] for n in nodes)))
    edge_counts = dict(Counter((e['type'] for e in edges)))
    core = sum((e['type'] != 'CO_OCCURS' for e in edges))
    case = local_case(observations)
    log(f'2/4 Graph generated: {len(nodes)} nodes; {core} evidence relationships; {len(edges) - core} co-occurrence relationships.')
    log(f'dataset_id = {dataset}')
    log(f"Local example query: {case['observations']} observations, {case['papers']} papers.")
    out = args.data_dir / 'neo4j_output' / dataset
    out.mkdir(parents=True, exist_ok=True)
    report = {'dataset_id': dataset, 'status': 'local_only', 'node_counts': node_counts, 'relationship_counts': edge_counts, 'evidence_relationships': core, 'case_query': case, 'audit': audit}
    report_path = out / 'import_validation_report.json'
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    write_queries(out, dataset)
    write_style(out)
    if EXPORT_HTML:
        export_html(out, nodes, edges, 'Local CSV preview; Neo4j import has not been verified.')
    if not dry_run:
        # validate_english_source(papers, observations)
        log('3/4 Importing into Neo4j. Progress is reported after each committed batch.')
        try:
            verified = import_graph(nodes, edges, dataset, case)
        except Exception as exc:
            report['status'] = 'failed_or_incomplete'
            report['error_type'] = type(exc).__name__
            report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
            raise
        report['status'] = 'verified'
        report['database_validation'] = verified
        report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
        if EXPORT_HTML:
            export_html(out, nodes, edges, 'Source: local CSV files. Neo4j nodes, relationships, counts and example query have been verified.')
    else:
        log('3/4 DRY_RUN: skipping database import; local outputs only.')
    log('4/4 Complete. Output folder: ' + str(out.resolve()))
    log('Open knowledge_graph_overview.html to explore counts and download SVG.')
    log('Open Neo4j_queries.cypher and run one query at a time in Desktop Query.')

def validate_english_source(papers, observations):
    import re
    issues = []
    for rows, key, fields in [(papers, 'Literature_ID', ['Literature_Title']), (observations, 'Record_ID', ['Manifestation_Text', 'Mitigation_Text'])]:
        for row in rows:
            for field in fields:
                if re.search('[\\u3400-\\u9fff]', row[field]):
                    issues.append(row[key] + ': ' + field)
    if issues:
        raise ValueError('Chinese text remains in ' + str(len(issues)) + ' source fields. Use a reviewed English copy of the CSV data. No automatic translation or database import was performed. Examples: ' + '; '.join(issues[:15]))

def write_style(out):
    style = 'node { caption: "{name}"; diameter: 60px; font-size: 10px; }\n'
    colors = {'Topic': '#3b82f6', 'HarmType': '#ef8354', 'GovernanceDomain': '#36a398', 'Stakeholder': '#9666c3', 'Paper': '#64748b', 'Observation': '#e5b34b'}
    for label, color in colors.items():
        style += 'node.' + label + ' { color: "' + color + '"; caption: "{name}"; }\n'
    style += 'relationship { caption: "<type>"; shaft-width: 1px; }\n'
    style += 'relationship.CO_OCCURS { caption: "{paper_count}"; }\n'
    (out / 'graph_style.grass').write_text(style, encoding='utf-8')
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        log('Interrupted. Committed batches may remain; rerunning identical data is idempotent.')
        sys.exit(130)
    except Exception as exc:
        code = getattr(exc, 'code', '') or ''
        kind = type(exc).__name__
        log('Failed: ' + kind)
        if kind == 'AuthError' or 'Unauthorized' in code:
            log('Authentication failed. Check the local URI, database username and password.')
        elif 'DatabaseNotFound' in code:
            log('Database not found. Check NEO4J_DATABASE; the default is neo4j, not the instance display name.')
        elif kind in ('ServiceUnavailable', 'SessionExpired', 'ConnectionAcquisitionTimeoutError'):
            log('Connection/session failed. Check that the Desktop instance is running and its URI is correct.')
        elif kind in ('FileNotFoundError', 'ValueError', 'RuntimeError'):
            log(str(exc))
        else:
            log('Database error code: ' + (code or 'none'))
            log('Check the driver version and constraint/write permissions. Import has not been reported as successful.')
        sys.exit(1)
