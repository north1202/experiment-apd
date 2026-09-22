Background Artificial intelligence has created new opportunities in higher education enhancing teaching and learning methods for both students and educators. However, it has also posed challenges to academic integrity. Objective To describe the evolution of scientific production on academic integrity and artificial intelligence in higher education. Methodology A bibliometric analysis was carried out using VOSviewer software and the Bibliometrix package in R. A total of 467 documents published between 2017 and 2025, retrieved from the Web of Science database, were analyzed. Results The analysis reveals a rapid expansion of the field, with an annual growth rate of 71.97%, concentrated in journals specializing in education, academic ethics, and technology. The field has evolved from a focus on the use of artificial intelligence in dishonest practices to the study of its integration in higher education. Four main lines of research were identified: the impact and adoption of artificial intelligence, implications for students, academic dishonesty, and associated psychological factors. Conclusions The field is at an early stage of development but is expanding rapidly, albeit with fragmented evolution, limited collaboration between research teams, and high editorial dispersion. The analysis shows a predominance of descriptive approaches, leaving room for the development of theoretical frameworks. Originality or value This study provides an overview and updated of the evolution of research on artificial intelligence and academic integrity, identifying trends, collaborations, and conceptual gaps. It highlights the need to promote theoretical reflection to guide future practice and research on the ethical use of artificial intelligence in higher education.

REVIEW

Open Access

# Exploring the nexus of academic integrity and artificial intelligence in higher education: a bibliometric analysis

![](images/c00cc4ac0f1092f2fb2befdc68ad05d0346d04c335005cecfff20e098fc161eb.jpg)

Daniela Avello<sup>1</sup> and Samuel Aranguren Zurita<sup>1\*</sup>

\*Correspondence:   
Samuel Aranguren Zurita   
investigacion.to@uc.cl   
<sup>1</sup>Departamento de Terapia   
Ocupacional, Escuela de Ciencias   
de la Salud, Facultad de Medicina,   
Pontificia Universidad Católica de   
Chile, Santiago, Chile

## Abstract

Keywords Academic integrity, Artificial intelligence, Higher education, Bibliometric analysis, Academic dishonesty

## Introduction

The field of artificial intelligence research began to take shape in the 1940s with the creation of basic neural network models aimed at mimicking the functioning of a neuron (Muthukrishnan et al. 2020; Salas-Pilco and Yang 2022). However, it was the public launch of ChatGPT in November 2022 that marked a turning point, leading to the widespread incorporation of artificial intelligence into everyday activities and various professional domains, such as industrial production, healthcare, and education (López-Chila et al. 2023; Wu et al. 2023).

In this context, artificial intelligence has enabled significant advancements in education. Students can utilize these tools to enhance their writing, brainstorm ideas, streamline the use of software through basic programming commands, and conduct deeper analyses of quantitative, qualitative, and even visual data, such as images or diagrams (Chan and Hu 2023; Salas-Pilco and Yang 2022). Meanwhile, educators can optimize grading processes, streamline lesson material preparation, personalize teaching and learning strategies based on individual student needs, identify gaps in student learning, enhance online education tools, and refine evaluation rubrics (Klyuchnikov et al. 2021; Nazarovets & Teixeira da Silva, 2024).

Some have even referred to this period as a new era—the “post-plagiarism” era— where advanced technology is deeply integrated into everyday life and cannot be decoupled from human society due to its complexity. In this era, a hybrid emerges between humans and machines, where human writing is enhanced by artificial intelligence (Birks and Clare 2023; Eaton 2023).

However, artificial intelligence has also introduced significant challenges for higher education. For instance, the capabilities of artificial intelligence have sparked debates about the necessity of professionals’ knowledge and skills, as well as how education can prepare individuals to add value beyond what artificial intelligence can ofer (van Slyke et al. 2023). The extensive use of artificial intelligence could potentially reduce students motivation to learn and develop skills, weaken academic culture, and ultimately devalue higher education (Navarro-Dolmestch 2023). Furthermore, the broad capabilities of artificial intelligence create opportunities for students to breach academic integrity (Eke 2023; Xia et al. 2024; Xu et al. 2024).

Academic integrity, understood as the commitment of all members of an academic community to the values of honesty, trust, fairness, respect, responsibility, and courage (International Center for Academic Integrity 2021; McCabe and Pavela 2004), is an interdisciplinary concern across multiple academic fields (Ahsan et al. 2022; Gottardello and Karabag 2022; Parnther 2020). Although academic integrity has traditionally been a central focus in higher education, the rapid advancements in artificial intelligence in recent years have significantly heightened its importance (Lo 2023; López-Chila et al. 2023; Moya et al. 2023; Rodrigues et al. 2024).

