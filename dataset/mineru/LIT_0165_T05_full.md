RESEARCH

Open Access

# Evaluating ChatGPT‑3’s eficacy in solving Check orfor coding tasks: implications for academic integrity in English language assessments

![](images/1b22a06955c626a1da270655e58528939761a81a1fc32d4ef7d0da11f20d30a8.jpg)

Seyedeh Elham Elhambakhsh<sup>1\*</sup>

\*Correspondence: s.e.elhambakhsh@yazd.ac.i

<sup>1</sup> Department of Language and Literature, Yazd University, Yazd, Iran

## Abstract

The purpose of this study was to examine ChatGPT-3’s capabilities to generate code solutions for assessment problems commonly assessed by automatic correction tools in the TEFL academic setting, focusing on the Kattis platform. The researcher explored potential implications for academic integrity and the challenges associated with AIgenerated solutions. The investigation involved testing ChatGPT on a subset of 124 English language assessment tasks from Kattis, a widely used automatic software grading tool. The results revealed that ChatGPT independently solved 16 tasks successfully. Data analysis demonstrated that while ChatGPT performed well on simpler problems, it faced challenges with more complex assessment tasks. To supplement quantitative findings, a qualitative follow-up investigation was conducted, including interviews with two EFL assessment instructors. The discussion encompassed methodological considerations, the efectiveness of Kattis in preventing cheating, and the limitations in detecting AI-generated code. ChatGPT independently solved 16 out of 124 assessment tasks assessed by Kattis. Performance varied based on task complexity, with better accuracy on simpler problems. Qualitative insights revealed both the strengths and limitations of Kattis in preventing cheating. While ChatGPT demonstrates competence in solving certain assessment problems, challenges persist with more complex tasks. The study emphasizes the need for continuous adaptation in EFL assessment methodologies to maintain academic integrity in the face of evolving AI capabilities. As students gain access to sophisticated AI-generated solutions, the need for vigilant strategies to uphold originality and critical thinking in academic work becomes increasingly crucial. The study’s findings have implications for multiple stakeholders, including (1) awareness of AI capabilities in generating code solutions, necessitating vigilant assessment strategies. (2) Understanding the importance of academic integrity and the limitations of AI in mastering complex assessment tasks. (3) Insights into the interplay between AI, automated assessment systems, and academic integrity, guiding future investigations. This performance illustrates the need for careful assessment design to mitigate the risk of AI-assisted academic dishonesty while maintaining rigorous academic standards.

Keywords: Automated assessment systems, ChatGPT, Cheating, English Language Assessment GPT-3, Kattis

## Introduction

In the realm of artificial intelligence, the rapid evolution of chatbot technology is evident in the development of ChatGPT-4, the latest iteration following GPT-3 (Khalil & Er, 2023). While GPT-3 is publicly available on OpenAI’s website as a free version, its remarkable proficiency in responding to diverse queries raises questions about its impact on academic evaluation, particularly in professional and educational contexts like English language assessments (OpenAI, 2023). ChatGPT-3 has gained recognition for its versatility in addressing a wide array of questions, sparking interest among students who seek assistance with assignments (Thornéus, 2023). Notably, ChatGPT has undergone successful trials, including examinations in fields such as law, teaching, and economics at various universities in the USA (CNN, 2023).

The rapid evolution of artificial intelligence, particularly in the form of advanced chatbots like ChatGPT, poses significant challenges to academic integrity in educational settings. The increasing accessibility of AI tools has made it easier for students to generate solutions to coding tasks and assignments, raising critical ethical concerns about the authenticity of their work. This shift towards AI-assisted solutions can lead to a rise in academic dishonesty, with students potentially viewing AI as a shortcut to success rather than a tool for learning (Geng et  al., 2023; Thornéus, 2023). As students utilize these technologies, educators face the pressing challenge of adapting assessment strategies to ensure that evaluations reflect genuine student understanding and efort. In the context of English language assessments, the potential for cheating facilitated by AI technologies underscores the need for vigilant oversight and innovative assessment practices.

The use of chatbots extends beyond general assistance, as they have the potential to generate completed program code, a practice observed among students (Geng et al., 2023). In many higher education assessment courses, automatic correction tools, like Kattis evaluate the correctness of students’ assessment codes through various test cases (Dalianis, 2022). Widely adopted by universities globally, Kattis is deemed a reliable correction tool with an embedded plagiarism checker, contributing to the preservation of academic integrity (Anders, 2023; Dalianis, 2022).

This study seeks to provide insights into ChatGPT-3’s English language assessment capabilities, specifically its performance in addressing coding tasks aligned with those presented to EFL students in higher education using the Kattis automatic correction tool. Additionally, the investigation aims to capture EFL educators’ perspectives on the potential risks of cheating facilitated by ChatGPT-3 and to explore potential solutions to mitigate such challenges. The evaluation of language assessment tasks often employs an automated approach known as an online judge. Online judging systems play a pivotal role in providing secure and reliable cloud-based assessments of algorithms submitted by users (Wasik et  al.,  2018). Central to these systems is the online judge, a software program designed to assess solution programs for assessment tasks by comparing them against expected input and output examples (Zhou et al., 2018).

The evaluation process within an online judge typically encompasses three main phases: submission, assessment, and feedback. In the submission phase, the code submitted by the user undergoes compilation and evaluation to determine if it can successfully execute within the standardized evaluation environment. This initial step ensures the code’s compatibility with the homogeneous environment. Upon successful verification during the submission phase, the assessment phase begins. The infrastructure of the submission is evaluated against a problem-specific set of test cases. For each test case, the evaluation checks for successful execution without errors, adherence to problem-specific constraints, and the correctness of the output.

Following the assessment of all test cases, binary feedback (right/wrong) is generated based on the outcomes. The final decision, termed a judgment, is determined by the collective results of the test cases. This binary feedback provides a clear indication of the correctness of the submitted solution. The final judgment is a crucial output of the evaluation process, indicating whether the submitted solution adheres to the expected criteria. The binary nature of the feedback simplifies decision-making, with a distinction between correct and incorrect outcomes based on the predefined rules and test cases (Wasik et al., 2018). Online judges serve as integral components in the automated assessment of assessment tasks, ofering eficiency, objectivity, and consistency in evaluating diverse algorithms submitted by users. They play a vital role in educational settings, particularly in assessment courses, where assessments require precision and impartiality.

Kattis stands as an automatic correction program that originated in 2005. Its primary objective was to alleviate the burden on teachers and teaching assistants, allowing them to dedicate more time to guiding students during lab sessions rather than manually checking the correctness of program code (Kattis, 2023). Kattis was designed to ofer a reliable, objective, and eficient evaluation of solution programs (Enström et al., 2010). The introduction of Kattis aims to shift the responsibility of program code evaluation from teachers to the online judge. This strategic move enabled teachers to streamline their focus on aiding student learning during practical sessions (Kattis, 2023). Kattis has become one among several web-based automatic correction programs accessible to university teachers for posting or using pre-existing problems in their teaching.

