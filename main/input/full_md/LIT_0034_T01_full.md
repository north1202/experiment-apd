Article

# Ethical Challenges of Artificial Intelligence in Higher Education: A Four-Pillar Student-Activity Framework for Institutional Governance

Radovan Madle ˇnák \* , Lucia Madle ˇnáková , Viktória Cvacho and Daniel Gachulinec

University of Žilina, Univerzitná 8215/1, 010 26 Žilina, Slovakia; lucia.madlenakova@uniza.sk (L.M.); viktoria.cvacho@stud.uniza.sk (V.C.); gachulinec@stud.uniza.sk (D.G.)   
Correspondence: radovan.madlenak@uniza.sk; Tel.: +421-41-513-31-24

## Abstract

This study introduces a four-pillar student-activity framework (Studying and Learning, Research and Projects, Personal and Career Development, and Campus and Community Life) to analyze AI’s ethical challenges in higher education. Drawing on peer-reviewed sources from 2022 to 2025, we identify recurring risks across pillars: academic integrity, privacy/data protection, bias/fairness/equity, student agency/(de)skilling, and governance gaps. We distill three cross-pillar principles: disclosure plus process evidence (e.g., prompt/version logs), privacy-by-design, and proportionality and equity/fairness scaffolds (institutional access, bias audits, and multilingual support). These translate into actionable strategies for assessment redesign, research supervision, career services, and campus operations. The framework unifies fragmented discourse, supports institutional decision making, and reveals gaps for longitudinal and causal research. It demonstrates that responsible AI use emerges when processes are visible, data practices are proportionate, and access is equitable, amplifying human learning without eroding trust or integrity.

Keywords: artificial intelligence; higher education; AI ethics; student activities; students; institutional governance; academic integrity; generative AI

## Check for updates

Academic Editor: Isabel Steinhard

Received: 3 March 2026   
Revised: 24 March 2026   
Accepted: 28 March 2026   
Published: 2 April 2026

Copyright: © 2026 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license.

## 1. Introduction

Since late 2022, advances in large language models (LLMs) and conversational agents have moved rapidly from experimentation to everyday use in universities. Students now enlist AI to brainstorm and revise assignments, plan study sessions, rehearse interviews, prototype code and analyses, coordinate student-club activities, and navigate campus services. The same affordances that make AI attractive (speed, availability, personalization) also unsettle established norms around academic integrity, authorship, privacy, equity, and the developmental aims of higher education. Much of the existing discourse treats these issues in a piecemeal manner (e.g., academic misconduct involving generative AI and AI-mediated recruitment), whereas institutional decisions must grapple with how AI actually intersects the full spectrum of student activities.

Policy frameworks focus on institutional compliance but overlook how students actually integrate AI across diverse activities. This article addresses that gap by adopting a student-activity lens. We organize a literature review into four interlocking pillars that capture what students do at university: (i) Studying and Learning, (ii) Research and Projects, (iii) Personal and Career Development, and (iv) Campus and Community Life. For each pillar, we identify the main ways AI is being used, the ethical challenges that follow (integrity; privacy/data protection; bias/fairness/equity; agency and potential de-skilling; policy/governance), and the design and policy responses proposed in recent scholarship.

Aim and contribution. Our aim is to deliver a concise, activity-aligned synthesis that helps educators, program leaders, and policy makers (a) see where AI is entering student practice, (b) understand the most salient ethical risks and safeguards in each arena, and (c) translate these insights into actionable changes to assessment, supervision, services, and governance. The contribution is threefold:

a unified, student-activity framework for analyzing ethical questions;

• a pillar-by-pillar synthesis of 2022–2025 evidence grounded in peer-reviewed sources;

a set of cross-pillar principles, disclosure with process evidence, privacy-by-design and proportionality, and equity/fairness scaffolds that generalize across contexts.

Research questions. RQ1: How does AI reconfigure key student activities across the four pillars? RQ2: What ethical risks and mitigations are reported for integrity, privacy, fairness/equity, and student agency/(de)skilling? RQ3: Which governance, pedagogical, and service-design strategies support responsible and equitable use?

Overview of the review method: We queried the Web of Science (Core Collection) for 2022–2025 (search executed in January 2026) using pillar-specific TS = topic searches that combine activity terms with AI terms. We limited the results to English articles/reviews and excluded school-level and purely medical-education items. Exports were deduplicated and screened for pillar relevance, then thematically coded for ethics constructs. The selection was documented with PRISMA-style counts: for Studying and Learning, a broad pull of 2150 records yielded 247 ethics-relevant items; Research and Projects comprised 68 records (43 synthesized); Personal and Career Development comprised 193 records (104 synthesized); and Campus and Community Life comprised 35 records (27 synthesized).

Screening and coding were conducted by the research team. The initial screening focused on a title and abstract review to assess pillar relevance and higher-education context. The full-text screening applied explicit inclusion criteria: (1) focus on higher education contexts (undergraduate or graduate students at universities or colleges), (2) explicit discussion of AI applications in student activities, and (3) substantive treatment of at least one ethical dimension. Articles were excluded if they focused exclusively on primary and secondary education, medical education outside university contexts, or technical AI development without educational application.

The coding framework emerged from an iterative process combining deductive and inductive approaches. We began with five predetermined ethical dimensions based on established AI ethics frameworks (Floridi & Cowls, 2019; Jobin et al., 2019): academic integrity and authorship, privacy and data protection, bias/fairness/equity, student agency and potential de-skilling, and governance and policy. The final codebook included codes organized hierarchically under these five main dimensions.

Articles were classified as “ethics-relevant” if they met at least one of the following criteria: (1) explicit use of ethics terminology (e.g., “fairness,” “privacy,” “integrity,” “bias,” “equity,” “transparency,” or “accountability”), (2) discussion of potential harms or risks related to AI use by students, (3) analysis of policy or governance implications, (4) recommendations for ethical design or implementation, or (5) empirical investigation of student or faculty perceptions of AI-related ethical issues.

To enhance consistency, a subset of coded articles was reviewed at multiple points during the analysis phase. Ambiguous cases were discussed with co-authors to reach a consensus on appropriate classification. Data extraction focused on: (1) pillar(s) addressed, (2) AI application(s) discussed, (3) ethical dimension(s) identified, (4) evidence type, (5) key findings or arguments, and (6) recommendations. Synthesis proceeded thematically within each pillar, identifying patterns, tensions, and gaps across studies.

## 2. Theoretical Backgrounds

A student-activity perspective on the ethics of AI in higher education draws on several well-established theories of learning, engagement, and development. Astin’s theory of involvement (Astin, 1999) foregrounds the quality and quantity of student effort as the principal driver of learning. In the context of AI, this implies that tools that compress timeon-task or automate intermediate steps can only enhance learning if they are embedded in designs that preserve deliberate practice and reflective engagement, rather than displacing them. Tinto’s model of academic and social integration (Tinto, 1975, 1993) similarly underscores that persistence depends on students’ felt connection to both the intellectual and communal life of the institution; AI that scaffolds tutoring, peer coordination, or access to services may strengthen integration, whereas opaque triage, excessive monitoring, or intrusive analytics can erode belonging and trust. Critically, Tinto distinguishes academic integration (intellectual development and faculty interaction) from social integration (peer relationships and extracurricular participation); AI tools may simultaneously strengthen academic integration through personalized tutoring while weakening social integration if they replace peer collaboration. Chickering’s vectors of student development (competence, autonomy, purpose, and integrity) extend this argument by positioning authorship, responsible agency, and ethical self-management as developmental outcomes in their own right—outcomes that AI-mediated study and authorship practices must nurture rather than supplant (Chickering & Reisser, 1993).

Complementary insights arise from Kuh’s engagement tradition (Kuh, 2008, 2009), which links high-impact practices to gains in learning and persistence. AI may broaden access to such practices (for example, through coding assistants, analytic copilots, or project management supports) yet risks stratifying participation when capabilities are paywalled, linguistically biased, or unevenly taught. Kolb’s experiential learning cycle (Kolb, 1984, 2015) clarifies the mechanism: effective learning rotates through experience, reflective observation, conceptualization, and active experimentation. AI can support the concrete experience and active experimentation phases by generating scenarios and enabling rapid prototyping, but risks bypassing reflective observation and abstract conceptualization—the phases where deep learning occurs. AI that supplies polished answers without uncertainty cues can short-circuit reflection, whereas designs that require verification, iteration, and comparison between human and AI outputs keep the cycle intact. Finally, Biggs’ 3P model (presage–process–product) situates AI as a contextual input that reshapes the learning process (Biggs, 1993; Biggs & Tang, 2011); therefore, constructive alignment must explicitly include AI governance so that the intended outcomes remain valid and interpretable.

Building on these foundations, we adopt a streamlined analytic model, guided by the principle of parsimony in maximizing explanatory power with minimal assumptions (Braithwaite, 1953), that links (i) the activity students undertake, (ii) the AI affordances that can support that activity, (iii) the ethical risk-value nodes most likely to be affected (integrity and authorship; privacy and data governance; bias, fairness, and equity; agency, (de)skilling, and wellbeing; policy and institutional governance), (iv) the design controls that mitigate risk while preserving value, and (v) the resulting outcomes (learning quality, research validity, employability, belonging, and trust). Rather than treating ethics as an external checklist, this model integrates ethical judgment into the core logic of academic and co-curricular activity design.

The model maps naturally onto the four pillars used in this review (see Figure 1). In Studying and Learning, Astin’s emphasis on effort, Kolb’s cycle, and Biggs’ alignment recommend pairing AI-enabled feedback with visible process evidence and structured verification so that efficiency gains do not come at the expense of metacognition. In Research and Projects, Kuh and Kolb’s accounts of high-impact, experiential work justify supervisory designs that combine permissible AI assistance with provenance tracking and benchmarked validation to protect epistemic quality. In Personal and Career Development, Chickering’s vectors and Tinto’s transition logic argue for AI coaching that enhances practice and feedback while retaining human oversight, transparent criteria, and fairness checks in advising and selection. In Campus and Community Life, Tinto’s social integration and Kuh’s engagement highlight the need for proportional data practices, opt-in participation, and clear escalation to human support so that smart-campus services strengthen, rather than undermine, belonging.

![](images/24ef65499239462652685b0d3c7426a4b02ca2bec8da5cc932176d1cd6c85378.jpg)  
Figure 1. The four-pillar framework for AI ethics in higher education.

