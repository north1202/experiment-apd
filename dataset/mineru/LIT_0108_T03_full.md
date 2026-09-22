Review

# Impact of Generative AI on Author’s Metrics and Copyright Ownership: Digital Labour, Ethical Attribution, and Traceability Frameworks for Future Internet Systems

Chukwuebuka Joseph Ejiyi <sup>1</sup> , Sandra Chukwudumebi Obiora <sup>2,</sup>\* , Ijuolachi Obiora <sup>3</sup>, Gladys Wauk <sup>4</sup>, Maryjane Ejiako <sup>5</sup>, Temitope Omotayo <sup>6</sup> and Olusola Bamisile <sup>1</sup>

College of Nuclear Technology and Automation Engineering, Sichuan Engineering Technology Research Centre for Industrial Internet Intelligent Monitoring Application, Chengdu University of Technology, Chengdu 610059, China; cjejiyi@cdut.edu.cn (C.J.E.); boomfem@cdut.edu.cn (O.B.)

2 Leeds Business School, Leeds Beckett University, Leeds LS1 3HB, UK

Faculty of Health, Hugh Baird University Centre, Liverpool L20 3AL, UK; ijuolachi.obiora@hughbaird.ac.uk

4 Institute of African Studies, Hunan University, Changsha 410082, China; gwauk@hnu.edu.cn

5 College of Management Science, Chengdu University of Technology, Chengdu 610059, China; ejiakomaryjane@stu.cdut.edu.cn

6 School of Built Environment, Engineering and Computing, Leeds Beckett University, Leeds LS1 3HB, UK; t.s.omotayo@leedsbeckett.ac.uk

\* Correspondence: s.s.obiora@leedsbeckett.ac.uk

## Abstract

The integration of generative artificial intelligence (GAI) into digital learning environments is a profound socio-technical transformation. While GAI promises enhanced accessibility and efficiency, it simultaneously obscures the human creativity and intellectual labour that underpins digital knowledge production. This opacity limits creators’ visibility into how their work is used, evaluated, and monetised. This review application work investigates how several leading large language models, including ChatGPT (GPT-4o), Gemini (1.5 Flash), and DeepSeek (V3), interact with a creative platform hosting over 300 original essays, poems, and artworks from various human creatives. Our review reveals that despite clear evidence of models engaging with original materials, standard platform analytics of the average creative record no attribution, referrals, or traceable interaction from their end, rendering creators’ labour invisible. This compels critical examination of knowledge provenance and power within AI-mediated education. To address this, we propose a socio-technical framework, Chujoyi-TraceNet, not as a technical fix, but a mechanism to re-centre ethics, justice, and recognition in digital governance. By integrating real-time tracking, blockchain-enabled licensing, and metadata watermarking, Chujoyi-TraceNet operationalises the principles of equitable attribution. This study argues for a re-imagining of digital ecosystems in education, one that links the technical act of attribution to broader debates on digital labour, platform ethics, and the pursuit of social justice, thereby contributing to more democratic and accountable learning media in the era of Industry 4.0 and 5.0.

## Check for updates

Academic Editors: Diego Vergara and Pablo Fernández-Arias

Received: 3 March 2026   
Revised: 25 March 2026   
Accepted: 1 April 2026   
Published: 4 April 2026

Copyright: © 2026 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license.

Keywords: generative artificial intelligence; future internet; information ethics; copyright; digital labour; content provenance; traceability and attribution; platform governance; AI accountability

## 1. Introduction

“Who owns knowledge in the age of artificial intelligence (AI)?” This question has become increasingly urgent as Large Language Models (LLMs) transform research, writing, and knowledge dissemination at an unprecedented scale [1]. Despite these advances, a true symbiosis between AI and human contributors in the knowledge creation process remains unrealised. State-of-the-art LLMs such as GPT-4.5, Deepseek, Grok-3, Gemini, Pi.ai, Phi-3, and other advanced AI systems have revolutionised how information is generated, processed, and shared, making high-quality content creation more efficient and widely accessible. Yet, their rapid rise also brings profound ethical concerns, challenging the very foundations of authorship recognition, attribution, and the responsible use of AI-generated knowledge. LLMs operate as powerful engines of information synthesis, transforming the research landscape in ways previously unimaginable [2]. By rapidly analysing vast amounts of text, generating coherent narratives, and assisting in academic and professional writing, these models streamline intellectual work, making knowledge more accessible and easily understood by its global audience [3]. Scholars, writers, and organisations leverage LLMs to expedite literature reviews, draft reports, and even co-author scientific paper models [4].

Despite these advances, LLMs introduce critical ethical challenges, particularly concerning attribution, transparency, and the invisibility of digital labour. While prior research has explored issues such as bias, misinformation, and accountability [5–7], comparatively less attention has been given to how LLMs extract, reproduce, and redistribute humancreated content without traceable attribution. This creates a structural disconnect between knowledge production and recognition, raising concerns about intellectual ownership, economic sustainability, and accountability in AI-mediated ecosystems. Across sectors such as academia, journalism, and digital publishing, attribution and visibility are central to impact, reputation, and economic value. Metrics such as citation counts, page views, and referral traffic serve as key indicators of influence and engagement [8–11]. However, these metrics fail to capture AI-mediated interactions, leaving content creators without visibility into how their work is accessed, reused, or disseminated through LLM-generated outputs.

A critical issue arises when LLMs generate responses derived from web-scraped content. In many cases, these systems neither attribute nor cite original authors, while content creators remain unaware of how, where, or by whom their work has been used. These interactions are not reflected in standard analytics metrics such as page views, location-based tracking, or referral data. As a result, human contributions become effectively invisible within AI-mediated processes, undermining recognition, traceability, and the economic value traditionally associated with content creation.

LLMs function by ingesting vast volumes of publicly available data, synthesising information without explicitly linking outputs to their original sources. Unlike traditional knowledge dissemination, where authorship and citation practices ensure recognition [12,13], AI-generated content often lacks clear provenance, thereby erasing the visibility of human intellectual labour. This opacity not only diminishes professional credibility but also raises broader ethical and legal concerns regarding intellectual property and fair use [14–17]. For knowledge-based professions, including researchers, journalists, and independent content creators such erosion of attribution has tangible consequences for career progression, reputation, and income generation [18,19].

Recent studies have explored various aspects of AI ethics, though largely at a general level. Jeon et al. examined the role of generative AI in social science research, employing a qualitative methodology to address institutionally grounded ethical frameworks [20]. Roberts et al. [21] investigated the potential risks associated with LLM assistance in the qualitative research writing process. Meanwhile, Bansal [22] analysed the accelerating paradigm shifts introduced by AI, focusing on ethical dimensions such as fairness, accountability, security, privacy, and environmental sustainability. However, these studies do not address the specific ethical challenges posed by LLMs during and after web crawling and scraping. Key gaps remain in areas such as traceability integration, attribution protocols, academic accountability, and frameworks for human reintegration into the AI-driven knowledge production process.

This study articulates three overarching novelty points. First, an in-depth review of weak research ethics in LLMs generates complex downstream effects across economic, sociological, business, and legal domains. It demonstrates how LLMs’ web scraping practices, characterised by poor traceability and the lack of digital visibility, leave a broad category of content creators (academic, journalistic, business, governmental) unaware of how their work contributes to AI-generated outputs. Illustrative webpages like apoetsbrain are used to demonstrate this gap, revealing the absence of referral metrics, location data, or traffic logs that would typically indicate content engagement. This invisibility challenges recognition, compensation, and intellectual ownership.

Second, this study proposes Chujoyi-TraceNet (CTN), a novel conceptual framework designed to address the ethical and operational deficiencies in current LLM architectures. CTN envisions a systems-level traceability infrastructure incorporating real-time content interaction tracking, dynamic licensing agreements, geospatial usage mapping, and attribution metadata. Through this, authors can determine how, where, and to what extent their work has influenced LLM outputs. Beyond technical mechanisms, CTN emphasises human reintegration in the AI-augmented knowledge lifecycle, enabling more equitable visibility, compensation, and accountability. It reframes traceability not only as a technical challenge but as a cornerstone for ethical and sustainable AI integration.

Third, in response to the growing concern over AI’s impact on productivity, innovation, and employment [23], outlines a multi-dimensional reintegration strategy for displaced human contributors. It offers a structured model for LLMs to ethically engage with content online, leaving meaningful digital footprints akin to human recognition. This model enables sector-specific measurement metrics, enhances SEO/SEM visibility for creators, promotes economic sustainability, and supports progress toward SDGs 9 and 10 in the context of Industry 4.0 and 5.0. It also delivers policy-relevant insights for LLM developers and regulators, advancing human–AI symbiosis in the creative economy.

Together, these contributions lay the groundwork for a comprehensive response to unresolved ethical issues surrounding LLMs.

## Research Objectives

This study seeks to interrogate the operational and ethical lacunae within generative AI content pipelines, with particular emphasis on LLM-mediated interactions with humanauthored online material, and to design a socio-technical framework Chujoyi-TraceNet (CTN), capable of real-time attribution and traceability. It further aims to validate this framework through simulation-based use cases, thereby assessing its potential to restore visibility, agency, and recognition to human contributors.

By examining the implications of invisible labour, poor attribution, and weak traceability across business, sociological, legal, and economic domains, the research situates content ownership within a broader ethical economy. Moreover, the study aligns CTN’s governance implications with the Sustainable Development Goals (SDGs), providing policy-relevant pathways for the reintegration of human creators into AI knowledge systems.

The paper is structured as follows: Section 2 details the theoretical underpinnings and ethical tensions in AI-driven knowledge acquisition; Section 3 introduces the CTN framework and its components; Section 4 provides use-case simulations and implications; and Section 5 concludes with policy recommendations and avenues for future research.

## 2. Related Works

## 2.1. Ethical Challenges Surrounding AI and Large Language Models (LLMs)

As LLMs become increasingly integrated into various domains, ethical concerns surrounding their deployment have gained significant attention. These challenges primarily stem from issues of bias [24], misinformation [25], lack of transparency [26], and the uncredited usage of intellectual property. Addressing these concerns is essential to ensuring the responsible and equitable development of AI technologies.

## 2.1.1. Bias, Misinformation, and Lack of Transparency

One of the most pressing ethical challenges of LLMs is the inherent bias present in their training data. Since these models learn from vast datasets sourced from the internet, historical records, and published works, they often inherit and amplify societal biases related to gender, race, politics, and culture. Studies have shown that AI-generated content can perpetuate stereotypes and reinforce prejudices [27], leading to ethical dilemmas in fields such as hiring, law enforcement, and academic publishing. Moreover, the probabilistic nature of LLMs means that they can generate factually incorrect or misleading information [28], posing risks in critical applications like medical diagnosis, legal advisory, and news reporting. Without clear mechanisms for validating AI-generated content, misinformation can spread rapidly, eroding trust in digital information ecosystems.

Transparency remains a fundamental issue in AI ethics, particularly regarding how LLMs process and generate responses [26]. These models function as “black boxes,” making it difficult to trace their decision-making processes or understand the sources that influence their outputs [29,30]. The lack of transparency undermines accountability, making it challenging for users to assess the credibility of AI-generated knowledge [31]. This opacity also raises concerns about potential manipulation, where biased or intentionally misleading content could be systematically generated without detection.

## 2.1.2. The Impact of Uncredited Usage on Intellectual Property and Creative Industries

