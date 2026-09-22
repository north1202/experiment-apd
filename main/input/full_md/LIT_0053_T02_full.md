ORIGINAL PAPER

![](images/cd04d311dbf2d5f3b30eea5c7976d57646780783e64c87187a5a368dd2cd0df1.jpg)

# Authenticity in authorship: the Writer’s Integrity framework for verifying human‑generated text

Sanad Aburass<sup>1,2</sup>  · Maha Abu Rumman<sup>2</sup>

Accepted: 22 August 2024 / Published online: 5 September 2024   
© The Author(s), under exclusive licence to Springer Nature B.V. 2024

## Abstract

The “Writer’s Integrity” framework introduces a paradigm shift in maintaining the sanctity of human-generated text in the realms of academia, research, and publishing. This innovative system circumvents the shortcomings of current AI detection tools by monitoring the writing process, rather than the product, capturing the distinct behavioral footprint of human authorship. Here, we ofer a comprehensive examination of the framework, its development, and empirical results. We highlight its potential in revolutionizing the validation of human intellectual work, emphasizing its role in upholding academic integrity and intellectual property rights in the face of sophisticated AI models capable of emulating human-like text. This pape also discusses the implementation considerations, addressing potential user concerns regarding ease of use and privacy, and outlines a business model for tech companies to monetize the framework efectively. Through licensing, partnerships, and subscriptions, companies can cater to universities, publishers, and independent writers, ensuring the preservation of original thought and efort in written content. This framework is open source and available here, https://github.com/sanadv/ Integrity.github.io.

Keywords Generative artificial intelligence · Human generated text · Natural language processing

## Introduction

In the rapidly evolving landscape of digital content creation, the distinction between human-generated and artificial intelligence (AI)-generated text has become a focal point of ethical, academic, and intellectual debate (Aburass et al., 2024a; Barrett & Pack, 2023; Hall, 2024). With the advent of sophisticated generative AI models, the ability to produce text that mimics human-like quality and creativity has raised significant concerns within academic institutions, research journals, and the broader publishing community (Aburass et al., 2024b; Walters, 2023; Walters & Wilder, 2023). These concerns are primarily centered around the authenticity and integrity of works required for academic degrees, research dissemination, and literary publications, where the value is traditionally placed on the human intellect and efort (Chan & Hu, 2023; Dorgham et al., 2024; Farrelly & Baker, 2023). Recognizing the challenges in distinguishing between human and AI-authored texts, we introduce a novel framework, “Writer’s Integrity,” designed to ensure the authenticity of human-generated content. The “Writer’s Integrity” framework stems from the premise that the process of writing, inherent to human authors, is fundamentally diferent from the capabilities of AI. Human writing is characterized by its iterative nature, including drafting, revising, and editing, often accompanied by a range of typing speeds and error correction patterns. In contrast, AI models can generate polished, sophisticated text instantaneously, without the need for such revisions (Aburass et al., 2022; Kaliyar, 2020; Kalyan et al., 2021). Current tools aimed at detecting AI-generated text often fall short, producing false positives and negatives due to their reliance on textual analysis alone. These tools struggle to diferentiate efectively between human and AI authors, especially in cases where humans use paraphrasing tools or when AI manages to mimic human writing patterns closely (AbuRass et al., 2020; Akram, 2023). To address these limitations, the “Writer’s Integrity” framework proposes a novel approach that does not analyze the text itself but rather the process and behavior behind its creation. This includes monitoring metrics such as typing speed, frequency of edits, and the ratio of pasted to original text. By focusing on these aspects, our framework aims to capture the uniquely human elements of the writing process, thereby providing a more reliable method for distinguishing between human and AI authors. Moreover, the framework addresses concerns related to the use of paraphrasing tools, recognizing them as legitimate aids in the human writing process, provided the original ideas and eforts remain human. A cornerstone of this framework is the issuance of a “Writer’s Integrity Certificate.” This certificate serves as a tangible attestation to the human authorship of a text, based on the analysis of the writing process. It provides a detailed log of the writing journey, including typing speed, revisions, and the originality of content, which can be shared with academic supervisors, journal reviewers, or publishers. This certificate is not just a document but a testament to the human efort, creativity, and intellectual engagement that went into the creation of the work. It stands as a bulwark against the encroachment of AI on spaces where human intellectual contribution is of paramount importance. This paper delves into the development and operational principles of the “Writer’s Integrity” framework, highlighting its potential to revolutionize the validation of human intellectual work. By focusing on the certification process, we underscore the framework’s utility in academic integrity, the afirmation of human creativity, and the ethical augmentation of human work with AI.

## Literature review on the detection of AI‑generated text

The detection of AI-generated text, particularly text produced by models like ChatGPT, poses significant challenges for current detection tools. Recent studies have attempted to assess the efectiveness of these tools, revealing a complex landscape of accuracy, biases, and limitations. A comprehensive study by Weber-Wulf et al., evaluated the general functionality of 12 publicly available tools and two commercial systems (Turnitin and PlagiarismCheck), revealing a significant bias towards classifying outputs as humanwritten rather than detecting AI-generated text. The study highlighted that these tools are neither accurate nor reliable, with content obfuscation techniques further deteriorating their performance (Weber-Wulf et al., 2023). Elkhatat et al., focused on the diagnostic accuracy of AI content detectors, employing a normalization process to standardize results across diferent tools. It was found that the tools often misclassified AI-generated text as human-written (false negatives) and vice versa (false positives), raising concerns about their efectiveness in accurately identifying AI-generated content (Elkhatat et al., 2023). Zhang et al., demonstrated that large language models (LLMs) can be guided to evade AI-generated text detection through substitution-based optimization strategies. This involves making semantic substitutions at both word and sentence levels to minimize the predicted probability of text being recognized as AI-generated. The study underscores the potential for LLMs to circumvent detection, questioning the eficacy of current detection tools against adaptive and sophisticated AI-generated texts (Lu et al., 2023). The efectiveness of detection tools varies across diferent AI models and tasks. For instance, some tools may perform better at identifying content generated by earlier versions of AI models but struggle with content from more advanced versions. This inconsistency can lead to varying levels of detection accuracy, complicating eforts to maintain academic integrity and combat misinformation (Bellini et al., 2024). The limitations of AI-generated text detection tools have significant implications for academic integrity and the fight against misinformation. The inability of these tools to reliably distinguish between human and AI-generated texts could undermine eforts to ensure the authenticity and credibility of information across various domains (Chaka, 2024).