Five propositions guide the subsequent synthesis. First, disclosure accompanied by process evidence (e.g., prompt/version trails and draft artifacts) enhances the reliability of judgments about integrity and contribution across all pillars. Second, privacy-by-design and proportionality are necessary conditions for legitimate AI mediation of study, research, career services, and campus life. Third, bias-aware design and equity scaffolds (including baseline institutional access to core capabilities, multilingual and accessibility support, and routine fairness audits) are required if AI is to widen rather than narrow opportunity. Fourth, metacognitive and verification scaffolds convert assistance into durable learning and skill development, reducing the risk of cognitive offloading and de-skilling. Fifth, constructive alignment must explicitly incorporate AI governance so that activities, assessments, and supports remain ethically and pedagogically coherent.

## Framework of Student Activities

The proposed framework organizes the ethical analysis of AI around four interdependent domains of student practice: Studying and Learning, Research and Projects, Personal and Career Development, and Campus and Community Life. Each domain is defined by a characteristic set of activities, typical AI affordances that mediate those activities, and a corresponding profile of ethical risk-value nodes. Rather than treating ethics as an external checklist, the framework treats these nodes as intrinsic design constraints that must be addressed to preserve learning quality, research validity, employability, belonging, and trust. Table 1 summarizes the framework structure.

Table 1. Overview of the four-pillar framework.
<table><tr><td>Pillar</td><td>Typical Student Activities</td><td>Main AI Affordances</td><td>Dominant Ethical Risk-Value Nodes</td></tr><tr><td>Studying &amp; Learning</td><td>Independent study, note-taking, drafting/revising, problem solving, formative feedback</td><td>Explanation, feedback generation, practice generation</td><td>Authorship boundaries, privacy in analytics, linguistic/cultural bias in feedback</td></tr><tr><td>Research &amp; Projects</td><td>Literature scoping, method design, coding/analysis, team collaboration, dissemination</td><td>Literature synthesis, code prototyping, data analysis</td><td>Epistemic quality (hallucinations), authorship transparency, research data governance</td></tr><tr><td>Personal &amp; Career Development</td><td>CV/portfolio curation, interview rehearsal, internship planning, up-/reskilling</td><td>Career profiling, interview simulation, skill coaching</td><td>Bias amplification in screening, over-reliance on automated coaching, data flows in career services</td></tr><tr><td>Campus &amp; Community Life</td><td>Student organizations, volunteering, campus services, wellbeing resources</td><td>Event coordination, service triage, behavioral analytics</td><td>Proportionality of monitoring, secondary data use, surveillance vs. belonging</td></tr></table>

In Studying and Learning, the activity set includes independent study, note-taking, drafting and revising written work, problem solving, receiving formative feedback, and preparing for assessment. AI affordances concentrate on explanation and exemplification, feedback generation, and practice generation. The primary ethical pressures are the blurring of authorship boundaries in take-home work, privacy concerns where tutoring and analytics capture fine-grained traces of student behavior, and fairness concerns when exemplars or feedback embed linguistic or cultural biases.

In Research and Projects, activities include scoping literature, articulating questions, designing methods and instruments, coding and data analysis, documenting provenance, collaborating in teams, and disseminating results. Ethical risks concentrate on epistemic quality (hallucinations, unverifiable citations, non-reproducible outputs), authorship and contribution transparency, and research data governance when participant information is processed by third-party systems.

In Personal and Career Development, activities range from exploring occupations and labor-market signals, curating CVs and portfolios, rehearsing interviews, and planning internships or mobility, to engaging in micro-credentialed up-/reskilling. Ethical tensions arise around profiling and data flows in career services, potential amplification of historical bias in screening or recommendation, and over-reliance on automated coaching that may crowd out reflective self-assessment.

In Campus and Community Life, activities include participating in student organizations and events, volunteering and civic engagement, using campus services, and engaging with wellbeing and safety resources. Ethical issues cluster around the proportionality of monitoring, the secondary use of behavioral data, and the risk that service automation drifts toward surveillance in social spaces that are central to belonging.

By articulating activities, affordances, risk-value nodes, and controls within each domain, the framework supplies a common grammar for aligning pedagogy, research governance, career services, and campus operations. This scaffold underpins the pillar-bypillar synthesis that follows.

Figure 2 visualizes the three cross-pillar ethical principles that emerged consistently across all four pillars in our synthesis. These principles provide actionable guidance for institutions implementing AI across the full spectrum of student activities.

![](images/5aa9d1577dda97a681e8cad763054f36526d0aeb32a95a40b35f5cf329cf297d.jpg)  
Figure 2. Three cross-pillar ethical principles for AI in higher education. These principles emerged consistently across all four pillars (Studying and Learning, Research and Projects, Personal and Career Development, Campus and Community Life) in our synthesis of 421 ethics-relevant publications from 2022 to 2025 (of which 147 were published in 2025). (1) Mandatory Disclosure with Process Evidence. (2) Privacy-by-Design and Proportionality. (3) Equity and Fairness Audits.

Principle 1: Mandatory Disclosure with Process Evidence. Students must be explicitly informed when AI is used in assessment, support systems, or decision-making processes. This includes documentation of prompts, AI versions, and iteration trails. The 2025 literature emphasizes that disclosure alone is insufficient; institutions must also require students to submit process evidence (e.g., prompt logs, draft versions) that demonstrates meaningful engagement rather than passive acceptance of AI outputs (Greenspan, 2025; Anwar, 2025; Usher & Faraon, 2025). This principle addresses academic integrity concerns while preserving AI’s legitimate role as a learning scaffold.

Principle 2: Privacy-by-Design and Proportionality. AI systems must minimize data collection to what is strictly necessary, with student consent as the default and clear optout mechanism. The principle of proportionality requires that data practices be matched to educational purpose: formative feedback systems warrant different data retention than high-stakes career-matching algorithms (Tariq et al., 2025; Al-Mahrouqi et al., 2025). Institution-governed platforms with defined retention policies and separated governance for academic versus wellbeing analytics emerged as best practices in the 2025 research.

Principle 3: Equity and Fairness Audits. Regular algorithmic auditing is essential to detect and mitigate bias, particularly in high-stakes applications such as career matching, admissions support, and mental health prediction. The 2025 literature documents concerning disparities in AI career system outcomes across demographic groups (P. Yang et al., 2025) and emphasizes the need for representative evaluation datasets, transparent reporting of algorithmic performance gaps, and remediation protocols when bias is detected. Beyond reactive auditing, this principle includes proactive equity scaffolds: baseline institutional access to core AI capabilities (preventing digital divides), multilingual and accessibility support, and student representation in AI governance processes (Kuhail et al., 2024; Faruque et al., 2025).

## 3. Methodology

To enhance transparency and replicability, we documented the review process according to the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) 2020 statement (Page et al., 2021). PRISMA provides an evidence-based minimum set of reporting items that emphasizes transparent documentation of study identification, screening, eligibility assessment, and inclusion.

The PRISMA diagram is presented in simplified form (Figure 3), reflecting the singledatabase design and the cross-pillar synthesis approach, rather than in the form of independent systematic reviews conducted separately for each pillar.

![](images/534b34b591f14122c8d738437645c21aacc3457e9b1a9fec01b977b8e166154e.jpg)  
Figure 3. Simplified PRISMA 2020 diagram for the four-pillar literature review. The diagram shows the identification, screening, eligibility assessment, and inclusion of peer-reviewed studies from the Web of Science (Core Collection, 2022–2025) across four student-activity pillars. From 2446 initial records, 421 studies were included in the final narrative synthesis and coded to five ethics constructs (integrity and authorship; privacy and data protection; bias, fairness and equity; agency, (de)skilling and wellbeing; and policy and governance).

We conducted a focused, activity-aligned review of peer-reviewed sources from the Web of Science (Core Collection). The review is organized around four domains of student practice (Studying and Learning, Research and Projects, Personal and Career Development, and Campus and Community Life) so that ethical analysis follows what students actually do at university rather than treating the phrase “AI in higher education” as an abstract, tool-centric topic. Searches were executed via Advanced Search using the TS = Topic field. For each domain, we paired pillar-specific activity terms (e.g., student learning, capstone projects, student organizations, and career development) with AI terms (artificial intelligence, machine learning, ChatGPT, generative AI, chatbot). We limited records to 2022–2025,

English, and articles/reviews and excluded school-level and purely medical-education items. Studies were eligible if they (i) were situated in higher education; (ii) treated AI as substantive to the design, delivery, evaluation, or governance of student activities; and (iii) engaged at least one ethics-relevant construct.

The query construction operationalizes the article’s student-activity lens. Each pillar’s search first foregrounds the activity (what students do) and only then intersects that activity with AI terminology. The AI term block combines general terminology (artificial intelligence, machine learning) with post-2022 vocabulary (ChatGPT, generative AI, chatbot) to avoid missing relevant studies due to shifting nomenclature. The 2022–2025 window aligns the evidence base with today’s LLM-mediated affordances and risks. Restricting to English, peer-reviewed Articles/Reviews supports interpretability and replicability.

The exact Web of Science queries used (uniform limits for all pillars: PY = 2022–2025, LA = English, DT = (Article OR Review), NOT TS = (“primary school” OR “secondary education” OR “high school” OR “medical student”)):

Studying and Learning: TS = ((“student learning” OR “study habits” OR “academic performance” OR “learning activities” OR “student engagement”) AND (“artificial intelligence” OR “AI” OR “machine learning” OR “deep learning” OR “ChatGPT” OR “generative AI” OR “chatbot”)) AND PY = 2022–2025 AND LA = English AND (DT = Article OR DT = Review).

Research and Projects: TS = ((“student research” OR “undergraduate research” OR “graduate research” OR “capstone projects” OR “group projects”) AND (“artificial intelligence” OR “AI” OR “machine learning” OR “deep learning” OR “ChatGPT” OR “generative AI” OR “chatbot”)) AND PY = 2022–2025 AND LA = English AND (DT = Article OR DT = Review).

Campus and Community Life: TS = ((“student organizations” OR “student clubs” OR “extracurricular activities” OR “student volunteering” OR “student sports”) AND (“artificial intelligence” OR “AI” OR “machine learning” OR “deep learning” OR “Chat-GPT” OR “generative AI” OR “chatbot”)) AND PY = 2022–2025 AND LA = English AND (DT = Article OR DT = Review).

Personal and Career Development: TS = ((“student internships” OR “career development” OR “employability skills” OR “student mobility” OR “study abroad”) AND (“artificial intelligence” OR “AI” OR “machine learning” OR “deep learning” OR “Chat-GPT” OR “generative AI” OR “chatbot”)) AND PY = 2022–2025 AND LA = English AND (DT = Article OR DT = Review).