Another significant ethical issue is the uncredited usage of intellectual property in AI-generated content. LLMs are trained on massive datasets [32] that include copyrighted books, articles, and creative works, often without explicit permission from the original authors. As a result, these models can produce text that closely resembles or directly paraphrases existing materials without proper attribution. This uncredited usage raises concerns about intellectual property violations, as authors, researchers, and content creators receive no recognition or compensation for their contributions.

The widespread deployment of AI-generated content [33–35] also threatens the sustainability of creative industries, including journalism, publishing, and academic research. Traditional revenue models for these sectors rely on readership engagement, citations, and licensing fees, all of which are undermined when AI systems generate derivative content without directing traffic or credit back to the original sources. This devaluation of intellectual labour risks job displacement for writers, journalists, and researchers, exacerbating economic disparities in knowledge-based professions.

Without robust frameworks for attribution and traceability, AI technologies risk diminishing human creativity and eroding professional opportunities in content-driven industries [36,37]. Ethical AI development must prioritise mechanisms that ensure proper recognition, transparency, and accountability, fostering a more sustainable and fair knowledge economy.

## 2.2. Traceability, Attribution, and Human Reintegration

To address these ethical concerns, traceability must become a foundational principle in AI development and deployment. Traceability here refers to the ability to track how AI systems generate content, including the sources they rely on and the transformations they apply. A robust traceability framework would ensure that authors, journalists, and researchers receive due recognition for their work, reinforcing intellectual integrity and economic fairness.

Implementing traceability in LLMs is essential for maintaining ethical AI practices and preserving intellectual integrity. By incorporating source references or citations in AIgenerated content, traceability can help restore value to authors and publishers by directing traffic back to original publications, thereby sustaining revenue models for journalists, researchers, and media outlets. Additionally, it enhances academic and ethical standards by ensuring that AI-generated research adheres to proper citation practices, mitigating the risks of misinformation and unverified knowledge proliferation. Furthermore, transparent attribution strengthens accountability in AI systems, allowing users to verify the credibility of AI-generated information and reducing the spread of biased or misleading content.

While implementing traceability presents technical and logistical challenges, its ethical necessity is clear. Without it, AI risks becoming a system that extracts value from human knowledge without giving back, undermining the very foundations of academic and journalistic integrity. Despite the growing discourse on AI ethics [17], existing research on LLMs exhibits significant gaps, particularly concerning traceability, attribution, and human reintegration into knowledge-creation processes. One of the most pressing challenges is the lack of mechanisms for traceability and attribution in AI-generated content. Current LLMs operate as black-box systems, generating text without providing clear references to their sources. This absence of transparency obscures the origins of knowledge and raises ethical concerns about intellectual property rights, credibility, and academic integrity. Without proper attribution, original content creators, including researchers, journalists, and publishers, face economic and professional disadvantages, as their contributions are neither recognised nor monetised.

Another critical oversight in AI ethics discussions is the limited focus on job restoration and human reintegration in fields disrupted by AI [38]. While much attention has been given to the risks of automation-induced job displacement [39–42], few studies propose actionable solutions for re-establishing human agency in AI-augmented workflows [43,44]. The conversation largely centres on mitigating bias and misinformation [45] rather than ensuring that AI advancements contribute to sustainable professional ecosystems. As LLMs continue to reshape industries such as academia, journalism, and publishing, it is imperative to develop strategies that reintegrate human expertise, ensuring that AI serves as a complement rather than a replacement for human intellectual labour.

The ethical and economic shortcomings of current LLMs necessitate urgent research that moves beyond critique to propose practical solutions for fair attribution, economic sustainability, and human-AI collaboration.

From a technical perspective, recent advances in machine learning and deep learning have also contributed to content attribution and provenance tracking. For instance, embedding-based similarity models, transformer architectures, and multimodal learning frameworks have been applied in tasks such as document matching, authorship identification, and image–text alignment [46]. In image analysis [47], deep convolutional and hybrid architectures have demonstrated strong capabilities in feature extraction, pattern recognition, and content reconstruction, which can be extended to support multimodal attribution and provenance tracing [48,49]. These developments highlight the potential for integrating advanced learning-based methods into traceability frameworks, although their application to LLM-driven knowledge ecosystems remains underexplored.

## 2.3. AI Provenance, Attribution, and Transparency Frameworks

Recent research has increasingly focused on AI provenance, attribution, and transparency as core requirements for responsible AI systems. Provenance frameworks aim to track the origin and transformation of data within AI pipelines [50], enabling accountability in generated outputs. Approaches such as dataset documentation, model cards, and data lineage tracking have been proposed to improve transparency in AI systems [51]. In parallel, watermarking techniques, ranging from statistical text watermarking to embedding-based signals, have been explored to identify AI-generated content and support traceability [52]. Similarly, attribution methods based on similarity modelling, embedding alignment, and information retrieval have been widely used in plagiarism detection and content matching [53]. Despite these advances, existing approaches remain limited in providing end-toend traceability that connects content access, transformation, attribution, and economic value redistribution within a unified framework. This gap motivates the need for integrated, socio-technical solutions such as the proposed Chujoyi-TraceNet framework.

## 3. Methodology

3.1. Case Study-Based Problem Presentation: The Invisible Footprint of AI Knowledge Extraction

This study adopts a qualitative case study methodology to explore how LLMs interact with publicly accessible online content, and whether such interactions leave measurable traces in standard web analytics. A case study approach is particularly suitable because the phenomenon under investigation, the invisible extraction of human-created content by AI systems, occurs within a complex, real-world setting where the boundaries between the system (LLMs) and its environment (digital publishing platforms) are not easily defined. This case is theoretically revelatory, as it exposes an underexplored phenomenon, AImediated content extraction without observable engagement signals, making it suitable for analytical generalisation rather than statistical generalisation.

The focal case is a digital creative platform established in 2018, which hosts over 300 original works, including essays, poetry, artwork, photography, and reflective writing [54]. The selection of this platform is both pragmatic and theoretically motivated. From a practical standpoint, the researchers had authorised access to the platform’s backend analytics, enabling real-time observation of engagement metrics that are typically unavailable for external platforms. This level of access is essential for examining the presence or absence of traceable interaction signals following AI-mediated content use.

From a theoretical perspective, the platform is representative of a broader class of small-scale creatives (authors, poets, journalists), bloggers, content creators, niche publishing platforms, and small and medium-sized businesses that rely heavily on standard and affordable analytics tools for visibility, attribution, and even monetisation. These platforms form a significant yet underrepresented segment of the digital knowledge economy, making them particularly relevant for studying issues of digital labour, traceability, and attribution in AI-mediated environments. Moreover, the case is revelatory in nature, as it exposes a largely unobservable phenomenon, the potential extraction and use of content by AI systems without generating measurable engagement signals. As such, the study prioritises analytical generalisation rather than statistical generalisation, aiming to extend theoretical insights into AI traceability and digital labour rather than to produce population-level inferences.

The platform’s backend provides analytics on visitor engagement, such as page views, referral sources, and visitor locations. This makes it an appropriate site for assessing whether LLM interactions leave detectable footprints. Figure 1 shows an overview of the platform and its hosted content, while Figure 2 illustrates the engagement metrics available through the platform’s built-in analytics dashboard (WordPress Analytics), which records real-time metrics including page views, referral sources, visitor counts, and geographic access data. An interaction was considered “traceable” only if it resulted in measurable changes in at least one analytics metric (page view, referral, or visitor location). The absence of such changes constituted “invisible interaction”.

![](images/ccfdea2eb14eced62d5dfb4e78e146e9f7f48595ead67da3c2106a4a65428d03.jpg)  
Figure 1. Overview of the digital platform and its content.

To examine this phenomenon, a structured experimental protocol was employed. Five LLMs, ChatGPT [55], Gemini [56], DeepSeek [57], Pi.ai [58], and Grok-3 [59] were prompted using standardised queries, including: “Tell me about www.apoetsbrain.com and its most popular poems,” “What is www.apoetsbrain.com (6 May 2025) and what type of content does it host?”, and “Identify notable or popular works from www.apoetsbrain.com (6 May 2025).” Each prompt was executed three times per model to ensure consistency, resulting in fifteen interaction instances. The experiments were conducted over a twoday period (6–7 May 2025), with all interactions time-stamped and aligned with backend monitoring windows. Analytics metrics were recorded prior to each interaction (Figure 2) and monitored for up to 60 min post-interaction at regular intervals (15, 30, and 60 min) to capture any delayed traffic signals.

![](images/0e78f9691b23e4b898c2d231bfb5de539ddfd219ddeeb134da1d22562efe1200.jpg)  
Figure 2. Backend analytics dashboard showing engagement metrics (views, visitors, referrals) [54].

Following the experimental protocol, five LLMs, ChatGPT [55], Gemini [56], DeepSeek [57], Pi.ai [58], and Grok-3 [59], were prompted with standardised queries requesting descriptions of the platform and its content. Their responses were analysed for evidence of content access, while the platform’s backend analytics were simultaneously monitored for any corresponding changes in engagement metrics.

For instance, when ChatGPT was prompted on 6 May 2025 (19:27), it generated an accurate description of the platform and provided direct URLs linking to its content (Figure 3). However, the backend analytics recorded during the same observation window showed no visits, page views, or referral sources (Figure 4), indicating no detectable interaction. This pattern remained consistent across all models. Gemini produced relevant summaries and navigational links (Figure 5), yet no corresponding engagement was observed in the analytics dashboard (Figure 6). Similarly, DeepSeek simulated exploratory interaction with the platform (Figure 7), Pi.ai demonstrated partial content awareness (Figure 8), and Grok-3 generated descriptive outputs with direct references to the site (Figure 9). Despite these outputs, backend analytics consistently failed to register any measurable footprint across all observation windows.

![](images/8bd1e752507fd3cfaf908b752ef1eae1f7fa05e3269558c30b1a20d6a27dd06a.jpg)  
Figure 3. ChatGPT’s prompt response and generated URLs (6 May 2025, 19:27) [55].

![](images/42939d322e84b4a194ffd3e2eb549031316dc8b8fb25deb4f8c476f1412c8436.jpg)

Figure 4. Backend analytics during ChatGPT’s reported access (no views recorded).  
![](images/6370947d89baa9fd7aa76533413c486a81fca5ec92b60bef0f435964180dec06.jpg)  
Figure 5. Gemini’s prompt response and generated links (7 May 2025, 09:55) [56].

![](images/75c6df09c456cc93730522931dcf41a0afc703082a47373b595df322a4bbbcba.jpg)  
Figure 6. Backend analytics during Gemini’s reported access (no footprint observed).

![](images/a72f0c00052aa8f5b69903baa38c2968435ab44209b3465c84f774e55b1f69c0.jpg)  
Figure 7. DeepSeek’s simulated browsing output (7 May 2025, 10:25) [57].

The full experimental window spanned approximately 16 h across two days, capturing both peak and non-peak periods of interaction. Across all models and repetitions, the absence of observable changes in engagement metrics confirms a consistent “no-footprint” condition, where AI-generated outputs referencing the platform did not translate into traceable user activity within standard analytics systems.

From the perspective of a small-scale content creator, these findings are deeply concerning. None of the five LLMs left a measurable footprint, even though their outputs clearly referenced the platform’s content. Even in the one instance where ChatGPT generated a tracking URL, the backend failed to register it. This disconnect highlights a systemic issue: AI systems are able to extract, repackage, and disseminate content without triggering the traditional analytics mechanisms upon which authors rely for visibility, attribution, and recognition.