Recent discussions in the AI community highlight the necessity of integrating detection mechanisms within generative AI models to ensure content authenticity. A proposal by Knott et al., argues that any organization developing a foundation model intended for public use must incorporate a reliable detection mechanism as a condition for its release. This detection tool would enable users to verify whether a piece of content was generated by AI, addressing the growing concern over the indistinguishability of AI-generated text from human-generated text. The proposal emphasizes that such mechanisms should be mandatory and publicly accessible, thereby aiding in the identification of AI-generated content across various domains. This initiative aligns with broader regulatory eforts, such as the Content Authenticity Initiative and the C2PA standard, which aim to safeguard the integrity of digital content. By embedding detection capabilities directly into AI models, these measures could significantly mitigate risks associated with AI-generated misinformation and ensure a higher level of transparency and trust in digital communications (Knott et al., 2023).

In summary, the literature suggests that while AI-generated text detection tools represent a crucial line of defense against the misuse of AI in content creation, they currently face significant challenges in terms of accuracy, reliability, and resistance to evasion techniques. These findings call for ongoing research and development to enhance the capabilities of detection tools and ensure they can efectively meet the challenges posed by advancing AI technologies.

In response to the limitations of textual analysis-based AI detection tools, the “Writer’s Integrity” framework proposes a novel approach that shifts the focus from the product of writing to the process. This framework assesses human authorship by analyzing behavioral metrics such as typing speed, frequency of edits, and the ratio of pasted versus original text. Central to this framework is the issuance of a “Writer’s Integrity Certificate,” which serves as evidence of human authorship, grounded in the processual and iterative nature of human writing. This innovative approach addresses the gaps left by existing tools, providing a robust mechanism for authenticating human-generated content.

The proliferation of AI-generated content raises profound questions about academic and intellectual integrity. The ease with which AI can generate sophisticated text challenges traditional concepts of authorship and originality, necessitating new measures to safeguard the authenticity of human intellectual eforts. The “Writer’s Integrity” framework emerges as a critical tool in this context, ofering a means to verify human authorship and maintain the integrity of academic and literary works against the backdrop of AI advancements.

## Proposed framework: Writer’s Integrity

The “Writer’s Integrity” framework is designed to authenticate the human origin of textual content, distinguishing it from AI-generated text. This framework is particularly crucial for academic, research, and publishing sectors where the authenticity of human intellectual efort is paramount. Unlike existing tools that focus on analyzing textual patterns to detect AI-generated content, the “Writer’s Integrity” framework evaluates the writing process, including typing speed, frequency of edits, and the use of pasted text, to ascertain human authorship. This framework is intended to be a standalone word processor that can run as a website or an application on any operating system.

The “Writer’s Integrity” framework operates through a series of processes designed to authenticate the human origin of textual content. Its approach diverges from conventional AI detection tools by focusing on the dynamics of the writing process rather than textual analysis. Figure 1 shows a breakdown of its core processes:

## 1. Real-Time Writing Activity Logging:

The framework initiates by monitoring and logging real-time writing activities in a designated text area. This includes every keystroke, edit (additions and deletions), and paste action performed by the writer.

2. Change Detection:

As the writer composes or modifies text, the framework detects and logs changes between the previous and current states of the text. This includes identifying new words added, existing words removed, or alterations to the text structure.

3. Paste Action Logging:

Special attention is given to text pasted into the document. The framework logs the occurrence of paste actions separately, including the length of the pasted text and its position within the document.

4. Analysis of Writing Behavior:

The collected data is then analyzed to calculate key metrics that characterize human writing behavior, such as typing speed, frequency of edits, and the ratio of pasted text to overall content.

5. Log Cleaning and Data Condensation:

To optimize storage and improve data readability, the framework processes the raw log data, condensing it by removing redundant information and summarizing the writing activity.

![](images/6918e93c58903279672b12bf56a73a24bc3530895c57e069edd53a74e970935b.jpg)

<table><tr><td rowspan=1 colspan=3>Initialize previousText with the current text in the text input fieldInitialize typingStartTime with the current date and timeInitialize totalTypedCharacters to 0When a user types in the text input field:Update currentText with the new text valueIf the input is not from pasting:Call detectChanges with previousText and currentTextIf changes are detected:Call logChanges with the detected changesElse if the input is from pasting:Call logPastedText with the pasted textUpdate previousText with currentTextUpdate totalTypedCharacters based on the number of characterstypedUpdate typing speed using current time, typingStartTime, andtotalTypedCharacters</td></tr><tr><td></td><td rowspan=1 colspan=2>Detecting Changes</td></tr><tr><td rowspan=2 colspan=3>Function detectChanges takes oldText and newText as inputs:Split oldText and newText into arrays of words, oldWords andnewWords respectivelyBuild an LCS (Longest Common Subsequence) matrix for old-Words and newWordsInitialize changes as an empty stringUsing the LCS matrix, backtrack to find differences:If words are the same, move diagonally and continueIf words differ, record as “added&quot; or “removed&quot; in changesReturn changes</td></tr><tr><td rowspan=1 colspan=1></td></tr><tr><td></td><td rowspan=3 colspan=1></td><td rowspan=1 colspan=1>Function logChanges takes changes as input:Record changes with a timestamp to a logFunction logPastedText takes pastedText as input:Find the position of the pastedText in the currentTextLog the pastedText with its position and a timestamp</td></tr><tr><td></td><td rowspan=1 colspan=1>Updating Typing Speed</td></tr><tr><td></td><td rowspan=1 colspan=1>Function updateTypingSpeed takes charCount, startTime, andtotalChars as inputs:Calculate the time elapsed since startTimeUpdate totalChars with charCountCalculate typing speed as totalChars divided by time elapsedDisplay or record the typing speed</td></tr><tr><td></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Cleaning Log Data</td></tr><tr><td></td><td rowspan=1 colspan=2>Function CleanLog takes logs as input:Extract “Pasted&quot; log entries and “Added/Removed&quot; entries fromlogsFor each “Pasted&quot; entry, add to pastedRecordsFor each “Added/Removed&quot; entry, process and add to finalRecordsCombine pastedRecords and finalRecords into a cleaned logReturn the cleaned log</td></tr><tr><td></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td></td><td rowspan=1 colspan=2>Function AnalyzeLog takes logData as input:Split logData into individual entriesFor each entry, extract relevant data (e.g., pastes, edits)Calculate metrics such as number of pastes, total pasted words,total typed words, and average changes per wordCalculate typing speed and paste to type ratioOutput or display the analysis results</td></tr></table>

6. Human Authorship Certification:

