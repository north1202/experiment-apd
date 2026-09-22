# ChatGPT-4.0 as a Tool for Automated Review of Ethics and Transparency in Biomedical Literature

Original Article Editing, Writing & Publishing

Check for updates

Received: Apr 10, 2025   
Accepted: May 13, 2025   
Published online: Dec 9, 2025

Address for Correspondence: Bohdana Doskaliuk, MD, PhD Department of Pathophysiology, Ivano-Frankivsk National Medical University, Halytska str. 2, Ivano-Frankivsk 76018, Ukraine. Email: doskaliuk\_bo@ifnmu.edu.ua

© 2026 The Korean Academy of Medical Sciences.

This is an Open Access article distributed under the terms of the Creative Commons Attribution Non-Commercial License (https:// creativecommons.org/licenses/by-nc/4.0/) which permits unrestricted non-commercial use, distribution, and reproduction in any medium, provided the original work is properly cited.

## ORCID iDs

Bohdana Doskaliuk   
https://orcid.org/0000-0003-1650-8928 Birzhan Seiil   
https://orcid.org/0000-0003-1524-8888 Ainur Qumar   
https://orcid.org/0000-0003-0457-7205

## Disclosure

The authors have no potential conflicts of interest to disclose.

## Data Availability Statement

The data supporting the findings of this study are available from the corresponding autho upon reasonable request.

## Author Contributions

Conceptualization: Doskaliuk B. Data curation: Doskaliuk B, Seiil B, Qumar A. Methodology:

Bohdana Doskaliuk ,1 Birzhan Seiil ,2 and Ainur Qumar 3

<sup>1</sup>Department of Pathophysiology, Ivano-Frankivsk National Medical University, Ivano-Frankivsk, Ukraine <sup>2</sup>Department of Biology and Biochemistry, South Kazakhstan Medical Academy, Shymkent, Kazakhstan <sup>3</sup>Department of Health Policy and Management, Asfendiyarov Kazakh National Medical University, Almaty, Kazakhstan

## ABSTRACT

Background: The integration of artificial intelligence, specifically large language models, into editorial processes, is gaining interest due to its potential to streamline manuscript assessments, particularly regarding ethical and transparency reporting in public health journals. This study aims to evaluate the capability and limitations of ChatGPT-4.0 in accurately detecting missing ethical and transparency statements in research articles published in high-ranked (Q1) versus low-ranked (Q4) public health journals. Methods: Articles from top-tier (Q1) and low-tier (Q4) public health journals were analyzed using ChatGPT-4.0 for the presence of essential ethical components, including ethics approval, informed consent, animal ethics, conflicts of interest, funding notes, and open data sharing statements. Performance metrics such as sensitivity, recall, and precision were calculated. Results: ChatGPT exhibited high sensitivity and recall across all evaluated components, accurately identifying all missing ethics statements. However, precision varied significantly between categories, with notably high precision for data availability statements (0.96) and significantly lower precision for funding statements (0.16). A comparative analysis between Q1 and Q4 journals showed a marked increase in missing ethics statements in the Q4 group, particularly for open data sharing statements (4 vs. 50 cases), ethics approval (2 vs. 5 cases), and informed consent statements (3 vs. 8 cases). Conclusion: ChatGPT-4.0 in preliminary screening shows considerable promise, providing high accuracy in identifying missing ethics statements. However, limitations regarding precision highlight the necessity for additional human checks. A balanced integration of artificial intelligence and human judgment is recommended to enhance editorial checks and maintain ethical standards in public health publishing.

Keywords: Artificial Intelligence; ChatGPT-4.0; Editorial Policies; Ethics; Natural Language Processing; Public Health

## INTRODUCTION

Incorporating artificial intelligence (AI) into academic publishing is gaining increasing attention. AI-driven platforms provide a range of tools to support editors in managing manuscript checks, detecting plagiarism, and refining content.1 The advance of natural

Doskaliuk B, Seiil B, Qumar A. Writing - original draft: Doskaliuk B. Writing - review & editing: Seiil B, Qumar A.

language processing (NLP) technology has significantly enhanced the eficiency of editorial workflows. It minimizes reliance on manual input and accelerates the decision-making process. However, despite these aachievements, AI tools have limitations due to concerns of accuracy, reliability, and ethical oversights.2 Recognizing both the advantages and limitations of AI-assisted editorial checks is essential for upholding the integrity of public health research publications.

One of AI’s notable contributions to journal editing is its ability to process large volumes of submissions eficiently. AI-based screening systems can evaluate manuscripts based on predetermined criteria, such as relevance, completeness, and adherence to ethical guidelines. For instance, AI can flag potential conflicts of interest, duplicate submissions, and identify ethical issues within study designs. These automated capabilities allow editors to focus more on assessing scientific significance and methodological soundness of submissions.3 Moreover, AI-powered language models support non-Anglophone authors in enhancing the clarity and readability of their manuscripts, promoting broader accessibility and inclusivity in public health literature.4

While AI tools ofer numerous benefits, they also pose challenges related to bias, contextual misinterpretation, and absence of human judgment. AI models are trained on vast datasets, which may inadvertently introduce biases that mirror systemic disparities in academic publishing.5-7 As a result, AI-generated recommendations may favour specific research topics or writing styles based on dominant trends in its training data. This may unintentionally exclude underrepresented areas of research, particularly those relevant to underserved communities. Additionally, AI may struggle to assess nuanced ethical concerns, such as appropriate participant selection and justification of study designs, which often require human expertise and contextual awareness.7

Another key issue with AI-assisted editorial workflows is the reliance of AI-generated responses on user inquiries. AI-powered chatbots and automated review systems can provide quick summaries and suggestions based on established guidelines, but they may also generate factually incorrect and misleading content.8 This phenomenon, termed “hallucination,” occurs when AI produces seemingly credible but unfounded information. Such inaccuracies pose risks in scientific publishing, where disseminating misinformation may have serious consequences. Ensuring the accuracy of AI-generated contents is still a challenge.9

Recent advancements in AI technology aim to overcome some of its challenges. In fact, newer AI models now feature improved contextual comprehension, enhanced citation verification mechanisms, and advanced bias-reduction strategies.10 Some AI systems cross-reference multiple sources before producing responses, reducing the likelihood of misinformation. Additionally, adaptive AI models refine their accuracy through iterative learning, incorporating feedback to improve performance over time.11

While these advances represent the progress in the field, little is known about the eficiency of AI models in real-world academic contexts. To date, no studies have compared large language models (LLMs) performance in identifying ethical transparency elements across journals of diferent quartiles.

This study aims to evaluate the capability and limitations of LLMs, specifically ChatGPT-4.0, in accurately detecting missing ethics and transparency statements in scholarly articles published in high-ranked (Q1) versus low-ranked (Q4) public health journals.

## METHODS

## Selection of articles

This analytical study is aimed at assessing the capability of AI to identify essential ethics and transparency statements in original and review articles. To assess it, a selected set of published articles was analyzed. Two journals were chosen based on their ranking within the Public Health category of the SCImago Journal Rank database,12 ensuring a contrast in editorial policies and publication practices.

The decision to focus on public health journals stems from their critical role at the intersection of scientific research, policy-making, and societal welfare. Public health research often engages vulnerable populations, addresses issues of equity and access, and has direct implications for community well-being. Therefore, assessing the use of AI in evaluating ethical standards within public health publications may provide valuable insights into both the integrity of research dissemination and the evolving landscape of ethical accountability in health sciences.

Specifically, 50 articles were selected from the Lancet Public Health (Q1) and 50 articles from the Public Health ofIndonesia (Q4). Only original research and review articles were included in the analysis.

## AI-based analysis using ChatGPT-4.0

All selected articles were analyzed using the ChatGPT-4.0 language model, employing a standardized, prompt-driven protocol to ensure consistency and reproducibility. A single, predefined prompt (detailed in Supplementary Data 1) was used to evaluate each manuscript for the presence of six key ethical and transparency components. To minimize variability, all analyses were conducted on the same day using the identical prompt across all articles. The six assessed criteria included:

1. Ethics approval – Verification that an Institutional Review Board or Ethics Committee reviewed and approved the study.

2. Informed consent – A confirmation that participants or their legal representatives provided informed consent for participation.

3. Animal ethics – Where applicable, compliance with national or international animal research guidelines.

4. Conflicts of interest (COI) statement – A declaration of any financial or personal relationships that could influence the study.

5. Funding statement – Acknowledgment of financial support or research grants received for the study.

6. Data availability statement – Information on the availability and accessibility of data supporting the study’s findings.

These six components were selected a<sub>p</sub>riori based on ethics and transparency criteria recommended by the ICMJE,13 CONSORT,14 ARRIVE15 guidelines, and common editorial policies across biomedical journals. These elements represent widely recognized standards for responsible reporting in human and animal research. ChatGPT-4.0 processed each article individually, generating a structured output identifying whether each component was present, absent, or unclear.

## Manual human verification

Two independent reviewers conducted a manual verification process to validate the AIgenerated results. Each article was assessed against the same six predefined criteria to confirm or correct the AI classifications. In cases where discrepancies or disagreements arose between the two reviewers, a third reviewer was consulted to adjudicate and reach a consensus. All discrepancies between AI-detected and manually verified components were documented for further analysis.

## Performance metrics evaluation

The performance of ChatGPT-4.0 was evaluated using standard classification metrics: precision, recall, accuracy, and the F1-score.16 These metrics were calculated as follows:

Precision = True Positives / (True Positives + False Positives)

Recall = True Positives / (True Positives + False Negatives)

Accuracy = (True Positives + True Negatives) / Total Predictions

$$
F 1 - s c o r e = 2 \times ( P r e c i s i o n \times R e c a l l ) / ( P r e c i s i o n + R e c a l l )
$$

These metrics provide a comprehensive measure of ChatGPT-4.0’s efectiveness in correctly identifying ethical and transparency statements while minimizing both false positives and false negatives. The F1-score, in particular, is a balanced metric combining precision and recall into a single value, which is especially useful when false positives and false negatives carry diferent weights in ethical compliance screening.

Separate performance metrics were computed for each of the six criteria to evaluate the model's consistency across diferent types of statements.

## Comparative analysis across journal tiers

A comparative evaluation was performed to explore diferences in ethical reporting practices between Q1 and Q4 journals. AI-based outputs and manual verification results were assessed in parallel to identify variations in the completeness of ethics and transparency statements, ofering insights into potential disparities in editorial rigour across journal quartiles.

## RESULTS

The evaluation of ChatGPT performance in identifying missing ethics statement revealed distinct trends across the diferent components assessed and between the two datasets (Q1 vs. Q4). The most frequently missing component across both quartiles was the data availability (open data sharing) statement, absent in 4 Q1 and 50 Q4 articles. Additionally, informed consent and ethics approval were more often missing in the Q4 journal (8 and 5 articles, respectively) than in the Q1 journal (3 and 2 articles, respectively). No omissions were observed for animal ethics or COI (Table 1).

Table 1. Summary of detection performance by ChatGPT 4.0 across key research transparency elements in Q1 and Q4 journals
<table><tr><td rowspan="2">Components</td><td colspan="2">No. of articles with missing component</td></tr><tr><td>Q1 journal</td><td>Q4 journal</td></tr><tr><td>Ethics approval</td><td>2</td><td>5</td></tr><tr><td>Informed consent</td><td>3</td><td>8</td></tr><tr><td>Animal ethics</td><td>0</td><td>0</td></tr><tr><td>Conflicts of interest (COI)</td><td>0</td><td>0</td></tr><tr><td>Funding statement</td><td>1</td><td>5</td></tr><tr><td>Data availability statement</td><td>4</td><td>50</td></tr></table>

The manual analyses by the reviewer indicated that while false negatives were entirely absent across all categories, false positives did occur, predominantly in ethical approval and funding statement categories (Table 2).

The evaluation of component detection revealed notable variation in performance across categories (Table 3). The data availability statement demonstrated the highest overall results, with perfect recall (1.0), high precision (0.96), an F1 score of 0.98, and an accuracy of 0.98— indicating both consistent identification and minimal false positives. Similarly, informed consent performed well with a recall of 1.0, a precision of 0.63, an F1 score of 0.77, and an accuracy of 0.96.

In contrast, the funding statement showed the weakest performance among components with available data. Although it also achieved a perfect recall of 1.0, the precision was markedly low at 0.16, resulting in an F1 score of 0.28 and an accuracy of 0.95—suggesting a high number of false positives in detection. Ethics approval followed a similar trend, with perfect recall (1.0) but low precision (0.29), leading to a modest F1 score of 0.45 and an accuracy of 0.95.

For animal ethics and COI, no relevant cases were present in the dataset, and as such, no precision or recall values were applicable. However, both components yielded a perfect accuracy score of 1,0, reflecting correct classification in the absence of missing statements.

Table 2. Distribution of false positives and false negatives in automated detection of transparency components across Q1 and Q4 journals
<table><tr><td rowspan="2">Components</td><td colspan="2">False positive</td><td colspan="2">False negative</td></tr><tr><td>Q1 journal</td><td>Q4 journal</td><td>Q1 journal</td><td>Q4 journal</td></tr><tr><td>Ethics approval</td><td>2</td><td>3</td><td>0</td><td>0</td></tr><tr><td>Informed consent</td><td>3</td><td>1</td><td>0</td><td>0</td></tr><tr><td>Animal ethics</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Conflicts of interest (COI)</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Funding statement</td><td>0</td><td>5</td><td>0</td><td>0</td></tr><tr><td>Data availability statement</td><td>2</td><td>0</td><td>0</td><td>0</td></tr></table>

Table 3. Performance metrics for automated detection of ethical and transparency components
<table><tr><td>Components</td><td>Recall</td><td>Precision</td><td>F1 score</td><td>Accuracy</td></tr><tr><td>Ethics approval</td><td>1</td><td>0.29</td><td>0.45</td><td>0.95</td></tr><tr><td>Informed consent</td><td>1</td><td>0.63</td><td>0.77</td><td>0.96</td></tr><tr><td>Animal ethics</td><td>NA</td><td>NA</td><td>NA</td><td>3.0</td></tr><tr><td>Conflicts of interest (COI)</td><td>NA</td><td>NA</td><td>NA</td><td>1.0</td></tr><tr><td>Funding statement</td><td>1</td><td>0.16</td><td>0.28</td><td>0.95</td></tr><tr><td>Data availability statement</td><td>1</td><td>0.96</td><td>0.98</td><td>0.98</td></tr></table>

NA = not applicable.

## DISCUSSION

The integration of LLMs such as ChatGPT into the preliminary assessment of ethics statements in scholarly articles holds promise. This study data reveal that ChatGPT demonstrates notable recall and accuracy across various ethics-related components, identifying all instances of missing ethics approvals, informed consent, funding, and open data sharing statements. Such consistent performance underscores the model’s capability as a reliable initial screening tool to flag potential oversights.

Notably, the precision of the LLM demonstrated considerable variability across the evaluated components. While high precision was observed in detecting data availability statements (0.96), markedly lower precision was recorded for funding disclosures (0.16). This disparity highlights the model's tendency toward false positive classifications. It successfully identifies all actual cases, but sometimes incorrectly flags statements as problematic even when they meet the required standards. For example, in several cases involving funding statements, the model flagged articles as lacking proper disclosure despite the presence of a “None” declaration. Upon review, ChatGPT rationale revealed that although such a response was provided, further clarification regarding funding was recommended. As this level of elaboration exceeds standard reporting requirements, the output was classified as a false positive. This underscores the need to interpret LLM-generated outputs within the context of accepted publication norms and editorial guidelines. Therefore, integrating LLM-driven preliminary checks must be accompanied by human oversight to address and correct these false positives.

Due to the low precision observed in some categories, the corresponding F1 scores were also reduced for certain components of the ethical statements. For instance, although the model achieved perfect recall (1.0) across all assessed components, the funding statement and ethics approval sections demonstrated relatively low F1 scores of 0.28 and 0.45, respectively. These results were primarily driven by a high rate of false positives, suggesting the model often flagged these elements even when they were insuficiently or ambiguously addressed. This over-identification may reflect sensitivity to loosely related text, which could compromise interpretive accuracy. In contrast, other components performed more favourably. Informed consent achieved a solid F1 score of 0.77, indicating a more balanced performance, while data availability statements stood out with an F1 score of 0.98, demonstrating the model’s strong reliability and consistency in identifying well-defined, structured elements of ethical compliance.

The comparison between selected Q1 and Q4 public health journals revealed a notable increase in missing ethics-related statements in the low-ranked journals. The most striking diference was observed in data availability statements, which were missing in only four articles of the Q1 journal and 50 articles of the Q4 journal. This substantial gap may reflect diferences in editorial policies, enforcement of reporting guidelines, or author awareness of data-sharing mandates.

Considering that this study focused on public health journals, there were few animalbased studies. The complete absence of missing statements related to animal ethics likely reflects the rigorous ethical standards and oversight typical of public health research involving animals. Similarly, the consistent and accurate detection of COI statements further underscores clearly articulated and standardized ethical reporting guidelines already established within these specialized journals.

Furthermore, considering the broader landscape, LLMs hold promise for streamlining manuscript review processes.17 Nonetheless, their integration must be viewed as complementary to human judgment rather than a substitute.18-20 Human oversight remains indispensable, particularly in nuanced or ambiguous cases.21 Addressing model limitations through targeted training, incorporating feedback loops, and clearly defining ethical reporting standards are crucial steps toward optimizing the role of LLMs within the review processes.22,23

Despite the promising potential of AI-assisted manuscript analysis, several limitations must be acknowledged. First, the accuracy of contextual interpretation remains a challenge, with a risk of misclassification or omission of relevant content. The performance of NLP algorithms is inherently dependent on the quality and diversity of the training data, which may not fully capture the variability of scientific expression. Furthermore, inconsistencies in journal formatting and structural diferences across manuscripts may have influenced the uniformity of LLM-generated outputs. Finally, the specificity and comprehensiveness of the prompts used to guide AI retrieval play a critical role in shaping the results, underscoring the importance of carefully designed input to ensure accurate and meaningful extraction of information.

Overall, this study demonstrates that ChatGPT-4.0 can support ethical evaluations in editorial workflows. Its performance can be unreliable for nuanced declarations, such as funding statements.

The obtained findings highlight the need for contextual understanding and human oversight when integrating LLMs into editorial processes. At present, it is not feasible to use publicly available AI chatbots, such as ChatGPT-4.0, for the evaluation of editorial processes, as uploading unpublished manuscripts into such systems raises significant ethical and confidentiality concerns. Publishers may opt for developing closed, secure LLM systems analogous to plagiarism detection tools to facilitate ethical evaluations. Such systems could significantly streamline editorial workflows. To ensure responsible and efective use of AI in academic publishing, continuous refinement of AI tools, clear and standardized reporting guidelines, and periodic performance reassessments are essential. Ultimately, a collaborative model that combines AI eficiency with expert human judgment will enhance ethical compliance and help maintain the integrity of public health research publishing.

## ACKNOWLEDGMENTS

The language editing of this manuscript was conducted using Grammarly. The graphical abstract was created with the assistance of Napkin AI.

## SUPPLEMENTARY MATERIAL

## Supplementary Data 1

The prompt example

## REFERENCES

1. Doskaliuk B, Zimba O, Yessirkepov M, Klishch I, Yatsyshyn R. Artificial intelligence in peer review: enhancing eficiency while preserving integrity. JKorean Med Sci 2025;40(7):e92. PUBMED | CROSSREF

2. Hanna MG, Pantanowitz L, Jackson B, Palmer O, Visweswaran S, Pantanowitz J, et al. Ethical and bias considerations in artificial intelligence (AI)/machine learning. Mod Pathol 2025;38(3):100686. PUBMED | CROSSREF

3. Fiorillo L, Mehta V. Accelerating editorial processes in scientific journals: leveraging AI for rapid manuscript review. Oral Oncol Re<sub>p</sub> 2024;10:100511. CROSSREF

4. Doskaliuk B, Zimba O. Beyond the keyboard: academic writing in the era of ChatGPT. J Korean Med Sci 2023;38(26):e207. PUBMED | CROSSREF

5. Ferrara E. Fairness and bias in artificial intelligence: a brief survey of sources, impacts, and mitigation strategies. Sci 2024;6(1):3. CROSSREF

6. Wei X, Kumar N, Zhang H. Addressing bias in generative AI: challenges and research opportunities in information management. InfMana<sub>g</sub>e 2025;62(2):104103. CROSSREF

7. Stahl BC, Brooks L, Hatzakis T, Santiago N, Wright D. Exploring ethics and human rights in artificia intelligence: a Delphi study. Technol Forecast Soc Chan<sub>g</sub>e 2023;191:122502. CROSSREF

8. Williamson SM, Prybutok V. The era of artificial intelligence deception: unraveling the complexities of false realities and emerging threats of misinformation. Information 2024;15(6):299. CROSSREF

9. Seiil B, Zimba O, Korkosz M, Bekaryssova D, Zhakipbekov K, Qumar AB, et al. Healthcare professionals’ knowledge, views, and perceptions of the roles and functions of research ethics committees: a web-based cross-sectional survey. J Korean Med Sci 2025;40(4):e9. PUBMED | CROSSREF

10. Hasanzadeh F, Josephson CB, Waters G, Adedinsewo D, Azizi Z, White JA. Bias recognition and mitigation strategies in artificial intelligence healthcare applications. NPJ Di<sub>g</sub>itMed 2025;8(1):154. PUBMED | CROSSREF

11. Xia Y, Shin SY, Lee HA. Adaptive learning in AI agents for the Metaverse: the ALMAA framework. A<sub>pp</sub>l Sc 2024;14(23):11410. CROSSREF

12. Scimago Journal & Country Rank. https://www.scimagojr.com/journalrank.php?category=2739. Updated 2025. Accessed April 8, 2025.

13. International Committee of Medical Journal Editors. Defining the role of authors and contributors. https://www.icmje.org/recommendations/. Updated 2025. Accessed May 6, 2025.

14. EQUATOR network. CONSORT2025 Statement: updated guideline for reporting randomised trials. https://www.equator-network.org/reporting-guidelines/consort/. Updated 2025. Accessed May 6, 2025.

15. Percie du Sert N, Hurst V, Ahluwalia A, Alam S, Avey MT, Baker M, et al. The ARRIVE guidelines 2.0: updated guidelines for reporting animal research. PLoS Biol 2020;18(7):e3000410. PUBMED | CROSSREF

16. Naidu G, Zuva T, Sibanda EM. A review of evaluation metrics in machine learning algorithms. In: Silhavy R, Silhavy P, editors. Artificial Intelli<sub>g</sub>ence A<sub>pp</sub>lication in Networks and S<sub>y</sub>stems. Cham, Switzerland: Springer; 2023. 15-25.

17. Lee J, Lee J, Yoo JJ. The role of large language models in the peer-review process: opportunities and challenges for medical journal reviewers and editors. J Educ Eval Health Prof 2025;22:4. PUBMED | CROSSREF

18. Zhaksylyk A, Zimba O, Yessirkepov M, Kocyigit BF. Research integrity: where we are and where we are heading. J Korean Med Sci 2023;38(47):e405. PUBMED | CROSSREF

19. Kocak B, Onur MR, Park SH, Baltzer P, Dietzel M. Ensuring peer review integrity in the era of large language models: a critical stocktaking of challenges, red flags, and recommendations. EurJ RadiolArtif 2025;2:100018. CROSSREF

20. Kocyigit BF, Zhaksylyk A. Advantages and drawbacks of ChatGPT in the context of drafting scholarly articles. CentAsianJMed H<sub>yp</sub>otheses Ethics 2023;4(3):163-7. CROSSREF

21. Mehta P, Zimba O, Gasparyan AY, Seiil B, Yessirkepov M. Ethics committees: structure, roles, and issues. J 2023;38(25):e198. PUBMED | CROSSREF

22. Lissack M, Meagher B. Responsible use of large language models: an analogy with the Oxford tutorial system. SheJi 2024;10(4):389-413. CROSSREF

23. Shahzad T, Mazhar T, Tariq MU, Ahmad W, Ouahada K, Hamam H. A comprehensive review of large language models: issues and solutions in learning environments. Discov Sustain 2025;6(1):27. CROSSREF