Search results were exported per pillar as RIS files. Within each pillar, we performed deduplication by DOI and near-duplicate title matching. Across all four pillars, 2446 records were initially identified from the Web of Science (Core Collection) using pillar-specific topic searches executed in January 2026. No records were removed before screening due to automation tools or duplicate removal across databases as we used a single database. After deduplication within each pillar by DOI and near-duplicate title matching, all 2446 records underwent a Level-1 screening (title and abstract review). At this stage, 1921 records were excluded for not meeting one or more eligibility criteria: (i) not situated in higher education context, (ii) AI peripheral or absent from the study design, or (iii) outside the pillar’s activity scope (e.g., studies on primary or secondary education, medical students in clinical rotations, or general workforce training).

The remaining 525 records underwent a Level-2 eligibility assessment (full-record skim) to verify the presence of at least one ethics-relevant construct. At this stage, 104 records were excluded for: (i) lacking engagement with ethics-relevant constructs (integrity, privacy, bias, agency, or governance), (ii) insufficient substantive engagement with AI governance or ethical implications, or (iii) methodological limitations that prevented reliable synthesis. The final corpus of 421 studies was included in the narrative synthesis, distributed across the four pillars as follows: Studying and Learning (n = 247), Research and Projects (n = 43), Personal and Career Development (n = 104), and Campus and Community Life (n = 27). All 421 studies were coded to five ethics constructs using a concept-driven taxonomy and synthesized narratively.

Ethics coding followed a concept-driven taxonomy: (1) integrity and authorship; (2) privacy and data protection; (3) bias, fairness and equity; (4) agency, (de)skilling and wellbeing; and (5) policy and governance. Coding combined keyword heuristics with manual validation. Within each pillar x ethics construct cell, we retained three to four studies to anchor the narrative, prioritizing recency (2024–2025 where available), explicit engagement with generative AI/ChatGPT, methodological clarity, and diversity of settings.

Limitations of the methodology: This narrative review is limited by its reliance on a single database (Web of Science), an English-only corpus, and the 2022–2025 publication window. These choices may omit relevant studies indexed elsewhere (e.g., Scopus, ERIC), published in other languages, or appearing before 2022 but still conceptually important. The selective synthesis (3–4 studies per ethics construct) prioritizes recency and generative AI relevance over exhaustive coverage. Future reviews could triangulate multiple databases, include formal risk-of-bias assessments, and extend the time frame to capture earlier AI ethics debates that inform current practice.

Strengths of methodology: The student-activity lens provides a novel organizational principle that unifies fragmented discourse across pedagogy, research, career services, and campus life. Pillar-specific search strings ensure relevance to actual student practices rather than abstract tool discussions. PRISMA-style transparency in record flows, explicit eligibility criteria, and the concept-driven ethics taxonomy enhance replicability and interpretability. The three cross-pillar principles that emerge from the synthesis offer actionable, generalizable guidance for institutional governance.

## 4. Literature Review

## 4.1. Studying and Learning

Following the methodology, the Studying and Learning pillar was retrieved with a pillar-specific TS = string, limited to 2022–2025, English, and Articles/Reviews. From the broad pull (part of a 2150-record retrieval), 247 publications met the inclusion criteria and were coded to ethics constructs. Below, we synthesize representative evidence in each construct, using 3–4 studies per theme selected by recency, explicit engagement with generative AI/ChatGPT, and methodological clarity.

## 4.1.1. Academic Integrity, Student Agency, and Assessment

Multiple studies document that students increasingly use generative AI for brainstorming assignments, receiving instant feedback, drafting essays, and preparing for exams (Davar et al., 2025; Giray et al., 2025; Martha et al., 2025). Our analysis of this pillar reveals risks around authorship boundaries, privacy in learning analytics, and biased feedback that can undermine learning quality.

Across survey, design-based, and policy analyses, researchers report that generative AI blurs authorship boundaries in take-home writing and problem-solving tasks, enabling plagiarism-by-paraphrase and outsourcing of reasoning. A consistent finding is that detector-led responses are neither robust nor educationally productive; instead, assessment redesign (iterative drafting with version trails, oral/interactive defenses, and authentic artifacts) better evidences student contribution and reduces incentives for misuse (Davar et al., 2025; Giray et al., 2025; Almpanis et al., 2025). Parallel work shows that course-level policies specifying permitted uses (e.g., brainstorming, language polishing) and disclosure requirements (e.g., prompt logs, draft histories) improve student decision making and reduce anxiety by clarifying expectations (Martha et al., 2025; Khlaif et al., 2025).

A 2025 field experiment by Greenspan demonstrates that AI policy framing significantly shapes student behavior and learning outcomes (Greenspan, 2025). Students in sections with permissive AI policies showed different patterns of tool use and academic performance compared to restrictive policy sections, highlighting that institutional guidance directly influences how students engage with generative AI in coursework.

Usher and Faraon (2025) conducted a mixed-methods comparison of ChatGPT, peer, and instructor grading across varying levels of student project quality (Usher & Faraon, 2025). Their study revealed that ChatGPT grading aligned moderately well with human evaluators for high-quality projects but showed greater divergence for lower-quality work, raising questions about the reliability of AI-assisted assessment without human oversight.

## 4.1.2. Privacy and Data Protection in Study Support

Studies of AI tutors, analytics-rich platforms, and proctoring foreground risks of opaque data flows, third-party processing, and disproportionate monitoring (S. T. S. Chan et al., 2024). Phua et al. (2025) found that students value on-demand assistance but express concern about collection scope, retention, and sharing, particularly when tools are external to the institution. Conceptual and empirical work recommends data minimization, purpose limitation, and, where feasible, institution-managed assistants that keep governance and retention policies aligned with educational aims (Rienties et al., 2025). Across these studies, the emerging consensus is privacy-by-design with proportional analytics.

## 4.1.3. Bias, Fairness, Equity, and Access

Generative systems can produce fluent but biased or incorrect explanations and examples, with novices particularly susceptible to persuasive errors. Experimental and perception studies link perceived fairness and trust to learners’ engagement and creativity, and show that fairness cues shape adoption and reliance (Shahzad et al., 2024). A recent meta-analysis indicates heterogeneous effects of chatbots on learning outcomes across contexts, reinforcing the need for representative evaluation datasets and transparent provenance of exemplars (Laun & Wolff, 2025). Several classroom studies recommend embedding uncertainty signals and verification steps into AI-supported tasks to sustain epistemic vigilance (Shahzad et al., 2024; Laun & Wolff, 2025).

Vinyard and Roosa (2025) conducted qualitative interviews with 16 undergraduates about their use of generative AI for research assignments (Vinyard & Roosa, 2025). Students reported using AI primarily for grammar checking, summarizing, brainstorming, and locating sources, but expressed significant concerns about accuracy and plagiarism. Participants highlighted a need for explicit guidance on prompt crafting and source evaluation, suggesting that AI literacy must be embedded in research-methods instruction.

These bias and fairness concerns translate directly into equity and access challenges.

While AI can expand access through language simplification, multimodal feedback, and 24/7 explanations, the benefits are uneven when premium capabilities are paywalled or systems behave English-centrically. Evaluations of AI-integrated courses report learning gains where institutions provide baseline access and usage scaffolds that keep students in control of their work (Al-Labadi et al., 2025). Motivational profiles also matter: students with higher initial motivation appear to benefit more from AI-assisted study unless structured supports counteract this gradient (Amorin & Gallaron, 2025). Equity therefore depends on institutional provision, multilingual design, and explicit scaffolding.

Closely related to integrity concerns, the question of student agency and potential de-skilling represents the other side of the same coin: how AI reshapes not only what students submit but what they learn in the process.

Evidence diverges on whether AI erodes core study skills or enhances them (Thandla et al., 2024). Unstructured use can encourage cognitive offloading and weaken retrieval practice; conversely, guided self-directed use with reflection checkpoints and justification prompts is associated with stronger engagement and better-quality revisions (Giray et al., 2025). Conceptual syntheses caution that the risk is not AI assistance itself but in assistance decoupled from metacognition (Davar et al., 2025). The pattern supports designs that cultivate agency and make reasoning visible.

Buniel et al. (2025) modeled the relationship between AI dependence and research productivity among STEM undergraduates in the Philippines (Buniel et al., 2025). Their structural equation modeling revealed that while moderate AI use correlated with higher research output, excessive dependence was associated with reduced critical thinking and problem-solving skills.

Yeung et al. (2025) examined Hong Kong university students’ perceptions of how generative AI shapes learning and research practices (Yeung et al., 2025). Using the 5E instructional model framework, they found that students recognized GenAI’s potential for innovative thinking and personalized learning but expressed concerns about content accuracy, over-reliance, and the erosion of deep learning.

## 4.1.4. Policy and AI Literacy for Study Contexts

Studies converge on the value of coupling clear policies with embedded AI literacy. Effective policies articulate permitted and prohibited uses, disclosure norms, and acceptable evidence of process, while literacy components teach bias awareness, privacy choices, uncertainty calibration, and prompt craft within the first assignment that allows AI (Martha et al., 2025; Khlaif et al., 2025). Institution-level proposals make the case for governed assistants to align data practices and reduce inequities (Rienties et al., 2025). Across themes, three design principles recur: disclosure and process evidence, privacy-by-design and proportional analytics, and equity-oriented scaffolds.

## 4.2. Research and Projects

AI supports students in literature reviews, code prototyping, data analysis, and collaborative project planning, but introduces challenges to epistemic quality, authorship transparency, and research data governance. Recent studies emphasize the need for provenance tracking and verification protocols.

Using the proposed methodology, the Research and Projects pillar was retrieved with a pillar-specific TS = string, limited to 2022–2025. From 68 records exported from the Web of Science, 64 met the inclusion criteria; 43 representative studies were selected for synthesis. The corpus spans empirical case studies, design papers, perception studies, and policy/position analyses.

## 4.2.1. Policy and Governance for AI in Research

Studies converge on the need for clear, workable policies that define permissible AI uses in research and require process evidence (prompt/version logs) so human intellectual contribution remains auditable. Institutional guidance is most effective when paired with workload-aware training and aligned tools, avoiding shadow adoption of external services (Neyem et al., 2024; Greenspan, 2025). Autoethnographic accounts of thesis writing underscore the value of disclosure and traceability for legitimacy in AI-assisted scholarly work (Schwenke et al., 2023).

Greenspan’s (2025) randomized field experiment in research methods courses demonstrated that AI policy design directly influences student research behaviors and outcomes (Greenspan, 2025). Students exposed to different policy framings showed distinct patterns in how they integrated AI into literature reviews, data analysis, and writing, with implications for research integrity and skill development.

## 4.2.2. Supervision, Capacity Building, and Researcher Literacy

Evidence demonstrates that AI can scaffold early-stage research skills (for example, through interview rehearsal, protocol drafting, and code prototyping), provided use is structured and mentored. Generative AI-supported interview simulations helped novices practice qualitative techniques when combined with reflective debriefs (Millen, 2025). In computational contexts, non-programmers produced runnable domain code with guided prompting and evaluation rubrics (Delcher et al., 2025). Broader reviews recommend embedding AI literacy (bias awareness, verification routines, documentation habits) into research methods curricula and supervisory meetings to counter over-reliance (Monib et al., 2024; Schwenke et al., 2023).