Based on the analyzed data, the framework generates a “Writer’s Integrity Certificate” for the document. This certificate provides a summary of the writing behavior metrics, attesting to the human origin of the content.

## Metrics

The operational metrics of the framework are defined mathematically as follows:

Typing Speed (TS):

$$
T S = { \frac { \mathrm { T o t a l ~ T y p e d ~ C h a r a c t e r s } } { \mathrm { T o t a l ~ W r i t i n g ~ T i m e } } } * 6 0\tag{1}
$$

Measured in characters per minute, this metric reflects the average speed at which a user types.

Edit Frequency (EF):

$$
E F = { \frac { \mathrm { T o t a l ~ E d i t s } } { \mathrm { T o t a l ~ W r i t i n g ~ T i m e } } }\tag{2}
$$

This ratio indicates how frequently the text is edited, embodying the iterative nature of human writing.

Paste Ratio (PR):

$$
P R = { \frac { \mathrm { T o t a l } \mathrm { C h a r a c t e r s } \mathrm { P a s t e d } } { \mathrm { T o t a l } \mathrm { C h a r a c t e r s } \mathrm { i n D o c u m e n t } } }\tag{3}
$$

Expressed as a percentage, this metric quantifies the proportion of the text that was pasted rather than typed.

Average Changes per Word (ACW):

$$
A C W = { \frac { \mathrm { T o t a l ~ E d i t s } } { \mathrm { T o t a l ~ N u m b e r ~ o f ~ W o r d s } } } \qquad ( 4 )
$$

Reflects the average number of edits applied to each word, indicating the depth of revision and thought process.

## Pseudocode for Writer’s Integrity framework functionality

This pseudocode outlines the core functionalities of the “Writer’s Integrity” framework, focusing on logging writing activities, detecting changes, cleaning log data, and analyzing writing behavior to identify human-generated texts.

Logging Writing Activity

This structured approach allows the “Writer’s Integrity” framework to capture and analyze the intricacies of human writing behavior, diferentiating it from AI-generated content through detailed logging and analysis of the writing process.

Empirical experimental results of the Writer’s Integrity framework

The “Writer’s Integrity” framework has been developed using ASP.Net and VB.net, with SQL Server managing the database operations. This section delves into the empirical experimental results derived from the deployment and testing of the framework, illustrating its efectiveness in ensuring the integrity of human-generated text.

## System overview

The framework operates through a user-friendly interface that begins with a login screen, ensuring secure access to users’ documents. Once logged in, users are presented with their saved documents, ofering options to edit existing documents or create new ones. The primary functionality kicks in as the user starts typing: every keystroke, edit, and paste action is meticulously logged. Upon saving a document, the logs are cleaned to optimize storage eficiency, and a unique certificate ID is generated for the document.

## Key features and results

1. Document Management: Users can seamlessly manage their documents, with each action from creation to modification being intuitively integrated within the system’s user interface.

2. Change Logging: The real-time logging of text changes and paste actions serves as the backbone of the framework. This feature not only captures the essence of the writing process but also aids in distinguishing human authorship from AI-generated content.

3. Log Cleaning and Certificate Generation: The log cleaning process, which is triggered upon saving a document, eficiently condenses the log data without losing the critical information necessary for verification. Each document is assigned a unique certificate ID, facilitating easy sharing and verification by reviewers or supervisors.

4. Certificate Verification: The certificate ID acts as a key to access the document’s log, presenting a detailed account of all changes and pasted text. This transparency ensures that reviewers can thoroughly assess the document’s authenticity.

## Screenshots and logs

Screenshots of the system in action and samples of the logs before and after cleaning were instrumental in visualizing the framework’s functionality. These empirical evidences underscore the framework’s capability to maintain a detailed and verifiable record of the writing process. Figure 2 depicts the initial interface where users authenticate their access, while Fig. 3 displays the user’s collection of stored documents. Figure 4 presents the interface for text input, where the user’s typing activity is recorded. In Fig. 5, we observe the detailed log and statistics associated with a document, as identified by its unique certificate ID. Lastly, Fig. 6 illustrates an example of a log that includes pasted text and highlights the calculated paste ratio.

## The mechanism of log detailing

In the Writer’s Integrity Framework, the writing process is meticulously logged to capture every textual change. Each addition and deletion is timestamped and recorded with positional accuracy. For example, as a user composes the phrase “Convolutional Neural Network is a methodology of deep learning that is based on feature extraction,” the system logs each incremental input, as shown in Table 1.

## The original log

The original log serves as a comprehensive record, tracking the user’s every action. It begins with the initial characters as they are typed, such as “C,” “Co,” “Con,” and continues as more of the word “Convolutional” is formed. Each logged entry includes the exact time of the edit and the specific

Fig. 2 User authentication screen

![](images/58898e1ea4be9dc6566f6c4305e3fa39238b49b92a60f826b63224463b5949da.jpg)

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>documentid</td><td rowspan=1 colspan=1>documentname</td><td rowspan=1 colspan=1>created</td><td rowspan=1 colspan=1>modified</td><td rowspan=1 colspan=1>certificateid</td></tr><tr><td rowspan=1 colspan=1>View</td><td rowspan=1 colspan=1>54</td><td rowspan=1 colspan=1>Chapter 1</td><td rowspan=1 colspan=1>13/02/2024 10:17:46am</td><td rowspan=1 colspan=1>13/02/2024 10:17:46am</td><td rowspan=1 colspan=1>c087b4fa-862f-40e1-96b4-ad1aa5450f77</td></tr><tr><td rowspan=1 colspan=1>View</td><td rowspan=1 colspan=1>55</td><td rowspan=1 colspan=1>Chapter 2</td><td rowspan=1 colspan=1>13/02/2024 10:18:55am</td><td rowspan=1 colspan=1>13/02/2024 10:18:55am</td><td rowspan=1 colspan=1>265947af-da73-4e4a-9775-5d97da78d03b</td></tr></table>

Fig. 3   Document management dashboard  
![](images/a5c1c670089b0e970b7bacc4e631787ea4f611498b422519461b809b3357de3a.jpg)  
Fig. 4   Text editing interface

change made character additions and deletions at precise positions within the text. This level of detail is crucial for supervisors or reviewers who need to verify the authenticity of the writing process. It ensures that the human intellect and efort behind the text can be observed and validated.

## Log cleaning process