For non-technical creators who depend on standard analytics to evaluate reach and audience impact, this creates profound challenges. It erodes the basis of search engine optimization (SEO) and monetization models that rely on human traffic, while exacerbating the invisibility of digital labour. As such, the case study underscores the widening digital divide: AI benefits from freely accessible content, yet the original creators are deprived of credit, recognition, and actionable insight into their audience. This raises not only ethical concerns around fairness and intellectual property but also broader implications for digital sustainability.

Ultimately, this illustrative case highlights a critical gap in the current knowledge ecosystem. While LLMs are becoming dominant tools for information access and synthesis, they simultaneously erase the feedback loops that validate and sustain human creators. Addressing this invisible footprint problem is essential to ensure equitable recognition, preserve content provenance, and support accountability in an AI-driven digital economy. While the study provides strong indicative evidence, it is limited to observable analytics and cannot directly capture internal model retrieval mechanisms, which remain proprietary.

![](images/b467def25e9764d6024c83dae39bd08b65567d1029188dc615f1aa1c2be89300.jpg)

Figure 8. Pi.ai’s partial prompt response (7 May 2025, 11:09) [58].  
![](images/6c1f5a4363bb33ef807cc0f4d60c153849f09e4c052e1ecb7a5b9122bdd1db9c.jpg)  
Figure 9. Grok-3’s prompt response (7 May 2025, 11:17) [59].

While the case study provides in-depth insight into AI–content interaction dynamics, it is inherently limited by its focus on a single digital platform and a small set of LLMs. The analysis does not cover other high-frequency domains (e.g., academic publishing, journalism, commercial content), nor does it account for multilingual or multimodal scenarios. In addition, the study relies on observable analytics data and cannot access the internal retrieval or training mechanisms of LLMs, which remain opaque. However, the objective is analytical rather than statistical generalisation, specifically to identify and characterise the “no-footprint” phenomenon in real-world AI-mediated content access. The consistent absence of traceable interaction across multiple state-of-the-art LLMs suggests that this issue is not platform-specific but indicative of a broader structural limitation. Future research should extend this work across multiple platforms, domains, languages, and content formats, while integrating complementary monitoring techniques to further validate and generalise the findings.

## 3.2. Impact on Professions

The LLMs have significantly altered the landscape of knowledge-based professions, particularly in academia, journalism, and other writing-intensive fields [60]. While these models offer enhanced efficiency and accessibility [61], they also introduce disruptive consequences, including job displacement [62] and the erosion of professional roles. Academic researchers and educators face challenges as LLMs automate literature reviews, content summarisation, and even research paper drafting, potentially diminishing the need for human expertise in scholarly communication. Similarly, in journalism, AI-generated news articles, automated reporting systems, and AI-driven content personalisation reduce the demand for human writers and editors, threatening traditional employment structures.

Beyond job displacement, the economic sustainability of these professions is also at risk due to reduced web traffic and readership engagement [63]. Digital media platforms and academic publishers rely on citation-based recognition and advertisement-driven revenue, both of which are compromised when AI systems generate content without proper attribution. Without mechanisms directing users back to sources, authors, journalists, and publishers lose critical opportunities for visibility, compensation, and professional validation. This trend devalues human contributions and also challenges the ethical foundation of knowledge dissemination, where credit and accountability are fundamental principles.

## 3.3. The Need for Traceability

As AI-generated content proliferates [64], the absence of traceability mechanisms raises significant ethical concerns. Traceability refers to the ability to track the origin of AI-generated information, ensuring that sources are credited and that knowledge transfer is transparent [65,66]. In the context of LLMs, this involves implementing robust citation systems, watermarking AI-generated content, and developing attribution frameworks that recognise human contributions.

Traceability is not only essential for preserving intellectual property rights but also for maintaining ethical AI development practices [5,67]. Without clear attribution, AIgenerated content risks amplifying misinformation [68,69], perpetuating biases [70–72], and diminishing accountability in digital knowledge systems [73–75]. Moreover, introducing traceability could restore value to authors and publishers by ensuring that AI-driven outputs generate engagement and financial compensation for original content creators. Establishing such systems would reinforce ethical norms in AI-assisted research [76], journalism, and digital publishing while mitigating the negative socio-economic effects of uncredited AI usage.

## 3.4. Current Efforts in Research Ethics and Their Limitations

Several initiatives have emerged to address the ethical concerns surrounding AIgenerated content [5,13,37,67,73], including efforts by academic institutions, publishers, and regulatory bodies to define best practices for AI-assisted research and writing [77–80]. Some AI developers have introduced citation features, dataset transparency reports, and AI content watermarking as potential solutions to attribution challenges. Additionally, organisations such as UNESCO and the European Union have proposed guidelines to regulate AI’s role in knowledge dissemination, emphasising the need for fairness, accountability, and transparency [81,82]. However, these efforts remain insufficient in addressing the full spectrum of ethical challenges posed by LLMs. Many AI-generated outputs still lack clear citation mechanisms, and existing attribution frameworks do not adequately compensate or recognise original content creators. Moreover, ethical guidelines often focus on mitigating bias and misinformation [25] while overlooking the economic impact of AI-driven content generation on professional sustainability. A more comprehensive approach is therefore required, one that integrates traceability, attribution, and economic sustainability into AI development and governance.

Building on these limitations, this study introduces a structured socio-technical framework to address the observed gaps in AI-mediated content ecosystems. The empirical findings from the case study directly inform the design of the Chujoyi-TraceNet (CTN) framework. The observed “no-footprint” condition, where LLMs accessed and utilised content without generating measurable analytics signals, reveals three critical deficiencies: lack of visibility, absence of attribution, and disconnection between content use and value recognition. These gaps motivate the core components of CTN. Specifically, the absence of detectable interaction informs the integration of real-time content fingerprinting and tracking mechanisms; the lack of attribution underpins token-level watermarking and probabilistic attribution models; and the inability to capture engagement motivates the inclusion of traceability scoring and geospatial analytics. Furthermore, the disconnect between content usage and creator benefit supports the development of a compensation model linked to attribution signals. Taken together, CTN is positioned as a problem-driven, socio-technical response grounded in empirical evidence, addressing the identified limitations while enhancing transparency, accountability, and value recognition in AI-mediated content ecosystems.

## 3.5. Proposed Framework for Traceability

To address the ethical and economic challenges posed by uncredited AI-generated content, we propose Chujoyi (Figure 10), a Framework for AI Traceability and Attribution that ensures transparent knowledge transfer, source attribution, and professional recognition. This framework integrates cryptographic techniques, probabilistic models, and web analytics within a modular system architecture (Figure 10), establishing an effective AI footprint system for traceability and attribution. It can be interpreted as a layered architecture comprising content ingestion and hashing, AI interaction, attribution modelling, traceability scoring, and analytics integration components.

The mathematical formulations presented in this section are intended as conceptual representations of how traceability and attribution mechanisms can be operationalised within AI-mediated systems, rather than as fully specified algorithms. These formulations are grounded in established techniques from cryptographic hashing [83] (e.g., SHA-256 for content fingerprinting), information retrieval and similarity modelling [84] (e.g., cosine similarity and TF-IDF weighting), and information theory [85] (e.g., entropy-based uncertainty measures). Prior research has demonstrated the applicability of such methods in digital content identification, plagiarism detection, and data provenance tracking. In this study, they are adapted to the context of generative AI to illustrate how attribution, traceability, and value distribution can be systematically modelled within a socio-technical framework.

![](images/8362dbbaec36af613098a45894f45bdb680bb9f0efe8e0ce0260359888122a15.jpg)  
The Proposed Chujoyi-TraceNet Framework  
Figure 10. The proposed Chujoyi-TraceNet Framework.

The following formulations are not intended as fully implemented algorithms but as conceptual operationalisations grounded in established principles from information retrieval, probabilistic modelling, and information theory.

## 3.5.1. Technical Design for an AI Footprint System

The following components are presented as modular design elements, illustrating how traceability can be operationalised within AI-enabled web platforms and digital ecosystems. A robust AI footprint system must satisfy key criteria, including content identification, probabilistic attribution, traceability scoring, and compensation mechanisms.

## 1. Unique Content Hashing for Source Identification

To establish the origin of AI-generated content, each knowledge unit (sentence, paragraph, or document) is assigned a unique digital fingerprint. Given an original content piece, its cryptographic hash [86] is computed as (1).

$$
H ( C _ { i } ) = S H A - 2 5 6 ( C _ { i } )\tag{1}
$$

where H(C<sub>i</sub>) Represents the cryptographic hash of the content. This supports that any AI-generated output can be compared against a database of original works, allowing traceability of knowledge origins.

## 2. Attribution Probability Model

Since LLMs process content from multiple sources, this is computed as an attribution probability function $P ( S _ { j } | O _ { k } )$ to quantify the likelihood that a source $S _ { j }$ contributed to an AI-generated output $O _ { k }$ as in (2).

$$
P \big ( S _ { j } \big | O _ { k } \big ) = \frac { \sum _ { i = 1 } ^ { n } w _ { j i } { \cdot } \delta \big ( C _ { i } , O _ { k } \big ) } { \sum _ { j = 1 } ^ { m } \sum _ { i = 1 } ^ { n } w _ { j i } { \cdot } \delta \big ( C _ { i } , O _ { k } \big ) }\tag{2}
$$

where $w _ { j i }$ is the weight assigned to the source $S _ { j }$ for content chunk $C _ { i } , \delta ( C _ { i } , O _ { k } )$ is a similarity function (such as Cosine similarity) [87] between content chunk $C _ { i }$ and the generated output $O _ { k } ,$ , m is the total number of sources, and n is the number of knowledge units within each source. This function allows for probabilistic attribution, ensuring that AI-generated content is mapped to its most likely sources.

This formulation captures the intuition that AI-generated outputs are typically derived from multiple underlying sources rather than a single origin. The attribution probability $P ( S _ { j } | O _ { k } )$ therefore represents the relative contribution of each source to the generated output, weighted by both content similarity and source importance. In practical terms, higher values of $P ( S _ { j } | O _ { k } )$ indicate stronger semantic alignment between the generated output and a given source, suggesting that the source has significantly influenced the model’s response. Within the proposed framework, this model enables partial and multisource attribution, reflecting the distributed nature of knowledge synthesis in LLMs.

## 3. Traceability Score for Generated Content

To measure the reliability of attribution, we introduce a traceability score $T ( O _ { k } )$ defined as (3).

$$
T ( { \cal O } _ { k } ) = \sum _ { j = 1 } ^ { m } P \big ( S _ { j } \big | { \cal O } _ { k } \big ) \cdot \log \left( \frac { 1 } { P \big ( S _ { j } \big | { \cal O } _ { k } \big ) } \right)\tag{3}
$$

This metric follows the Shannon entropy principle [88], where a higher score reflects greater uncertainty in attribution (i.e., lower traceability). A low traceability score suggests that the output is closely linked to a few specific sources, thus warranting proper citation.