Kattis employs a black-box testing methodology in its assessments. This approach assesses the output of the solution program against expected results without delving into the program’s internal logic (Dalianis, 2022; Enström et al., 2011; Gao et al., 2003). The black box testing ensures that the program performs its intended function without scrutinizing the specific method employed to solve the problem. All tasks on Kattis are accompanied by a problem description outlining the expected format of input data and the anticipated output. Both input and output are presented as text files, and there is no restriction on the number of times a program code can be submitted. Users can submit code by either uploading a file or entering it directly into Kattis’s text window. Kattis evaluates all potential test cases, requiring approval for each to consider the solution program valid. Some test cases are openly provided in the task description, while others remain hidden. In case of test case failure, the test run is halted, and Kattis, adhering to its black box approach, provides no feedback on the specific issues with the program (Dalianis, 2022; Gao et al., 2003). During the program run on Kattis, users receive realtime feedback in the form of filled circles, each representing a test case. A green tick fills the circle for successfully passed tests, while a red cross indicates failure. Additionally, Kattis provides the type of error message responsible for the last test case failure (Table 1 outlines the most common “judgments” returned by Kattis and how they are referred to in this study).

Table 1 Description of various results in Kattis
<table><tr><td>Accepted</td><td>Accepted (AC)</td><td>Returned by Kattis when a program gives the correct output for all test cases. It is considered approved and then all the circles will be filled with green ticks</td></tr><tr><td>Compile error</td><td>Compilation Error (CE)</td><td>Kattis is unable to compile the program code</td></tr><tr><td>Wrong answer</td><td>Wrong answer (WA)</td><td>Wrong output from one of the test cases but the program terminated within the scope of the time limit. Does not imply whether the program is fast enough or that it</td></tr><tr><td>Run time error</td><td>Execution error (RTE)</td><td>will not crash In the event of a program crash in a test case</td></tr><tr><td></td><td></td><td>Time limit exceeded Time limit (TLE) exceeded It takes too long to run the program in at least one of the input sets</td></tr></table>

For each task on Kattis, associated metadata includes relevant information such as the CPU time limit and the problem’s severity. The CPU time limit signifies the maximum execution time allowed for the program code, exceeding it resulting in a “Time Limit Exceeded” (TLE) judgment (Wikipedia, 2023). Severity is categorized into difficulty levels ranging from 1 to 10, classified as “easy” (1.0–2.7), “medium” (2.8–5.4), and “hard” (5.4–10.0). Dificulty is estimated using a variant of the Elo rating system, where tasks solved by many with few attempts are considered easier, and tasks attempted frequently but rarely solved are deemed harder (Wikipedia, 2023). Problems with minimal submissions typically fall into the “medium” dificulty category due to insuficient data (Kattis, 2023).

Additional metadata under “statistics” provides insights into the problem’s number of submissions, approved submissions, approved persons, and their relationships. Key parameters for this study include the following:

Represents submissions with the “Accepted” (AC) verdict relative to the total submissions. Indicates users with at least one submission resulting in the “Accepted” (AC) verdict relative to the total users submitting a problem solution. In the realm of TEFL education, instances of cheating and plagiarism are prevalent, surpassing rates observed in many other academic disciplines (Sheard et al., 2017). Drawing insights from interviews conducted at 21 universities, 5 overarching themes emerge as strategies to counteract cheating in assessment courses.

Focused on clarifying permissible practices, particularly in addressing the common occurrence of code reuse. Clear guidelines are essential to elucidate how reused code should be appropriately cited and employed, considering its prevalence in the professional assessment sphere. Encompasses various approaches, including highlighting the consequences of cheating, vigilant observation of work during the process, promoting group work, and incorporating oral presentations as assessment methods.

Involves mitigating the impact of failed submissions/examinations and ensuring that the consequences do not disproportionately afect students. Verification of knowledge, as tested in submissions or examinations, is also emphasized. Encompasses strategies such as monitoring assessment points and designing individual tasks that are challenging to cheat on. Focuses on providing support to students and fostering a positive relationship with them through interactive and engaging lessons. Building a supportive learning environment is crucial to empowering students. To simplify these categories, strategies to counteract cheating can be broadly classified into two approaches:

These involve active measures to monitor and restrict opportunities for cheating, ensuring a rigorous assessment process, and maintaining the academic integrity of evaluations. These aim to create an environment where students feel less compelled to cheat by providing support, fostering understanding through education, and structuring assessments in a way that minimizes the potential benefits of cheating.

Academic dishonesty is an integral aspect of students’ experiences. Students encounter numerous compelling incentives to engage in academic dishonesty due to their interpersonal ties, particularly through unauthorized assistance from peers. Consequently, individuals frequently engage with technology-assisted cheating-detection systems on their computers and during examinations (Keyser & Doyle, 2020). Generative platforms like ChatGPT and Bard empower students by providing substantial computer power that immediately enhances their academic productivity. Numerous earlier AI chatbots and associated technologies were pre-configured with a restricted array of responses; however, generative AI systems like ChatGPT and Bard can generate replies informed by the context and tone of the encounter (Floridi, 2023).

Nonetheless, this empowerment frequently jeopardizes the authenticity and integrity of their work, raising doubts among certain skeptical instructors and prospective employers, regardless of the degree to which they utilize an AI system (Jimenez, 2023). The initiatives for detecting cheating in AI-generated materials are still in their nascent phases (Crawford, Cowling, and Allen, 2023; Leatham, 2023; Ryznar, 2023), thereby exposing academic players in contemporary institutions to significant and perhaps detrimental disputes. Dahmen et al., (2023) assert that “conventional plagiarism detection tools… may not be suficient and/or sensitive enough to appropriately detect plagiarism arising from chatbots” (p. 1187). Certain faculty members have cautioned students in their syllabi against utilizing ChatGPT, which may be counterproductive (Gillard & Rorabaugh, 2023); students might see these admonitions as a provocation and endeavor to escalate the “arms race” (Högberg, 2011).

Curriculum developers might opt to modify their assignments to mitigate concerns over ChatGPT usage (Tlili et al., 2023). This will require significant efort and money, as classwork frequently consists of standardized textbook assignments and exercises that demand substantial time for development, evaluation, and distribution. Prior to the emergence of ChatGPT, Bard, and other generative AI systems, academic cheating detection programs evolved technologically with the introduction of personal profiling and facial recognition.

Profiling and face recognition technology have created significant hurdles with privacy issues and other detrimental personal and societal efects (Heilweil, 2020; Hofman, 2019; Marano et al., 2023). Transparency is frequently deficient in the characterization of student cheating-detection methods for students. Students frequently receive insufficient information regarding the procedures involved, as institutions typically ofer only cursory mentions in syllabi or student handbooks, despite their obligation to report on numerous other educational and quality of life metrics. Numerous academic conduct policies lack clarity and may be deliberately imprecise, granting faculty discretion in specific instances (Zamastil, 2004). Numerous instances of cheating might be unintentional and stem from errors or erroneous assumptions regarding assignments (Dow, 2015), and the advent of new technologies like ChatGPT and Bard increases the likelihood of such misunderstandings. Allegations regarding the utilization of these AI systems might have significant repercussions for students, regardless of their eventual vindication.