To maintain an eficient and readable log, redundant entries that capture the step-by-step typing process are consolidated to reflect only significant changes, such as the completion of words or phrases. The cleaning process highlights the final version of words or phrases, as they appear in the completed text, and associates them with the corresponding timestamp and change history. For instance, multiple entries recording the sequential typing of “Convolutional” are condensed into a single entry in the cleaned log, showcasing the word as it is fully typed along with the last removal that occurred before its completion.

## The cleaned log

The cleaned log presents a streamlined view, it removes the minute-by-minute keystroke details, instead of providing a clear snapshot of the significant changes that occurred during the writing session. This cleaned version is not only easier to read but also focuses on the end result of the writing process, which is more relevant for authenticity verification. Highlighting in the cleaned log allows reviewers to quickly discern the final text and the key changes, enabling them to assess the integrity of the document eficiently.

![](images/92baaccbc57cec1dabdb8ecf674b454b12709e6cc758e67414302f643fd9d991.jpg)  
Fig. 5 Document log and statistical analysis display

![](images/0ff8b1eda5f921d0f8a68a14f0a8aaf694c483949113d35c327ac205e6994bf6.jpg)  
Fig. 6   Log excerpt with pasted text and paste ratio indicator

Table1An example of a log before and after cleaning
<table><tr><td colspan="2">The Original Log</td><td>The Cleaned Log</td></tr><tr><td>[13/02/2024, 10:14:37 am] Added: “C&quot;,Removed: “&quot;;; at position 1</td><td>[13/02/2024, 10:15:06 am] Added: “&quot;,[13/02/2024, 10:15:08 am] Added: “a&quot;,Removed: ‘;; at position 5 [13/02/2024, 10:15:08 am] Added: “&quot;,[13/02/2024, 10:15:09 am] Added: &quot;m&quot;,Removed: &quot;&quot;;; at position</td><td>[13/02/2024, 10:14:43 am] Added: &quot;Convolutional&quot;,Removed: &quot;Convolu-</td></tr><tr><td>[13/02/2024, 10:14:37 am] Added: “Co&quot;,Removed: &quot;C&quot;;; at position 1 [13/02/2024, 10:14:37 am] Added: &quot;Con&quot;,Removed: &quot;Co&quot;;; at position 1 6</td><td></td><td>tiona&quot;;; at position 1</td></tr><tr><td></td><td>[13/02/2024, 10:15:09 am] Added: &quot;me&quot;,Removed: &quot;m&quot;”;; at position 6</td><td></td></tr><tr><td>[13/02/2024, 10:14:38 am] Added: &quot;Conv&quot;,Removed: &quot;Con&quot;;; at position 1</td><td></td><td>[13/02/2024, 10:14:47 am] Added:</td></tr><tr><td>[13/02/2024, 10:14:41 am] Added: &quot;Convo&quot;,Removed: &quot;Conv&quot;;; at position 1</td><td>[13/02/2024, 10:15:10 am] Added: &quot;met&quot;,Removed: &quot;me&quot;;; at position 6</td><td>&quot;Neural&quot;,Removed: &quot;Neura&quot;;; at</td></tr><tr><td>[13/02/2024, 10:14:41 am] Added: &quot;Convol&quot;,Removed: &quot;Convo&quot;;; at position 1</td><td>[13/02/2024, 10:15:10 am] Added: &quot;meth&quot;,Removed: “met&quot;;; at position 6</td><td>position 2</td></tr><tr><td>[13/02/2024, 10:14:42 am] Added: &quot;Convolu&quot;,Removed: &quot;Convol&quot;;; at position 1</td><td>[13/02/2024, 10:15:11 am] Added: &quot;metho&quot;,Removed: &quot;meth&quot;;; at position 6</td><td>[13/02/2024, 10:15:54 am] Added:</td></tr><tr><td>[13/02/2024, 10:14:42 am] Added: &quot;Convolut&quot;,Removed: &quot;Convolu&quot;;; at position 1</td><td>[13/02/2024, 10:15:11 am] Added: &quot;methol&quot;,Removed: &quot;metho&quot;;; at position 6</td><td>&quot;Network&quot;,Removed: &quot;Network,&quot;;; at</td></tr><tr><td>[13/02/2024, 10:14:42 am] Added: &quot;Convoluti&quot;,Removed: &quot;Convolut&quot;; at position 1</td><td>[13/02/2024, 10:15:12 am] Added: &quot;methold&quot;,Removed: &quot;methol&quot;;; at position 6</td><td>position 3</td></tr><tr><td>[13/02/2024, 10:14:42 am] Added: &quot;Convolutio&quot;,Removed: &quot;Convoluti&quot;;; at position 1</td><td>[13/02/2024, 10:15:12 am] Added: &quot;metholdo&quot;,Removed: &quot;methold&quot;;; at position 6</td><td>[13/02/2024, 10:15:05 am] Added:</td></tr><tr><td>[13/02/2024, 10:14:43 am] Added: &quot;Convolution&quot;,Removed: &quot;Convolutio&quot;;; at position 1</td><td>[13/02/2024, 10:15:12 am] Added: &quot;metholdol&quot;,Removed: &quot;metholdo&quot;;; at position 6</td><td></td></tr><tr><td>[13/02/2024, 10:14:43 am] Added: &quot;Convolutiona&quot;,Removed: &quot;Convolution&quot;;; at position 1</td><td>[13/02/2024, 10:15:13 am] Added: &quot;metholdolg&quot;,Removed: &quot;metholdol”;; at position 6</td><td>&quot;is&quot;,Removed: &quot;i&quot;;; at position 4</td></tr><tr><td>[13/02/2024, 10:14:43 am] Added: &quot;Convolutional&quot;,Removed: &quot;Convolutiona&quot;;; at position 1</td><td>[13/02/2024, 10:15:13 am] Added: &quot;metholdolgy&quot;,Removed: &quot;metholdolg&quot;;; at position 6</td><td>“”,[13/02/2024, 10:15:08 am] Added:</td></tr><tr><td>[13/02/2024, 10:14:43 am] Added: “&quot;,[13/02/2024, 10:14:45 am] Added: &quot;N&quot;,Removed: “&quot;;; at position</td><td>[13/02/2024, 10:15:13 am] Added: “&quot;,[13/02/2024, 10:15:16 am] Added: &quot;methodology&quot;,Removed:</td><td>“a&quot;,Removed: &quot;&quot;;; at position 5</td></tr><tr><td>2</td><td>&quot;metholdolgy&quot;;; at position 6</td><td>[13/02/2024, 10:15:13 am] Added:</td></tr><tr><td>[13/02/2024, 10:14:46 am] Added: &quot;Ne&quot;,Removed: &quot;N&quot;;; at position 2</td><td>[13/02/2024, 10:15:19 am] Added: “o&quot;,[13/02/2024, 10:15:19 am] Added: &quot;of’,Removed: &quot;o&quot;;; at</td><td>“”,[13/02/2024, 10:15:16 am] Added:</td></tr><tr><td>[13/02/2024, 10:14:46 am] Added: &quot;Neu&quot;,Removed: &quot;Ne&quot;;; at position 2</td><td>position 7</td><td>&quot;methodology&quot;,Removed: &quot;methold-</td></tr><tr><td>[13/02/2024, 10:14:47 am] Added: &quot;Neur&quot;,Removed: &quot;Neu&quot;;; at position 2</td><td>[13/02/2024, 10:15:20 am] Added: “d&quot;,[13/02/2024, 10:15:20 am] Added: &quot;de&quot;,Removed: &quot;d&quot;;; at</td><td>olgy&quot;;; at position 6</td></tr><tr><td>[13/02/2024, 10:14:47 am] Added: &quot;Neura&quot;,Removed: &quot;Neur&quot;;; at position 2</td><td>position 8</td><td>[13/02/2024, 10:15:19 am] Added:</td></tr><tr><td>[13/02/2024, 10:14:47 am] Added: &quot;Neural&quot;,Removed: &quot;Neura&quot;;; at position 2</td><td>[13/02/2024, 10:15:20 am] Added: &quot;dee&quot;,Removed: “de&quot;;; at position 8</td><td>&quot;o&quot;,[13/02/2024, 10:15:19 am] Added:</td></tr><tr><td>[13/02/2024, 10:14:47 am] Added: &quot;,[13/02/2024, 10:14:48 am] Added: “N&quot;,Removed: “”;; at position</td><td>[13/02/2024, 10:15:21 am] Added: “deep&quot;,Removed: &quot;dee&quot;;; at position 8</td><td>&quot;of&#x27;,Removed: &quot;o&quot;;; at position 7</td></tr><tr><td>3</td><td>[13/02/2024, 10:15:21 am] Added: &quot;T,[13/02/2024, 10:15:21 am] Added: “le&quot;,Removed: &quot;l&quot;;; at posi-</td><td>[13/02/2024, 10:15:21 am] Added:</td></tr><tr><td>[13/02/2024, 10:14:49 am] Added: &quot;Ne&quot;,Removed: &quot;N&quot;;; at position 3 [13/02/2024, 10:14:49 am] Added: &quot;Net&quot;,Removed: &quot;Ne&quot;;; at position 3</td><td>tion 9 [13/02/2024, 10:15:21 am] Added: &quot;lea&quot;,Removed: “le&quot;”;; at position 9</td><td>&quot;deep&quot;,Removed: &quot;dee&quot;;, at position 8</td></tr><tr><td>[13/02/2024, 10:14:49 am] Added: &quot;Netw&quot;,Removed: &quot;Net&quot;;; at position 3</td><td>[13/02/2024, 10:15:22 am] Added: &quot;lear&quot;,Removed: &quot;lea&quot;;; at position 9</td><td>[13/02/2024, 10:15:22 am] Added: &quot;learning&quot;,Removed: &quot;learnin&quot;;; at</td></tr><tr><td>[13/02/2024, 10:14:50 am] Added: &quot;Netwo&quot;,Removed: &quot;Netw&quot;;; at position 3</td><td>[13/02/2024, 10:15:22 am] Added: &quot;learn&quot;,Removed: &quot;lear&quot;;; at position 9</td><td>position 9</td></tr><tr><td>[13/02/2024, 10:14:50 am] Added: &quot;Networ&quot;,Removed: &quot;Netwo&quot;;; at position 3</td><td>[13/02/2024, 10:15:22 am] Added: &quot;learni&quot;,Removed: &quot;learn&quot;;; at position 9</td><td>[13/02/2024, 10:15:27 am] Added:</td></tr><tr><td>[13/02/2024, 10:14:51 am] Added: &quot;Network&quot;,Removed: &quot;Networ&quot;;; at position 3</td><td>[13/02/2024, 10:15:22 am] Added: &quot;learnin&quot;,Removed: &quot;learni&quot;;; at position 9</td><td></td></tr><tr><td>[13/02/2024, 10:14:51 am] Added: &quot;Networks&quot;,Removed: &quot;Network&quot;;; at position 3</td><td>[13/02/2024, 10:15:22 am] Added: &quot;learning&quot;,Removed: &quot;learnin&quot;;; at position 9</td><td>&quot;that&quot;&#x27;,Removed: &quot;tha&quot;;; at position 10</td></tr><tr><td>[13/02/2024, 10:14:52 am] Added: &quot;Networks,&quot;,Removed: &quot;Networks&quot;;; at position 3</td><td>[13/02/2024, 10:15:26 am] Added: “t&#x27;,[13/02/2024, 10:15:26 am] Added: &quot;th&quot;,Removed: &quot;t”;; at posi-</td><td>[13/02/2024, 10:15:27 am] Added</td></tr><tr><td>[13/02/2024, 10:14:53 am] Added: “&quot;,[13/02/2024, 10:14:53 am] Added: “a&quot;,Removed: “&quot;”;; at position 4</td><td>tion 10</td><td>&quot;is&quot;,Removed: &quot;i&quot;;; at position 11</td></tr><tr><td>[13/02/2024, 10:14:54 am] Added: “ar&quot;,Removed: “a&quot;;; at position 4</td><td>[13/02/2024, 10:15:27 am] Added: &quot;tha&quot;,Removed: &quot;th&quot;;; at position 10</td><td>[13/02/2024, 10:15:28 am] Added:</td></tr><tr><td>[13/02/2024, 10:14:54 am] Added: &quot;are&quot;,Removed: “ar&quot;;; at position 4</td><td>[13/02/2024, 10:15:27 am] Added: &quot;that&quot;,Removed: &quot;tha&quot;”;; at position 10</td><td>&quot;based&quot;,Removed: &quot;base&quot;;; at posi-</td></tr><tr><td>[13/02/2024, 10:14:54 am] Added: &quot;”,[13/02/2024, 10:14:59 am] Added: “a&quot;,Removed: &quot;;; at position 5</td><td>[13/02/2024, 10:15:27 am] Added: “i&quot;,[13/02/2024, 10:15:27 am] Added: “is&quot;,Removed: “i&quot;;; at posi-</td><td>tion 12</td></tr><tr><td>[13/02/2024, 10:15:01 am] Added: “&quot;,Removed: “a&quot;;; at position 5</td><td>tion 11 [13/02/2024, 10:15:28 am] Added: &quot;b&quot;,[13/02/2024, 10:15:28 am] Added: “ba&quot;,Removed: &quot;b&quot;;; at</td><td>[13/02/2024, 10:15:29 am] Added:</td></tr><tr><td>[13/02/2024, 10:15:02 am] Removed: “; at position 5</td><td>position 12</td><td>“o&quot;,[13/02/2024, 10:15:29 am] Added:</td></tr><tr><td>[13/02/2024, 10:15:02 am] Added: “ar&quot;,Removed: “are&quot;;; at position 4</td><td>[13/02/2024, 10:15:28 am] Added: &quot;bas&quot;,Removed: &quot;ba&quot;;; at position 12</td><td>&quot;on&quot;,Removed: &quot;o&quot;;; at position 13</td></tr><tr><td>[13/02/2024, 10:15:02 am] Added: “a&quot;,Removed: “ar&quot;;; at position 4</td><td>[13/02/2024, 10:15:28 am] Added: &quot;base&quot;,Removed: &quot;bas&quot;;; at position 12</td><td>[13/02/2024, 10:15:33 am] Added:</td></tr><tr><td>[13/02/2024, 10:15:03 am] Added: “&quot;,Removed: “a&quot;;; at position 4</td><td>[13/02/2024, 10:15:28 am] Added: &quot;based&quot;,Removed: &quot;base&quot;;; at position 12</td><td>&quot;feature&quot;,Removed: &quot;featur&quot;;; at</td></tr><tr><td>[13/02/2024, 10:15:03 am] Removed: “&quot;;; at position 4</td><td>[13/02/2024, 10:15:29 am] Added: “o&quot;,[13/02/2024, 10:15:29 am] Added: “on&quot;,Removed: “o&quot;;; at</td><td>position 14 [13/02/2024, 10:15:48 am] Added:</td></tr><tr><td>[13/02/2024, 10:15:03 am] Added: &quot;Networks&quot;,Removed: &quot;Networks,&quot;;; at position 3</td><td>position 13 [13/02/2024, 10:15:32 am] Added: “f&#x27;,[13/02/2024, 10:15:32 am] Added: “fe&quot;,Removed: “f&#x27;;; at posi-</td><td>&quot;extraction.&quot;,Removed: &quot;extraction&quot;;;</td></tr><tr><td>[13/02/2024, 10:15:03 am] Added: &quot;Network&quot;,Removed: &quot;Networks&quot;;; at position 3</td><td></td><td>at position 15</td></tr><tr><td>[13/02/2024, 10:15:04 am] Added: &quot;Network,&quot;,Removed: &quot;Network&quot;;; at position 3</td><td>tion 14</td><td></td></tr><tr><td>[13/02/2024, 10:15:04 am] Added: &quot;&quot;,[13/02/2024, 10:15:05 am] Added: “i&quot;,Removed: &quot;&quot;;; at position 4</td><td>[13/02/2024, 10:15:32 am] Added: &quot;fea&quot;,Removed: &quot;fe&quot;;; at position 14</td><td></td></tr><tr><td>[13/02/2024, 10:15:05 am] Added: “is&quot;,Removed: “i”;; at position 4</td><td>[13/02/2024, 10:15:33 am] Added: &quot;feat&quot;,Removed: &quot;fea&quot;;; at position 14</td><td></td></tr><tr><td></td><td>[13/02/2024, 10:15:33 am] Added: &quot;featu&quot;,Removed: &quot;feat&quot;;; at position 14</td><td></td></tr><tr><td></td><td>[13/02/2024, 10:15:33 am] Added: “featur&quot;,Removed: “featu&quot;;; at position 14</td><td></td></tr><tr><td></td><td>[13/02/2024, 10:15:33 am] Added: &quot;feature&quot;,Removed: “featur&quot;; at position 14</td><td></td></tr><tr><td></td><td>[13/02/2024, 10:15:33 am] Added: “e&quot;”,[13/02/2024, 10:15:34 am] Added: “ex&quot;,Removed: “e&quot;;; at posi-</td><td></td></tr><tr><td></td><td>tion 15</td><td></td></tr><tr><td></td><td>[13/02/2024, 10:15:37 am] Added: “extraction&quot;,Removed: &quot;ex&quot;;; at position 15</td><td></td></tr><tr><td></td><td>[13/02/2024, 10:15:48 am] Added: &quot;extraction.&quot;,Removed: &quot;extraction&quot;;; at position 15</td><td></td></tr><tr><td></td><td>[13/02/2024, 10:15:54 am] Added: &quot;Network&quot;,Removed: &#x27;Network,&quot;;; at position 3</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr></table>

