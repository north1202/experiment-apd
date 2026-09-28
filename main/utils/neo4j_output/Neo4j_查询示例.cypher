// 每次复制一个查询到 Neo4j 的 Query/Browser 执行。
// 所有查询限定当前数据版本：academic_e0d548a1d145af39

// 1. 概览：线条上的 paper_count / observation_count 是共现数量。
MATCH (a:AcademicKG {dataset_id:'academic_e0d548a1d145af39'})-[r:CO_OCCURS]->(b:AcademicKG {dataset_id:'academic_e0d548a1d145af39'})
RETURN a,r,b;

// 2. 查回 REC_0001 的来源、主题与标签，可改成其他 Record_ID。
MATCH (p:AcademicKG:Paper {dataset_id:'academic_e0d548a1d145af39'})-[s:HAS_OBSERVATION]->(o:AcademicKG:Observation {record_id:'REC_0001'})
MATCH (p)-[pt:IN_TOPIC]->(t:AcademicKG:Topic)
OPTIONAL MATCH (o)-[r:HAS_HARM|IN_DOMAIN|INVOLVES]->(c:AcademicKG)
RETURN p,s,o,pt,t,r,c;

// 3. 查看原始文本和来源 DOI。
MATCH (p:AcademicKG:Paper {dataset_id:'academic_e0d548a1d145af39'})-[:HAS_OBSERVATION]->(o:AcademicKG:Observation)
RETURN o.record_id AS Record_ID,p.literature_id AS Literature_ID,p.title AS title,
       p.doi AS DOI,o.manifestation AS manifestation,o.mitigation AS mitigation
ORDER BY Record_ID LIMIT 50;

// 4. 主题文献数与观察数；Topic的paper_count包括无观察记录的文献。
MATCH (t:AcademicKG:Topic {dataset_id:'academic_e0d548a1d145af39'})
RETURN t.code AS topic,t.name AS name,t.paper_count AS papers,
       t.supporting_paper_count AS papers_with_observations,t.observation_count AS observations
ORDER BY papers DESC;

// 5. 与论文一致的最小应用实例。
MATCH (p:AcademicKG:Paper {dataset_id:'academic_e0d548a1d145af39'})-[:HAS_OBSERVATION]->(o:AcademicKG:Observation)
WHERE EXISTS { MATCH (o)-[:IN_DOMAIN]->(:AcademicKG:GovernanceDomain {code:'Scenario_PeerReview'}) }
  AND EXISTS { MATCH (o)-[:INVOLVES]->(:AcademicKG:Stakeholder {code:'Stakeholder_Publishers'}) }
RETURN count(DISTINCT o) AS observations, count(DISTINCT p) AS papers;

// 6. 追溯一个类别对的共现证据，以下以同行评议—出版者/编辑为例。
MATCH (a:AcademicKG:GovernanceDomain {dataset_id:'academic_e0d548a1d145af39',code:'Scenario_PeerReview'})
      -[r:CO_OCCURS]-(b:AcademicKG:Stakeholder {dataset_id:'academic_e0d548a1d145af39',code:'Stakeholder_Publishers'})
UNWIND r.record_ids AS rid
MATCH (p:AcademicKG:Paper {dataset_id:'academic_e0d548a1d145af39'})-[:HAS_OBSERVATION]->
      (o:AcademicKG:Observation {dataset_id:'academic_e0d548a1d145af39',record_id:rid})
RETURN o.record_id AS Record_ID,p.literature_id AS Literature_ID,p.doi AS DOI,
       o.manifestation AS manifestation,o.mitigation AS mitigation
ORDER BY Record_ID;