A chatbot is a software program crafted to engage with users via text or voice interfaces, simulating human-like conversation (Dictionary.com, 2023). Leveraging artificial intelligence (AI), machine learning, and Natural Language Understanding (NLU), chatbots comprehend user queries and execute desired actions. Ranging from basic question–answer bots to sophisticated virtual assistants, chatbots serve diverse purposes, including customer service, marketing, education, health, and other applications aimed at enhancing eficiency and reducing workloads (Adamopoulou & Moussiades, 2020a, 2020b).

Chatbots can adopt two primary approaches for handling input data: “rule-based” or “smart machine-based. Rule-based chatbots: utilize predetermined responses stored in a database, employing programmed if-while statements to analyze keywords from user input (Adamopoulou & Moussiades, 2020a, 2020b). Smart machine-based chatbots: leverage AI and natural language processing (NLP) to provide personalized responses. These chatbots can understand context, even in response to complex queries. The use of NLP allows them to learn from mistakes, adapt, and improve over time (Adamopoulou & Moussiades, 2020a, 2020b).

ChatGPT-3, introduced on November 30, 2022, represents a significant advancement in AI-driven chatbot technology (OpenAI, 2023). Built upon the generative pre trained transformer of the 3rd generation (GPT-3), this language model is designed to handle sequence-based data, particularly natural language (Wei et al., 2023). GPT-3 is a notable evolution from its predecessor, GPT-2, boasting an impressive 175 billion parameters, a staggering 116 times more than GPT-2. Trained on a vast dataset of 570 GB, equivalent to 300 billion words sourced from articles, books, and internet texts, GPT-3 exhibits substantial growth in both scale and knowledge (Frederik, 2020).

One of GPT-3’s strengths lies in its multilingual proficiency. Beyond English, it incorporates texts from various languages, allowing users to interact with ChatGPT in multiple languages. OpenAI identifies Python as its area of greatest expertise, while also demonstrating proficiency in more than twelve additional programming languages, such as JavaScript, Perl, PHP, Go, Ruby, Swift, SQL, TypeScript, and Shell (OpenAI, 2023). The underlying Transformer model focuses on learning connections between words and sentences in text. When users pose questions to ChatGPT, the model leverages its trained knowledge and statistical models to generate answers by comprehending the underlying meaning of the inquiry (Dunder & Lundborg, 2023).

OpenAI states that ChatGPT is most proficient in Python and has proficiency in a number of other assessment languages, such as JavaScript, Go, Perl, PHP, Ruby, Swift, TypeScript, SQL, and Shell (OpenAI, 2023). It is crucial to acknowledge that ChatGPT operates as a probabilistic model, implying that it can produce varying answers for the same question based on the statistical probability of diferent potential responses (Ouyang, et al. 2022). Consequently, while ChatGPT can provide clear responses to a wide array of questions, there is no guaranteed truthfulness or impartiality in the answers generated.

OpenAI acknowledges the challenge of false facts and biased opinions in ChatGPT’s responses. Work is underway to filter out such inaccuracies, although the process is still a work in progress. Due to the probabilistic nature of the model, ensuring the accuracy of all text inputs manually is impractical. Additionally, the GPT-3 model is built on data up to July 2021, which means that it may lack information on events or developments post-dating that period (ChatGPT, 2023).

In one study Geng, et al. (2023) investigated GPT-3’s performance in introductory courses on functional assessment. The researchers conducted two types of tests, one without additional instructions to GPT-3 and another with additional instructions to enhance problem understanding. GPT-3 passed more than half of the assessment tasks (16 out of 31) without additional instructions and was ranked 220 out of 314, alongside ChatGPT as one of the students. With additional help, GPT-3 improved to rank 155 out of 314, indicating a significant enhancement. However, the study highlighted GPT-3’s dificulty in solving larger assessment tasks.

Finnie-Ansley, et  al. (2022) in another investigation, compared the performance of OpenAI’s Codex with students on an assessment exam. In this research, Codex, a descendant of GPT-3, was designed specifically for assessment tasks. Codex scored 15.7/20 (78.5%) on the exam, ranking 17th out of 71 students in an introductory computer science course (CS1). The study discusses the potential consequences of Codex’s use in education, including concerns about students not learning enough, potential incorrect teachings, and the impact on assessment systems.

In a third study by Sobania, et  al. (2023), ChatGPT’s capability to resolve bugs in the Python coding language was assessed using problems from QuixBugs as their benchmark. QuixBugs serves as a platform for evaluating automatic repair programs (ARPs), which are designed to identify and fix bugs in code. The study compared ChatGPT’s performance with other ARPs.

Out of 40 problems, ChatGPT successfully solved 19, a performance comparable to CoCoNut, a deep learning ARP program. The standard ARP program, not based on AI, solved 7 out of the 40 problems. A dialogue study with ChatGPT was conducted, presenting the same problems in a conversational format. In this setting, ChatGPT successfully solved 31 out of 40 problems, surpassing all other programs in the study. The study highlighted the potential of a dialogue-based approach, demonstrating that ChatGPT’s problem-solving abilities can be enhanced and refined through user interaction and clarification. ChatGPT exhibits promising potential for addressing assessment problems, showcasing its adaptability and competence in resolving coding issues.

This study distinguishes itself from previous investigations by examining ChatGPT’s coding competence across a broader range of dificulty levels. The dificulty levels are influenced by a larger pool of contributors, making the study more diverse than assessments tied to specific introductory courses or exams. The study’s scope encompasses various types of questions and dificulty levels, providing a more extensive evaluation compared to assessments based on a narrower context, such as introductory courses. However, unlike some previous studies, this research does not employ a dialogue-based study methodology. By encompassing a wider array of question types and dificulty levels, this study ofers a more comprehensive understanding of Chat-GPT’s coding capabilities. The study’s methodology broadens the context of evaluation, allowing for insights into ChatGPT’s performance beyond specific educational settings.

Amidst the rapid advancements in AI-based chatbots and their potential integration into assessment courses, it is imperative to explore the compatibility of chatbots like ChatGPT-3 with data generated and assessed by automatic correction tools like Kattis. Key questions guiding this investigation include:

1. Can chatbots, exemplified by ChatGPT-3, efectively engage with data generated and assessed by automatic correction tools like Kattis?

2. To what extent can ChatGPT-3 successfully address English language assessment tasks commonly found on Kattis, and what discernible patterns emerge from these attempts?

3. How do EFL educators at institutions perceive the risk of academic cheating associated with ChatGPT, and what preventative measures do they propose?

## Materials and methods

## Research design

This study is classified as an experimental investigation, where Kattis assessment serves as the independent variable, and the questions and answers from ChatGPT act as the dependent variables. A total of 127 coding tasks were chosen through a random selection process from Kattis in March 2023. The selection aimed for a comprehensive representation of dificulty levels ranging from 1 to 10. The random sampling was undertaken to manage the study within the available time constraints. The 124 coding tasks were chosen with a deliberate efort to maintain an even distribution of dificulty levels. This approach ensures a varied and representative set of challenges for language assessment. For this experimental investigation, the study employed OpenAI’s ChatGPT, utilizing GPT-3 as the current free model. Additionally, an automatic correction tool (Kattis) was utilized as part of the experimental setup.