Millen (2025) developed and piloted an AI-powered interview simulator for biology education that used GPT-4o and Claude-3.7 to mimic interviews with older adults (Millen, 2025). The simulator helped students prepare for real-world research interactions by improving their interviewing skills, empathy, and cultural competence. A pilot study with senior nursing students indicated improved confidence and ethical awareness.

Delcher et al. (2025) explored using ChatGPT to train non-programmers in generating genomic sequence analysis code (Delcher et al., 2025). Biology students with minimal programming experience successfully created functional code for sequence analysis tasks using guided prompts and evaluation rubrics. The study highlighted both the potential for AI to democratize computational research skills and the critical need for verification protocols.

Anwar (2025) introduced the PAIR framework (Problem, AI, Interaction, Reflection) for developing student research, critical thinking, and problem-solving skills in a law coursework assignment (Anwar, 2025). The framework successfully guided students to develop AI literacy while maintaining academic rigor, demonstrating that structured reflection can convert AI assistance into deeper learning (see Figure 4).

![](images/586a839914bbd4f6515aef9a76c339bf4f2e92fdedf669747ad5731f0f7d7a10.jpg)  
Figure 4. The PAIR framework for AI-assisted research projects (based on Anwar, 2025).

## 4.2.3. Research Integrity, Authorship, and Epistemic Quality

Across disciplines, authors report uncertainty about where assistance ends and authorship begins. Survey and policy analyses recommend disclosure norms, contribution statements, and the explicit assignment of human accountability for claims, data, and compliance (Monib et al., 2024; Yeung et al., 2025). Discussions in professional education raise concerns about token authorship and the ethics of attributing lead roles when AI has materially shaped text or analysis, advocating robust contributorship taxonomies and mentoring to prevent ghostwriting (Korytnikova et al., 2025).

Yeung et al. (2025) found that Hong Kong students using GenAI for research expressed confusion about authorship boundaries and contribution disclosure (Yeung et al., 2025). Many students were uncertain whether AI-assisted literature synthesis, data coding, or manuscript drafting constituted a form of co-authorship or required explicit acknowledgment. This ambiguity highlights the urgent need for discipline-specific guidance on AI disclosure in research outputs.

Authorship concerns are inseparable from broader questions of reproducibility and epistemic quality when AI mediates research workflows.

When AI mediates literature synthesis, coding, or analysis, risks include hallucinations, unverifiable citations, and opaque provenance. Recommended mitigations are consistent: prompt/version logging, side-by-side source verification, preregistered or benchmarked validation datasets, and explicit uncertainty cues so researchers treat model outputs as proposals rather than facts (Schwenke et al., 2023; Monib et al., 2024). Methodological work illustrates how to integrate AI-assisted steps into reproducible pipelines (Y. Yang et al., 2024).

Vinyard and Roosa (2025) documented student concerns about AI-generated source accuracy in research contexts (Vinyard & Roosa, 2025). Undergraduates reported that AI tools sometimes provided plausible but non-existent citations or misrepresented source content, creating risks for literature reviews and evidence synthesis.

## 4.2.4. Data Governance, Consent, and Privacy in Research Settings

Where AI workflows touch participant data (interviews, student artifacts, images, logs), authors foreground purpose limitation, data minimization, security-by-design, and IRB/ethics-committee alignment. Practical guidance includes consent language that explicitly covers AI processing and cross-border transfers, and institutional vetting of platforms used in research projects (Tovmasyan, 2025; Ibeh et al., 2025; Nalyvaiko, 2023).

K. C. Chan et al. (2025) proposed a human–AI collaborative framework for cybersecurity consulting in capstone projects for small businesses (K. C. Chan et al., 2025). The authors emphasized that when student projects involve real client data, AI processing must be explicitly covered in consent forms, data must be minimized and purpose-limited, and institution-vetted tools should be preferred over external APIs.

## 4.2.5. Implications for Supervision, Lab Courses, and Research Governance

Our synthesis across themes suggests a cohesive implementation stance:

Codify permissible uses with traceability. State where AI may assist and require prompt/version logs and change histories so human contribution is visible (Neyem et al., 2024; Schwenke et al., 2023).

Design supervision as a quality system. Embed verification checkpoints and reflection prompts in supervision meetings and project milestones (Millen, 2025; Delcher et al., 2025).

Protect authorship integrity. Mandate AI-use disclosure and contributorship statements; teach boundary cases (Monib et al., 2024; Yeung et al., 2025).

Engineer reproducibility. Log prompts and model versions; archive intermediate artifacts; validate AI-mediated steps against benchmarks (Schwenke et al., 2023; Y. Yang et al., 2024).

Align with data governance. Prefer institution-vetted tools, adopt purpose-limited data flows, and include AI clauses in consent when human data are processed (K. C. Chan et al., 2025; Tovmasyan, 2025).

## 4.3. Personal and Career Development

Career services leverage AI for CV optimization, interview simulations, job matching, and skill gap analysis, raising concerns about the amplification of algorithmic bias and over-reliance on automated coaching. Equity of access to premium tools is emerging as a key governance issue.

The Personal and Career Development pillar was retrieved with a pillar-specific TS = string, limited to 2022–2025. From 193 Web of Science records, 184 met the inclusion criteria after screening; 104 representative studies were synthesized. The 2025 literature shows a marked expansion in this pillar, with 84 publications focused specifically on employability and career preparation (See Figure 5).

![](images/256f6db2ce3b8bead474f158c9c48208b9d6c9ad8754863b7cfe16a250997c5a.jpg)  
Key Insight: Career development dominates 2025 Al in higher education research Focus areas - coaching, confidence-building, skills matching, interview practice, fairness monitoring  
Figure 5. Six AI applications in career development (according to 2025 research data).

## 4.3.1. Employability and the Skills Gap

Researchers conducting labor-market-facing analyses and program reports frame AI as both a disruptor of routine graduate tasks and a catalyst for demand for higher-order competencies, critical thinking, adaptability, ethical judgment, and human–AI collaboration. Studies argue for explicit up-/reskilling pathways within degree programs and microcredential ecosystems that document the human contribution alongside AI-assisted outputs (Yupelmi et al., 2024).

Xiao and Zheng (2025) examined whether ChatGPT use boosts students’ employment confidence using regression analysis, IPW, and SEM (Xiao & Zheng, 2025). Their study found that regular ChatGPT use significantly enhanced confidence in securing employment, with stronger effects among undergraduate students and those in social sciences.

Babu and Jafari (2025) developed a comprehensive AI-driven system for personalized career guidance that integrates resume parsing, company-based skill recommendation, and job recommendation (Babu & Jafari, 2025). This work demonstrates the potential for AI to scale personalized career advising while raising questions about fairness, transparency, and the need for human oversight in high-stakes career decisions.

## 4.3.2. AI Coaching, Mentoring, and Career Guidance

Studies of AI-driven coaching (cover letters/CVs critique, interview simulations, goal-attainment nudges) demonstrate promise for scalable, individualized preparation, particularly when combined with human feedback and reflection (Millen, 2025; Delcher et al., 2025). Policy and design work cautions that coaching systems must be transparent about limitations and decision logic and remain complementary to professional advising (Kuhail et al., 2024; Monib et al., 2024).

Kuhail et al. (2024) investigated college students’ perceptions of AI-delivered counseling compared to human counseling (Kuhail et al., 2024). Participants reported that the AI coach provided accessible, judgment-free support for goal setting and reflection, but emphasized the importance of human follow-up for complex career decisions and emotional support.

## 4.3.3. Bias, Fairness, Diversity, and Inclusion in Career Pathways

Studies interrogating AI-mediated screening, recommendation, and evaluation warn that historical and linguistic skews can reproduce disparities in access to internships and jobs. Perception and policy analyses call for fairness audits, representative evaluation datasets, and explicit standards for acceptable use in selection contexts (Yupelmi et al., 2024; Yeung et al., 2025).

P. Yang et al. (2025) investigated university students’ psychological and behavioral responses to AI tools in job-search contexts using quantitative analysis (P. Yang et al., 2025). Results showed that AI tools significantly reduced students’ anxiety and increased confidence during their job search, though students expressed needs for greater personalization and transparency to address trustworthiness concerns.

Cross-cultural studies from China and Hong Kong (Cao et al., 2025; He et al., 2024; Yeung et al., 2025) revealed that students’ perceptions of AI in career development vary by cultural context. Chinese students generally expressed positive attitudes toward ChatGPT’s potential for career preparation but raised concerns about content accuracy and the risk of over-reliance.

Fairness considerations extend naturally to lifelong learning and professional development, where AI tools shape ongoing skill acquisition.

Generative AI enables just-in-time microlearning, code/data exploration, and writing support for mid-program and alumni learners. Reviews and case studies report positive effects when AI activities are embedded in deliberate practice with verification steps (Monib et al., 2024; Schwenke et al., 2023). Yet access remains uneven: institutional provision and training reduce gaps linked to tool cost or prior skill (Greenspan, 2025; Delcher et al., 2025).

## 4.3.4. Privacy, Profiling, and Transparency in Career Systems

Career services and third-party platforms increasingly profile student trajectories, competencies, and fit. Articles emphasize purpose limitation, data minimization, and transparent consent language that explicitly covers AI processing. Analyses of data-intensive infrastructures further recommend clear separation of learning analytics for advising from high-stakes selection tools, with distinct governance and user rights (Nalyvaiko, 2023; Schwenke et al., 2023).

## 4.3.5. Implications for Programs, Services, and Policy

Our synthesis across themes yields a coherent implementation agenda:

Align curricula with future-proof skills. Integrate AI collaboration, uncertainty handling, and ethical reasoning into program outcomes (Monib et al., 2024; Yupelmi et al., 2024).

Use AI coaching as practice, not proxy. Deploy interview and portfolio assistants with human feedback loops, explicit limits, and reflection prompts (Millen, 2025; Kuhail et al., 2024).

Institutionalize fairness safeguards. Require audits for screening/recommendation logic; retain human oversight for decisions affecting access to internships and jobs (Yeung et al., 2025; P. Yang et al., 2025).

Adopt privacy-by-design in career platforms. Prefer institution-vetted tools; implement purpose-limited data flows and plain-language consent (Tovmasyan, 2025; Nalyvaiko, 2023).

Guarantee equitable access and literacy. Provide baseline capabilities and contextual AI-literacy training so employability gains are not contingent on paywalled tools (Greenspan, 2025; Xiao & Zheng, 2025).

## 4.4. Campus and Community Life