The traceability score $T ( O _ { k } )$ provides an interpretable measure of how an AI-generated output can be linked to its underlying sources. By adopting an entropy-based formulation, the metric captures the degree of uncertainty in attribution. A low traceability score indicates that the output is dominated by a small number of sources, making attribution more precise and actionable. Conversely, a high score reflects a more diffuse contribution across many sources, resulting in greater uncertainty and reduced traceability. In practical deployment, this metric can be used as a decision threshold: outputs with low entropy can be automatically annotated with source references, while those with high entropy may require aggregation-based attribution or be flagged for limited traceability.

## 4. Compensation Model for Attribution-Based Revenue Sharing

If traceability is established, a revenue-sharing system can be designed based on the attribution weight function given as (4).

$$
R _ { j } = \alpha { \cdot } \sum _ { k = 1 } ^ { K } P \big ( S _ { j } \big | O _ { k } \big ) { \cdot } V ( O _ { k } )\tag{4}
$$

where $R _ { j }$ is the compensation or revenue allocated to the source $S _ { j } ,$ α is an adjustable revenue distribution coefficient, $V ( O _ { k } )$ represents the economic value of AI-generated output $O _ { k } ,$ and K is the number of the AI-generated output.

This function ensures that content creators are compensated in proportion to the AI’s reliance on their work.

## 3.5.2. Integration with Existing Web Analytics Tools

To make traceability actionable, we propose integrating AI attribution tracking with existing web analytics platforms like Google Analytics, OpenAI API, and blockchain-based verification systems. This integration includes:

## AI-Watermarking for Web Monitoring

Here, each AI-generated content piece should be embedded with an invisible digital watermark using Fourier transforms (5):

$$
W ( O _ { k } ) = O _ { k } + \beta { \cdot } { \sin } ( 2 \pi f _ { k } x )\tag{5}
$$

where $W ( O _ { k } )$ is the watermarked AI-generated content, $\beta$ is a scaling factor, $f _ { k }$ is a frequency modulation parameter, and x represents the spatial index of the content.

The proposed watermarking mechanism can be further strengthened by incorporating advances from existing steganography and robust watermarking literature. For instance, techniques from image steganography in colour space transformation [89] enable more effective embedding of imperceptible signals in multimodal content, improving compatibility with visual and hybrid data formats. In addition, recent work on adversarially robust watermarking demonstrates that incorporating perceptual loss functions and generative modelling can enhance resistance to tampering, removal, or distortion of embedded signals [90]. Integrating these approaches can improve the robustness and generalisability of CTN’s watermarking layer, particularly in environments where AI-generated content may be subject to modification or adversarial manipulation.

This allows web crawlers to detect AI-generated content and link it to original sources. Additionally, statistical fingerprinting (6) can be applied using Term Frequency-Inverse Document Frequency (TF-IDF). This enhances the ability to track AI-generated content across the web.

$$
S ( O _ { k } ) = \sum _ { i = 1 } ^ { n } T F - I D F ( t _ { i } ) \cdot I ( t _ { i } \in O _ { k } )\tag{6}
$$

In practice, these components can be implemented through integration with existing digital infrastructures. For instance, content hashing can be embedded at the point of data ingestion or publication, while similarity-based attribution can be operationalised using vector embeddings generated by LLM pipelines. Traceability scores can be computed dynamically as part of content auditing systems, and attribution-linked compensation models can be integrated into platform-level monetisation or licensing frameworks. Importantly, the framework does not require full modification of existing LLM architectures but can function as an overlay system, interacting with APIs, analytics tools, and blockchain-based registries to enable traceability and accountability in real-world deployments.

The security and robustness of CTN’s metadata and provenance tracking can be further enhanced by incorporating advanced techniques such as hyperchaotic encryption for secure metadata handling and grid recovery methods for improved content reconstruction [91,92]. These approaches strengthen the framework’s ability to ensure tamper-resistant and reliable attribution across complex digital environments.

## 3.5.3. System Architecture and Implementation Considerations

Building on the conceptual architecture in Figure 10, CTN can be understood as a modular system integrating content ingestion, hashing, AI interaction, and attribution analytics. Content is first processed into unique fingerprints and stored in a knowledge repository, enabling comparison with AI-generated outputs. Attribution and traceability are then derived through similarity-based matching and probabilistic modelling.

While CTN is not implemented in this study, its components align with existing technologies and can be supported using scalable, distributed infrastructures. Batch processing may be used for large-scale content indexing, while real-time monitoring can be applied to AI outputs. Common performance challenges, such as high computational load, can be mitigated through parallelisation and efficient search techniques. The architecture illustrates a feasible pathway for embedding traceability and attribution within AI systems, extending existing analytics practices without requiring fundamental redesign.

## 3.6. Alternative Frameworks for AI Attribution

## 1. Federated Attribution Learning Framework (FALF)

The concept is a distributed AI training approach where attribution is embedded into model parameters, and the core Components include:

I. Federated Learning (FL) Mechanism where AI models train across multiple sources without centralising data, following the update rule given by (7).

$$
w _ { t } = w _ { t - 1 } - \eta \nabla L ( w _ { t } ; D )\tag{7}
$$

II. Attribution-aware Backpropagation achieved by adjusting model weights based on content origin (8).

$$
w _ { t } ^ { n e w } = w _ { t } - \gamma \sum _ { j = 1 } ^ { m } P \big ( S _ { j } \big | O _ { k } \big ) \nabla L \big ( w _ { t } ; S _ { j } \big )\tag{8}
$$

III. Personalised Source Tracking, where the model tracks which sources influenced its predictions.

## 2. Web-Based Digital Rights Management (DRM) Framework

The concept here is different from the above-mentioned FALF and is based on a centralised repository where AI-generated content is cross-checked against registered sources. Its core components include:

Content Licensing Registry, where users can submit their work, and AI-generated content is compared against it. The second component is the AI Usage Transparency Dashboard, which is to be designed to track which AI models use specific content. And then Automated Copyright Violation Alerts, which can notify authors of potential uncredited usage.

To mathematically quantify licensing violations, a similarity function is computed as (9):

$$
S ( C _ { i } , O _ { k } ) = \frac { \sum _ { n } \delta \Big ( t _ { n } ^ { C _ { i } } , ~ t _ { n } ^ { O _ { k } } \Big ) } { | C _ { i } | }\tag{9}
$$

Another important function is the licensing violation metric (10), which will ensure ethical AI usage.

$$
V ( { \cal O } _ { k } ) = \sum _ { j = 1 } ^ { m } I ( S _ { j } \notin { L } ) { \cdot } P ( S _ { j } \Big | { \cal O } _ { k } )\tag{10}
$$

where $I ( S _ { j } \notin L )$ indicates unauthorised usage.

This proposed Chujoyi-TraceNet introduces a scalable and ethically robust solution for AI traceability and attribution. By integrating cryptographic hashing, probabilistic attribution models, entropy-based traceability metrics, and blockchain verification, we ensure transparent knowledge transfer, fair compensation, and accountability in AI-generated content. This framework establishes a new standard for AI ethics, protecting content creators while fostering responsible AI deployment.

## 4. Results and Discussion

## 4.1. Feasibility of Traceability Systems

## Demonstration of an AI Footprint System in Action

To illustrate the feasibility of an AI footprint system, we present a conceptual implementation in a controlled setting using a case study. Consider Case Study: AI-Generated News Content Attribution, where a major online publication, The Global Times, integrates an AI-driven article generator to assist journalists. In this illustrative scenario, the system is assumed to use an LLM to generate drafts based on vast sources, including publicly available news archives, research articles, and expert blogs.

To ensure ethical AI-generated content attribution, The Global Times adopts the Chujoyi-TraceNet (CTN) framework, which establishes a robust traceability mechanism from content origin to attribution and compensation. The process begins with content hashing, where each source document $C _ { i }$ is assigned a unique cryptographic fingerprint (1). This hash has the potential to enable real-time cross-referencing between AI-generated outputs and the original materials stored in the publication’s knowledge repository. As the AI generates new content, it is decomposed into discrete knowledge units, and attribution probabilities are computed to identify the influence of each source using a probabilistic matching function (2). This function identifies the relative influence of different sources on the generated text. A traceability score is then calculated (3) to quantify the semantic and structural alignment between AI-generated content and its originating sources. Lower traceability scores indicate stronger alignment, automatically triggering attribution and citation requirements. Lastly, a compensation model is employed (4), which redistributes revenue based on the weighted contribution of each source. This is designed to support fair recognition and economic inclusion, and it encourages ethical content reuse, thus aligning AI-assisted journalism with principles of transparency, equity, and digital sustainability. This scenario is conceptual and serves to demonstrate how the proposed framework could operate in practice rather than representing a deployed system.

## 4.2. Potential Challenges and Solutions in Implementation

While AI footprint systems offer promising avenues for enforcing traceability and attribution, several implementation challenges must be addressed to ensure their practical viability.

One of the primary challenges is scalability and performance. Real-time operations such as hashing, similarity computations, and probabilistic attribution over massive textual datasets are computationally intensive. To mitigate these limitations, scalable architectures can be conceptually implemented using approximate nearest neighbour (ANN) search methods for efficient similarity detection. Additionally, blockchain storage systems can facilitate decentralised and tamper-proof tracking of content usage, balancing performance with traceability integrity. Another major obstacle is resistance from AI content providers. Developers and organisations may hesitate to adopt traceability mechanisms due to perceived trade-offs in computational efficiency or concerns about model performance degradation. This can be addressed through the adoption of Federated Attribution Learning Frameworks (FALF), where attribution is embedded within decentralised AI training processes. This is designed to support models to respect content ownership without the need to centralise sensitive training data, preserving both performance and privacy.

The robustness of AI watermarking presents another technical challenge. Watermarks embedded in AI-generated content can often be removed or distorted through adversarial attacks or minor textual alterations. To enhance resilience, techniques such as Fourier watermarking and statistical fingerprinting can be employed using the watermark function (11), for instance. This adds an imperceptible signature that resists tampering and preserves traceability under content transformation.

$$
W ( O _ { k } ) = O _ { k } + \beta { \cdot } { \sin } ( 2 \pi f _ { k } x )\tag{11}
$$

However, it is important to note that the watermarking mechanism presented in this study is conceptual and has not been empirically evaluated against transformations such as rewriting, summarisation, or adversarial removal. Addressing these limitations would require the integration of more robust, transformation-invariant watermarking techniques, which remain an important direction for future work.

Ethical and legal compliance also represents a significant challenge. Attribution laws and regulations vary across jurisdictions, making it difficult to enforce a single standard globally. To address this, the development of international AI governance protocols, supported by centralised Digital Rights Management (DRM) frameworks, is essential. These systems can ensure consistent monitoring, licensing, and enforcement of attribution standards, regardless of geographical or legal boundaries.

While there are non-trivial technical, legal, and organisational barriers, this analysis suggests that traceable AI content generation is both feasible and ethically imperative. By integrating cryptographic hashing, probabilistic attribution modelling, and compensation mechanisms within a cohesive system, AI footprint frameworks can restore transparency and accountability in digital content ecosystems. Success will depend on multi-stakeholder collaboration involving AI developers, legal experts, policymakers, and content creators to ensure the responsible use of generative technologies.

## 4.3. Impact on Authors and Publishers

Restoring Recognition and Value to Content Creators

## Case Study: AI in Digital Publishing and Author Recognition