## Instruments and parameters

Various instruments and parameters were considered to provide a comprehensive understanding of the experimental results. These parameters include:

## Degree of dificulty

Each coding task’s metadata provided a numerical dificulty level ranging from 1 to 10. This scale indicated the perceived dificulty, with 1 being the easiest and 10 being the most challenging.

## Percentage of approved submissions

Metadata from Kattis included information on the percentage of submitted answers that had been approved for each coding task. This percentage reflects the success rate of submissions for a given task.

## Percentage of task completion

Data from Kattis Open included information on the percentage of individuals who completed a specific coding task. This metric provided insights into the task’s overall completion rate.

## Kattis assessment result

Following Kattis’ language assessment, the results were recorded, indicating whether the task was approved or not. This assessment considered factors such as having all test cases approved or encountering partial approval.

## Error messages

In cases where submissions were not approved, the type of error message generated by either Kattis or ChatGPT was noted. Understanding the nature of errors provides additional insights into the challenges encountered during the assessment.

## Interviews

In this study, interviews were conducted with teachers, both before and after the experimental phase. The details of the interviews are as follows:

## Initial Interview - Professor 1

TEFL professor from Yazd University with substantial experience as an examiner in various assessment courses. Discuss the methodology chosen for the study, especially considering the limited existing research in the domain of chatbots and automatic correction tools. Professor 1 was selected due to their extensive knowledge of the functions of the autocorrect program Kattis, providing valuable insights into the study’s methodology.

## Follow-up interview—professor 2

Another distinguished associate professor in the same field of education. Further understanding of the study’s results and contribution to an ongoing discussion about cheating in the context of the study. Professor 2 was chosen to bring an additional perspective and insights to the discussion about the study’s outcomes, especially in the context of academic integrity. Conducting interviews with professors added a qualitative dimension to the study, allowing for insights and reflections from experts in the field.

## Procedure

## Task description

The coding problem description from Kattis was obtained. These problem descriptions served as the input for the subsequent stages of the experiment.

## Solution proposal

The generated problem descriptions were subsequently submitted to ChatGPT, with the instruction to formulate a proposed solution in Python code corresponding to the specified coding problem.

## Evaluation by Kattis

The solution generated by ChatGPT was submitted to the text window of Kattis for assessment. Subsequently, Kattis issued a response indicating the approval status of the proposed solution.

## Error messages

In instances where Kattis was unable to issue an approved verdict or where errors occurred, notations were made regarding the type of error message. This documentation adds granularity to the analysis of results.

## Number of measurements

A total of 124 measurements were performed, each corresponding to a distinct coding task randomly selected from Kattis.

## Standard test

The standard test English language test was conducted without modifying the task description. This approach provided a baseline assessment of ChatGPT’s ability to generate Python code solutions within the given context.

## Data analysis

The data analysis for this study employed a quantitative method with a focus on descriptive statistics. The percentage of successfully resolved issues by ChatGPT was calculated in relation to the total number of coding tasks. The percentage of issues which did not receive approval from Kattis was examined, and the frequency of various error notifications generated by both Kattis and ChatGPT was analyzed. An analysis was performed to determine the dificulty levels at which ChatGPT could handle coding tasks successfully, considering scenarios where at least one test case passed. An analysis was conducted to explore the correlation between the total number of submissions, the number of participants, the dificulty level, and the number of approved submissions.

![](images/9351e73db454f241db254a00b385c83adce75f86d949cd117475c13ab742689c.jpg)  
Fig. 1 Range of dificulty levels

![](images/a58f9eb9f30a246d6e6b4dc3635e479de406cb39aaa26de6244eb0ea224dbf30.jpg)  
Fig. 2 The scatter plot

## Results and discussion

The results which are discussed in this section are taken from both a quantitative survey where 124 language task tests were performed and a qualitative survey where interviews with two teachers were held.

## Results and analysis of ChatGPT’s assessment skills

One hundred twenty-four coding assignments from Kattis were submitted to Chat-GPT-3. From the solutions generated by ChatGPT-3, 16 out of 124 were approved by

![](images/a456cb895265dd26bbeb3613e6be800d6dab4bad66339b7b24fbb094f62876df.jpg)  
Fig. 3 Degree of dificulty on each task where Kattis passed some cases

Kattis. One hundred eight solutions could not be approved by passing all test cases for the tasks.

## ChatGPT’s ability to solve Kattis tasks

Approval rate: after testing ChatGPT on 124 coding tasks, 13% were judged as accepted, and 87% were judged as not accepted.

## Distribution of dificulty

Range of dificulty levels: the easiest task had a dificulty of 1.4, while the most dificult had a dificulty of 8.9 (see Fig. 1).

Visualization of dificulty levels: a bar graph categorized dificulty levels as integers from 1 to 10, with tasks between 1.0 to 1.9 classified as level 1. Tasks between 3 and 4 are “medium,” and those between 5 and 10 are “hard” (Fig. 2).

Detailed distribution: ChatGPT-3 passed 16 tasks, with 10 at dificulty level 1, 4 in the range of dificulty level 3, and 2 tasks at dificulty level 4 (see Fig. 3).

## Error messages

The feedback from Kattis in cases where approval was not granted often indicated wrong answers. Some cases of failure were attributed to network errors. The most common error message was “wrong answer,” occurring in cases where Kattis did not approve the task. “Execution error” ranked second in frequency, and “time limit exceeded” occurred least frequently. This implies that program crashes were more common, while programs running too long were less common.

Table 2 Number of settled cases, type of verdict, and which one degree of dificulty on each task where Kattis passed some cases
<table><tr><td>% passed test cases</td><td>Kattis judgment</td><td>Level of difficulty</td></tr><tr><td>8%</td><td>WA</td><td>1,9</td></tr><tr><td>22%</td><td>TLE</td><td>2,4</td></tr><tr><td>3%</td><td>WA</td><td>2,6</td></tr><tr><td>1%</td><td>WA</td><td>2,6</td></tr><tr><td>22%</td><td>WA</td><td>2,7</td></tr><tr><td>8%</td><td>WA</td><td>2,7</td></tr><tr><td>15%</td><td>WA</td><td>2,7</td></tr><tr><td>58%</td><td>TLE</td><td>3,2</td></tr><tr><td>3%</td><td>WA</td><td>3,3</td></tr><tr><td>25%</td><td>WA</td><td>3,5</td></tr><tr><td>15%</td><td>WA</td><td>3,9</td></tr><tr><td>55%</td><td>WA</td><td>4,1</td></tr><tr><td>30%</td><td>WA</td><td></td></tr><tr><td>50%</td><td>RTE</td><td>4,8</td></tr><tr><td>28%</td><td>TLE</td><td>5,0</td></tr><tr><td>4%</td><td>WA</td><td>6,4 6,5</td></tr></table>