AI streamlines event coordination, service triage, wellbeing check-ins, and student organization management, but risks disproportionate monitoring and erosion of trust in communal spaces. Proportionality in the use of behavioral data becomes paramount for preserving belonging.

The Campus and Community Life pillar was retrieved with a pillar-specific TS = query, limited to 2022–2025. From 35 Web of Science records, 30 met the inclusion criteria; 27 representative studies were synthesized. The corpus spans evaluations of campus chatbots and service triage, case studies of student clubs and co-/extracurricular initiatives, analyses of inclusion and accessibility, and conceptual work on privacy and surveillance in smart-campus settings.

## 4.4.1. Campus Life, Community Engagement, and Inclusion

Studies report that student organizations increasingly adopt AI to curate events, coordinate projects, and scaffold peer learning. Researchers identified benefits including lower coordination costs and expanded participation for newcomers, alongside documented risks of over-automation of learning scaffolds and unequal access when advanced capabilities are paywalled. Recommended controls include lightweight contributorship statements for club projects, prompt/version logs for shared artifacts, and onboarding that teaches uncertainty reading and bias awareness (Xiao & Zheng, 2025; Faruque et al., 2025; Ahmed et al., 2025).

Xiao and Zheng (2025) documented the influence of ChatGPT on university students’ employment confidence and career readiness in higher education contexts (Xiao & Zheng, 2025). The author emphasized that AI interaction can enhance students’ professional preparedness and employment confidence, but noted the necessity to evaluate ethical and practical implications when integrating generative AI into student skill-building activities.

Evidence from community-linked learning and outreach shows AI can broaden access to multilingual, plain-language communication, event discovery, and assistive supports. Yet authors caution that community-facing deployments can inadvertently exclude or stereotype groups if content generation lacks representative prompts, accessibility checks, or human review. Institutions are advised to pair deployments with periodic inclusion audits and to publish channel-specific standards for tone, accuracy, and representation (Xiao & Zheng, 2025; Wajid & Camacho-Zuniga, 2025).

## 4.4.2. Campus Services, Safety, and Administrative AI

Universities increasingly pilot chatbots for advising, libraries, IT helpdesks, and firstline safety triage. Evaluations highlight measurable gains in responsiveness and after-hours coverage but warn about opaque escalation rules, hallucinated guidance, and the tendency for convenience features to drift toward behavioral monitoring. Effective designs clearly delimit service boundaries, display uncertainty cues with links to authoritative pages, and provide human-in-the-loop escalation with guaranteed response windows.

Faruque et al. (2025) developed a decision support system using explainable AI to reveal future career paths based on students’ surveys (Faruque et al., 2025). The authors emphasized the importance of explainability and transparency in AI-driven campus services to maintain student trust and enable informed decision making.

## 4.4.3. Wellbeing, Mental Health, Privacy, and Surveillance

Several studies explore AI supports for check-ins, reflective journaling, and resource navigation. Researchers reported benefits including lower stigma to first contact and improved wayfinding to appropriate services. These studies also identified ethical concerns centered on false reassurance, scope creep (from guidance to quasi-counseling), and privacy for sensitive disclosures. Recommended safeguards are opt-in defaults, explicit purpose limitation, data minimization, and proactive handoffs to humans when certain keywords or risk signals appear (Tariq et al., 2025; Al-Mahrouqi et al., 2025).

Tariq et al. (2025) developed an explainable AI model for the predictive modeling of student stress in higher education (Tariq et al., 2025). Using survey-based data and multiple machine learning algorithms, the study created a cost-effective, interpretable stress classification model. The authors emphasized that such systems must be opt-in, purpose-limited to wellbeing support (not surveillance), and paired with human follow-up to ensure appropriate care.

Al-Mahrouqi et al. (2025) explored university students’ attitudes toward AI mental health chatbots through qualitative analysis at Sultan Qaboos University (Al-Mahrouqi et al., 2025). Their study reinforces that AI in mental health contexts requires heightened ethical scrutiny and governance, with students raising substantial concerns about data security, cultural sensitivity, and ethical limitations that necessitate robust safeguards before campus-wide deployment.

Smart-campus initiatives (access control, occupancy sensing, incident analytics) intersect with student social spaces. Conceptual and policy analyses converge on proportionality: collect the least data necessary for a defined service; avoid secondary use; and communicate retention and sharing plainly. Where face recognition or continuous behavioral tracking is contemplated, authors recommend open impact assessments, viable non-AI alternatives, and governance separation between safety monitoring and academic analytics.

## 4.4.4. Implications for Campus Services, Student Organizations, and Governance

Our synthesis across themes yields a practical implementation agenda:

Codify AI use in student organizations. Provide simple contributorship templates, require disclosure for AI-generated outward-facing content, and teach uncertainty/bias literacy in club onboarding (Xiao & Zheng, 2025; Faruque et al., 2025).

Anchor community-facing AI in inclusion standards. Co-design prompts and review workflows with student groups; run accessibility and representation audits (Wajid & Camacho-Zuniga, 2025).

Design service chatbots for safety and legitimacy. Show capability limits and confidence indicators, link to authoritative sources, and implement human escalation with accountable timeframes.

Adopt privacy-by-design for smart-campus tools. Enforce purpose limitation, data minimization, and separation of functions; publish impact assessments and retention policies.

Use opt-in wellbeing supports with human follow-up. Keep wellbeing wayfinding distinct from therapy, log handoffs, and evaluate for false-positive/negative risk (Tariq et al., 2025; Al-Mahrouqi et al., 2025).

## 5. Discussion

The preceding four chapters traced how AI is entering students’ day-to-day practice across all four pillars, using a common, ethics-focused coding scheme. Taken together, the evidence depicts a shift from one-shot, product-centric tasks toward multi-turn, traceable workflows in which students and staff prompt, compare, verify, and explain. Benefits (greater access, rapid feedback, scalable practice) coexist with risks to integrity, privacy, fairness, and student agency when assistance is unbounded or opaque.

Two integrative patterns guide the argument. First, ethical quality emerges when processes are made visible and checkable, through disclosure and process evidence, verification routines, and role-clear accountability, rather than from tool bans or detector-led policing alone. Second, proportional data practices and equity scaffolds determine whether AI widens opportunity or entrenches disadvantage; institutional provisioning (baseline access, multilingual and accessible design) and governance (privacy-by-design, fairness audits) are decisive.

## 5.1. RQ1: How Does AI Reconfigure Key Student Activities Across the Four Pillars?

Studying and Learning. AI shifts study from purely human drafting and practice to co-production with generative systems. Core activities become more iterative and conversational: students prompt, receive alternatives, and refine. The center of gravity moves from write and submit to prompt, compare, verify, and explain. The 2025 evidence shows that assessment and evaluation have become central concerns, with 41 publications examining how AI reshapes grading, feedback, and validity (Greenspan, 2025; Usher & Faraon, 2025).

Research and Projects. In inquiry and design work, AI functions as a research scaffold for scoping literature, drafting protocols, generating code stubs, and exploring analyses. This reconfigures supervision into a quality system: checkpoints for verification, traceable prompts/versions, and benchmarked validation become routine. The 2025 literature documents a significant expansion in human–AI collaborative frameworks (24 publications) (K. C. Chan et al., 2025; Millen, 2025; Delcher et al., 2025).

Personal and Career Development. Preparation for internships and employment becomes practice-rich and personalized. The 2025 data reveal a dramatic expansion in this pillar, with 84 publications focused on employability and career preparation. Studies document AI chatbot coaches for goal attainment (Kuhail et al., 2024), AI-driven personalized career guidance systems (Babu & Jafari, 2025), and evidence that ChatGPT use significantly boosts students’ employment confidence (Xiao & Zheng, 2025).

Campus and Community Life. Clubs and services leverage AI to coordinate, curate, and triage. Social participation gains speed and scale but demands clear boundaries to avoid drifting into surveillance. The 2025 literature introduces new applications in extracurricular AI education (Xiao & Zheng, 2025), explainable AI for stress prediction (Tariq et al., 2025), and career decision support systems (Faruque et al., 2025).

Across pillars, AI converts one-shot, product-centric activities into multi-turn, traceable workflows. The 2025 evidence strongly reinforces that policy design matters: institutions that provide clear guidance, baseline access, and structured scaffolds see better learning and integrity outcomes.

## 5.2. RQ2: What Ethical Risks and Mitigations Are Reported?

Integrity and authorship. Risks: plagiarism-by-paraphrase, ghostwriting, and blurred contribution boundaries. Mitigations: disclosure with process evidence (prompt/version logs, draft trails), authentic assessments (oral defenses, data diaries, applied tasks), and contributorship taxonomies. Greenspan’s (2025) field experiment showed that permissive versus restrictive AI policies led to measurably different patterns of use and academic performance (Greenspan, 2025).

Privacy and data protection. Risks: opaque third-party processing, excessive analytics/proctoring, and function creep in services. Mitigations: privacy-by-design and proportionality (data minimization, purpose limitation), institution-vetted assistants, opt-in consent, and separated governance for wellbeing versus academic analytics (K. C. Chan et al., 2025; Tariq et al., 2025; P. Yang et al., 2025).

Fairness, bias and equity. Risks: linguistic/cultural skews in feedback and examples; disparate impacts in recommendation/screening; inequality from paywalled capabilities. Mitigations: fairness audits, representative evaluation sets, baseline institutional access, multilingual and accessibility supports. The 2025 literature documents cross-cultural variations in AI perceptions (Cao et al., 2025; He et al., 2024; Yeung et al., 2025).

Student agency, metacognition and (de)skilling. Risks: cognitive offloading, overreliance on fluent but uncertain outputs, reduced retrieval practice. Mitigations: verification routines, uncertainty cues, reflective checkpoints, and assessment designs that require students to evaluate, adapt, or reject AI suggestions. Buniel et al. (2025) found that moderate AI use correlates with higher research productivity, but excessive dependence reduces critical thinking (Buniel et al., 2025).

The literature converges on a consistent pattern: pair AI’s scale and fluency with controls that surface human reasoning (disclosure, verification), protect persons (privacyby-design), and equalize opportunity (baseline access and fairness checks). Where these controls are absent, risks dominate; where present, AI’s benefits are realized without sacrificing integrity or equity.

5.3. RQ3: Which Governance, Pedagogical, and Service-Design Strategies Support Responsible and Equitable Use?

Governance strategies require pillar-specific permitted-use policies that define allowed/prohibited applications and required process evidence (prompt logs, draft histories, contribution statements). Institutions should standardize AI disclosure across assessments, research, and career services; prefer vetted assistants with privacy impact assessments and fairness audits; and recognize that permissive policies with clear scaffolds outperform restrictive approaches (Greenspan, 2025).