By implementing such detailed logging and cleaning mechanisms, the Writer’s Integrity Framework ensures that the human-generated content can be efectively diferentiated from AI-generated text. The logs provide transparency and accountability, which are essential in settings where authorship and original thought are of the utmost importance.

## Implementation considerations for the Writer’s Integrity framework

## Ease of use and privacy concerns

The implementation of the Writer’s Integrity Framework necessitates a delicate balance between ease of use and privacy. While some students and writers might initially perceive the system as intrusive, it is imperative to understand the context and necessity of such a framework. In academia and professional writing, particularly where Ph.D. dissertations, published research, or career advancements are at stake, the authenticity of the text is paramount. Monetary compensation or academic credentials based on the text further necessitate this verification.

Users should be reassured that, much like proctoring systems used during online examinations, the Writer’s Integrity Framework is a tool designed to uphold academic and professional standards. If the text is original and the authors have nothing to conceal, the use of this system should be viewed similarly to any other academic integrity practice. It is a safeguard, not a surveillance measure, ensuring that the credit and recognition received are rightfully earned.

## Drafting system focus

This framework is tailored as a drafting system, specifically designed for the initial creation and development of text. It is not intended to replace comprehensive word-processing software. Users are encouraged to utilize the Writer’s Integrity Framework for drafting their work, benefiting from the robust logging and authenticity verification processes. Subsequently, they can transfer their drafts into their preferred word-processing programs to finalize formatting, insert figures, and add tables. Adopting this specialized approach allows implementers to concentrate on refining the core functionalities that diferentiate human-authored content from AI-generated text. This focus ensures the framework’s resources are dedicated to enhancing the key features that support its primary purpose—authenticating the integrity of written work.