Table 3 Correlation values between the number of submissions, people, and approved solutions and degree of dificulty
<table><tr><td>Value 1</td><td>Value 2</td><td>Correlation</td></tr><tr><td>Approved</td><td>Submissions</td><td>0.41</td></tr><tr><td>Approved</td><td>People</td><td>0.35</td></tr><tr><td>Submissions</td><td>People</td><td>0.69</td></tr><tr><td>Approved</td><td>Level of difficulty</td><td>-0.46</td></tr><tr><td>Submissions</td><td>Level of difficulty</td><td>-0.68</td></tr><tr><td>People</td><td>Level of difficulty</td><td>-0.82</td></tr></table>

## Approved test cases

In most cases resulting in non-approval (87%), no test case on Kattis was approved. In 13% of cases, some test cases passed but not all. Diferent error messages returned by Kattis for partially approved test cases included “wrong answer” (WA), “timed out” (TLE), and “execution errors” (RTE). Details of these cases are presented in Table 2.

## Correlation table

## Correlation analysis

The number of approved submissions and the number of approved users have a relatively strong positive correlation of 0.68. A positive correlation implies that when one

variable increases, the other usually also increases. Details of these cases are presented in Table 3.

## Focus on rows 1 and 2

In the column under “passed,” submissions show a positive correlation of 0.41, and persons show a positive correlation of 0.35. This indicates that the number of individuals attempting and having little success correlates more with ChatGPT’s ability to solve the problem than the number of successful submission attempts.

## Negative correlation

There exists a negative correlation of -48% between the level of dificulty and the number of approved solutions. This indicates that as the dificulty level rises, the quantity of solutions approved by ChatGPT tends to decline.

## Diferences between easiest and hardest completed tasks

The easiest completed task had a dificulty level of 1.4, while the hardest completed task was at level 4.2. The task description for the easiest task on Kattis was significantly shorter than that of the most dificult task. Characteristics difering between the two task solutions:

The easiest task primarily consisted of it and else statements. The most dificult tasks included for-loops, functions, lists, matrices, and more. The most dificult task required a broader range of operations and data types than the easiest.

## Nature of the assessment tasks

Most problems could be solved through proper formatting of input data and subsequent operations. Operations often involved for-loops, while-loops, mathematical operations, or sorting. Data formatting included lists, dictionaries, tuples, or sets.

Some tasks were based solely on an if-else clause. Examples include tasks like “Aaah!” or “Quadrant Selection.”

## Professors’ assessment of ChatGPT’s performance and strategies to prevent cheating Reflection on ChatGPT’s performance

Professor 2’s comments Professor 2 considers the 13% completion rate of tasks as relatively low. Anticipates an increase in performance over time.

Dificulty Levels ChatGPT-3 managed to completely solve tasks up to dificulty level 4.2 (classified as “medium”). Handles more dificult tasks to some extent, with partial approval up to dificulty level 6.5.

Handling complex problems ChatGPT demonstrates the ability to handle complex problems, where certain inputs may not produce approved output. Performance in more dificult tasks may involve issues with special edge cases or runtime errors.

Data‑driven nature Professor 2 highlights ChatGPT’s data-driven nature, relying on available training data. Speculates that solving tasks with no similar solutions in the training data is challenging for ChatGPT.

Future speculation ChatGPT’s ability to solve more complex tasks is contingent on the availability of similar solutions in the training data. Challenges arise when faced with tasks that lack similar solutions in the training data.

## Cheating with ChatGPT

## Solutions Produced by ChatGPT

Even when ChatGPT produces a solution not fully approved by Kattis, it often provides a half-finished solution. Knowledgeable programmers may work on and supplement these incomplete solutions.

## Professors’ testing and observations

Both professors tested ChatGPT-3 on their courses and found that most tasks can be handled with corrections. ChatGPT struggles with open-ended tasks lacking clues on the appropriate method.

## Open‑ended and complex tasks

In handling more open-ended and complex tasks, both teachers observed ChatGPT’s limitations. The concern arises regarding students’ skill development when using half-finished solutions from ChatGPT.

## Skill development and code‑reviewing

Professor 2 suggested that using ChatGPT’s solutions for correction is akin to codereviewing. Professor 1 likened taking code from ChatGPT to reading an essay, while coding oneself is like writing the essay, emphasizing diferent learning aspects.

## Importance of assessment skills

Both professors emphasized the necessity of having assessment skills before using tools like ChatGPT. Learning to program thoroughly requires the ability to understand and write code independently.

## ChatGPT as a tool for experienced programmers

Professor 2 saw ChatGPT as a useful tool for experienced programmers to expedite certain processes. It aids in assessing whether the produced code is well-adapted, which might be challenging for beginners.

Countering and detecting cheating caused by ChatGPT

ChatGPT’s ability to solve tasks

ChatGPT demonstrates a 13% completion rate in solving tasks for students.

## Strategies to prevent cheating

Appropriately dificult tasks Professor 1 suggests preventing cheating by designing tasks or labs with an appropriate level of dificulty. Tasks should feel achievable for students without resorting to unauthorized help.

“While ChatGPT can provide quick answers, it often leads students to skip the crucial step of understanding the underlying concepts.” (Professor 1).

Student awareness Professor 2 proposed explaining to students that relying on external help undermines their learning. Acknowledged that cheating, facilitated by tools like ChatGPT, is not a new issue; students previously sought solutions from peers or other sources.

Social capital impact ChatGPT introduces a new way to obtain solutions that may not require the same social capital as asking peers. Noted instances where students submitted drastically diferent solutions just before the deadline, indicating potential external assistance.

## ChatGPT and learning to program

Problem with ChatGPT Professor 2 highlights the problematic nature of using Chat-GPT for learning as it lacks quality control. ChatGPT can provide incorrect information and teach flawed theories.

Students might assume that if it comes from ChatGPT, it must be correct, which is dangerous.” (Professor 2).

“In some cases, it can ofer a decent starting point, but there’s no substitute for rigorous learning.” (Professor 1).

Comparisons with stack overflow Stack overflow, recommended by the teacher, involves solutions that users have interacted with, providing feedback and reactions. Unlike ChatGPT, Stack Overflow ofers some form of quality control and community validation.

Use with caution While ChatGPT can be used for learning about programming, it should be approached with caution and source criticism. Overreliance on ChatGPT may lead to misinformation and flawed learning outcomes.

Wrong answer was the most common error type, occurring in the unapproved tasks. These errors often stem from logical flaws in the code generated by ChatGPT. For example, tasks requiring specific algorithmic approaches may expose the model’s tendency to misinterpret the problem requirements or overlook crucial conditions. Certain types of tasks that involve intricate logic or multi-step reasoning, such as dynamic programming problems or those requiring backtracking, might frequently result in WA errors.

This suggests that while ChatGPT can generate code that compiles correctly, it may struggle with the underlying logic necessary for correct problem-solving. Execution errors accounted for unapproved submissions. Execution errors often indicate that the generated code has attempted to perform operations that are not permissible within the constraints of the Kattis platform (e.g., using unsupported libraries, and variable mismanagement). Tasks that require specific libraries or unique data structures might lead to execution errors, especially if ChatGPT fails to recognize the limitations of the coding environment. For instance, the use of libraries not recognized by Kattis or the definition of variables outside acceptable scope can lead to RTE.