Pedagogical redesign shifts assessments toward authentic tasks evidencing process (iterative drafts, verification micro-tasks) and embeds contextual AI literacy from the first permitted assignment. Baseline access to core capabilities reduces inequities, while comparative studies validate the boundaries of AI-assisted evaluation (Usher & Faraon, 2025).

Research supervision becomes a quality system with scheduled verification checkpoints, provenance tracking, benchmark validations, and structured human–AI collaboration frameworks (K. C. Chan et al., 2025; Anwar, 2025).

Career services treat AI as practice scaffolding (not proxy decision making) with mandatory fairness audits, human review of high-stakes outputs, and transparent data practices addressing perceived fairness concerns (P. Yang et al., 2025).

Campus deployments implement chatbots with capability labels, uncertainty signals, and human escalation paths; wellbeing applications adopt opt-in defaults and purposelimited analytics with proactive counselor handoffs (Tariq et al., 2025; Faruque et al., 2025).

These pillar-specific recommendations converge on a five-step implementation playbook that operationalizes the three cross-pillar principles (disclosure and evidence, privacyby-design, equity scaffolds) into institutional workflow:

1. Map and prioritize: inventory AI touchpoints by pillar; locate high-stakes decisions and sensitive data flows.

2. Codify and template: promulgate permitted-use and evidence standards; provide templates (prompt/draft logs, contribution statements, validation checklists).

3. Enable and train: provision institutional assistants; embed contextual micro-modules for literacy.

4. Assure and monitor: run privacy/fairness audits; track disclosure rates, incident profiles, equity of access/benefit, and outcome quality.

5. Iterate and share: revise policies and tasks based on evidence; publish exemplars and open artifacts.

Responsible and equitable AI use is achieved when governance, pedagogy, and services are designed as a single system: policies define the rules and evidence; teaching and supervision make those rules practicable; and services implement proportional, auditable tools. The 2025 evidence demonstrates that this alignment is not only theoretically sound but empirically validated.

## 5.4. AI Hallucinations as Pedagogical Challenge

AI hallucinations—instances where large language models generate plausible but factually incorrect content—pose a distinct pedagogical challenge in higher education. While computer scientists frame hallucinations as model limitations requiring algorithmic fixes, educators must address them as obstacles that directly threaten learning objectives and academic integrity. The confident tone with which AI systems present false information creates “epistemic vulnerability”: students may lack the domain knowledge or verification skills to distinguish accurate guidance from fabricated citations or flawed explanations (Dang & Nguyen, 2025).

AI hallucinations manifest across the four-pillar framework. In Studying and Learning, students encounter fabricated academic sources and logical inconsistencies (Danyaro et al., 2025; Li, 2025). In Research and Projects, hallucinations include non-existent citations and methodological guidance that contradicts disciplinary standards (Lane, 2025). In Personal and Career Development, AI may fabricate job market statistics. Across Campus and Community Life, chatbots may misrepresent institutional policies. What unifies these manifestations is surface plausibility combined with factual incorrectness, which exploits students’ trust in authoritative-sounding text.

Empirical studies reveal predictable patterns: initial trust, subsequent discovery, and strategic adaptation. Students initially assume AI outputs are accurate because the prose is fluent. Discovery of errors triggers “trust degradation” and frustration (Ammari et al., 2025). However, rather than abandoning AI entirely, many students develop “epistemic vigilance”: they learn to cross-reference AI outputs with authoritative sources and approach AI-generated explanations with healthy skepticism—a form of “algorithmic labor” students perform to make unreliable systems educationally useful (Ammari et al., 2025).

Hallucinations create both risks and opportunities. Students with limited prior knowledge are most vulnerable to accepting false information (Birthare, 2025). In mathematics, hallucinations in step-by-step solutions can lead to systematic errors (Steinbach et al., 2025). Research suggests students with higher prior knowledge better identify erroneous AI feedback, meaning hallucinations pose greatest risk to those who most need support (Dang & Nguyen, 2025). Over-reliance on unchecked outputs can atrophy critical evaluation skills (Zhai et al., 2024). However, when properly scaffolded, encounters with hallucinations can become pedagogical opportunities: students who learn to detect AI errors develop stronger fact-checking habits and more sophisticated understanding of knowledge validation (Li, 2025).

Institutional responses include policy-level disclosure requirements, curricular AI literacy modules teaching verification techniques, and assessment designs that expose hallucinations through oral defenses and process portfolios (Danyaro et al., 2025; Li, 2025). Some instructors now use “hallucination-aware pedagogy,” deliberately exposing students to AI-generated errors to transform error detection into an explicit learning objective (Yap & Wong, 2025). Discipline-specific approaches teach students to recognize domain-specific hallucination types and verification strategies (Lane, 2025; Chiang, 2024).

The equity dimensions demand attention: students from under-resourced backgrounds may lack the prior knowledge and information literacy skills to detect AI errors, creating a digital divide where privileged students safely leverage AI while vulnerable students are harmed (Dang & Nguyen, 2025). Institutions must ensure AI literacy interventions are culturally responsive and accessible, democratizing the capacity for critical AI engagement.

## 5.5. Epistemic Hypervigilance

Epistemic hypervigilance captures the distinctive cognitive and emotional stance students must adopt when working with AI systems. Unlike traditional learning tools students can generally trust, generative AI requires continuous questioning, verification, and interpretation. Students must treat AI as a “knowledgeable but fallible collaborator” whose contributions require critical scrutiny (Ammari et al., 2025). This demands significant cognitive resources: students must simultaneously engage with AI content, evaluate its accuracy, cross-reference claims, and make moment-by-moment decisions about which outputs to trust, modify, or reject.

This represents a fundamental shift in learning’s cognitive demands. Traditional study practices assume authoritative sources can be trusted, allowing students to focus on comprehension and application. AI-mediated learning disrupts this: students cannot simply “use” AI outputs but must actively interrogate them (Ammari et al., 2025). This creates a paradox: students who most need AI assistance (those with limited prior knowledge or constrained time) are least equipped for the hypervigilant evaluation that safe AI use requires (Dang & Nguyen, 2025).

Students must develop “algorithmic metacognition”—understanding how AI systems work, what errors they make, and when outputs are likely reliable (Reihanian et al., 2025). They must detect subtle unreliability signs: overly confident assertions, plausible-butfabricated citations, and authoritative-sounding explanations with logical gaps (Ammari et al., 2025).

The emotional dimensions are equally significant. Students describe constant uncertainty and anxiety, as they are never quite sure whether to trust AI outputs (Ammari et al., 2025). This creates cognitive dissonance: students want to believe AI outputs are accurate (saving time) but fear consequences of being wrong (academic penalties). Managing this requires emotional regulation—tolerating ambiguity and persisting in verification despite tedium. For students already experiencing academic stress, the additional emotional burden can become unsustainable, leading some to avoid AI entirely while others oscillate between uncritical acceptance and excessive skepticism (Ammari et al., 2025).

Epistemic hypervigilance also highlights tensions between necessary verification and cognitive overload. Students who fact-check every AI-generated sentence may spend more time verifying than completing the task without AI, negating efficiency gains (Ammari et al., 2025). Constant verification fragments attention and disrupts creative flow. Effective AI-mediated learning requires metacognitive strategies for deciding when verification is necessary (high-stakes claims, unfamiliar domains) versus when provisional acceptance is reasonable (low-stakes brainstorming, familiar topics).

Educational institutions must teach epistemic hypervigilance without inducing paralysis. This requires explicit instruction in verification strategies tailored to different disciplines:

citation verification for literature reviews, solution validation for problem sets, and crossreferencing for factual claims (Li, 2025). Students also need metacognitive frameworks for calibrating verification effort based on stakes and their own knowledge state.

## 5.6. Calibrated Trust

Calibrated trust addresses a fundamental paradox: students must simultaneously trust AI systems enough to benefit from assistance while maintaining sufficient skepticism to avoid being misled. Uncalibrated trust—whether naive over-reliance or blanket rejection— undermines learning. Students who trust too readily accept fabricated citations and flawed reasoning, leading to misconceptions and integrity violations (Dang & Nguyen, 2025; Ammari et al., 2025). Conversely, students who reject AI entirely forgo legitimate benefits, potentially disadvantaging themselves (Ammari et al., 2025). Calibrated trust represents a middle path: learning when to trust, when to verify, and how to integrate AI responsibly.

Calibrated trust is dynamic and context-dependent. Appropriate trust levels vary by task type, domain, stakes, and the student’s knowledge state. Low-stakes brainstorming may warrant provisional trust; high-stakes tasks demand skeptical verification. Trust should vary by domain: AI-generated grammar corrections may warrant high trust; legal citations demand rigorous verification. Students must also calibrate based on their expertise: graduate students with deep knowledge can more safely use AI than undergraduates encountering topics for the first time (Dang & Nguyen, 2025). Developing this nuanced trust requires metacognitive sophistication—assessing one’s own knowledge, recognizing task demands, and adjusting verification strategies.

Students report working with AI involves constant judgment calls: Should I trust this explanation? Is this citation real? Does this advice reflect current realities (Ammari et al., 2025)? These decisions are rarely clear-cut. AI outputs often mix accurate and inaccurate information, making wholesale acceptance or rejection inappropriate. Students must parse contributions, accepting some elements while questioning others—a cognitively demanding task requiring domain knowledge and information literacy. Making these judgments under time pressure, with incomplete information and often unclear instructor guidance, creates chronic uncertainty that many find stressful (Ammari et al., 2025).

Students’ trust decisions are shaped by perceptions of instructor expectations, institutional policies, and peer norms (Ammari et al., 2025). Clear instructor guidance about permitted uses and required verification practices increases student confidence in trust calibration. Vague or contradictory policies lead students to err toward excessive caution or risky over-reliance. Effective calibrated trust requires institutional environments communicating both AI’s benefits and limitations, providing realistic expectations and practical verification strategies.

Pedagogical implications are substantial. Rather than teaching uniform trust or distrust, educators must help students develop conditional, context-sensitive strategies. Students need explicit instruction in AI capabilities and limitations (Reihanian et al., 2025), practice in verification techniques tailored to different domains (Li, 2025), metacognitive frameworks for assessing their own knowledge, and opportunities to reflect on trust calibration experiences. Students describe relationships with AI in anthropomorphic terms— “helpful assistant,” “unreliable friend,” “knowledgeable but careless tutor”—suggesting trust calibration involves cognitive assessment plus emotional and social dynamics (Jose & Thomas, 2025). When AI provides accurate assistance, students develop positive affect and increased reliance; when AI produces errors causing harm, students experience betrayal and avoidance (Ammari et al., 2025). Effective pedagogy must acknowledge these emotional dimensions.

