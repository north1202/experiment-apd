# AI Ethics in Scholarly Publishing

**Data and research code for linking sociotechnical harms, mitigation measures, publishing scenarios, stakeholders, and source publications.**

This project supports research on artificial intelligence (AI) ethics in scholarly publishing. It combines literature screening, BERTopic topic modeling, full-text information extraction, content auditing, and knowledge graph construction. Each observation links a reported harm manifestation and any associated mitigation measures to its source publication.

The accompanying manuscript is titled *A dataset linking sociotechnical harms and governance for research on artificial intelligence ethics in scholarly publishing*.

- **Code repository:** [north1202/experiment-apd](https://github.com/north1202/experiment-apd)
- **Data archive cited in the manuscript:** [Zenodo, DOI 10.5281/zenodo.23021106](https://doi.org/10.5281/zenodo.23021106)

## Dataset at a glance

| Component | Count | Unit or interpretation |
|---|---:|---|
| Literature metadata | 244 | Publication records |
| Observations | 772 | Structured observation records |
| Literature topics | 12 | Publication-level BERTopic categories, `class0`–`class11` |
| Sociotechnical harm types | 5 | One harm category per observation |
| Publishing scenarios | 4 | Multiple labels may apply to one observation |
| Stakeholder categories | 5 | Multiple labels may apply to one observation |

The manuscript describes a six-file CSV release. This GitHub repository contains the two core tables in `main/utils/neo4j_desktop_english/`. The remaining dimension-specific tables belong to the six-file data package described below.

The manuscript reports 1,042 knowledge graph nodes, 4,391 base relationships, and 219 category co-occurrence relationships. These are snapshot-specific figures. Recalculate them when the data or graph construction rules change.

## Repository guide

| Path | Purpose |
|---|---|
| `requirements.txt` | Pinned dependencies for the research environment |
| `main/settings.yaml` | Configuration for model-related processing |
| `main/utils/database_clean.py` | Literature data cleaning |
| `main/utils/bert.py` | BERTopic modeling and topic visualizations |
| `main/utils/bert_coherence.py` | Topic coherence analysis |
| `main/utils/annotated_150.py` | Preparation of annotation-related data |
| `main/utils/auto_tagging.py` | Automated labeling |
| `main/utils/llm_inference.py` | Large language model (LLM) inference |
| `main/utils/Summarize_types_of_injuries.py` | Extraction of harms and mitigation measures |
| `main/utils/Audit_first_injure.py` | Full-text audit of extracted information |
| `main/utils/evaluate_matrix.py` | Evaluation of results |
| `main/utils/time_trend.py` | Temporal analysis |
| `main/utils/neo4j_desktop_english/` | Core CSV tables and Neo4j construction script |

This table lists the main entry points rather than every intermediate file. The repository contains research scripts with stage-specific inputs and settings, rather than a single command that runs the entire workflow.

## Data files and relationships

| File | Rows | Columns | Contents |
|---|---:|---:|---|
| `Literature_Metadata.csv` | 244 | 5 | Publication identifiers, titles, DOIs, years, and topic categories |
| `HarmType_Observations.csv` | 772 | 3 | Observation identifiers, source identifiers, and harm types |
| `ProblemsAndSolutions_Observations.csv` | 772 | 4 | Harm manifestations and mitigation measures |
| `PublishingScenario_Observations.csv` | 772 | 6 | Four binary scenario labels |
| `Stakeholder_Observations.csv` | 772 | 7 | Five binary stakeholder labels |
| `Summary_Observations.csv` | 772 | 14 | Complete observation-level data |

`Literature_ID` is the primary key of the literature metadata table. `Record_ID` is the primary key of each observation table, and `Literature_ID` links each observation to its source publication.

The five observation tables describe the **same 772 records**. Their row counts must not be added together as independent samples. Join dimension-specific tables by `Record_ID`, check that their `Literature_ID` values agree, and join publication metadata by `Literature_ID`.

The manuscript reports 27,306 non-empty field values across the six files. This storage-level total includes information repeated between component tables and the summary table. It does not represent 27,306 independent pieces of evidence.

### Field dictionary

| Field | Meaning |
|---|---|
| `Literature_ID` | Source publication identifier |
| `Literature_Title` | Publication title |
| `Literature_Doi` | Digital object identifier (DOI) |
| `Publication_Year` | Publication year |
| `BERTopic_Cluster` | Publication-level topic label |
| `Record_ID` | Observation identifier |
| `Social_Harm_Type` | Single sociotechnical harm category |
| `Manifestation_Text` | Description of the harm manifestation |
| `Mitigation_Text` | Mitigation measures identified in the source |
| `Scenario_Submission` | Submission scenario indicator |
| `Scenario_Screening` | Editorial screening scenario indicator |
| `Scenario_PeerReview` | Peer review scenario indicator |
| `Scenario_MacroPolicy` | Macro policy scenario indicator |
| `Stakeholder_Authors` | Authors indicator |
| `Stakeholder_Publishers` | Publishers indicator |
| `Stakeholder_Reviewers` | Reviewers indicator |
| `Stakeholder_Institutions` | Institutions indicator |
| `Stakeholder_AIDevs` | AI developers indicator |

Keep field names unchanged, including the capitalization of `Literature_Doi`. Scenario and stakeholder indicators use `1` for an assigned label and `0` otherwise. A zero indicates that the label was not assigned to the observation, not that the corresponding issue can never occur.

In the checked core tables, 81 observations have an empty `Mitigation_Text`. Preserve these empty values. They indicate that no explicit mitigation measure was captured for that record, rather than proving that no possible measure exists.

### Classification dimensions

**Harm Type** uses five fixed values.

- `Allocative Harms`
- `Representational Harms`
- `Quality-of-Service Harms`
- `Interpersonal Harms`
- `Social System Harms`

**Scenario** uses four categories: Submission, Screening, Peer Review, and Macro Policy. Macro Policy covers institutional governance and research assessment, so these categories should not be interpreted as four consecutive workflow stages.

**Stakeholder** uses five categories: Authors, Publishers, Reviewers, Institutions, and AI Developers. Authors includes researchers, and Publishers includes editors and editorial teams.

**Topic** is assigned at the publication level. An observation inherits its source publication's topic through `Literature_ID`. The 12 topics are distinct from the four scenario categories.

The following descriptive labels follow the current graph script's `TOPICS` mapping. Publication counts were checked against the repository's metadata table.

| Topic | Descriptive label | Publications |
|---|---|---:|
| `class0` | Academic Integrity and Institutional Governance | 52 |
| `class1` | Ethical Boundaries of LLMs in Research | 51 |
| `class2` | Authorship and Human-AI Collaboration | 27 |
| `class3` | AI Use and Perceptions in Academic Communities | 26 |
| `class4` | AI Writing and Use Disclosure | 21 |
| `class5` | Research Integrity and Academic Misconduct | 16 |
| `class6` | AI Ethics Education | 11 |
| `class7` | Individual Factors in AI Misuse | 10 |
| `class8` | AI-Generated Text Detection | 10 |
| `class9` | Institutional Compliance and Integrity Support | 8 |
| `class10` | Editorial Quality Control and Peer Review | 7 |
| `class11` | Educational Ecosystems and Ethical Responses | 5 |
| **Total** | | **244** |

## Quick start

### 1. Obtain the repository

```bash
git clone https://github.com/north1202/experiment-apd.git
cd experiment-apd
```

Use Python 3.10 or later for the graph script. Create an isolated environment before installing dependencies.

```bash
python -m venv .venv
```

Activate it on Windows PowerShell with `.\.venv\Scripts\Activate.ps1`, or on macOS/Linux with `source .venv/bin/activate`.

### 2. Query the core tables

The following example uses only the Python standard library. Save it as `query_example.py` in the repository root and run `python query_example.py`. It preserves empty fields and attempts UTF-8 with BOM support before GB18030 decoding.

```python
import csv
import io
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "main/utils/neo4j_desktop_english"


def read_csv(filename):
    raw = (DATA_DIR / filename).read_bytes()
    for encoding in ("utf-8-sig", "gb18030"):
        try:
            text = raw.decode(encoding)
            return list(csv.DictReader(io.StringIO(text, newline="")))
        except UnicodeDecodeError:
            continue
    raise ValueError(f"Cannot decode {filename} as UTF-8 or GB18030")


publications = read_csv("Literature_Metadata.csv")
observations = read_csv("Summary_Observations.csv")
metadata = {row["Literature_ID"]: row for row in publications}

matches = [
    row for row in observations
    if row["Scenario_PeerReview"] == "1"
    and row["Stakeholder_Publishers"] == "1"
]
source_ids = {row["Literature_ID"] for row in matches}

print(f"Publications: {len(publications)}")
print(f"Observations: {len(observations)}")
print(f"Matching observations: {len(matches)}")
print(f"Distinct source publications: {len(source_ids)}")

for row in matches[:3]:
    source = metadata[row["Literature_ID"]]
    print(row["Record_ID"], source["Literature_Title"])
```

For the checked repository snapshot, the query returns **50 observations from 34 source publications**, out of 772 observations and 244 publication records. It retrieves observations labeled with both Peer Review and Publishers. It does not estimate the prevalence of ethical problems in publishing.

### 3. Validate and visualize without Neo4j

From the repository root, run:

```bash
python main/utils/neo4j_desktop_english/neo4j_desktop_english.py --dry-run
```

This mode validates the local data and generates output without connecting to Neo4j. The script reads the two core CSV files beside it. If the four dimension-specific tables are also present, it checks them against the summary table.

Generated files are placed under `main/utils/neo4j_desktop_english/neo4j_output/<dataset_id>/`, including:

- `import_validation_report.json`
- `knowledge_graph_overview.html`
- `Neo4j_queries.cypher`
- `graph_style.grass`

The local HTML overview supports inspection of graph counts and SVG export. A successful dry run verifies local processing, not a database import.

### 4. Import into Neo4j Desktop

Install the Python driver:

```bash
python -m pip install "neo4j>=5.28,<7"
```

Start your Neo4j database, then configure the connection URI, username, password, and database name in the local settings of `neo4j_desktop_english.py`. Use your own credentials and keep them out of public commits. Run:

```bash
python main/utils/neo4j_desktop_english/neo4j_desktop_english.py
```

Open the generated `Neo4j_queries.cypher` file and execute the relevant queries in Neo4j Desktop Query. Check `import_validation_report.json` for the import status and validation results.

The current code uses `GovernanceDomain` as the Neo4j node label for a Scenario domain and `IN_DOMAIN` for its relationship type. These technical identifiers remain unchanged in the script even when figures or manuscript prose use “Scenario domain”.

| Relationship | Connection |
|---|---|
| `HAS_OBSERVATION` | Publication to observation |
| `IN_TOPIC` | Publication to topic |
| `HAS_HARM` | Observation to harm type |
| `IN_DOMAIN` | Observation to scenario domain |
| `INVOLVES` | Observation to stakeholder |
| `CO_OCCURS` | Category co-occurrence within observations |

Relationship directions support storage and querying. They do not establish causal direction or responsibility for causing a harm.

## Re-running the research workflow

The conceptual workflow is:

1. Search, deduplicate, and screen literature.
2. Model abstracts with BERTopic and interpret the resulting themes.
3. Parse eligible full texts and link them to publication identifiers.
4. Extract harm manifestations and mitigation measures.
5. Audit the extracted content and assign structured labels.
6. Assemble and validate the CSV tables.
7. Construct the graph and perform cross-dimensional queries.

Install the pinned environment dependencies with:

```bash
python -m pip install -r requirements.txt
```

The current requirements file does not list every dependency imported by the topic-modeling scripts. For `bert.py`, additional packages include `bertopic`, `sentence-transformers`, `umap-learn`, and `hdbscan`. Install compatible versions and record them with the Python version, model identifier, parameters, and Git commit used for each run.

The current `bert.py` reads `core_dataset.csv` from its working directory and uses the `Abstract` column. Run it from `main/utils/` after checking the input file and local paths. Its embedding model is `allenai/specter2_base`. It uses UMAP and HDBSCAN, and sets BERTopic's `nr_topics` argument to `13`. The reported result contains 12 non-outlier categories. Check the actual topic output, including `Topic -1`, rather than assuming that the numeric argument alone guarantees the final topic count.

Model-based stages may require downloads, network access, service credentials, and paid API calls. CSV queries do not require these services. Re-running model-dependent stages may produce different results when model versions, inputs, dependencies, or parameters differ.

For a review limited to the **12-topic literature corpus**, use `Literature_Metadata.csv` and the source publications. The later harm-extraction and graph stages are not required. Count publications from the metadata table rather than from the number of extracted observations.

## Interpretation and limitations

- Observation records represent information extracted and coded from publications. They are not necessarily independent real-world incidents.
- Topic sizes describe this corpus, not the full distribution of research across scholarly publishing.
- Some publications concern higher education and academic integrity. Their applicability to editorial and publishing practice should be assessed individually.
- Mitigation measures reflect what sources propose or report. Inclusion does not demonstrate that a measure is effective.
- Scenario and stakeholder fields allow multiple labels, so their percentages can sum to more than 100%.
- Source traceability is at the publication level. The six-file schema does not provide page-level evidence locations or complete per-record audit trails.
- The published tables and intermediate experiment files may represent different processing stages. Use a consistent data version and record any deduplication or other preprocessing.

## Data access, licensing, and citation

Use the linked Zenodo record for the archived data release and its version-specific metadata. The manuscript describes `full_md.zip` and `MinerU.zip` as supplementary parsing resources for 147 publications, with full texts and parsing outputs withheld for the other 97 publications. Consult the release inventory for the files actually included and their conditions of use.

Third-party publications and parsing outputs retain their applicable source licenses. A license for the structured dataset does not replace those licenses. Refer to the data archive for the dataset license. No software license is specified by this README.

When citing the data, use the citation exported by Zenodo for the version used. When citing the code, include this repository URL and the Git commit or release used. Cite the accompanying paper when its final bibliographic details are available.

## Questions and corrections

Please use [GitHub Issues](https://github.com/north1202/experiment-apd/issues) to report problems or suggest corrections. Include the affected filename, `Record_ID` or `Literature_ID`, the data version or Git commit, and a short description of the issue. Do not include credentials in issue reports.