Time limit exceeded was the least common error type, occurring in attempts. It occurs when the code exceeds the allocated CPU time limit, often due to ineficiencies or infinite loops. Tasks involving larger datasets or those that require optimizing algorithms (such as sorting or searching) may lead to TLE, particularly if the generated code is not eficient. This indicates that while ChatGPT may understand how to approach a problem, it might not always generate eficient code.

The current study highlights that the initial result, with 13% of completed tasks by ChatGPT, indicates some capability in handling tasks independently. The analysis considers the variety of problems that ChatGPT can handle, examining their complexity levels. This involves understanding the nature of coding tasks and the corresponding dificulty levels that the model can successfully navigate. The passage suggests an exploration of the error messages generated by ChatGPT and their frequency. This is important for understanding the challenges faced by the model and areas where it may struggle.

Examining error messages provides insights into common pitfalls and misconceptions. The analysis considers the correlation between ChatGPT’s success and the number of users who have previously solved the same problem. This could shed light on whether the model’s performance is influenced by patterns learned from a collective user base. The study mentions the inclusion of perspectives from teachers. This involves discussing their views on the study’s methodology and results. Additionally, it explores teachers’ opinions on the risk of cheating with ChatGPT and the potential solutions they propose.

The study notes that upon closer analysis of the tasks approved by Kattis, ChatGPT’s solutions align with the degree of dificulty set by Kattis, falling within the range of dificulty levels 1–4. Most solved tasks are around dificulty level 2, indicating that ChatGPT tends to perform well on moderately challenging tasks. The study reveals that ChatGPT’s solutions are often short, and attempts to generate longer code snippets are less likely to be accepted by Kattis. Similar findings are referenced from another study (Chuqin Geng et al., 2023), suggesting limitations in handling larger assessment tasks. There is a clear distinction in complexity between easy and more dificult tasks, with the latter involving a greater variety of operations.

A comparison between the easiest and hardest completed tasks is mentioned in Sect. 4.1.7. The study addresses the dificulty level of the task that ChatGPT managed, highlighting that it fell into the medium category. It emphasizes that a medium-dificulty task does not necessarily indicate greater dificulty than tasks at lower levels. The lack of submissions and data on dificulties on Kattis complicates drawing conclusions about

ChatGPT’s ability to handle medium-dificulty tasks. The passage attempts to relate the dificulty level of the 13% completed tasks to university assessment courses. It suggests that these tasks align with the theory taught in the first assessment course, where no prior assessment experience is required. Reference is made to a similar study (Ansley et al., 2022) on OpenAI’s Codex, supporting the conclusion that ChatGPT can handle simple tasks found in introductory assessment courses.

The study discusses the correlation between ChatGPT’s ability to solve an English language assessment task and the number of people who were able to solve the same task, as well as the correlation with the dificulty level of the task. ChatGPT’s ability to solve a task is reported to have an approximate 45% correlation with the number of people who successfully solved the same problem. This suggests that if many people can handle a task, ChatGPT may also be able to handle it. The explanation provided is that if many people can solve a task, it indicates the availability of similar solutions online.

Since ChatGPT has been trained on similar data, it can potentially match the problem with the exact or similar solutions. The study notes that the number of people passing certain tasks correlates primarily with dificulty, which is an index of task complexity. There is a 82% negative correlation between dificulty and the number of approved human coders, indicating that humans, like ChatGPT, find it easier to cope with tasks of lower complexity.

ChatGPT’s correlation with dificulty is reported to be 46%, supporting the idea that both humans and ChatGPT face greater challenges with tasks of higher complexity. The study compares the correlation between dificulty and approved submissions for Chat-GPT ( 46%) with the correlation between dificulty and the number of approved human coders ( 82%). It is mentioned that there is a stronger negative correlation for humans. The study acknowledges that no definite conclusions can be drawn from this comparison. This is due to ChatGPT making submission attempts rated 0 or 1, while the percentage of human coders passing comes from a large number of people who attempted the problem.

The majority of error messages were related to wrong answers, indicating that Chat-GPT is proficient in writing code that does not crash but fails to produce the correct output. The wrong answers stem from logical errors, possibly due to how ChatGPT interprets the task or what it values as important. This complexity suggests that Kattis task descriptions may be challenging for ChatGPT to fully comprehend.

Execution errors can result from various reasons, including the use of libraries not recognized by Kattis. For example, using the “public” library led to an execution error because Kattis lacked recognition of it. To address such errors, one can request Chat-GPT not to use specific libraries. For other execution errors, running the code locally and debugging may be necessary. Tasks like “Equations” with an unrecognized library and “Straza” with an undefined variable led to execution errors.

Time limit-exceeded errors were the least common. TLE happens when code exceeds the specified CPU time limit, typically 1 or 2 s. It may result from ineficiency or infinite loops. ChatGPT generally demonstrated eficiency, and TLE was the least common error. This could be attributed to the standard practice of programmers writing eficient code, which ChatGPT has learned from its training data. Providing feedback to

ChatGPT about the CPU limit may help, and debugging is required for cases involving infinite loops.

ChatGPT-3 struggled with the majority of tasks from Kattis that were tested, indicating dificulty in producing finished solutions. The conclusion is drawn that Kattis currently has suficiently complex task descriptions that ChatGPT cannot handle efectively. While ChatGPT often failed to provide complete solutions, it sometimes demonstrated an understanding of certain concepts and could generate solutions accepted by some test cases but not all. This suggests a potential scenario where students use ChatGPT to start code but may need to complete the solution themselves. Kattis incorporates hidden test cases, revealing that even if ChatGPT generates a solution that passes some test cases, logical errors may exist that require manual correction by students. Teachers can view all student submissions on Kattis, allowing them to identify suspicious patterns or identical solutions, contributing to discouraging the submission of AI-generated code. Without hidden test cases, a majority of these solutions might pass, suggesting that Kattis’ structure, with hidden test cases and descriptive task descriptions, acts as a deterrent against cheating with ChatGPT.

ChatGPT often produces code that runs without errors but fails to deliver the correct output. This indicates a lack of deeper logical reasoning and understanding of problem requirements. Students may mistakenly rely on ChatGPT for solutions, leading to superficial understanding rather than deep learning of programming concepts. A high percentage of ChatGPT-generated solutions receive “wrong answer” feedback, reflecting its struggles with logical accuracy and context comprehension. If assessments are designed solely based on code submissions, they may not accurately reflect a student’s understanding, as AI-generated solutions can appear valid without genuine student comprehension. ChatGPT’s performance is influenced by the training data it was exposed to, which may not encompass all nuances of specific programming tasks. Educators must consider that AI may struggle with unique or innovative tasks that deviate from common coding patterns, making it dificult to assess students’ critical thinking and problem-solving skills. Students might lean too heavily on ChatGPT for coding help, potentially stunting their growth as independent problem solvers. This reliance may hinder the development of essential skills, including debugging, critical analysis, and creative problem-solving.