When students develop sophisticated trust calibration skills, they gain greater control over learning processes and can strategically deploy AI where it adds value while maintaining independent judgment where AI is unreliable. As AI systems become ubiquitous in professional and civic life, the ability to calibrate trust appropriately—knowing when to rely on algorithmic recommendations and when to seek human expertise—will be critical. Educational experiences developing this competency serve immediate learning goals and students’ preparation for lifelong learning in AI-rich environments.

Institutional strategies for fostering calibrated trust must operate at multiple levels: policy-level guidance about appropriate use and verification expectations, pedagogical embedding of trust calibration as an explicit learning objective, support-level workshops on verification techniques, and technical-level deployment of AI systems that communicate uncertainty transparently (Li, 2025). These recognize calibrated trust is not an individual skill students develop in isolation but a socio-technical achievement requiring supportive environments, clear guidance, and thoughtfully designed systems.

The three concepts—AI hallucinations as pedagogical challenge, epistemic hypervigilance, and calibrated trust—collectively illuminate the complex cognitive and emotional work students must perform to use AI responsibly. They move beyond simplistic beneficialor-harmful framings, revealing the nuanced, context-dependent judgments characterizing actual student practice. These concepts underscore that responsible AI integration requires not just technical solutions or policy mandates but sustained pedagogical attention to help students develop the metacognitive, emotional, and practical capacities needed to navigate AI-mediated learning successfully.

## 6. Conclusions

This study shows that contemporary AI reshapes university life by making student work more iterative, interactive, and documented across learning, research, career preparation, and campus participation. The clearest benefits are speed, availability of feedback, and expanded opportunities to practice complex tasks; the clearest hazards arise when outputs are accepted uncritically, when data practices outstrip educational purposes, or when access to capable tools is uneven. Across pillars, the most convincing studies point in the same direction: value is realized when human contribution remains visible, when data handling is conservative and purpose-bound, and when institutions lower structural barriers so that support is not contingent on one’s resources or language background.

The 2025 evidence base reveals three major developments that extend and refine earlier findings. First, assessment and evaluation have emerged as central concerns, with 41 publi cations examining how AI reshapes grading, feedback, and validity. Comparative studies demonstrate that AI-assisted assessment requires careful design and human oversight to maintain reliability and fairness, particularly for lower-quality work (Usher & Faraon, 2025). Field experiments show that policy framing significantly influences student behavior and learning outcomes, with permissive policies paired with clear scaffolds outperforming purely restrictive approaches (Greenspan, 2025).

Second, human–AI collaborative frameworks have matured, with 24 publications documenting structured approaches to integrating AI into research, projects, and skill development. These frameworks emphasize mentored use, verification checkpoints, and explicit documentation of AI contributions (K. C. Chan et al., 2025; Anwar, 2025). AI simulations for interview practice (Millen, 2025) and coding education for non-programmers (Delcher et al., 2025) demonstrate that AI can effectively scaffold complex skills when paired with guided practice and reflection. The PAIR framework (Problem, AI, Interaction, Reflection) provides a replicable model for developing AI literacy while maintaining academic rigor (Anwar, 2025).

Third, the employability of university students and their career development have seen dramatic growth, with 84 publications in 2025, more than double the combined total from earlier years. This expansion reflects institutional recognition that AI is fundamentally reshaping workforce readiness. However, this growth is accompanied by heightened concerns about fairness in AI-mediated screening (P. Yang et al., 2025) and the need for human oversight in high-stakes career decisions.

For educators and service leaders, the practical message is to redesign activities so that they elicit reasoning, not just polished products, and to require artifacts that show how AI was used and appraised. The 2025 evidence demonstrates that governance and pedagogy must co-evolve: institutions that couple clear policies with assessment redesign, supervisory scaffolds, and equity provisions see measurably better outcomes across all ethical dimensions.

The study has boundaries that readers should keep in mind. It draws exclusively on Web of Science records published in English between 2022 and 2025 and synthesizes heterogeneous designs narratively rather than through meta-analysis. Topic-field retrieval may miss relevant contributions, and screening and coding were conducted by a single analyst.

These constraints suggest a clear research agenda. Future work should follow cohorts over time, compare AI-supported and conventional designs with common outcome and governance measures, and report reusable artifacts. Longitudinal studies are particularly urgent given the rapid evolution of AI capabilities and institutional policies. Cross-cultural comparative research should expand beyond the China–Hong Kong studies documented here to include diverse global contexts. Causal evaluations using randomized or quasiexperimental designs (building on Greenspan, 2025) are needed to rigorously test which policy and pedagogical interventions most effectively balance AI’s benefits with integrity, fairness, and skill development.

In sum, the core finding is straightforward. The promise of AI for higher education is realized when institutions design activities and services so that evidence of learning and responsibility is easy to see, data practices are proportionate to educational aims, and access is broad enough to prevent new divides. When implemented this way, students learn more, research remains credible, career signals stay trustworthy, and campus life retains the human qualities that make universities worth defending.

Author Contributions: Conceptualization, R.M. and L.M.; methodology, R.M. and V.C.; investigation, R.M., L.M., V.C. and D.G.; resources, R.M.; data curation, V.C. and D.G.; writing—original draft preparation, R.M. and L.M.; writing—review and editing, R.M., L.M., V.C. and D.G.; visualization, V.C.; supervision, R.M.; project administration, R.M. All authors have read and agreed to the published version of the manuscript.

Funding: Slovak Research and Development Agency VV-MVP-24-0375—An ethical concept for the use of artificial intelligence in higher education.

Institutional Review Board Statement: Not applicable.

Informed Consent Statement: Not applicable.

Data Availability Statement: No new data were created or analyzed in this study.

Acknowledgments: The authors acknowledge all researchers whose work is cited in this review.

Conflicts of Interest: The authors declare no conflicts of interest.

## Abbreviations

The following abbreviations are used in this manuscript:

AI Artificial intelligence   
LLM Large language model   
GenAI Generative Artificial Intelligence   
RQ Research Question   
IRB Institutional Review Board   
SEM Structural equation modeling   
PAIR Problem, AI, Interaction, Reflection   
PRISMA Preferred Reporting Items for Systematic Reviews and Meta-Analyses

## References

Ahmed, W., Wani, M. A., Plawiak, P., Meshoul, S., Mahmoud, A., & Hammad, M. (2025). Machine learning-based academic performance prediction with explainability for enhanced decision-making in educational institutions. Scientific Reports, 15, 26879. [CrossRef] [PubMed]

Al-Labadi, L., Jazi, O. A., Ataei, M., Bao, K., & Yu, R. (2025). AI meets academia: Enhancing statistics education with ChatGPT in undergraduate courses. TechTrends, 69, 1279–1287. [CrossRef]

Al-Mahrouqi, T., Al Lawati, A., Al Aufi, H., Al Riyami, Q., & Al Sinawi, H. (2025). Students’ perceptions of AI mental health chatbots an exploratory qualitative study at Sultan Qaboos University. BMJ Open, 15, e103893. [CrossRef]

Almpanis, T., Conroy, D., & Joseph-Richard, P. (2025). Practical implications of generative AI on assessment: Snapshot of early reactions to assessment redesign in an HRM and a psychology course. The Electronic Journal ofe-Learning, 23, 19–29. [CrossRef]

Ammari, T., Chen, M., Zaman, S. M. M., & Garimella, V. R. K. (2025). How students (really) use ChatGPT: Uncovering experiences among undergraduate students. arXiv, arXiv:2505.24126. [CrossRef]

Amorin, R. B., & Gallaron, G. M. (2025). The mediating effect of learning motivation on attitudes towards using ChatGPT (ATUC) as educational resource and academic performance. MIER Journal ofEducational Studies Trends & Practices, 15(1), 214–239. [CrossRef]

Anwar, N. (2025). The use of generative artificial intelligence to develop student research, critical thinking, and problem-solving skills. Trends in Higher Education, 4, 34. [CrossRef]

Astin, A. W. (1999). Student involvement: A developmental theory for higher education. Journal ofCollege Student Development, 40(5), 518–529.

Babu, C., & Jafari, F. (2025). Empowering career development: A comprehensive AI-driven system for personalised guidance and recommendations. Cluster Computing, 28, 1028. [CrossRef]

Biggs, J. (1993). What do inventories of students’ learning processes really measure? A theoretical review and clarification. British Journal of Educational Psychology, 63(1), 3–19. [CrossRef]

Biggs, J., & Tang, C. (2011). Teaching for quality learning at university (4th ed.). Open University Press.

Birthare, A. (2025). Guarding minds: Addressing LLM hallucinations for reliable school education. International Journal of Science, Engineering and Technology, 13, 5. [CrossRef]

Braithwaite, R. B. (1953). Scientific explanation; A study of the function of theory, probability and law in science. Cambridge University Press.

Buniel, J. M., Intano, J., Cuartero, O., Grustan, K. J., Sumaoy, R., Reyes, N., Calipayan, J., Arreo, R., Duero, D., Rosil, I., Agustin, S., Diron, T. J., Pingol, R. J., Sapuras, J. V., Miranda, K., Julve, J., Josol, M., Mercado, K. R., Latoja, L., . . . Cortes, S. (2025). Modeling the influence of AI dependence to research productivity among STEM undergraduate students. Frontiers in Education, 10, 1535466. [CrossRef]

Cao, X., Lin, Y.-J., Zhang, J.-H., Tang, Y.-P., Zhang, M.-P., & Gao, H.-Y. (2025). Students’ perceptions about the opportunities and challenges of ChatGPT in higher education: A cross-sectional survey based in China. Education and Information Technologies, 30, 12345–12364. [CrossRef]

Chan, K. C., Gururajan, R., & Carmignani, F. (2025). A human-AI collaborative framework for cybersecurity consulting in capstone projects for small businesses. Journal of Cybersecurity and Privacy, 5, 21. [CrossRef]

Chan, S. T. S., Lo, N. P. K., & Wong, A. M. H. (2024). Enhancing university level English proficiency with generative AI: Empirical insights into automated feedback and learning outcomes. Contemporary Educational Technology, 16, ep541. [CrossRef]

Chiang, L. H. (2024). Navigating hallucinations in generative AI for education: A case study in legal teaching and learning. In ICERI2024 proceedings. IATED. [CrossRef]

Chickering, A. W., & Reisser, L. (1993). Education and identity (2nd ed.). Jossey-Bass.

Dang, C. T., & Nguyen, A. (2025). Distinguishing fact from fiction: Student traits, attitudes, and AI hallucination detection in business school assessment. arXiv, arXiv:2506.00050. [CrossRef]

Danyaro, K. U., Abdullahi, S., Abdallah, A. S., & Chiroma, H. (2025). Hallucinations in large language models for education: Challenges and mitigation. International Journal of Technology and Learning in Education, 4(6), 639993. [CrossRef]