Consider the case of the ScholarNet Publishing Platform, a digital repository for academic and creative works. With the rise of generative AI, the platform faced increasing complaints from authors whose articles were being paraphrased and repackaged by AI models without citation. To address this, ScholarNet integrated the Chujoyi-TraceNet (CTN) to ensure attribution and enforce digital ownership. The CTN operates through a multi-stage process beginning with embedding digital signatures in published content. Every article is assigned a cryptographic watermark using a combination of Stylometric Analysis (SA) and Lexical Hashing (LH). This is expressed mathematically as (12)

$$
W ( A _ { i } ) = H ( A _ { i } ) \oplus F ( S A ( A _ { i } ) )\tag{12}
$$

where $H ( A _ { i } )$ is the cryptographic hash of the article $A _ { i }$ and $F ( S A ( A _ { i } ) )$ represents the stylometric features unique to the author’s writing style.

Next, AI content attribution matching is carried out whenever AI-generated content exhibits noticeable similarity to archived documents. A content match probability score is computed using Equation (13).

$$
P ( A _ { i } | G _ { k } ) = { \frac { S ( A _ { i } , G _ { k } ) } { \sum _ { j = 1 } ^ { m } S \left( A _ { j } , G _ { k } \right) } }\tag{13}
$$

where $S ( A _ { i } , ~ G _ { k } )$ represents the semantic similarity between the AI-generated content $G _ { k }$ and the original article $A _ { i } .$ . This is designed to support that probable content sources are correctly attributed.

In the final stage, automated author recognition and citation enforcement are to be mandated such that any AI platform utilising text from ScholarNet would require embedding author metadata before content is published, thereby encouraging attribution as a standard practice. The implementation of CTN is conceptually expected to improve attribution visibility, potentially increasing formal citations and reducing unauthorised AI-based content reuse, although these outcomes require empirical validation. This case study illustrates how traceability can restore recognition to content creators, ensuring that human-generated work retains its intellectual value even in an AI-driven ecosystem.

Taken together, the findings and conceptual analysis demonstrate the potential of Chujoyi-TraceNet (CTN) to address critical gaps in AI-mediated knowledge ecosystems. By integrating real-time content fingerprinting, probabilistic attribution, and traceability scoring, CTN makes previously invisible AI–content interactions observable and measurable, thereby enhancing traceability. The incorporation of token-level watermarking further strengthens the linkage between generated outputs and their original sources, supporting more transparent and accountable attribution. From a governance perspective, CTN provides a socio-technical foundation for aligning AI systems with principles of fairness, accountability, and recognition, with implications for regulatory frameworks, platform policies, and organisational decision-making. Although requiring empirical validation, the framework represents a meaningful step toward more transparent, equitable, and sustainable AI-driven digital ecosystems.

## 5. Proposed Framework Towards Better AI Research Ethics and Higher Human-Reintegration

The increasing sophistication of AI systems has raised concerns regarding ethical AI usage, accountability, and human reintegration in AI-driven ecosystems. To address these issues, this framework introduces a structured approach that integrates AI research ethics with mechanisms ensuring transparent AI interactions, responsible content generation, and enhanced human-AI collaboration.

## 5.1. Technical Design

The proposed CTN framework emphasises a traceability-first approach, ensuring that AI models interacting with digital environments leave a unique and verifiable identifier while maintaining compatibility with existing web analytics tools.

## 5.1.1. Mechanisms for AI to Leave a Unique Identifier on Visited Websites

To ensure transparency and ethical accountability, AI models should be required to embed a digital footprint whenever they visit, extract, or generate content from a website. This identifier would allow website owners, regulators, and content creators to track AI interactions, preventing unauthorised content scraping or misuse.

To establish robust traceability in AI content interactions, several technically feasible approaches can be explored, and some have been proposed. One such approach is AI digital watermarking [93], whereby each AI system is assigned a unique cryptographic identifier embedded into its operations. This identifier is activated whenever the AI reads, extracts, or generates content, allowing it to automatically tag the source material. This tagging mechanism facilitates seamless traceability, ensuring that original content creators receive due recognition and enabling regulatory bodies to audit AI behaviour. In addition, blockchain-based interaction logging [94] offers a secure and immutable method for tracking AI activities. Each instance of content retrieval, transformation, or reuse by an AI model can be recorded on a decentralised blockchain ledger. This ledger ensures that all interactions are transparent, tamper-proof, and verifiable, creating a foundation for trustworthy AI accountability. Another promising method can involve metadata injection into HTTP requests. Here, AI agents embed distinct metadata within HTTP headers when accessing online content. This metadata signals the AI’s identity and purpose, allowing websites to detect, log, and analyse AI-driven traffic independently from human visitors. Such mechanisms enhance the capability of content platforms to monitor AI access patterns and respond accordingly.

A practical example of these mechanisms in action is TikTok’s initiative to automatically label AI-generated content, even if created outside its platform [95]. By utilising digital watermarks developed by the Coalition for Content Provenance and Authenticity (C2PA), TikTok enhances transparency and helps users identify synthetic media [96]. This move shows the tangible benefits of implementing traceability measures, not only in fostering ethical compliance but also in building user trust and mitigating misinformation.

These illustrate the feasibility and advantages of integrating unique identifiers into AI interactions with digital content. By adopting such mechanisms, we can enhance transparency, uphold content creators’ rights, and promote responsible AI usage across digital platforms.

## 5.1.2. Ensuring Compatibility with Existing Web Analytics Tools

To maintain stability and continuity in existing digital ecosystems, the successful deployment of AI traceability systems requires seamless integration with current web analytics platforms such as Google Analytics, Adobe Analytics, and Matomo. Ensuring compatibility will help avoid disruption to existing monitoring processes as well as enable a holistic view of web traffic that includes both human and AI interactions.

One core strategy involves enabling AI identifier tracking within web analytics dashboards. This allows website analytics tools to distinguish AI agents from human users, classifying and presenting AI activity separately. As AI systems engage with content, whether through scraping, summarisation, or content retrieval, their behaviours can be logged, quantified, and interpreted within the same reporting interfaces that web administrators already use. This approach provides transparency into AI usage trends, frequency of content access, and potential misuse, supporting better-informed decisions by content owners. To further standardise AI-related transparency, an AI Compliance API for websites can be introduced. This opt-in tool would work alongside web analytics platforms to flag and log AI-driven interactions. When enabled, the API enforces ethical compliance by detecting AI activities, applying traceability tags, and making this data accessible to site owners. This offers a straightforward route for websites to align with ethical AI standards without overhauling existing infrastructure.

Another crucial layer of integration involves tag management for AI traceability. Just as tag managers like Google Tag Manager [97] allow tracking of human user events, AI systems can embed standardised tags during interaction. These tags allow site administrators to monitor, regulate, or restrict AI engagement according to defined policies. Moreover, this tagging mechanism ensures alignment with major data protection and transparency laws such as GDPR, CCPA, and emerging AI-specific regulations.

A conceptual model suggests that integrating AI interaction logs into platforms like Google Analytics could allow site administrators to differentiate between human and AI behaviours. Such functionality would support more accurate traffic reporting, improve AI training outcomes, and enhance transparency and compliance. In theory, this could reduce user concerns about bias, strengthen regulatory alignment, and foster trust in AI-enhanced services.

## 5.2. Reporting and Analytics

The implementation of AI traceability mechanisms necessitates a comprehensive reporting and analytics framework capable of systematically monitoring and evaluating AI interactions with digital content. This framework will reinforce transparency and ethical compliance and empower content creators, publishers, and regulatory bodies to make informed decisions based on reliable data. Reporting on AI usage helps assess the extent of AI engagement across different knowledge domains and ensures that original contributors receive appropriate recognition and protection under evolving digital content laws.

## 5.2.1. Periodic Reporting on AI Usage of Specific Fields or Sources

To improve transparency and accountability in AI content interaction, periodic reporting mechanisms should be standardised and enforced. These reports would offer structured visibility into how AI systems engage with different types of content and knowledge domains, whether for purposes such as training, summarisation, recommendation, or content generation. Regular reporting is essential for maintaining an ethical and legally compliant AI ecosystem, particularly as the role of AI continues to grow across digital content workflows.

A central strategy to achieve this transparency involves the development of automated AI usage dashboards that produce monthly or quarterly summaries of AI-driven content interactions. These dashboards would display detailed metrics that include the categories and domains of content accessed, such as journalism, academic research, or healthcare; the volume and types of data retrieved; the specific context in which the data was used, whether for training models or for real-time tasks like summarisation; and the level of source integrity and attribution maintained. This level of granularity would empower stakeholders, including content creators, intellectual property holders, and regulators, to assess whether AI systems are functioning within appropriate ethical and legal frameworks, in addition to having information on how the information is being disseminated.

By disaggregating data based on specific domains, these dashboards could also illuminate sectors where AI reliance is disproportionately high. Such insights could trigger targeted policy responses. For instance, if AI systems are found to heavily consume academic literature, it could prompt the development of new citation requirements, the establishment of licensing frameworks for academic content, or even financial compensation mechanisms for original authors and researchers. Thus, periodic reporting would not only aid in regulatory oversight but also inform broader debates on equity and value distribution in AI ecosystems.

Furthermore, these AI usage reports would serve as the foundation for compliance audits conducted by either regulatory authorities or independent watchdog entities. Integrating the reporting tools into broader governance frameworks would enable automated anomaly detection, such as instances where protected content is accessed without proper attribution, or when AI activity appears to violate licensing terms. These irregularities could be automatically flagged for further review, creating a hybrid human-AI oversight loop. This layered mechanism would enhance both scalability and precision in enforcing compliance and ensuring trustworthiness in AI practices.

To structure these mechanisms systematically, the AI Usage Transparency Framework (AI-UTF) Figure 11 can be applied. This framework consists of three interconnected components. The first is the AI Interaction Logging Engine, which is embedded directly into AI models. It captures and logs all content interaction events along with essential metadata such as the domain, timestamp, source type, and the intent behind the interaction. This creates a traceable and verifiable record of AI activities.

![](images/f9e74865a9679f8955336ca279cfabe50c5621231038c92f39c60ec4bb416fef.jpg)  
Conceptual Model: AI Usage Transparency Framework (AI-UTF)  
Figure 11. The conceptual AI Usage Transparency Framework (AI-UTF).

The second component is the Usage Dashboard Interface, which acts as a dynamic visualisation layer. It aggregates insights across time periods and presents them in a segmented manner based on domain and compliance indicators. Stakeholders can utilise this interface to monitor AI behaviour in real-time or review historical summaries, offering a clear lens into the system’s behaviour and alignment with governance expectations.

The third component is the Regulatory Compliance Layer, which connects with licensing registries and legal databases to assess whether AI interactions conform to intellectual property rules, fair use guidelines, and contractual agreements. This layer includes an alert system for flagging irregular patterns and can automatically generate audit-ready compliance reports. These outputs can support institutional reviews and legal enforcement where needed.

Together, these components form a robust and auditable pathway for monitoring AI’s interaction with human-authored content. The AI-UTF model offers a scalable infrastructure to safeguard ethical integrity and accountability while allowing AI-driven innovation to flourish responsibly.

## 5.2.2. Creation of a Meta-Database for Authors and Publishers to Track Impact

To further strengthen traceability and ensure recognition and reward for original content creators, this framework proposes the establishment of a centralised meta-database designed specifically for authors, publishers, and content creators. This database would serve as a transparent digital registry that tracks AI interactions with published materials in real time, enabling users to view how their content is accessed, cited, and utilised by AI systems. The overarching aim is to provide a fair and accountable system that bridges the gap between content generation and AI consumption.