## Privacy and security

Given the sensitive nature of the documents handled by the Writer’s Integrity Framework—ranging from confidential research to doctoral dissertations—the system is engineered with stringent security measures. The privacy and protection of intellectual property are of utmost importance. As such, the framework must incorporate advanced security protocols to safeguard against unauthorized access and data breaches. Security measures, including robust encryption, secure authentication mechanisms, and regular security audits, are vital to protect the integrity of the text and the privacy of the users. The implementation of these measures ensures that while the framework serves its function in verifying authorship, it also maintains the confidentiality and security that users rightfully expect for their scholarly and professional work.

## Business model for the Writer’s Integrity framework

The Writer’s Integrity Framework presents a unique opportunity for tech companies to ofer a valuable service to universities, publishing companies, and individual writers. The framework’s ability to verify the human origin of text is a critical asset in an era where the distinction between human and AI-generated content is increasingly blurred. Below is an outline of a potential business model that companies can adopt to monetize this framework:

## Licensing to academic institutions

Universities are prime candidates for implementing this system to preserve academic integrity. Tech companies can ofer the framework as a licensed product, allowing institutions to integrate it into their existing digital infrastructure. A tiered licensing model can be established, depending on the size of the institution and usage volume, ensuring scalability and accessibility for universities with varying budgets and requirements.