Davar, N. F., Dewan, M. A. A., & Zhang, X. (2025). AI chatbots in education: Challenges and opportunities. Information, 16, 235. [CrossRef]

Delcher, H. A., Alsatari, E. S., Haastrup, A. I., Naaz, S., Hayes-Guastella, L. A., McDaniel, A. M., Clark, O. G., Katerski, D. M., Prinsloo, F. O., Roberts, O. R., Shaddix, M. A., Sullivan, B. N., Swan, I. M., Hartsell, E. M., DeMeis, J. D., Paudel, S. S., & Borchert, G. M. (2025). Using ChatGPT as a tool for training nonprogrammers to generate genomic sequence analysis code. Biochemistry and Molecular Biology Education, 53, 433–444. [CrossRef]

Faruque, S. H., Khushbu, S. A., & Akter, S. (2025). Decision support system to reveal future career over students’ survey using explainable AI. Education and Information Technologies, 30, 14471–14509. [CrossRef]

Floridi, L., & Cowls, J. (2019). A unified framework of five principles for AI in society. Harvard Data Science Review, 1, 1–14. [CrossRef]

Giray, L., Nemeno, J., & Edem, J. (2025). Self-directed learning using ChatGPT positively affects student engagement. Internationa Journal of Technology in Education, 8, 667–680. [CrossRef]

Greenspan, R. L. (2025). Artificial intelligence policies in higher education: A randomized field experiment. Journal ofCriminal Justice Education, 36, 1–14. [CrossRef]

He, A. J., Zhang, Z., Anand, P., & McMinn, S. (2024). Embracing generative artificial intelligence tools in higher education: A survey study at the Hong Kong University of Science and Technology. Journal of Asian Public Policy, 18, 352–376. [CrossRef]

Ibeh, L., Mutai, N. C., Popoola, O. M., Cuong, N. M., & Ejiofor, S. (2025). Exploring perspectives on ChatGPT integration in education: A student-centered study of benefits, concerns, and global implications for responsible AI integration. Research in Learning Technology, 33, 3384. [CrossRef]

Jobin, A., Ienca, M., & Vayena, E. (2019). The global landscape of AI ethics guidelines. Nature Machine Intelligence, 1, 389–399. [CrossRef]

Jose, B., & Thomas, A. (2025). Digital anthropomorphism and the psychology of trust in generative AI tutors: An opinion-based thematic synthesis. Frontiers in Computer Science, 7, 1638657. [CrossRef]

Khlaif, Z. N., Hamamra, B., Bensalem, E., Mitwally, M. A. A., & Sanmugam, M. (2025). Factors influencing educators’ technostress while using generative AI: A qualitative study. Technology Knowledge and Learning. [CrossRef]

Kolb, D. A. (1984). Experiential learning: Experience as the source of learning and development. Prentice Hall.

Kolb, D. A. (2015). Experiential learning: Experience as the source of learning and development (2nd ed.). Pearson Education.

Korytnikova, E., Zhou, A. E., Sloan, B., & Grant-Kels, J. M. (2025). Ethical considerations of assigning first authorship to medical students. Clinics in Dermatology, 43, 413–415. [CrossRef]

Kuh, G. D. (2008). High-impact educational practices: What they are, who has access to them, and why they matter. Association of American Colleges and Universities.

Kuh, G. D. (2009). What student affairs professionals need to know about student engagement. Journal of College Student Development, 50(6), 683–706. [CrossRef]

Kuhail, M. A., Alturki, N., Thomas, J., & Alkhalifa, A. K. (2024). Human vs. AI counseling college students’ perspectives. Computers in Human Behavior Reports, 16, 100534. [CrossRef]

Lane, R. (2025). Mitigating generative AI hallucinations in geographical education. Geographical Education, 38, 1–17. [CrossRef]

Laun, M., & Wolff, F. (2025). Chatbots in education: Hype or help? A meta-analysis. Learning and Individual Differences, 119, 102646. [CrossRef]

Li, Y. (2025). Addressing “hallucinations” in AI-generated content: Strategies for developing student fact-checking and information evaluation skills. AI Education and Social Engineering, 1(2), 48–62. [CrossRef]

Martha, A. S. D., Widowati, S., & Rahayu, D. P. (2025). Assessing student readiness and perceptions of ChatGPT in learning: A case study in Indonesian higher education. Journal of Information Technology Education: Research, 24, 023. [CrossRef]

Millen, J. I. (2025). Using generative AI for interview simulations to enhance student research skills in biology education. Journal of Microbiology & Biology Education, 26, e0012225. [CrossRef] [PubMed]

Monib, W. K., Qazi, A., Apong, R. A., Azizan, M. T., De Silva, L., & Yassin, H. (2024). Generative AI and future education: A review, theoretical validation, and authors’ perspective on challenges and solutions. PeerJ Computer Science, 10, e2105. [CrossRef] [PubMed]

Nalyvaiko, O. O. (2023). Prospects of using neural networks in higher education of Ukraine. Information Technologies and Learning Tools, 97, 1–17. [CrossRef]

Neyem, A., Gonzalez, L. A., Mendoza, M., Alcocer, J. P. S., Centellas, L., & Paredes, C. (2024). Toward an AI knowledge assistant for context-aware learning experiences in software capstone project development. IEEE Transactions on Learning Technologies, 17, 1599–1614. [CrossRef]

Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., Shamseer, L., Tetzlaff, J. M., Akl, E. A., Brennan, S. E., Chou, R., Glanville, J., Grimshaw, J. M., Hróbjartsson, A., Lalu, M. M., Li, T., Loder, E. W., Mayo-Wilson, E., McDonald, S., . . . Moher, D. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. BMJ, 372, n71. [CrossRef]

Phua, J. T. K., Neo, H.-F., & Teo, C.-C. (2025). Evaluating the impact of artificial intelligence tools on enhancing student academic performance: Efficacy amidst security and privacy concerns. Big Data and Cognitive Computing, 9, 131. [CrossRef]

Reihanian, I., Hou, Y., Chen, Y., & Zheng, Y. (2025). A review of generative AI in computer science education: Challenges and opportunities in accuracy, authenticity, and assessment. arXiv, arXiv:2507.11543. [CrossRef]

Rienties, B., Tessarolo, F., Coughlan, E., Coughlan, T., & Domingue, J. (2025). Students’ perceptions of AI digital assistants (AIDAs): Should institutions invest in their own AIDAs? Applied Sciences, 15, 4279. [CrossRef]

Schwenke, N., Sobke, H., & Kraft, E. (2023). Potentials and challenges of chatbot-supported thesis writing: An autoethnography. Trends in Higher Education, 2, 611–635. [CrossRef]

Shahzad, M. F., Xu, S., Liu, H., & Zahid, H. (2024). Generative artificial intelligence (ChatGPT-4) and social media impact on academic performance and psychological well-being in China’s higher education. European Journal ofEducation, 60, e12835. [CrossRef]

Steinbach, M., Bhandari, S., Meyer, J., & Pardos, Z. (2025). When LLMs hallucinate: Examining the effects of erroneousfeedback in math tutoring systems. Zenodo. [CrossRef]

Tariq, R., Orozco-Del-Castillo, M. G., Zamir, M. T., Ramirez-Montoya, M. S., & Wilberforce, T. (2025). Explainable artificial intelligence for predictive modeling of student stress in higher education. Scientific Reports, 15, 38375. [CrossRef]

Thandla, S. R., Armstrong, G. Q., Menon, A., Shah, A., Gueye, D. L., Harb, C., Hernandez, E., Iyer, Y., Hotchner, A. R., Modi, R., Mudigonda, A., Prokos, M. A., Rao, T. M., Thomas, O. R., Beltran, C. A., Guerrieri, T., LeBlanc, S., Moorthy, S., Yacoub, S. G., . . . Zimmerman, P. A. (2024). Comparing new tools of artificial intelligence to the authentic intelligence of our global health students. BioData Mining, 17, 58. [CrossRef]

Tinto, V. (1975). Dropout from higher education: A theoretical synthesis of recent research. Review of Educational Research, 45(1), 89–125. [CrossRef]

Tinto, V. (1993). Leaving college: Rethinking the causes and cures of student attrition (2nd ed.). University of Chicago Press.

Tovmasyan, G. (2025). Higher education in Armenia adopting AI and digital technologies: Students’ experiences and perspectives. Issues in Educational Research, 35(2), 798–817.

Usher, M., & Faraon, M. (2025). Who grades best? Comparing ChatGPT, peer, and instructor evaluations across varying levels of student project quality. Assessment & Evaluation in Higher Education, 1–20. [CrossRef]

Vinyard, M., & Roosa, M. (2025). Student perspectives on using generative artificial intelligence for research: A qualitative approach. Portal: Libraries and the Academy, 25, 729–752. [CrossRef]

Wajid, M. A., & Camacho-Zuniga, C. (2025). Mapping WUN expert discourse on responsible and ethical AI: A multinational expert network analysis. Frontiers in Communications, 10, 1689751. [CrossRef]

Xiao, Y., & Zheng, L. (2025). Can ChatGPT boost students’ employment confidence? A pioneering booster for career readiness. Behavioral Sciences, 15, 362. [CrossRef]

Yang, P., Wang, X., Zhang, J., Sivaraman, S., & Song, P. (2025). Exploring the impact of artificial intelligence on university students’ perception of slow employment a psychological and behavioral analysis. International Journal of Interactive Mobile Technologies, 19(18), 57243. [CrossRef]

Yang, Y., Luo, J., Yang, M., Yang, R., & Chen, J. (2024). From surface to deep learning approaches with generative AI in higher education: An analytical framework of student agency. Studies in Higher Education, 49, 817–830. [CrossRef]

Yap, K., & Wong, J. (2025). Teaching the unteachable: Purposeful AI hallucination as a pedagogical framework for 21st century skill development. In EDULEARN25 Proceedings. IATED. [CrossRef]

Yeung, R. S. K., Tian, R., Chiu, D. K. W., & Choi, S. P.-M. (2025). University students’ perceptions on how generative artificial intelligence shape learning and research practices: A case study in Hong Kong. The Journal ofAcademic Librarianship, 51, 103082. [CrossRef]

Yupelmi, M., Giatman, M., Ernawati, Hidayat, H., Wulansari, R. E., & Islami, S. (2024). Transformation of students’ career orientation in the era of artificial intelligence: A systematic literature review. Indonesian Journal of Computer Science, 13(3), 2510–2525. [CrossRef]

Zhai, C., Wibowo, S., & Li, L. D. (2024). The effects of over-reliance on AI dialogue systems on students’ cognitive abilities: A systematic review. Smart Learning Environments, 11(1), 28. [CrossRef]

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.