One of the foundational components of this meta-database is an AI Attribution Registry, where AI systems are required to log interactions with content. By embedding unique cryptographic identifiers into both AI systems and content entries, the registry can ensure that each engagement with a piece of content is traced back to its original source. This allows authors and publishers to monitor how their materials are being used and, where appropriate, initiate compensation claims.

Another core feature is the provision of impact metrics and citations, which deliver actionable insights into how AI-generated content builds upon original works. These analytics can include citation counts, references within AI-generated summaries, frequency of derivative content creation, and domain-specific influence assessments. Through these metrics, authors gain a clear understanding of their content’s reach and influence in the AI-driven knowledge ecosystem.

Additionally, the meta-database would enable content monetisation and smart licensing models using blockchain technology. Content creators could establish customised licensing terms, such as access fees or usage limits, which would be automatically enforced through smart contracts. This innovation allows for scalable, automated micropayments when AI models utilise registered content, ensuring that economic value flows back to the rightful owners.

Consider a hypothetical case in the journalism sector, where a consortium of publishers and AI developers launches an AI impact-tracking meta-database for news content. In this scenario, journalists could access dashboards showing which AI models referenced their work and how it was incorporated into generated reports. The system would include automated micropayments to content creators, enabling new revenue streams and promoting ethical AI practices. Over time, such a framework could hypothetically lead to a significant rise in AI-compliant licensing agreements, potentially reducing unauthorised scraping and enhancing transparency in digital media ecosystems.

## 5.3. Monetisation Opportunities

The integration of AI traceability systems will strengthen ethical oversight and also promise to open new avenues for revenue generation across the content ecosystem. By harnessing data on AI interactions with digital content, content creators, publishers, and regulatory institutions can establish monetisation models that promote accountability, transparency, and fair compensation. This section explores innovative strategies that transform AI-driven content consumption into financially sustainable practices, ensuring that intellectual property holders benefit from the expanding role of artificial intelligence.

## 5.3.1. Monetising AI Usage Data for Authors and Publishers

AI systems increasingly depend on vast repositories of intellectual content, including books, scholarly articles, news reports, and multimedia assets, to power functionalities such as summarisation, training, and content generation. Despite this heavy reliance, original content creators often receive little to no compensation for the use of their work. Implementing structured monetisation frameworks can correct this imbalance, enabling a more equitable distribution of financial rewards.

One such approach involves AI consumption-based royalties, whereby AI models log each instance of content utilisation. This data triggers automated micro-payments to the rightful owners using smart contracts and blockchain technologies, ensuring transparent and secure revenue flows. This model supports real-time compensation and reduces administrative burdens on rights holders. Another viable strategy is the subscription-based AI access model, where publishers offer specialised content licenses tailored for AI consumption. Under this framework, AI companies subscribe to access curated or proprietary datasets, providing a predictable income stream for academic institutions, media organisations, and independent authors. Additionally, AI-generated content attribution fees can be applied when AI models produce derivative outputs such as summaries, synthesised articles, or insights based on original content. In such cases, content owners would receive royalties that scale with the extent of the AI system’s reliance on their intellectual property.

A hypothetical example is the AI Research Monetisation Initiative (ARMI), which imagines a royalty-based model for academic publishers. In this scenario, AI systems would be required to log their usage of peer-reviewed content, with compensation tied to the level of engagement. A dynamic pricing mechanism could be implemented, where increased AI-driven interaction leads to proportionally higher royalties. In such a framework, academic publishers could potentially see a measurable rise in revenue from AI-mediated content usage.

## 5.3.2. New Business Models in AI Ethics and Traceability

Beyond direct content monetisation, AI traceability systems can catalyse entirely new business models focused on ethical compliance, governance, and transparency. As the use of AI continues to grow, so too does the demand for services that ensure responsible behaviour and regulatory alignment. These emerging business opportunities can foster market-driven incentives for ethical AI development while empowering stakeholders to maintain control over their digital assets.

One such model can be AI Traceability-as-a-Service (TaaS). Companies in this space may offer tools and platforms that track, audit, and report AI interactions with online content. Thus, businesses, publishers, and government institutions can subscribe to these services to monitor AI compliance, detect unauthorised usage, and generate documentation for regulatory reporting. Another innovative concept is the AI usage licensing marketplace, where creators and publishers can list their content and auction access rights to AI developers. This model introduces flexible pricing structures, such as tiered or exclusive access agreements, allowing content owners to retain control over how, when, and by whom their materials are used.

To reinforce industry standards, ethical AI certification programs can be developed by traceability firms. These certifications are awarded to AI models that demonstrate compliance with fair use, transparent attribution, and equitable monetisation policies. Companies that obtain such certifications gain reputational advantages, improved regulatory standing, and increased trust from users and partners.

A hypothetical example of these principles in action can be “EthicAI,” an imagined startup envisioned to be a consortium of AI researchers. In this scenario, EthicAI offers traceability and compliance tools adapted for publishers and content platforms. The conceptual model includes partnerships with media organisations to monitor AI interactions with journalistic content, alongside a flexible licensing framework that enables authors to set differential rates for AI-driven summarisation, reuse, and citation. In this envisioned case, the model gains traction globally and forms hypothetical agreements with AI developers and news networks, demonstrating the potential economic and ethical viability of traceability-focused business models.

## 6. Proposed System’s Novelty, Contributions, and Solutions Towards Human-Reintegration

This research introduces CTN, a socio-technical framework that advances ethical standards in generative AI by embedding mechanisms for traceability and attribution. Unlike existing approaches that primarily focus on bias mitigation, misinformation, or algorithmic transparency, CTN addresses an overlooked but critical gap: the systematic recognition of digital labour and intellectual contributions within large language model ecosystems. Through metadata tagging, attribution protocols, and real-time content usage reporting, the framework provides a transparent and verifiable means of documenting how AI systems interact with external sources. In doing so, it extends AI ethics from abstract principles to an operational design that reinforces human dignity, safeguards intellectual ownership, and supports more equitable AI-human symbiosis.

The framework also restores value and visibility to professions most vulnerable to appropriation, including writers, journalists, educators, and small publishers. Whereas current ethical debates often highlight risks of job displacement without embedding recognition into system design, CTN ensures that human contributions are identified, credited, and, where applicable, monetised through fair distribution models. This not only mitigates the invisibility of digital labour but also generates new professional opportunities in compliance auditing, ethical licensing, and content validation. By protecting originality and revaluing intellectual contributions, CTN sustains creative economies and positions human creativity as indispensable in the future of digital content.

Beyond its technical functions, CTN makes distinct theoretical and practical contributions. Theoretically, it reframes digital labour as a locus of ethical concern and links traceability and attribution to the principle of moral recognition in digital economies, an area underexplored in current scholarship. By conceptualising traceability as both a normative principle and a system design feature, CTN advances a socio-technical account of responsibility in AI. Practically, it offers operational tools such as watermarking, blockchainenabled licensing, and geospatial analytics that can be implemented by organisations to safeguard contributions, align with emerging regulations, and strengthen public trust. Its monetisation and redistribution mechanisms embed ethical governance into market practices rather than treating them as external oversight. Taken together, CTN provides the first integrated framework that unites ethical principles, technical mechanisms, and socio-economic reintegration, establishing a foundation for both academic advancement and real-world adoption.

No dataset was used in this study, as the work is conceptual and methodological rather than empirical. The purpose is not to optimise performance on benchmark datasets but to articulate a framework that systematically enables the ethical recognition of digital labour. Accordingly, direct baseline comparisons with state-of-the-art models such as LLMs are inappropriate at this stage. Instead, this research offers a foundational contribution that, to the best of our knowledge, is the first to integrate socio-technical principles of traceability with the recognition of digital contributions in generative AI. By articulating both its theoretical and practical implications, CTN provides a groundwork that future empirical studies can build upon through implementation, testing, and comparative evaluation.

## 7. Conclusions and Future Work

The rapid integration of large language models (LLMs) into digital knowledge ecosystems has introduced a critical challenge: the extraction and reuse of human-generated content without traceable attribution or measurable engagement. This study addressed this problem by demonstrating, through a case-based analysis, how LLM interactions with online content can occur without leaving detectable footprints in standard analytics systems, thereby obscuring authorship, diminishing visibility, and undermining digital labour recognition.

To respond to this gap, the study proposed Chujoyi-TraceNet (CTN), a socio-technical framework designed to restore traceability, attribution, and accountability in AI-mediated content ecosystems. By integrating mechanisms such as content fingerprinting, probabilistic attribution modelling, watermarking, and traceability scoring, CTN provides a structured approach for making AI–content interactions observable and for linking generated outputs back to their original sources. In doing so, the framework repositions traceability as a foundational requirement for ethical AI deployment rather than an optional feature.

The contributions of this study lie in (i) empirically highlighting the “invisible interaction” problem in current LLM architectures and (ii) proposing a scalable, conceptually grounded framework that aligns AI system design with principles of transparency, fairness, and digital labour recognition. These insights have implications for AI developers, platform providers, and policymakers seeking to build more accountable and sustainable digital ecosystems.

Future research should focus on the technical implementation and empirical validation of CTN in real-world environments, including integration into existing AI pipelines, evaluation of attribution accuracy, and assessment of its impact across domains such as academia, journalism, and digital publishing. Advancing such systems will be essential for ensuring that the evolution of generative AI remains both innovative and ethically grounded.

Author Contributions: Conceptualisation, $S . C . O . j$ methodology, C.J.E. and ${ \mathrm { S . C . O . } } ;$ validation, C.J.E. and ${ \mathrm { S . C . O . } } ;$ formal analysis, C.J.E.; investigation, ${ \mathrm { S . C . O . , C . J . E . } } ,$ and $\operatorname { I . O . } ;$ writing—original draft preparation, C.J.E. and S.C.O.; writing—review and editing, C.J.E., S.C.O., T.O., I.O. and O.B.; visualisation, G.W. and M.E.; supervision, T.O. and O.B. All authors have read and agreed to the published version of the manuscript.

Funding: This research received no external funding.

Data Availability Statement: Not applicable.

Conflicts of Interest: No potential conflicts of interest are reported by the author(s).

## References

1. Chen, Z.; Xu, L.; Zheng, H.; Chen, L.; Tolba, A.; Zhao, L.; Yu, K.; Feng, H. Evolution and Prospects of Foundation Models: From Large Language Models to Large Multimodal Models. Comput. Mater. Contin. 2024, 80, 1753–1808. [CrossRef]

2. Kim, S.; Ha, J.; Lee, H.; Park, S.; Cho, S. Human-guided collective LLM intelligence for strategic planning via two-stage information retrieval. Inf. Process. Manag. 2026, 63, 104288. [CrossRef]

3. Lieberum, J.-L.; Töws, M.; Metzendorf, M.-I.; Heilmeyer, F.; Siemens, W.; Haverkamp, C.; Böhringer, D.; Meerpohl, J.J.; Eisele Metzger, A. Large language models for conducting systematic reviews: On the rise, but not yet ready for use—A scoping review. J. Clin. Epidemiol. 2025, 181, 111746. [CrossRef] [PubMed]

4. Aggarwal, T.; Salatino, A.; Osborne, F.; Motta, E. Large language models for scholarly ontology generation: An extensive analysis in the engineering field. Inf. Process. Manag. 2026, 63, 104262. [CrossRef]