## Partnerships with publishing entities

Publishers, research journals, and press agencies are stakeholders in ensuring the authenticity of published content. A tech company can partner with these organizations, ofering licenses to use the framework to vet submissions eficiently. Such partnerships could involve a flat fee for access to the system or a pay-per-use model, providing flexibility for publishers with fluctuating volumes of content to authenticate.

## Subscriptions for individual writers

Independent writers seeking to certify the originality of their work can benefit from subscribing to the Writer’s Integrity Framework. Subscription tiers can be established based on usage, such as the number of texts to be authenticated or a specific period. A premium model can ofer additional features like advanced analytics on writing habits, priority support, and storage options for documented logs and certificates.

## Verified profiles for writers

Tech companies can create a platform where writers can have verified profiles, akin to social media verifications. These profiles would display authenticated certificates from the Writer’s Integrity Framework, showcasing the writer’s commitment to originality. Verified profiles could include metrics reflecting the individual’s typing habits and other behavioral analytics that reinforce their status as human authors. Access to these profiles could be provided to publishing companies, serving as a credibility benchmark for writers. This could be monetized by charging writers a fee for verification or ofering subscription-based access to publishers.

## Data privacy services

For institutions and individuals concerned with data privacy, tech companies can ofer additional security services. These might include on-premises implementations, encrypted data storage, or private cloud services. These specialized privacy services can be ofered as part of a premium package or as add-ons to the standard licensing or subscription model.

## Ancillary services

Tech companies can also explore ancillary services such as training for university staf, workshops for writers on maintaining integrity, and consultation for publishing companies on integrating the framework into their workflow. These services can be charged separately, providing a supplementary revenue stream while adding value to the core oferings of the framework.

By leveraging these monetization strategies, tech companies can build a profitable business while providing a critical service that upholds the integrity of written content across various industries and sectors.

## Future work

To build upon the current capabilities of the Writer’s Integrity Framework, several avenues for future work can be explored. One significant enhancement involves adding a built-in paraphraser using an API. Paraphrasing is a recognized and legitimate process within the manuscript and integrating this service would benefit users by increasing transparency. The framework could present both the original and paraphrased text within the report, thus validating the authenticity of the user’s contributions and ensuring that the paraphrased content is appropriately acknowledged. This addition would not only enhance user experience but also strengthen the overall credibility and trustworthiness of the documents produced using the framework.

Another important area of development is the integration of a similarity measure to evaluate the percentage of similarity with previously published works or online content. This feature is crucial for maintaining academic integrity, as it would help detect potential overlaps and unintentional plagiarism. By providing a detailed analysis of content originality, the framework can ofer more comprehensive support to users, ensuring that their work remains distinct and original. This enhancement aligns with the framework’s primary goal of upholding the authenticity of human-generated text.

Initially, the generated report should be manually examined to judge whether the writing process was conducted by a human or AI. This manual review will allow for a nuanced understanding of the writing behavior metrics. However, as the framework evolves, a machine learning model could be developed and trained to automate this evaluation process. This model would analyze the writing behavior data to determine if the writing process was human-generated, especially as new cheating methods emerge. By incorporating these machine learning techniques, the framework can ensure a more objective and scalable approach to verifying human authorship, adapting to future challenges in maintaining academic integrity.

Additionally, it is essential to protect the framework against spoofing and adversarial attacks. Spoofing, where attackers manipulate the user’s keyboard and mouse to enter pre-existing text, poses a significant threat to the integrity of the system. Such attacks can mimic genuine human inputs, making it challenging to distinguish between real and automated actions. Beyond spoofing, the framework must also guard against other potential threats, such as malware that could alter the writing logs or inject AI-generated text into the document. Keyloggers and screen scrapers could capture sensitive information, compromising user privacy and the authenticity of the writing process (AbuRass & Qatawneh, 2018; González et al., 2022; Monaco & Tappert, 2017).

To address these threats, the framework should incorporate advanced security measures, such as real-time monitoring of user behavior patterns to detect anomalies that could indicate malicious activity. Ensuring the framework is robust against network-based attacks is also crucial, as hackers might attempt to intercept or alter data transmitted between the user and the server. Implementing end-to-end encryption and secure authentication methods will be vital in maintaining the integrity and confidentiality of user data.

By anticipating and countering these diverse threats, the Writer’s Integrity Framework can ensure reliable verification of human authorship and maintain its efectiveness in an increasingly complex security landscape. This proactive approach will ensure the framework remains a trustworthy and reliable tool for verifying the authenticity of humangenerated text.

By focusing on these enhancements, the Writer’s Integrity Framework can further solidify its position as a critical tool for verifying human-generated text. These developments will not only improve the framework’s functionality but also reinforce its role in maintaining high standards of academic and intellectual integrity.

## Conclusion