To date, some uses of artificial intelligence have raised concerns about potential infringements on the principles of academic integrity (Birks and Clare 2023). For example, AI tools can simplify plagiarism by allowing texts to be quickly rephrased without a deep understanding of the subject matter (Navarro-Dolmestch 2023). It can also assist in solving and copying answers during exams or in writing essays, as studies have shown that artificial intelligence is capable of achieving high scores in these types of assessments (Surahman and Wang 2022; Yeadon et al. 2023). Moreover, artificial intelligence has introduced a new dimension to contract cheating, allowing students to easily generate a wide range of content and falsely claim authorship (Ahsan et al. 2022; Xu et al. 2024).

Artificial intelligence, which represents both a source of opportunities and challenges, and is currently experiencing rapid expansion, growth, and evolution (Wu et al. 2023; Xu et al. 2024), compels educators and researchers to stay informed about advancements in this field. It also demands continuous ethical reflection on the uses of new technologies in education (Salas-Pilco and Yang 2022; Xia et al. 2024).

In this context, literature reviews are crucial for keeping the scientific community updated on advancements in their fields. While research exists on topics related to academic integrity, such as plagiarism (Lynch et al. 2017) and contract cheating (Ahsan et al. 2022), as well as studies addressing the challenges that artificial intelligence and technological advancements pose to academic integrity (Garg and Goel 2022; King 2023), bibliometric reviews specifically analyzing the relationship between artificial intelligence and academic integrity remain scarce (Nazarovets & Teixeira da Silva, 2024; Rodrigues et al. 2024; Xia et al. 2024).

Given that this remains an emerging field (Imran and Almusharraf 2023; Salas-Pilco and Yang 2022; Wang et al. 2024), with significant knowledge gaps still to be addressed and the continuous emergence of new lines of inquiry, the aim of this study is to describe the evolution of scientific output on academic integrity and artificial intelligence in higher education. Specifically, it seeks to identify trends, collaborations, and emerging themes to inform and guide future research and policymaking.

## Method

To explore the research question, a bibliometric analysis was carried out utilizing VOSviewer software alongside R tools, specifically the Bibliometrix package and the Biblioshiny application (Aria and Cuccurullo 2017). These tools are valuable for describing the behavior and dynamics of scientific publications, enabling the analysis and visualization of complex bibliometric data (Arruda et al. 2022; Dervis 2019).

## Information sources and search strategy

The articles were sourced from the Web of Science database on May 28, 2025. The search was conducted by topic, employing a horizontal search strategy that encompassed the three main themes of the study, associated with the Boolean codes shown in Table  1. Search terms were initially selected independently by two authors and later refined through collaborative discussions.