5. Ong, J.C.L.; Chang, S.Y.H.; William, W.; Butte, A.J.; Shah, N.H.; Chew, L.S.T.; Liu, N.; Doshi-Velez, F.; Lu, W.; Savulescu, J.; et al. Ethical and regulatory challenges of large language models in medicine. Lancet Digit. Health 2024, 6, e428–e432. [CrossRef]

6. Garry, M.; Chan, W.M.; Foster, J.; Henkel, L.A. Large language models (LLMs) and the institutionalization of misinformation. Trends Cogn. Sci. 2024, 28, 1078–1088. [CrossRef]

7. Anibal, J.T.; Huth, H.B.; Gunkel, J.; Gregurick, S.K.; Wood, B.J. Simulated misuse of large language models and clinical credit systems. npj Digit. Med. 2024, 7, 317. [CrossRef] [PubMed]

8. Johann, D.; Neufeld, J.; Thomas, K.; Rathmann, J.; Rauhut, H. The impact of researchers’ perceived pressure on their publication strategies. Res. Eval. 2024, rvae011. [CrossRef]

9. Teplitskiy, M.; Duede, E.; Menietti, M.; Lakhani, K.R. How status of research papers affects the way they are read and cited. Res. Policy 2022, 51, 104484. [CrossRef]

10. IxDF. What Is Search Engine Optimization (SEO)? Interaction Design Foundation—IxDF: Austin, TX, USA, 2025. Available online: https://www.interaction-design.org/literature/topics/search-engine-optimization?srsltid=AfmBOorPpnyBCyTWdnET3ROaUu eW5m2JdCySyuKC\_bGfxRG45SYBfQkd (accessed on 12 May 2025).

11. Rizvanovi´c, B.; Zutshi, A.; Grilo, A.; Nodehi, T. Linking the potentials of extended digital marketing impact and start-up growth: Developing a macro-dynamic framework of start-up growth drivers supported by digital marketing. Technol. Forecast. Soc. Change 2023, 186, 122128. [CrossRef]

12. Bowden, J. 7 Examples ofAI Misuse in Education; Inspera: Oslo, Norway, 2024. Available online: https://www.inspera.com/ai/exam ples-of-ai-misuse-in-education/ (accessed on 25 March 2025).

13. Ethical Requirements-IEEE Author Center Books. Available online: https://books.ieeeauthorcenter.ieee.org/book-publishing-atieee/publishing-ethics/ethical-requirements/ (accessed on 25 March 2025).

14. Oketch, K.; Lalor, J.P.; Yang, Y.; Abbasi, A. Bridging the LLM Accessibility Divide? Performance, Fairness, and Cost of Closed versus Open LLMs for Automated Essay Scoring. arXiv 2025, arXiv:2503.11827.

15. Cao, C.; Zhuang, J.; He, Q. LLM-Assisted Modeling and Simulations for Public Sector Decision-Making: Bridging Climate Data and Policy Insights. In Proceedings of the AAAI-2024 Workshop on Public Sector LLMs, PubLLM 2024, Vancouver, BC, Canada, 27 February 2024.

16. Rodrigues, N.S.; Ralha, C.G. A novel framework with ComMAND: A combined method for author name disambiguation. Inf. Process. Manag. 2026, 63, 104304. [CrossRef]

17. Ferguson, L.M.; Genderjahn, S.; Schworm, S.K. Research Ethics in the Age ofAI: Embracing Openness as a Path Forward—Workshop-Report; HIDA: Berlin, Germany, 2025.

18. Molinillo, S.; Japutra, A.; Ekinci, Y. Building brand credibility: The role of involvement, identification, reputation and attachment. J. Retail. Consum. Serv. 2022, 64, 102819. [CrossRef]

19. Tang, X.; Wang, L.; Wang, J. Language model collaboration for relation extraction from classical Chinese historical documents. Inf. Process. Manag. 2026, 63, 104286. [CrossRef]

20. Jeon, J.; Kim, L.; Park, J. The ethics of generative AI in social science research: A qualitative approach for institutionally grounded AI research ethics. Technol. Soc. 2025, 81, 102836. [CrossRef]

21. Roberts, J.; Baker, M.; Andrew, J. Artificial intelligence and qualitative research: The promise and perils of large language model (LLM) ‘assistance’. Crit. Perspect. Account. 2024, 99, 102722. [CrossRef]

22. Bansal, C. AI ethics and sustainability: Accelerating paradigm shifts toward sustainable development. J. Strategy Innov. 2025, 36, 200537. [CrossRef]

23. Saba, C.S.; Pretorius, M. The impact of artificial intelligence (AI) investment on human well-being in G-7 countries: Does the moderating role of governance matter? Sustain. Futures 2024, 7, 100156. [CrossRef]

24. Fang, X.; Che, S.; Mao, M.; Zhang, H.; Zhao, M.; Zhao, X. Bias of AI-generated content: An examination of news produced by large language models. Sci. Rep. 2024, 14, 5224. [CrossRef]

25. Chen, C.; Shu, K. Combating misinformation in the age of LLMs: Opportunities and challenges. AI Mag. 2024, 45, 354–368. [CrossRef]

26. Liao, Q.V.; Vaughan, J.W. AI Transparency in the Age of LLMs: A Human-Centered Research Roadmap. Harv. Data Sci. Rev. 2023. [CrossRef]

27. Hofmann, V.; Kalluri, P.R.; Jurafsky, D.; King, S. AI generates covertly racist decisions about people based on their dialect. Nature 2024, 633, 147–154. [CrossRef]

28. Steyvers, M.; Tejeda, H.; Kumar, A.; Belem, C.; Karny, S.; Hu, X.; Mayer, L.W.; Smyth, P. What large language models know and what people think they know. Nat. Mach. Intell. 2025, 7, 221–231. [CrossRef]

29. Ejiyi, C.J.; Qin, Z.; Ukwuoma, C.C.; Nneji, G.U.; Monday, H.N.; Ejiyi, M.B.; Ejiyi, T.U.; Okechukwu, U.; Bamisile, O.O. Comparative performance analysis of Boruta, SHAP, and Borutashap for disease diagnosis: A study with multiple machine learning algorithms. Netw. Comput. Neural Syst. 2024, 36, 507–544. [CrossRef]

30. Ejiyi, C.J.; Qin, Z.; Amos, J.; Ejiyi, M.B.; Nnani, A.; Ejiyi, T.U.; Agbesi, V.K.; Diokpo, C.; Okpara, C. A robust predictive diagnosis model for diabetes mellitus using Shapley-incorporated machine learning algorithms. Healthc. Anal. 2023, 3, 100166. [CrossRef]

31. Cheong, B.C. Transparency and accountability in AI systems: Safeguarding wellbeing in the age of algorithmic decision-making. Front. Hum. Dyn. 2024, 6, 1421273. [CrossRef]

32. Raiaan, M.A.K.; Mukta, M.S.H.; Fatema, K.; Fahad, N.M.; Sakib, S.; Mim, M.M.J.; Ahmad, J.; Ali, M.E.; Azam, S. A Review on Large Language Models: Architectures, Applications, Taxonomies, Open Issues and Challenges. IEEE Access 2024, 12, 26839–26874. [CrossRef]

33. AlDahoul, N.; Hong, J.; Varvello, M.; Zaki, Y. Towards a World Wide Web powered by generative AI. Sci. Rep. 2025, 15, 7251. [CrossRef] [PubMed]

34. Williamson, S.M.; Prybutok, V. The Era of Artificial Intelligence Deception: Unraveling the Complexities of False Realities and Emerging Threats of Misinformation. Information 2024, 15, 299. [CrossRef]

35. Rillig, M.C.; Mansour, I.; Hempel, S.; Bi, M.; König-Ries, B.; Kasirzadeh, A. How widespread use of generative AI for images and video can affect the environment and the science of ecology. Ecol. Lett. 2024, 27, e14397. [CrossRef]

36. Erickson, K. AI and work in the creative industries: Digital continuity or discontinuity? Creat. Ind. J. 2024, 10, 1–21. [CrossRef]

37. Bankins, S.; Formosa, P. The Ethical Implications of Artificial Intelligence (AI) For Meaningful Work. J. Bus. Ethics 2023, 185, 725–740. [CrossRef]

38. Hémono, P.; Nait Chabane, A.; Sahnoun, M. Multi objective optimization of human–robot collaboration: A case study in aerospace assembly line. Comput. Oper. Res. 2025, 174, 106874. [CrossRef]

39. Filippi, E.; Bannò, M.; Trento, S. Automation technologies and their impact on employment: A review, synthesis and future research agenda. Technol. Forecast. Soc. Change 2023, 191, 122448. [CrossRef]

40. Wang, K.H.; Lu, W.C. AI-induced job impact: Complementary or substitution? Empirical insights and sustainable technology considerations. Sustain. Technol. Entrep. 2025, 4, 100085. [CrossRef]

41. Broady, K.E.; Booth-Bell, D.; Barr, A.; Meeks, A. Automation, artificial intelligence, and job displacement in the U.S., 2019–22. Labour Hist. 2025, 67, 257–273. [CrossRef]

42. Wong, L.P.W. Artificial Intelligence and Job Automation: Challenges for Secondary Students’ Career Development and Life Planning. Merits 2024, 4, 370–399. [CrossRef]

43. Herath Pathirannehelage, S.; Shrestha, Y.R.; von Krogh, G. Design principles for artificial intelligence-augmented decision making: An action design research study. Eur. J. Inf. Syst. 2025, 34, 207–229. [CrossRef]

44. Rashid, A.B.; Kausik, M.A.K. AI revolutionizing industries worldwide: A comprehensive overview of its diverse applications. Hybrid Adv. 2024, 7, 100277. [CrossRef]

45. Moon, W.K.; Kahlor, L.A. Fact-checking in the age of AI: Reducing biases with non-human information sources. Technol. Soc. 2025, 80, 102760. [CrossRef]

46. Agbesi, V.K.; Chen, W.; Ejiyi, C.J.; Gosu, G.S.; Ukwuoma, C.C.; Bamisile, O. TFMPHGNN: Two-Fold Multi-Perspective Heterogeneous Graph Neural Network for Sentiment Analysis. Neural Netw. 2026, 201, 108885. [CrossRef]

47. Ejiyi, C.J.; Qin, Z.; Ukwuoma, C.; Agbesi, V.K.; Oluwasanmi, A.; Al-antari, M.A.; Bamisile, O. A unified 2D medical image segmentation network (SegmentNet) through distance-awareness and local feature extraction. Biocybern. Biomed. Eng. 2024, 44, 431–449. [CrossRef]

48. Ejiyi, C.J.; Qin, Z.; Agbesi, V.K.; Ejiyi, M.B.; Chikwendu, I.A.; Bamisile, O.F.; Onyekwere, F.E.; Bamisile, O.O. ATEDU-NET: An Attention-Embedded Deep Unet for multi-disease diagnosis in chest X-ray images, breast ultrasound, and retina fundus. Comput. Biol. Med. 2025, 186, 109708. [CrossRef] [PubMed]

49. Ejiyi, C.J.; Qin, Z.; Agbesi, V.K.; Ejiyi, M.B.; Chikwendu, I.A.; Bamisile, O.F.; Onyekwere, F.E.; Bamisile, O.O. Attention-enriched deeper UNet (ADU-NET) for disease diagnosis in breast ultrasound and retina fundus images. Prog. Artif. Intell. 2024, 13, 351–366. [CrossRef]