Assessments should emphasize students’ coding processes, including planning, debugging, and problem-solving methodologies. This can be achieved through oral examinations, coding logs, or peer reviews, which require students to articulate their thought processes. Creating tasks that challenge students with unique or less common problems that ChatGPT might struggle with. These tasks can assess students’ understanding and creative thinking. Incorporating theoretical components that require students to explain their code and the logic behind their solutions. This helps develop their understanding and reduces reliance on AI. Encouraging students to engage in projects that require extensive planning and multiple stages of development, makes it harder to rely on AI for entire solutions.

## Conclusions

ChatGPT-3 demonstrates the ability to solve language assessment tasks of lower complexity, equivalent to assignments in introductory assessment courses at the university level. Students have the opportunity to use ChatGPT to obtain pre-written solutions, posing a risk of academic cheating. Introductory courses should be prioritized for support resources to address this potential issue. ChatGPT-3 faces challenges in writing ready-made solutions for more dificult tasks. While it may provide solutions to complex tasks, these may require adjustments by students to achieve correctness. Teachers expressed concerns about using ChatGPT as it does not contribute to teaching students to code from scratch and lacks source criticism. Relying on ChatGPT does not align with efective learning practices.

ChatGPT struggles more with writing correct code but demonstrates relative eficiency in generating code that does not crash. The complexity of task descriptions on Kattis is considered a challenge for ChatGPT, as it may not fully understand how to compile proper code for more complex tasks. Features such as hidden test cases and the ability for teachers to check submission history contribute to making it harder for students to cheat using ChatGPT. Kattis remains a valuable tool for verifying the correctness of task solutions.

In conclusion, while ChatGPT-3 exhibits capabilities for certain tasks, its use raises concerns about academic integrity and the efectiveness of student learning. The study underscores how crucial it is to comprehend AI tools’ limitations in educational settings and highlights the role of teachers and platforms like Kattis in maintaining academic standards. Future research studies could delve deeper into qualitative analysis, incorporating feedback from users or teachers to supplement the quantitative findings. Longitudinal studies could assess the evolution of ChatGPT’s coding capabilities over time and with iterative model improvements. As technology and ethical standards evolve, future research could incorporate ongoing discussions and frameworks related to the ethical use of AI and chatbots in academic settings.

Incorporating projects that require students to engage in complex problem-solving, research, and collaboration, which are harder to cheat on and allow for a deeper understanding of the material. Using verbal assessments where students explain their thought processes and solutions. This not only tests their understanding but also mitigates the likelihood of using AI-generated content. Requiring students to maintain a reflective journal documenting their learning process, challenges faced, and how they overcame them. This encourages self-assessment and a deeper engagement with the material.

Implementing a system where students submit their work in stages, allows educators to monitor progress and provide feedback throughout the learning process. This encourages ongoing engagement rather than a one-time submission. Implementing structured peer review where students critique each other’s work. This not only fosters collaborative learning but also increases accountability as students are aware that their work will be evaluated by their peers. Providing regular feedback on assignments to guide students in their learning journey. This not only supports improvement but also reinforces the value of the learning process over merely getting the correct answer.

In future studies, researchers can acknowledge the possibility of cheating in introductory assessment courses using ChatGPT and design exam forms to discourage such

behavior. Also, further studies need to actively mention the consequences of cheating with ChatGPT or other methods to students. It is highly recommended, that researchers in the future prioritize available help resources in courses where ChatGPT has the competence to solve tasks efectively.

Students should be encouraged to use sources like Stack Overflow rather than Chat-GPT to learn and emphasize the importance of critically reviewing information. In future investigations, researchers need to highlight that ChatGPT or similar tools developed by OpenAI can be reasonable tools for individuals who can already program, for tasks such as streamlining and automating work, but may not be efective for learning programming.

Conducting a follow-up study involving methodical conversations with ChatGPT can help to explore its ability to handle dificult tasks, incorporating improvement suggestions from a human. Finally, it is suggested, that future studies examine whether the number of input and output examples influences ChatGPT’s ability to solve tasks. This aspect could provide insights into how variations in task presentation impact the AI’s performance. Advocates for a follow-up study on GPT-4 or newer models, can extend the research to explore the capabilities of the latest iterations of ChatGPT.

The current study primarily focuses on coding tasks from Kattis that are of varying complexity. While this provides valuable insights, it does not encompass the full spectrum of tasks across diferent disciplines and levels of dificulty. The findings may not be generalizable to other types of academic assessments, such as written assignments or complex problem-solving tasks in non-computing fields. The study briefly touches on concerns regarding academic integrity but does not delve deeply into the ethical implications of AI in education. Issues such as dependency on AI, implications for teaching methodologies, and the potential devaluation of traditional assessment methods warrant more extensive examination. While the study identifies correlations between task dificulty and ChatGPT’s performance, it stops short of establishing causation. Understanding the specific factors that contribute to successful task completion by ChatGPT, such as user behavior or task characteristics, requires further investigation.

Future research should expand the scope of investigation to include a diverse range of tasks across various academic disciplines. This would provide a more comprehensive understanding of how AI tools like ChatGPT perform in diferent contexts and the implications for student learning. As AI technologies continue to evolve, longitudinal studies should be undertaken to track changes in AI capabilities over time and their impact on academic performance and integrity. This could involve periodic assessments of newer iterations of AI models and their efectiveness in solving increasingly complex tasks. Research should aim to develop ethical guidelines for the use of AI in educational contexts.

This includes establishing best practices for integrating AI tools into curricula, fostering critical thinking about AI-generated content, and promoting responsible usage among students. Investigating the impact of AI tools on learning outcomes, retention, and skill development is crucial. Future studies should explore how students who engage with AI tools perform compared to those who rely solely on traditional methods, particularly in coding and programming courses. It is important to assess whether reliance on AI tools like ChatGPT diminishes students’ ability to think critically and solve problems independently. Research should investigate strategies to encourage students to use AI as a supplementary tool rather than a primary source of solutions.

## Abbreviations

AC Accepted

AI Artificial Intelligence

ARP Automatics Repair Program

CS Computer Science

EFL English as Foreign Language

GPT Generative Pre-trained Transformer

NLP Natural Language Processing

NLUU Natural Language Understanding

TEFL Teaching English as Foreign Language

TLE Time Limit Exceeded

WA Wrong Answer

## Acknowledgements

The author is grateful to the participants who participated in this study.

## Authors’ contributions

Seyedeh Elham Elhambakhsh: Writing – original draft, Investigation, Formal analysis, review & editing, Supervision.

## Funding

No funds, grants, or other support were received.

## Data availability

The raw data supporting the conclusion of this article will be made available by the author, without undue reservation.

## Declarations

## Competing interests

The author declares that they have no competing interests.

Received: 20 August 2024 Accepted: 19 November 2024

Published: 2 July 2025

## References

Adamopoulou, E., & Moussiades, L. (2020a). An Overview of Chatbot Technology. Artificial Intelligence Applications and Innovations. https://doi.org/10.1007/978-3-030-49186-4\_31