Table 1 Search strategy
<table><tr><td>Theme</td><td>Boolean code</td></tr><tr><td>Academic Integrity</td><td>(“academic integrity&quot;OR&quot;plagiarism&quot;OR&quot;academic dishonesty&quot;OR&quot;misconduct&quot;OR&quot;contract cheating&quot;OR&quot;academic fraud&quot;OR&quot;academic honesty&quot;OR &quot;academic ethics&quot;OR&quot;cheating&quot;OR &quot;ghostwriting&quot;OR“ethical use of Al&quot; OR&quot;research integrity&quot;OR&quot;values education&quot;OR &quot;academic values&quot;OR“moral education&quot;OR&quot;academic morality&quot;OR&quot;moral development&quot;OR&quot;moral</td></tr><tr><td>Artificial Intelligence</td><td>values&quot;) (“artificial intelligence&quot;OR Al OR &quot;chatgpt&quot;OR&quot;gpt&quot; OR &quot;generative artificial intelligence&quot;OR &quot;generative AI&quot;OR openai OR &quot;large language models&quot; OR“GenAI&quot;OR“machine learning&quot;OR</td></tr><tr><td>Higher</td><td>&quot;deep learning&quot;OR“neural networks&quot;OR“natural language processing&quot; OR “intelligent systems&quot;) (&quot;higher education&quot;OR&quot;college student*&quot;OR&quot;university&quot;OR&quot;faculty&quot;OR&quot;college&quot;OR &quot;under-</td></tr></table>

The initial search identified a total of 605 records, of which two were duplicates. For the screening process, both authors independently reviewed the titles, abstracts, and keywords of each article using the Rayyan platform (https://new.rayyan.ai). At the end of this stage, a 96% agreement was reached between the two reviewers regarding inclusion decisions. Discrepancies were resolved in a joint meeting, during which the titles, abstracts, and keywords of the disputed articles were reviewed again, and inclusion or exclusion was determined by consensus. Following this screening process, a total of 467 records were included for full analysis.

Inclusion criteria considered texts that met the following conditions: (1) the study focused on the use of artificial intelligence and addressed academic integrity either as a primary or (2) secondary topic, with its mention accepted in any section of the article (introduction, results, or conclusions); and (3) the context of the research was within higher education.

Exclusion criteria included: (1) studies addressing the use of artificial intelligence and academic integrity in non-academic contexts; (2) studies focusing on primary or secondary education; (3) studies addressing academic integrity in higher education without a direct connection to artificial intelligence; or (4) studies focused on professional or disciplinary ethics.

## Data analysis

To identify the leading authors and the most influential publications, the Bibliometrix package in R was used, focusing on metrics such as the number of publications, citation counts, and authors’ h-index. Similarly, to visualize the evolution of the research field and highlight the main current and emerging lines of inquiry, the keyword co-occurrence function in VOSviewer was employed. In addition, some of the figures were created using Flourish (https://flourish.studio) to enhance visual clarity.

## Results

## Main results

The analysis of data from the period 2017:2025 reveals a rapidly expanding field of study, with an academic output of 467 documents sourced from 258 distinct outlets. The annual growth rate of 71.97% and an average of 12.11 citations per document underscore the relevance and sustained impact of these investigations. Furthermore, collaboration is prominent, with an average of 3.93 co-authors per document and a noteworthy 21.63% of international co-authorships. Most publications are journal articles, indicating a preference for this format in disseminating research findings (see Table 2).

## Annual scientific production

In this research field, publications were identified starting from 2017, with an annual growth rate of 28.31%, indicating rapid expansion. An analysis of its evolution reveals that only five publications were recorded between 2017 and 2021, compared to 462 additional works published between 2022 and May 2025. As shown in Figs. 1 and 2022 marked a significant increase in scientific output, with the majority of publications concentrated between 2022 and 2025.

Table 2 Compiled data
<table><tr><td>Main information about the data</td><td>Description</td></tr><tr><td>Timespan</td><td>2017:2025</td></tr><tr><td>Sources</td><td>258</td></tr><tr><td>Documents</td><td>467</td></tr><tr><td>Annual Growth Rate (%)</td><td>71.97</td></tr><tr><td>Average Document Age</td><td>0.897</td></tr><tr><td>Average Citations per Document</td><td>12.11</td></tr><tr><td>References</td><td>16,428</td></tr><tr><td>Author Keywords (DE)</td><td>1187</td></tr><tr><td>Authors</td><td>1727</td></tr><tr><td>Single-Authored Document Authors</td><td>86</td></tr><tr><td>Co-authors per Document</td><td>3.93</td></tr><tr><td>International Co-authorship (%)</td><td>21.63</td></tr></table>

![](images/c52fbabedc6caf6f2a8a92d9e6bed05e2d248f0ad62ccb72f6c2945770555e7e.jpg)  
Fig. 1 Annual scientific production

Although 2024 was the year with the highest scientific output, it is noteworthy that in the first half of 2025 (when this research was conducted), 153 publications had already been recorded, compared to 240 for the entirety of 2024. This suggests a continuing upward trend in scientific production in the coming years (see Fig. 1).

## Annual scientific production

It was observed that 21.63% of the texts linking academic integrity, higher education, and artificial intelligence were published in 10 sources (see Table 3). As expected, the journals with the highest output in this area are specialized in education, academic ethics, and technology. Education Sciences accounts for the largest number of publications on the topic, with a total of 20 articles published between 2023 and 2025. In second place is Education and Information Technologies, with 10 of its 15 articles on the topic published in the current year, 2025. These findings indicate that this is an emerging and rapidly developing research field.

Table 3 Top ten sources of publications
<table><tr><td>Sources</td><td>Documents</td><td>Percentage</td></tr><tr><td>Education Sciences</td><td>20</td><td>4.28%</td></tr><tr><td>Education and Information Technologies</td><td>15</td><td>3.21%</td></tr><tr><td>Journal of Academic Ethics</td><td>14</td><td>3.00%</td></tr><tr><td>International Journal for Educational Integrity</td><td>9</td><td>1.93%</td></tr><tr><td>Journal of University Teaching and Learning Practice</td><td>9</td><td>1.93%</td></tr><tr><td>Frontiers in Education</td><td>8</td><td>1.71%</td></tr><tr><td>Interactive Learning Environments</td><td>7</td><td>1.50%</td></tr><tr><td>International Journal of Educational Technology in Higher Education</td><td>7</td><td>1.50%</td></tr><tr><td>Cogent Education</td><td>6</td><td>1.28%</td></tr><tr><td>Electronic Journal of e-Learning</td><td>6</td><td>1.28%</td></tr></table>

![](images/921509fc5112918d37284e607fb6bd97965f1357e0f4122e6cec8c44c791bb1f.jpg)  
Fig. 2 Temporal overlap of co-occurring keywords plus

## Evolution of the field

The evolution of the co-occurrence of Keywords Plus used in publications from the 2023–2025 period was analyzed (see Fig. 2).

The blue clusters represent the predominant keywords at the beginning of this period, highlighting terms such as dishonesty, attitudes, and misconduct. The green clusters reflect an intermediate stage, where both concepts related to academic integrity—such as plagiarism and academic dishonesty—and keywords associated with higher education—such as university, education, and students—are observed. Finally, the yellow clusters correspond to the most frequent keywords toward the end of the analyzed period, with notable terms including ChatGPT and artificial intelligence.

This distribution suggests a thematic shift in the scientific literature: from an initial focus on concerns regarding the use of artificial intelligence for academic dishonesty, toward a broader interest in its integration within the context of higher education. It is particularly noteworthy that, at the beginning of the analyzed period, the most prominent terms were associated with explanatory frameworks such as the Theory of Planned Behavior and attitudes; whereas toward the end of the period, the most frequent keywords were ChatGPT, challenges, acceptance, and adoption. This indicates that the field is currently in a phase focused on describing the impact of artificial intelligence on education, while theoretical frameworks for explaining academic integrity-related behaviors in this new reality have been largely overlooked or, alternatively, researchers have opted to adapt existing models.

The temporal co-occurrence analysis did not include articles published prior to November 2022 due to the lack of co-occurring keywords. For this reason, these texts were manually reviewed, identifying 15 articles published before the release of ChatGPT. Of these, six focus on plagiarism detection using early natural language processing models, applied to both written assignments and programming tasks. Five studies address intelligent proctoring systems for exam monitoring, utilizing technologies such as facial recognition or neural network-based algorithms. Two articles examine the use of artificial intelligence in academic writing tools, and the other two focus on discussing the risks and benefits of emerging artificial intelligence in educational contexts. Collectively, these works show a predominant emphasis on the development of technologies aimed at controlling and detecting academic dishonesty. Nevertheless, all of them include some reflection on the impact of artificial intelligence on higher education, and specifically, on academic integrity.

Figure 3 illustrates the frequency and co-occurrence of Keywords Plus in research on academic integrity. The analysis highlights the emergence of four distinct thematic clusters within the field. The size of the nodes indicates the relevance of each term within the network, while the thickness of the connecting lines reflects the strength of the relationships between the terms.

Red cluster The largest and most densely connected, is led by the keyword artificial intelligence, accompanied by other terms such as ChatGPT, performance, technology, user acceptance, model, adoption, and AI. This cluster reveals lines of research focused on the impact and adoption of artificial intelligence-based technologies. It includes studies that examine both the implementation of tools like ChatGPT in educational settings and the acceptance of such tools by users, as well as the academic performance associated with their use and the application of theoretical models of technology adoption.

![](images/83f73e0e2dbc808a0db0a66d1314ecb12439e74a179d3c39defe30c45b92ceb8.jpg)  
Fig. 3 Network map of co-occurring keywords plus related to research on academic integrity

Green cluster Composed of terms such as students, knowledge, higher education, university, impact, system, and challenges, shows strong connections with both AIrelated terms and those linked to academic dishonesty. This cluster groups research that addresses the impact of artificial intelligence with students as central actors, exploring phenomena such as knowledge creation, challenges faced by both the educational system and teaching staf, and the implications for academic integrity.

Yellow cluster Made up of terms such as plagiarism, attitude, perceptions, academic dishonesty, and online, represents research focused on academic ethics in the age of artificial intelligence. Publications in this group concentrate on phenomena associated with academic dishonesty and its connection to the use of digital tools based on AI.

Blue cluster Which includes keywords such as education, motivation, dishonesty, integrity, and planned behavior, presents a perspective more focused on psychological and behavioral variables. This cluster encompasses research lines that examine individual and motivational factors influencing the use of artificial intelligence, academic integrity, and dishonest behaviors.

Figure 4 presents the strategic map of the themes identified through the co-occurrence analysis of Keywords Plus. In the upper-right quadrant, corresponding to motor themes, terms such as education, students, and higher-education are located. These themes exhibit both high density and high centrality, indicating well-established and actively developing lines of research within the field.

In the lower-right quadrant are the basic themes, among which lines focused on artificial-intelligence, chatgpt, and a.i. stand out. These represent fundamental topics for the area of study, although they are still undergoing theoretical and methodological consolidation. This is consistent with the emerging nature of the field and the rapid pace of technological change associated with it.

![](images/22d5f83c7ef7a3bd8aa0d27b1df7296a3f84eaf7100066d04b953e309837f43a.jpg)  
Fig. 4 Thematic map of research on academic integrity and artificial intelligence

The niche or specialized themes are in the upper-left quadrant, including topics such as information technology, technology acceptance, and unified theory. These themes show a high level of internal development but are less connected to the core topic of the research, suggesting conceptually robust approaches with limited transversal integration in the field’s broader literature.

Finally, the lower-left quadrant contains emerging or marginal themes, characterized by low density and centrality. This group includes concepts such as generative a.i., models, and science. Their position on the map suggests that these are either nascent areas still under development or peripheral in relation to the main thematic axis of the analyzed corpus.

## Most influential authors

The most productive authors in this field are Bannister, Peter; Eaton, Sarah Elaine; and Perkins, Mike, each with five publications (see Table  4). Among the ten most prolific authors, Currie, Geofrey (30 local citations), as well as Perkins, Mike and Roe, Jasper (28 local citations each), stand out as the most cited within the analyzed corpus.

Specifically, the work “Academic Integrity and Artificial Intelligence: Is ChatGPT Hype, Hero or Heresy?” by Currie, Geofrey (18 local citations), and the article “Detection of GPT-4 Generated Text in Higher Education: Combining Academic Judgement and Software to Identify Generative AI Tool Misuse”, co-authored by Perkins, Mike and Roe, Jasper (15 local citations), represent their most influential contributions to the field.

## Analysis of co-authorship networks and international collaborations

The network analysis reveals that the institution currently leading research in this field is Charles Sturt University in Australia. From the same country, the University of Tasmania shares the fifth position with Multimedia University and the University of Central Florida, making Australia the only country with more than one institution in this top (see Table 5). It can also be observed that the most productive institutions in this field collaborate relatively little with other institutions.

Figure 5 shows the country’s leading research in this field. In this case, the United States stands out with 260 publications featuring at least one author from that country. Notably, only one of its universities ranks among the five most productive in the world, which suggests that many institutions in the U.S. are conducting research in this area. The list of the five most productive countries in this field is completed by Australia (127), China (117), the United Kingdom (113), and Spain (71).

Table 4 Top ten authors with the highest output in the field
<table><tr><td>Authors</td><td>Articles</td><td>Local Citations</td></tr><tr><td>Bannister, Peter</td><td>5</td><td>3</td></tr><tr><td>Eaton, Sarah Elaine</td><td>5</td><td>3</td></tr><tr><td>Perkins, Mike</td><td>5</td><td>28</td></tr><tr><td>Roe, Jasper</td><td>4</td><td>28</td></tr><tr><td>Wang, Xinghua</td><td>4</td><td>1</td></tr><tr><td>Wu, Chuxiang</td><td>4</td><td>0</td></tr><tr><td>Asad, Muhammad Mujtaba</td><td>3</td><td>0</td></tr><tr><td>Crawford, Joseph</td><td>3</td><td>1</td></tr><tr><td>Currie, Geoffrey</td><td>3</td><td>30</td></tr><tr><td>Hysaj, Ajrina</td><td>3</td><td>0</td></tr></table>

Table 5 International collaborations by institution
<table><tr><td>Institution</td><td>Country</td><td>Documents</td><td>Collaborative Documents</td></tr><tr><td>Charles Sturt University</td><td>Australia</td><td>21</td><td>0</td></tr><tr><td>University of the Basque Country</td><td>Spain</td><td>11</td><td>1</td></tr><tr><td>Sultan Qaboos University</td><td>Oman</td><td>10</td><td>3</td></tr><tr><td>University of Calgary</td><td>Canada</td><td>10</td><td>0</td></tr><tr><td>Multimedia University</td><td>Malaysia</td><td>9</td><td>3</td></tr><tr><td>University of Central Florida</td><td>United States</td><td>9</td><td>3</td></tr><tr><td>University of Tasmania</td><td>Australia</td><td>9</td><td>4</td></tr></table>

Note: All institutions with the same number of publications as the fifth-ranked university were included

![](images/ae6d9302d52f5bbcc6c54434cc7e283400cf33baf1910a38ebb47f518b1a725d.jpg)  
Fig. 5 Geographical distribution of research output in academic integrity and artificial intelligence

![](images/c0429ac131dac7b6456e0f00a7fe13d481050fe9dcbb612d54b8228f0d77aa6b.jpg)  
Fig. 6 International Collaborations by research teams

Finally, Fig. 6 illustrates the specific connections between research teams in this field. A total of 11 research teams were identified as co-authors of at least two articles on the topic. It is worth noting that only two connections were observed between authors from diferent teams, suggesting that, despite the increase in publications on the subject in recent years, research is still being conducted by teams that have not established collaborations with one another.

Denser connections indicate that these research teams have collaborated on a greater number of joint publications. In this case, the strongest link corresponds to the collaboration between Perkins M. and Roe J., who have co-authored four publications. On the other hand, Wang, X. stands out as a bridge between two research teams. Similarly, Middleton, R. and Nikolic, S., who belong to two diferent nodes, have also collaborated with each other. This occurs in a context where there are still few authors with more than two published texts, reflecting the emerging and developing nature of the field.

## Discussion

The aim of this study was to describe the evolution of scientific production on academic integrity and artificial intelligence in higher education, identifying trends, collaborations, and emerging topics to inform future research and policy development. In this context, the study provides a detailed overview of the development of the field and its collaboration dynamics.

The results reveal an accelerated growth in scientific output, particularly associated with the public release of ChatGPT by OpenAI in November 2022 (López-Chila et al. 2023; Wu et al. 2023). This may be attributed not only to the launch of the tool itself, but also to the fact that its accessibility and ease of use have had a significant impact on the educational landscape and academic integrity (Klyuchnikov et al. 2021; Navarro-Dolmestch 2023; van Slyke et al. 2023), as was already anticipated by research conducted prior to the emergence of ChatGPT.

In terms of scientific production, a high dispersion of publications stands out: 467 articles published across 258 diferent sources. Considering that 21.63% are concentrated in only 10 journals, the average number of articles in the remaining sources is just 1.52. This dispersion may be due to the multidisciplinary interest the topic generates, its emerging nature, and possibly the limited number and early stage of development of editorial lines specialized in the intersection between artificial intelligence and academic integrity, features that are typical of research fields in their early stages. (Singh et al. 2022).

In this sense, our findings confirm that this is an emerging field, as highlighted by previous studies (Imran and Almusharraf 2023; Wang et al. 2024). However, it is important to emphasize that the rapid increase in publication volume, along with the high diversity of authors, afiliations, and countries, suggests that this growth is a response to the disruptive phenomenon that artificial intelligence has become.

This expansion, driven by both the urgency to address the efects of these technologies and the speed at which they are transforming the academic environment (López-Chila et al. 2023; Eaton 2023), suggests that the current literature is primarily oriented toward documenting the development, scope, and impact of artificial intelligence in education, rather than consolidating robust conceptual frameworks. This is also reflected in the thematic analysis, where the cluster associated with explanatory theories of behavior related to artificial intelligence and academic integrity is the smallest and least developed to date.

The limited collaboration among research teams suggests that the field has not yet reached a suficient level of maturity to articulate shared research agendas. This may be explained by the field’s recent emergence, this may be because many studies have been driven by institutions responding to immediate and locally rooted ethical challenges. Both patterns are typical of early-stage fields, where small research teams working in isolation tend to predominate (Singh et al. 2022), often with fragmented theoretical and epistemological approaches.

Furthering this point, the broad distribution of publications across institutions in the United States, the country with the highest output, suggests a decentralized approach that could, in the future, translate into advances from multiple disciplines and perspectives. This contrasts with countries like Australia, where the concentration of publications in a small number of universities may promote the development of more cohesive research communities with more elaborated theoretical and methodological frameworks.

Finally, a clear geographical asymmetry can be observed in the development of the field. Despite the global relevance of the issue, scientific production on this topic remains scarce in regions such as Latin America and Africa. This indicates that local perspectives from these contexts still have a marginal impact on the international debate, a phenomenon that has already been documented in other areas of knowledge (Adams et al. 2021; Ezugwu et al., 2023). This gap presents an opportunity to promote the inclusion of diverse regional perspectives through international collaboration networks, funding mechanisms, and research agendas that recognize the importance of these contexts in formulating global responses to the ethical use of artificial intelligence in education.

It is important to acknowledge certain limitations of this study. First, the analysis was based exclusively on publications indexed in the Web of Science database. Although this source is known for its rigorous indexing standards, it excludes relevant repositories such as Scopus, ERIC, or regional databases. This may have limited the inclusion of studies from non-English-speaking countries or from institutions with lower international visibility, thereby potentially reinforcing existing asymmetries in knowledge production.

Additionally, given the rapid and ongoing evolution of this field, some patterns identified (such as editorial fragmentation or limited inter-institutional collaboration) may shift in the coming years. These limitations should be seen as opportunities for future research to adopt more inclusive and comprehensive bibliometric approaches and to explore how the field evolves as it continues to consolidate.

## Conclusions

The results suggest that the accelerated growth experienced by this field since late 2022, following the emergence of tools such as ChatGPT, is occurring within a context of limited collaboration between research teams and high levels of editorial, institutional, and authorial fragmentation. A total of 93.8% of authors have published only one article in the area, and co-authorship networks reveal weak connections among teams, with mostly isolated collaborations. This dynamic, along with the concentration of scientific output in countries such as the United States and Australia, suggests that the field is still in an early developmental stage and far from forming a cohesive scientific community.

The thematic analysis revealed four well-defined clusters. The first focuses on academic dishonesty (plagiarism, cheating, integrity); the second addresses artificial intelligence and its associated technologies (ChatGPT, natural language processing); the third is linked to higher education as the main context of application; and the fourth—smaller in size—brings together theoretical and ethical concepts applicable to the analysis of AI.

The lower density of this last cluster suggests that the literature has primarily focused on describing uses, impacts, and immediate challenges, rather than on building solid conceptual frameworks around the phenomenon.

In this regard, future research could aim to systematize the theoretical approaches currently being applied in the field, as well as explore the adaptation of existing models from psychology, education, and other social sciences. Eaton (2023) argues that the advancement of artificial intelligence is profoundly transforming the educational ecosystem, which may require new theoretical models to understand academic integrity within this new reality.

Finally, although the findings ofer an up-to-date and detailed overview of the field, their practical implications remain to be explored more thoroughly. Higher education institutions, academic integrity ofices, and public agencies could use these insights to inform the design of institutional strategies, ethical guidelines, and faculty development programs, leveraging the most current information available to promote the responsible use of artificial intelligence in educational contexts.

## Abbreviations

AI Artificial Intelligence

## Author contributions

D.A. received funding for the project, created the research design, participated in data extraction, use of software, data analysis, writing the manuscript, and revising the manuscript. S.A.Z. participated in the research design, data extraction, use of software, data analysis, writing the manuscript, and revising the manuscript.

## Funding

This study was funded by the National Fund for Scientific and Technological Development (FONDECYT) for Initiation, project number 11240191, granted by the National Agency for Research and Development (ANID).

## Data availability

The datasets generated during and/or analysed during the current study are available in the Pontificia Universidad Católica de Chile repository, doi: 10.60525/04teye511/IHMXP3.

## Declarations

## Ethics approval and consent to participate

Approval was obtained from the Ethical Scientific Committee in Social Sciences, Arts, and Humanities at the Pontificia Universidad Católica de Chile in 2024, under number 230327001.

## Consent for publication

Not applicable.

## Competing interests

The authors declare no competing interests.

Received: 2 January 2025 / Accepted: 13 August 2025

Published online: 29 August 2025

## References

Adams J, Pendlebury D, Potter R, Szomszor M (2021) Global research report Latin America: South and Central America, Mexico and the Caribbean

Ahsan K, Akbar S, Kam B (2022) Contract cheating in higher education: a systematic literature review and future research agenda. Assess Evaluation High Educ 47(4):523–539. https://doi.org/10.1080/02602938.2021.1931660

Aria M, Cuccurullo C (2017) Bibliometrix: an R-tool for comprehensive science mapping analysis. J Informetrics 11(4):959–975. https://doi.org/10.1016/j.joi.2017.08.007

Arruda H, Silva ER, Lessa M, Proença D Jr., Bartholo R (2022) VOSviewer and bibliometrix. J Med Libr Association 110(3):392–395. https://doi.org/10.5195/jmla.2022.1434

Birks D, Clare J (2023) Linking artificial intelligence facilitated academic misconduct to existing prevention frameworks. Int J Educational Integr 19(1). https://doi.org/10.1007/s40979-023-00142-3

Chan CKY, Hu W (2023) Students’ voices on generative AI: perceptions, benefits, and challenges in higher education. Int J Educational Technol High Educ 20(1):43. https://doi.org/10.1186/s41239-023-00411-8

Dervis H (2019) Bibliometric analysis using bibliometrix an R package. J Scientometr Res 8(3):156–160. https://doi.org/10.5530/ JSCIRES.8.3.32

Eaton SE (2023) Postplagiarism: transdisciplinary ethics and integrity in the age of artificial intelligence and neurotechnology. Int J Educational Integr 19(1):23. https://doi.org/10.1007/s40979-023-00144-1

Ezugwu AE, Oyelade ON, Ikotun AM, Agushaka JO, Ho YS (2023) Machine Learning Research Trends in Africa: A 30 Years Overview with Bibliometric Analysis Review. In Archives of Computational Methods in Engineering (Vol. 30, Issue 7, pp. 4177–4207). Springer Science and Business Media B.V. https://doi.org/10.1007/s11831-023-09930-z

Garg M, Goel A (2022) A systematic literature review on online assessment security: current challenges and integrity strategies. Computers Secur 113:102544. https://doi.org/10.1016/j.cose.2021.102544

Gottardello D, Karabag SF (2022) Ideal and actual roles of university professors in academic integrity management: a comparative study. Stud High Educ 47(3):526–544. https://doi.org/10.1080/03075079.2020.1767051

Imran M, Almusharraf N (2023) Analyzing the role of ChatGPT as a writing assistant at higher education level: A systematic review of the literature. Contemp Educational Technol 15(4):ep464. https://doi.org/10.30935/cedtech/13605

International Center for Academic Integrity (2021) The Fundamental Values of Academic Integrity (3rd ed.). International Center for Academic Integrity. www.academicintegrity.org/the-fundamental-values-

King MR (2023) A conversation on artificial intelligence, chatbots, and plagiarism in higher education. Cell Mol Bioeng 16(1):1–2. https://doi.org/10.1007/s12195-022-00754-8

Klyuchnikov D, Shurukhina T, Gavrilova T, Zhikharev A, Deeney I (2021) Some aspects of AI-Technologies in education. Revista San Gregorio 1(44):186–197. https://doi.org/10.36097/rsan.v1i44.1610

Lo CK (2023) What is the impact of ChatGPT on education?? A rapid review of the literature. Educ Sci 13(4):410. https://doi.org/ 10.3390/educsci13040410

López-Chila R, Llerena-Izquierdo J, Sumba-Nacipucha N, Cueva-Estrada J (2023) Artificial intelligence in higher education: an analysis of existing bibliometrics. Educ Sci 14(1):47. https://doi.org/10.3390/educsci14010047

Lynch J, Everett B, Ramjan LM, Callins R, Glew P, Salamonson Y (2017) Plagiarism in nursing education: an integrative review. J Clin Nurs 26(19–20):2845–2864. https://doi.org/10.1111/jocn.13629

McCabe DL, Pavela G (2004) Ten (Updated) principles of academic integrity: how faculty can foster student honesty, vol 36. Taylor & Francis, Ltd., 3

Moya BA, Eaton SE, Pethrick H, Hayden KA, Brennan R, Wiens J, Mcdermott B, Lesage J (2023) Academic integrity and artificial intelligence in higher education contexts: A rapid scoping review protocol. Can Perspect Acad Integr 5(2). https://doi.org /10.11575/cpai.75990

Muthukrishnan N, Maleki F, Ovens K, Reinhold C, Forghani B, Forghani R (2020) Brief history of artificial intelligence. Neuroimaging Clin N Am 30(4):393–399. https://doi.org/10.1016/j.nic.2020.07.004

Navarro-Dolmestch R (2023) Risks and challenges posed by artificial intelligence generative applications for academic integrity. Derecho PUCP 91:231–270. https://doi.org/10.18800/derechopucp.202302.007

Nazarovets S, da Teixeira JA (2024) ChatGPT as an author: bibliometric analysis to assess the validity of authorship. Account Res 1–11. https://doi.org/10.1080/08989621.2024.2345713

O. Eke D (2023) ChatGPT and the rise of generative AI: threat to academic integrity? J Responsible Technol 13. https://doi.org/1 0.1016/j.jrt.2023.100060

Parnther C (2020) Academic misconduct in higher education: A comprehensive review. J High Educ Policy Leadersh Stud 1(1):25–45. https://doi.org/10.29252/johepal.1.1.25

Rodrigues M, Silva R, Borges AP, Franco M, Oliveira C (2024) Artificial intelligence: threat or asset to academic integrity? A biblio metric analysis. Kybernetes. https://doi.org/10.1108/K-09-2023-1666

Salas-Pilco SZ, Yang Y (2022) Artificial intelligence applications in Latin American higher education: a systematic review. Int J Educational Technol High Educ 19(1):21. https://doi.org/10.1186/s41239-022-00326-w

Singh CK, Barme E, Ward R, Tupikina L, Santolini M (2022) Quantifying the rise and fall of scientific fields. PLoS ONE 17(6). https:// doi.org/10.1371/journal.pone.0270131

Surahman E, Wang TH (2022) Academic dishonesty and trustworthy assessment in online learning: A systematic literature review. J Comput Assist Learn 38(6):1535–1553. https://doi.org/10.1111/jcal.12708

van Slyke C, Johnson RD, Sarabadani J (2023) Generative artificial intelligence in information systems education: challenges, consequences, and responses. Commun Association Inform Syst 53:1–21. https://doi.org/10.17705/1CAIS.05301

Wang N, Wang X, Su YS (2024) Critical analysis of the technological afordances, challenges and future directions of generative AI in education: a systematic review. Asia Pac J Educ 44(1):139–155. https://doi.org/10.1080/02188791.2024.2305156

Wu T, He S, Liu J, Sun S, Liu K, Han QL, Tang Y (2023) A brief overview of chatgpt: the history, status quo and potential future development. IEEE/CAA J Automatica Sinica 10(5):1122–1136. https://doi.org/10.1109/JAS.2023.123618

Xia Q, Weng X, Ouyang F, Lin TJ, Chiu TKF (2024) A scoping review on how generative artificial intelligence transforms assessment in higher education. Int J Educational Technol High Educ 21(1):40. https://doi.org/10.1186/s41239-024-00468-z

Xu X, Chen Y, Miao J (2024) Opportunities, challenges, and future directions of large Language models, including ChatGPT in medical education: a systematic scoping review. J Educational Evaluation Health Professions 21:6. https://doi.org/10.3352 /jeehp.2024.21.6

Yeadon W, Inyang O-O, Mizouri A, Peach A, Testrow CP (2023) The death of the short-form physics essay in the coming AI revolution. Phys Educ 58(3):035027. https://doi.org/10.1088/1361-6552/acc5cf

## Publisher’s note