50. Kalokyri, V.; Tachos, N.S.; Kalantzopoulos, C.N.; Sfakianakis, S.; Kondylakis, H.; Zaridis, D.I.; Colantonio, S.; Regge, D.; Papanikolaou, N.; Marias, K.; et al. AI Model Passport: Data and system traceability framework for transparent AI in health. Comput. Struct. Biotechnol. J. 2025, 28, 386–404. [CrossRef]

51. Longpre, S.; Mahari, R.; Chen, A.; Obeng-Marnu, N.; Sileo, D.; Brannon, W.; Muennighoff, N.; Khazam, N.; Kabbara, J.; Perisetla, K.; et al. A large-scale audit of dataset licensing and attribution in AI. Nat. Mach. Intell. 2024, 6, 975–987. [CrossRef]

52. Liang, Y.; Xiao, J.; Gan, W.; Yu, P.S. Watermarking techniques for large language models: A survey. Artif. Intell. Rev. 2026, 59, 74. [CrossRef]

53. Amirzhanov, A.; Turan, C.; Makhmutova, A. Plagiarism types and detection methods: A systematic survey of algorithms in text analysis. Front. Comput. Sci. 2025, 7, 1504725. [CrossRef]

54. Apoetsbrain. A Collection of Thoughts, Quotes, Art, Poems, and Randoms. 2025. Available online: https://apoetsbrain.wordpres s.com/ (accessed on 1 October 2025).

55. OpenAI. Models—OpenAI API; OpenAI Platf.: San Francisco, CA, USA, 2025. Available online: https://platform.openai.com/doc s/models (accessed on 25 March 2025).

56. Google AI. Google Gemini AI; Google LLC.: Mountain View, CA, USA, 2023. Available online: https://gemini.google.com (accessed on 7 May 2025).

57. DeepSeek AI. DeepSeek AI Model; Deep. AI: Hangzhou, China, 2024. Available online: https://www.deepseek.com/ (accessed on 7 May 2025).

58. Inflection AI. Pi AI Assistant; Inflection AI: Palo Alto, CA, USA, 2023. Available online: https://pi.ai (accessed on 7 May 2025).

59. xAI. Grok AI Assistant; xAI Corp.: Palo Alto, CA, USA, 2024. Available online: https://grok.x.ai (accessed on 7 May 2025).

60. Ananthaswamy, A. How close is AI to human-level intelligence? Nature 2024, 636, 22–25. [CrossRef]

61. Shahzad, T.; Mazhar, T.; Tariq, M.U.; Ahmad, W.; Ouahada, K.; Hamam, H. A comprehensive review of large language models: Issues and solutions in learning environments. Discov. Sustain. 2025, 6, 27. [CrossRef]

62. Ellingrud, K.; Sanghvi, S.; Dandona, G.S.; Madgavkar, A.; Chui, M.; White, O.; Hasebe, P. Generative AI and the Future of Work in America; McKinsey: New York, NY, USA, 2023. Available online: https://www.mckinsey.com/mgi/our-research/generative-aiand-the-future-of-work-in-america (accessed on 26 March 2025).

63. Yao, Y.; Duan, J.; Xu, K.; Cai, Y.; Sun, Z.; Zhang, Y. A survey on large language model (LLM) security and privacy: The Good, The Bad, and The Ugly. High-Confid. Comput. 2024, 4, 100211. [CrossRef]

64. Knott, A.; Pedreschi, D.; Jitsuzumi, T.; Leavy, S.; Eyers, D.; Chakraborti, T.; Trotman, A.; Sundareswaran, S.; Baeza-Yates, R.; Biecek, P.; et al. AI content detection in the emerging information ecosystem: New obligations for media and tech companies. Ethics Inf. Technol. 2024, 26, 63. [CrossRef]

65. Maliˇcki, M.; Aalbersberg, I.J.; Bouter, L.; Mulligan, A.; ter Riet, G. Transparency in conducting and reporting research: A survey of authors, reviewers, and editors across scholarly disciplines. PLoS ONE 2023, 18, e0270054. [CrossRef]

66. Aguinis, H.; Li, Z.A.; Der Foo, M. The research transparency index. Leadersh. Q. 2024, 35, 101809. [CrossRef]

67. Cooperman, S.R.; Brandão, R.A. AI assistance with scientific writing: Possibilities, pitfalls, and ethical considerations. Foot Ankle Surg. Tech. Rep. Cases 2024, 4, 100350. [CrossRef]

68. Zhou, J.; Zhang, Y.; Luo, Q.; Parker, A.G.; De Choudhury, M. Synthetic Lies: Understanding AI-Generated Misinformation and Evaluating Algorithmic and Human Solutions. In Proceedings ofthe 2023 CHI Conference on Human Factors in Computing Systems; Association for Computing Machinery: New York, NY, USA, 2023. [CrossRef]

69. Vicari, R.; Komendatova, N. Systematic meta-analysis of research on AI tools to deal with misinformation on social media during natural and anthropogenic hazards and disasters. Humanit. Soc. Sci. Commun. 2023, 10, 332. [CrossRef]

70. Tavares, S.; Ferrara, E. Fairness and Bias in Artificial Intelligence: A Brief Survey of Sources, Impacts, and Mitigation Strategies. Science 2023, 6, 3. [CrossRef]

71. Chen, Z. Ethics and discrimination in artificial intelligence-enabled recruitment practices. Humanit. Soc. Sci. Commun. 2023, 10, 567. [CrossRef]

72. Currie, G.M.; Hawk, K.E.; Rohren, E.M. Generative Artificial Intelligence Biases, Limitations and Risks in Nuclear Medicine: An Argument for Appropriate Use Framework and Recommendations. Semin. Nucl. Med. 2025, 55, 423–436. [CrossRef]

73. Al-kfairy, M.; Mustafa, D.; Kshetri, N.; Insiew, M.; Alfandi, O. Ethical Challenges and Solutions of Generative AI: An Interdisci plinary Perspective. Informatics 2024, 11, 58. [CrossRef]

74. Ali, O.; Murray, P.A.; Momin, M.; Dwivedi, Y.K.; Malik, T. The effects of artificial intelligence applications in educational settings: Challenges and strategies. Technol. Forecast. Soc. Change 2024, 199, 123076. [CrossRef]

75. Spatola, N. The efficiency-accountability tradeoff in AI integration: Effects on human performance and over-reliance. Comput Hum. Behav. Artif. Hum. 2024, 2, 100099. [CrossRef]

76. Resnik, D.B.; Mohammad, M. The ethics of using artificial intelligence in scientific research: New guidance needed for a new tool. AI Ethics 2024, 5, 1499–1521. [CrossRef]

77. Black, R.W.; Tomlinson, B. University students describe how they adopt AI for writing and research in a general education course. Sci. Rep. 2025, 15, 8799. [CrossRef]

78. Chen, C.; Gong, Y. The Role of AI-Assisted Learning in Academic Writing: A Mixed-Methods Study on Chinese as a Second Language Students. Educ. Sci. 2025, 15, 141. [CrossRef]

79. Writing the rules in AI-assisted writing. Nat. Mach. Intell. 2023, 5, 469. [CrossRef]

80. Khalifa, M.; Albadawy, M. Using artificial intelligence in academic writing and research: An essential productivity tool. Comput. Methods Programs Biomed. Update 2024, 5, 100145. [CrossRef]

81. UNESCO. Guidance for Generative AI in Education and Research; UNESCO: Paris, France, 2024. Available online: https://www.unesco.org/en/articles/guidance-generative-ai-education-and-research (accessed on 26 March 2025).

82. European Union. AI Act|Shaping Europe’s Digital Future; European Union: Brussels, Belgium, 2024. Available online: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai (accessed on 26 March 2025).

83. Martinoviˇc, J.; Gajdoš, P.; Snášel, V. Similarity in information retrieval. In Proceedings of the 2008 7th Computer Information Systems and Industrial Management Applications; IEEE Computer Society: Washington, DC, USA, 2008; pp. 145–150. [CrossRef]

84. Mainguet, J.-F. Fingerprints Hashing. In Encyclopedia of Biometrics; Springer: Berlin/Heidelberg, Germany, 2009; pp. 543–549. [CrossRef]

85. Varley, T.F. Information theory for complex systems scientists: What, why, and how. Phys. Rep. 2025, 1148, 1–55. [CrossRef]

86. Martino, R.; Cilardo, A. Designing a SHA-256 processor for blockchain-based IoT applications. Internet Things 2020, 11, 100254. [CrossRef]

87. Rahim, M.; Abosuliman, S.S.; Alroobaea, R.; Shah, K.; Abdeljawad, T. Cosine similarity and distance measures for p,q−quasirung orthopair fuzzy sets: Applications in investment decision-making. Heliyon 2024, 10, e32107. [CrossRef]

88. Saraiva, P. On Shannon entropy and its applications. Kuwait J. Sci. 2023, 50, 194–199. [CrossRef]

89. Li, Q.; Ma, B.; Wang, X.; Wang, C.; Gao, S. Image Steganography in Color Conversion. IEEE Trans. Circuits Syst. II Express Briefs 2024, 71, 106–110. [CrossRef]

90. Li, Q.; Wang, X.; Ma, B.; Wang, X.; Wang, C.; Gao, S.; Shi, Y. Concealed Attack for Robust Watermarking Based on Generative Model and Perceptual Loss. IEEE Trans. Circuits Syst. Video Technol. 2022, 32, 5695–5706. [CrossRef]

91. Lin, Y.; Liao, Y.; Zeng, W.; Wei, Y.; Chen, D.; Yuan, X.; Li, Y.; Erkan, U.; Toktas, A.; Zhang, C.; et al. 3D Non-degenerate Hyperchaos: Design, Analysis, and Application in Image Encryption. IEEE Trans. Consum. Electron. 2026. [CrossRef]

92. Olasehinde, D.O.; Bamisile, O.; Ejiyi, C.J.; Zhang, G.; Cai, D.; Li, J.; Wei, L.; Huang, Q. Cybersecurity in cyber-physical power systems: Analyzing vulnerabilities, threats, and control structures. Clust. Comput. 2026, 29, 133. [CrossRef]

93. Rijsbosch, B.; van Dijck, G.; Kollnig, K. Adoption of Watermarking for Generative AI Systems in Practice and Implications under the new EU AI Act. arXiv 2025, arXiv:2503.18156. [CrossRef]

94. Bouchiha, M.A.; Telnoff, Q.; Bakkali, S.; Champagnat, R.; Rabah, M.; Coustaty, M.; Ghamri-Doudane, Y. LLMChain: Blockchain-Based Reputation System for Sharing and Evaluating Large Language Models. In Proceedings of the 2024 IEEE 48th Annua Computers, Software, and Applications Conference (COMPSAC); Institute of Electrical and Electronics Engineers (IEEE): New York, NY, USA, 2024; pp. 439–448.

95. Hern, A. TikTok to Auto-Flag AI Videos—Even if Created on Other Platforms|TikTok|. The Guardian, 9 May 2024.

96. Chapman, M. TikTok to start labeling AI-generated content as technology becomes more universal. AP News, 9 May 2024.

97. Editorial Team. Google Tag Manager Event Tracking Guide (2025). 2025. Available online: https://analytify.io/google-tagmanager-event-tracking/ (accessed on 6 May 2025).

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.