In conclusion, the “Writer’s Integrity” framework heralds a new era in the verification of human-generated text, crucial for academic, research, and publishing sectors. The system’s innovative approach, focusing on the writing process’s dynamics rather than solely on the final product, ofers a robust solution to the challenges posed by AI-generated content. By analyzing metrics such as typing speed, change logs, and the ratio of pasted to original text, the framework can efectively discern between human and AI authorship, providing a level of assurance that traditional AI detection tools have struggled to achieve. The practical implementation of this framework has been carefully considered, with attention given to user experience and privacy concerns. By positioning the system as a drafting tool and ensuring high-security standards, the framework respects the privacy of its users while providing a secure environment for the creation of original works. From a business perspective, the “Writer’s Integrity” framework presents a viable model for companies aiming to implement this technology. By ofering various licensing and subscription options to universities, publishing houses, and individual authors, the system promises to open up new revenue streams while bolstering the integrity of written works. As we move forward, the adoption of “Writer’s Integrity” could become a standard in industries where the authenticity of human intellect is of paramount importance. This would not only safeguard the value of human creativity and critical thinking but also maintain the credibility and authenticity of human contributions in an increasingly AI-assimilated world.

Acknowledgements Not applicable.

Funding Not applicable.

Data availability This framework is open source and available here.   
https://github.com/sanadv/Integrity.github.io.

## References

Aburass, S., Dorgham, O., & Rumman, M. A. (2024a). An Ensemble approach to question classification: Integrating electra transformer, GloVe, and LSTM. International Journal of Advanced Computer Science and Applications. https://doi.org/10.14569/ IJACSA.2024.0150148

Aburass, S., Dorgham, O., & Shaqsi, J. A. (2024b). A hybrid machine learning model for classifying gene mutations in cancer using LSTM, BiLSTM, CNN, GRU, and GloVe. Systems and Soft Computing, 6, 200110. https://doi.org/10.1016/j.sasc.2024.200110

AbuRass, S., Huneiti, A., & Al-Zoubi, M. B. (2020). Enhancing convolutional neural network using Hu’s moments. International Journal of Advanced Computer Science and Applications, 11(12), 130–137. https://doi.org/10.14569/IJACSA.2020.0111216

Aburass, S., Huneiti, A., & Al-Zoubi, M. B. (2022). Classification of transformed and geometrically distorted images using convolutional neural network. Journal of Computer Science, 18(8), 757–769. https://doi.org/10.3844/jcssp.2022.757.769

AbuRass, S., & Qatawneh, M. (2018). Performance evaluation of AES algorithm on supercomputer IMAN1. International Journal of Computer Applications, 179(48), 32–34. https://doi.org/10.5120/ ijca2018917282

Akram, A. (2023). An empirical study of AI generated text detection tools. ArXiv Preprint arXiv:2310.01423

Barrett, A., & Pack, A. (2023). Not quite eye to A.I.: Student and teacher perspectives on the use of generative artificial intelligence in the writing process. International Journal of Educational Technology in Higher Education, 20(1), 59. https://doi.org/10.1186/ s41239-023-00427-0

Bellini, V., Semeraro, F., Montomoli, J., Cascella, M., & Bignami, E. (2024). Between human and AI: Assessing the reliability of AI text detection tools. Current Medical Research and Opinion, 1–6. https://doi.org/10.1080/03007995.2024.2310086

Chaka, C. (2024). Reviewing the performance of AI detection tools in diferentiating between AI-generated and human-written texts: A literature and integrative hybrid review. Journal of Applied Learning and Teaching, 7(1).

Chan, C. K. Y., & Hu, W. (2023). Students’ voices on generative AI: Perceptions, benefits, and challenges in higher education. International Journal of Educational Technology in Higher Education, 20(1), 43. https://doi.org/10.1186/s41239-023-00411-8

Dorgham, O., Aburass, S., & Issa, G. F. (2024). Framework for enhanced digital image transmission security: Integrating hu moments, digital watermarking, and cryptographic hashing for integrity verification. In 2024 2nd international conference on cyber resilience (ICCR) (pp. 1–5). https://doi.org/10.1109/ICCR6 1006.2024.10532924

Elkhatat, A. M., Elsaid, K., & Almeer, S. (2023). Evaluating the efficacy of AI content detection tools in differentiating between human and AI-generated text. International Journal for Educational Integrity, 19(1), 17. https://doi.org/10.1007/ s40979-023-00140-5

Farrelly, T., & Baker, N. (2023). Generative artificial intelligence: Implications and considerations for higher education practice. Education Sciences, 13(11), 1109. https://doi.org/10.3390/educs ci13111109

González, N., Calot, E. P., Ierache, J. S., & Hasperué, W. (2022). Towards liveness detection in keystroke dynamics: Revealing synthetic forgeries. Systems and Soft Computing, 4, 200037. https:// doi.org/10.1016/j.sasc.2022.200037

Hall, R. (2024). Generative AI and re-weaving a pedagogical horizon of social possibility. International Journal of Educational Technology in Higher Education, 21(1), 12. https://doi.org/10.1186/ s41239-024-00445-6

Kaliyar, R. K. (2020). A multi-layer bidirectional transformer encoder for pre-trained word embedding: A survey of BERT. In 2020 10th international conference on cloud computing, data science & engineering (confluence) (pp. 336–340). https://doi.org/10.1109/ Confluence47617.2020.9058044

Kalyan, K. S., Rajasekharan, A., & Sangeetha, S. (2021). AMMUS : A survey of transformer-based pretrained models in natural language processing. arXiv:2108.05542

Knott, A., Pedreschi, D., Chatila, R., Chakraborti, T., Leavy, S., Baeza-Yates, R., Eyers, D., Trotman, A., Teal, P. D., Biecek, P., Russell, S., & Bengio, Y. (2023). Generative AI models should include detection mechanisms as a condition for public release. Ethics and Information Technology, 25(4), 55. https://doi.org/10.1007/ s10676-023-09728-4

Lu, N., Liu, S., He, R., Wang, Q., Ong, Y.-S., & Tang, K. (2023). Large language models can be guided to evade AI-generated text detection.

Monaco, J. V, & Tappert, C. C. (2017). Obfuscating keystroke time intervals to avoid identification and impersonation. arXiv:1609. 07612

Walters, W. H. (2023). The efectiveness of software designed to detect AI-generated writing: A comparison of 16 AI text detectors. Open Information Science, 7(1), 20220158. https://doi.org/10.1515/ opis-2022-0158

Walters, W. H., & Wilder, E. I. (2023). Fabrication and errors in the bibliographic citations generated by ChatGPT. Scientific Reports, 13(1), 14045. https://doi.org/10.1038/s41598-023-41032-5

Weber-Wulf, D., Anohina-Naumeca, A., Bjelobaba, S., Foltýnek, T., Guerrero-Dib, J., Popoola, O., Šigut, P., & Waddington, L. (2023). Testing of detection tools for AI-generated text. International Journal for Educational Integrity, 19(1), 26. https://doi.org/10. 1007/s40979-023-00146-z

Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional afiliations.

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law.