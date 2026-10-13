// Query example for this dataset version.
// Query example for this dataset version.academic_desktop_en_v1_e0d548a1d145af39

// Query example for this dataset version.
MATCH (a:AcademicKG {dataset_id:'academic_desktop_en_v1_e0d548a1d145af39'})-[r:CO_OCCURS]->(b:AcademicKG {dataset_id:'academic_desktop_en_v1_e0d548a1d145af39'})
RETURN a,r,b;

// Query example for this dataset version.
MATCH (p:AcademicKG:Paper {dataset_id:'academic_desktop_en_v1_e0d548a1d145af39'})-[s:HAS_OBSERVATION]->(o:AcademicKG:Observation {record_id:'REC_0001'})
MATCH (p)-[pt:IN_TOPIC]->(t:AcademicKG:Topic)
OPTIONAL MATCH (o)-[r:HAS_HARM|IN_DOMAIN|INVOLVES]->(c:AcademicKG)
RETURN p,s,o,pt,t,r,c;

// Query example for this dataset version.
MATCH (p:AcademicKG:Paper {dataset_id:'academic_desktop_en_v1_e0d548a1d145af39'})-[:HAS_OBSERVATION]->(o:AcademicKG:Observation)
RETURN o.record_id AS Record_ID,p.literature_id AS Literature_ID,p.title AS title,
       p.doi AS DOI,o.manifestation AS manifestation,o.mitigation AS mitigation
ORDER BY Record_ID LIMIT 50;

// Query example for this dataset version.
MATCH (t:AcademicKG:Topic {dataset_id:'academic_desktop_en_v1_e0d548a1d145af39'})
RETURN t.code AS topic,t.name AS name,t.paper_count AS papers,
       t.supporting_paper_count AS papers_with_observations,t.observation_count AS observations
ORDER BY papers DESC;

// Query example for this dataset version.
MATCH (p:AcademicKG:Paper {dataset_id:'academic_desktop_en_v1_e0d548a1d145af39'})-[:HAS_OBSERVATION]->(o:AcademicKG:Observation)
WHERE EXISTS { MATCH (o)-[:IN_DOMAIN]->(:AcademicKG:GovernanceDomain {code:'Scenario_PeerReview'}) }
  AND EXISTS { MATCH (o)-[:INVOLVES]->(:AcademicKG:Stakeholder {code:'Stakeholder_Publishers'}) }
RETURN count(DISTINCT o) AS observations, count(DISTINCT p) AS papers;

// Query example for this dataset version.
MATCH (a:AcademicKG:GovernanceDomain {dataset_id:'academic_desktop_en_v1_e0d548a1d145af39',code:'Scenario_PeerReview'})
      -[r:CO_OCCURS]-(b:AcademicKG:Stakeholder {dataset_id:'academic_desktop_en_v1_e0d548a1d145af39',code:'Stakeholder_Publishers'})
UNWIND r.record_ids AS rid
MATCH (p:AcademicKG:Paper {dataset_id:'academic_desktop_en_v1_e0d548a1d145af39'})-[:HAS_OBSERVATION]->
      (o:AcademicKG:Observation {dataset_id:'academic_desktop_en_v1_e0d548a1d145af39',record_id:rid})
RETURN o.record_id AS Record_ID,p.literature_id AS Literature_ID,p.doi AS DOI,
       o.manifestation AS manifestation,o.mitigation AS mitigation
ORDER BY Record_ID;