Adamopoulou E, & Moussiades L. (2020). Chatbots: History, technology, and application

Anders, B. A. (2023). Is using ChatGPT cheating, plagiarism, both, neither, or forward thinking? Patterns, 4(3), 100694

ChatGPT (2023). Optimizing language models for dialogue [internet]. Available at: https://openai.com/blog/chatgpt/ GoogleScholar

CNN. 2023. ChatGPT passes exams from law and business schools

Crawford, J., Cowling, M., & Allen, K. A. (2023). Leadership is needed for ethical ChatGPT: Character, assessment, and learn ing using artificial intelligence (AI). Journal of University Teaching & Learning Practice, 20(3), 1–19. https://doi.org/10. 53761/1.20.3.02

Dahmen, J., Kayaalp, M., Ollivier, M., Pareek, A., Hirschmann, M. T., Karlsson, J., & Winkler, P. W. (2023). Artificial intelligence bot ChatGPT in medical research: The potential game changer as a double-edged sword. Knee Surgery, Sports Traumatology, Arthroscopy,31, 1187–1189

Dictionary.com. (2023). Definition av chatbot. https://www.dictionary.com/browse/chatbot

Dow, G. T. (2015). Do cheaters never prosper? The impact of examples, expertise, and cognitive load on cryptomnesia and inadvertent self-plagiarism of creative tasks. Creativity Research Journal, 27(1), 47–57. https://doi.org/10.1080/ 10400419.2015.992679

Dunder, N., & Lundborg, S. (2023). Kan chatbotar lösa kodningsuppgifter bedömda av automatiska rättningsverktyg inom högre utbildningar?: En studie av ChatGPT. https://arxiv.org/abs/2005.14165

Enström E, Kreitz G, Niemelä F, & Kann V. (2010).Testdriven utbildning - strukturerad formativ examination

Enström E, Kreitz G, Niemelä F, Söderman P, & Kann V. (2011). Five Years with Kattis - Using an Automated Assessment System in Teaching

Finnie-Ansley, J., Denny, P., Becker, B. A., Luxton-Reilly, A., & Prather, J. (2022). The robots are coming: Exploring the implica tions of openai codex on introductory programming. In Proceedings of the 24th Australasian Computing Education Conference (pp. 10–19). https://doi.org/10.1145/3511861.3511863

Floridi, L. (2023). AI as agency without intelligence: on ChatGPT, large language models, and other generative models. Philosophy & Technology, 36(1). https://doi.org/10.1007/s13347-023-00621-y

Frederik B, 2020. Will The Latest AI Kill Coding?

Gao J, Tsao HS, Wu Y, (2003). Testing and quality assurance for component-based software

Geng, C., Yihan, Z., Pientka, B., & Si, X. (2023). Can ChatGPT Pass An Introductory Level Functional Language Programming Course?. arXiv preprint arXiv:2305.02230

Gillard, C., & Rorabaugh, P. (2023). You’re not going to like how colleges respond to ChatGPT. Slate. Retrieved on April 14, 2023 from https://slate.com/technology/2023/02/chat-gpt-cheating-college-ai-detection.htm

Heilweil, R. (2020). Paranoia about cheating is making online education terrible for everyone. Vox.https://www.vox.com/ recode/2020/5/4/21241062/schools-cheating-proctorio-artif​icial-intelligence

Hera D, 2022. Automatisk återkoppling på programmeringsuppgifter

Hofmann, A. L. (2019). Where fairness fails: Data, algorithms, and the limits of antidiscrimination discourse. Information, Communication & Society,22(7), 900–915. https://doi.org/10.1080/1369118X.2019.1573912

Högberg, R. (2011). Cheating as subversive and strategic resistance: Vocational students’ resistance and conformity towards academic subjects in a Swedish upper secondary school. Ethnography and Education,6(3), 341–355. https:// doi.org/10.1080/17457823.2011.610584

Jimenez, K. (2023). Professors are using ChatGPT detector tools to accuse students of cheating. But what if the software is wrong? USA Today. https://www.usatoday.com/story/news/education/2023/04/12/how-ai-detection-tool-spawn ed-false-cheating-case-uc-davis/11600777002

Kattis. We help you educate great programmers 2023. https://www.kattis.com/universities

Keyser, R. S., & Doyle, B. S. (2020). Clever methods students use to cheat and ways to neutralize them. Journal of Higher Education Theory & Practice, 20(16), 11–21. http://www.m.www.na-businesspress.com/JHETP/JHETP20-16/1\_Keyse rFinal.pdf

Khalil, M., & Er, E. (2023). Will ChatGPT get you caught? Rethinking of plagiarism detection. ArXiv Preprint

Leatham, X. (2023). Schools should make pupils do some of their coursework ‘in front of teachers’, exam boards say - amid fears students are using AI bots like ChatGPT to cheat. Daily Mail,https://www.dailymail.co.uk/sciencetech/artic le-11916241/Pupils-coursework-teachers-amidfears-use-ChatGPT-cheat.html

Marano, E., Newton, P. M., Birch, Z., Croombs, M., Gilbert, C., & Draper, M. J. (2023). What Is the student experience of remote proctoring? A pragmatic scoping review. Swansea University Medical School Working Papers. https://www. edarxiv.org/jrgw9/

OpenAI. 2023. ChatGPT: Optimizing Language Models for Dialogue

Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C. L., Mishkin, P., ... & Lowe, R. (2022). Training language models to follow instructions with human feedback, 2022. https://www.arxiv.org/abs/2203.02155,13.

Ryznar, M. (2023). Exams in the time of ChatGPT. Washington and Lee Law Review Online,80(5), 305–322.

Sheard J, Simon, Butler M, Falkner K, Morgan M, (2017). Strategies for Maintaining Academic Integrity in First-Year Computing Courses.

Sobania, D., Briesch, M., Hanna, C., & Petke, J. (2023). An analysis of the automatic bug fixing performance of chatgpt. arXiv preprint arXiv:2301.08653

Thornéus, E. Aftonbladet. (2023). Lärarlarmet: Måste hänga med i GPT-utvecklingen

Tlili, A., Shehata, B., Adarkwah, M. A., Bozkurt, A., Hickey, D. T., Huang, R., & Agyemang, B. (2023). What if the devil is my guardian angel: ChatGPT as a case study of using chatbots in education. Smart Learning Environments, 10(1), 1–24. https://link.springer.com/article/10.1186/s40561-023-00237-x#citeas

Wasik, S, Antczak M, Badura J, Laskowski A, & Sternal T. (2018). A Survey on Online Judge Systems and Their Applications

Wei, C, Wang Y, Wang B, &Jay Kuo C.C. (2023). An Overview on Language Models: Recent Developments and Outlook. Wikipedia. Elo rating system 2023.

Zamastil, K. (2004). Legal issues in US higher education. Common Law Review, 6, 70–94.

Zhou W, Pan Y, Zhou Y & Sun G. (2018). The Framework of a New Online Judge System for Programming Education

## Publisher’s Note