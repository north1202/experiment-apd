![](images/c8654a73a609dd8db90ba82567902ba723346457078e52dbf7fcb90fd4a0aac4.jpg)

# Developing the Luciano Floridi (LuFlot) Bot: An Accessible AI Chatbot Trained on a Philosopher’s Manuscripts

Nicolas Gertler<sup>1</sup>  · Rithvik Sabnekar<sup>2</sup>

Received: 16 June 2025 / Accepted: 26 December 2025 / Published online: 19 January 2026   
© The Author(s), under exclusive licence to Springer Nature B.V. 2026

## Abstract

This paper presents the Luciano Floridi Bot (LuFlot), the first freely and publicly accessible AI chatbot trained on a corpus of literature by a living philosopher, designed to broaden access to insights into AI ethics, digital ethics, the philosophy of information, and the philosophy of technology. Built using OpenAI’s Assistants API and implementing Retrieval-Augmented Generation (RAG) technology, LuFlot leverages the manuscripts of Luciano Floridi’s works to provide cited, academically rigorous responses to questions about digital ethics and philosophy, while maintaining accessibility for diverse audiences. The system employs advanced prompt engineering techniques, including Chain of Thought and Few-Shot prompting, and ofers multilingual capabilities and adaptable explanation levels. Unlike existing philosophical chatbots, LuFlot ofers free access, direct citations, and customizable interaction depth tailored to each user’s query. While the system demonstrates promising applications in education and research, particularly for researchers in philosophy, its limitations include the potential for reductionism and the need for critical evaluation of its outputs. This implementation demonstrates how pedagogically optimized AI systems can efectively mediate between complex academic thought and public understanding while maintaining scholarly integrity through proper attribution.

Keywords AI ethics · Digital ethics · Luciano Floridi · Educational chatbot · Retrieval-Augmented Generation (RAG) · Prompt engineering

## 1 Introduction

The increasing omnipresence of artificial intelligence (AI) has given rise to a myriad of ethical concerns, including transparency, bias, and privacy (Floridi, 2024). Despite growing discourse on AI ethics, the general public lacks accessible and interactive tools to engage meaningfully with these issues. While governments, non-profits, and corporations have developed AI ethics frameworks, these eforts often remain technical or policy-driven (Borenstein & Howard, 2021). As AI systems continue to shape decisions across healthcare, education, governance, and many other domains bridging the gap between ethical AI discourse and public understanding is critical.

To address this challenge, we developed the Luciano Floridi Bot (LuFlot)—accessible at lucianofloridi.com/bot—the first freely accessible AI chatbot trained on the works of a living philosopher specializing in digital ethics, philosophy of information, and other related domains. LuFlot democratizes access to Luciano Floridi’s scholarship, one of the world’s leading voices on the ethics of digital technology and the philosophy of information, allowing users to engage in interactive discussions on AI ethics, digital ethics, and other related topics using an AI-powered conversational interface.

The design of LuFlot builds on emerging research suggesting that generative AI tools, like ChatGPT, can help learners develop critical thinking skills—primarily through a pedagogically constructivist lens—in STEM education (Vasconcelos & Santos, 2023). However, a significant challenge in AI-driven education is ensuring that large language models (LLMs) maintain academic rigor while making complex concepts accessible to diverse audiences. Because LLMs distill information, their responses risk being overly reductionist, leading to oversimplified understandings, particularly for non-experts. Additionally, LLM-generated content is prone to fabricated citations, necessitating critical evaluation of AI-generated information (Day, 2023).

To overcome these limitations, LuFlot addresses both inclusivity and reliability. A key feature is its multilingual capability, allowing users to engage with AI ethics in 26 diferent languages (McGregor, 2023). While LLMs perform worse than specialized Natural Language Processing (NLP) models in direct translation tasks,they excel at generating coherent multilingual responses due to their broad training data (Lai et al., 2023). This enables a larger audience to access Floridi’s insights in their native language, fostering greater inclusivity in AI ethics literacy. While multilingual access broadens reach, the English-only source texts mean that non-English users engage with translated interpretations rather than the primary materials; in efect, they are one layer removed from the original manuscripts.

To address reliability, LuFlot incorporates citations from Floridi’s original works, using Retrieval-Augmented Generation (RAG) to ensure responses are academically grounded and verifiable. By providing credible references, LuFlot mitigates the risk of AI-generated misinformation while allowing users to explore the original texts further. This commentary’s central contribution is to show that a citation-grounded RAG system can serve as a reliable pedagogical channel for complex philosophical scholarship, enabling non-specialists to access Floridi’s work with verifiable interpretive fidelity.

## 2 LuFlot: Technical Design

## 2.1 Motivation for LuFlot

The creation of LuFlot was primarily motivated by a desire to broaden access to academic discussions on digital ethics and AI ethics. To achieve this, we leveraged GPT-4-Turbo, one of the most capable large language models (LLMs) at the time of its creation, designed to be more capable and cost-efective than its predecessor, GPT-4. Notably, GPT-4-Turbo can maintain a context window of 128,000 tokens, output a maximum of 4096 tokens, and has a knowledge cutof date of November 30, 2023 (OpenAI, 2024). We used this model through OpenAI’s Assistants API, whereby we inserted Floridi’s manuscripts into the system, and then built a custom user interface (UI), for the following reasons:

Accessibility. While Poe—an AI model aggregator—is a powerful tool, it required users to have an account to access the models, which would have limited LuFlot’s outreach to a broader audience. Furthermore, even if users were to create a Poe account, they could only interact with chatbots that were built upon Poe’s freely available models, which excluded the leading foundational models at the time, including GPT-4-Turbo and Claude 3 Opus. Given these limitations, we decided against using Poe. Similarly, we decided against using OpenAI’s GPT environment, as, at the time of LuFlot’s development and release, it precluded non-paying users from accessing other GPTs, which would have limited access to LuFlot for those without ChatGPT-Plus subscriptions.

Customization for Specific Needs. By developing a custom UI (Fig. 1), we tailored the interface and the user experience directly to the needs of our project. This customization ensured that LuFlot provided a unique, engaging, and intuitive interaction tailored to discussing digital ethics and philosophy. Through our custom UI, we emphasized the bot’s purpose and its limitations. We built the “Provide Feedback” and “Generate Question” buttons, respectively, to enable users to share their feedback and generate a random question to ask LuFlot related to the domain at hand. The question generator draws from a curated bank of queries relevant to Floridi’s work, such as ‘How does Floridi propose we should address privacy concerns in the digital age?’ and ‘How does Floridi address the challenge of digital inequality?‘”.

![](images/4a569820a4e69cff8748a5be8b392c4d859909c7965820bc2cae037be10fcc50.jpg)  
Fig. 1 Luciano Floridi Bot UI

To ensure that LuFlot delivers accurate, relevant, and domain-specific responses, we embedded Prompt Engineering and RAG into the fabric of LuFlot via OpenAI’s Assistants API.

## 2.2 Prompt Engineering

Prompt engineering is the practice of providing instructions to an LLM to enforce rules, automate processes, and build specific qualities of a generated output (White et al., 2023). Prompt engineering served as a critical foundation for structuring how LuFlot interacted with users, ensuring that the LLM’s responses were aligned with user expectations and insights illuminated in Floridi’s work. Here are some key elements developed through prompt engineering:

Chain of Thought and Few-Shot Prompting. To optimize the consistency of LuFlot’s responses, we employed Chain of Thought (CoT) prompting, which has been shown to improve LLMs’ reasoning abilities on a range of arithmetic, commonsense, and symbolic reasoning tasks (Wei et al., 2022). Additionally, we leveraged Few-Shot prompting, whereby you provide an LLM with input-output examples (Sadeq et al., 2025), as opposed to not providing any examples (Zero-shot prompting), to clarify the desired answer structure. Both of these strategies were conducive to eliciting concise, structured, and nuanced responses by the LLM. By using these techniques, we optimized responses to contain concise answers to users’ queries and provided a corresponding citation in cases in which LuFlot extracted information from Floridi’s original manuscripts.

Domain-Specific Guardrails. We specified domain-specific guardrails in our prompt engineering (e.g., “You must only discuss digital ethics, philosophy of information, and other related domains.” “If a user’s question veers beyond the data provided in your knowledge base, inform them that the data is not within the scope of your understanding.”) These guardrails were implemented to codify LuFlot’s pedagogical value for users and to ensure that the bot was not used for unrelated tasks.

Responsive Depth Control. Due to the verbose nature of LLMs, we embedded a directive into the prompting of LuFlot to maintain brevity (e.g., “By default, respond to user queries in \~ 100–250 words, ensuring you optimize concision.”). However, the UI explicitly states: “[LuFlot] will respond concisely to your queries unless otherwise directed.” Thus, we allowed users to prompt LuFlot to respond at varying levels of depth, to fit individual learning goals.

Adaptable Content Explanation Levels. The UI states: “You can also ask me to explain concepts in diferent ways, such as by saying: ‘Explain the concept(s) mentioned above as if I were a high school student’ or ‘Explain the concept(s) mentioned above using analogies.’” Recognizing the diverse backgrounds of LuFlot’s users and the pedagogical value of explaining content at diferent levels of sophistication, we enabled users to customize LuFlot’s manner of explanations to their needs. This flexibility facilitated the dissemination of complex philosophical concepts to learners at various educational stages.

Multilingual Ability. While LuFlot’s primary language is English, it seamlessly engages with users in multiple languages, including Italian, Mandarin, Spanish, and French, among others. Although the underlying source material is in English, LuFlot’s ability to communicate across languages has facilitated a broader discourse on digital ethics, reaching a diverse worldwide audience.

## 2.3 Retrieval Augmented Generation (RAG)

Retrieval-Augmented Generation (RAG) is a technique used to augment an LLM’s understanding with an external corpus of knowledge (Chen, 2024). The external corpus of knowledge that served as the foundation of LuFlot contained original manuscripts of Floridi’s books. Using OpenAI’s Assistants API, a sophisticated retrieval pipeline was built, containing the following attributes:

Document Processing Pipeline. Floridi’s manuscripts were processed through the Files API, where they were automatically vectorized using the text-embeddingada-002 model, the default embedding model on OpenAI’s API at the time. This converted the text into 1536-dimensional vectors, preserving semantic relationships through cosine similarity. The system automatically chunked the text into manageable sections, ensuring that philosophical coherence and context were maintained. These embeddings formed a dense semantic space that captures the nuanced connections between concepts in Floridi’s work.

Retrieval Mechanism. When a user queries LuFlot, the system performs a semantic search by embedding the query and comparing it to the document embeddings using cosine similarity, a technique that OpenAI’s API leverages for its vector embedding procedure. It then ranks and selects relevant passages based on relevance scoring. The system ensures that retrieved passages are accurately attributed to Floridi’s original texts.

Citation Augmentation. The retrieval engine prioritizes citations from Floridi’s literature. Due to the stochastic nature of LLMs, hallucinations can occur (Xu et al., 2025). However, our testing, driven by tweaking the prompt engineering instructions, demonstrated promising results in accurately extracting and reproducing direct quotes from Floridi’s works.

## 3 Comparison of Other Academic and Philosophically Related Generative AI Tools

This table compares LuFlot and other similar philosophy-based and conversational LLM-based chatbots. We selected these conversational AI systems for comparison because they represent significant attempts to implement philosophical frameworks, ideologies, or ethical reasoning capabilities in language models.

The following table summarizes the reported features of several philosophy-oriented conversational AI systems. The availability and maturity of these tools vary considerably, and consequently, the sources of information difer. Direct hands-on testing was conducted only for FlowGPT’s Aristotle Bot and for general-purpose large language models (e.g., OpenAI’s GPT and Anthropic’s Claude). For the remain-

ing systems—Debate Nature Bot, the Daniel Dennett Bot, and the Peter Singer Bot—the table reflects information drawn from published descriptions, promotional materials, and/or publicly documented capabilities.
<table><tr><td>Feature</td><td>Debate Nature Bot (Altay et al., 2022)</td><td>Aristotle Bot (FlowGPT, 2024)</td><td>Daniel Dennett Bot (Schwitzgeb- el, 2022)</td><td>Peter Singer Bot (Singer, 2024)</td><td>LuFlot Bot</td><td>General LLMs</td></tr><tr><td>Purpose</td><td>Engages in structured debates, focusing on argument and counterargument.</td><td>Facilitates philosophical conversa- tions based on Aristotle&#x27;s teachings.</td><td>Simulates Dennett&#x27;s conversation- al style and philosophical</td><td>Brings Singer&#x27;s insights into the &quot;digital realm.&quot;</td><td>Provides insights into AI eth- ics and the philosophy of infor- mation, drawing on</td><td>General- purpose lan- guage model for a wide</td></tr><tr><td>Use Case</td><td>Simulate debate and argumentation.</td><td>Learn about Aristotle&#x27;s philosophy.</td><td>Explore Dennett&#x27;s philosophi- cal views through a simulated conversation.</td><td>Explore Singer&#x27;s views on animal rights, the impact of sentience on ethical treat-</td><td>Floridi. Educate interested individuals about digi- tal ethics, AI ethics, philosophy of technol- ogy, and philosophy</td><td>Ver- satile, used for anything from natural lan- guage genera- tion to</td></tr><tr><td>Knowl- edge Base edge combined</td><td>Human knowl- with extracted and synthesized text from various sources.</td><td>Aristotle&#x27;s philosophi- cal writings; however, there is no clarity on the specific cor- pus, nor can the chatbot quote ver-</td><td>Dennett&#x27;s literature.</td><td>Singer&#x27;s literature.</td><td>Luciano Floridi&#x27;s literature.</td><td>Trained on a vast dataset covering diverse topics; domain- general.</td></tr><tr><td>Content Genera- tion</td><td>Generates arguments, Provides counterarguments, and structured debate based on speeches.</td><td>responses Aristotelian philosophy.</td><td>Produces Dennett- style text, potentially paraphrasing or providing an original</td><td>Produces text with a neutral tone.</td><td>Generates responses that incorporate specific passages from Flo-</td><td>Pro- duces varied content based on input</td></tr></table>

Developing the Luciano Floridi (LuFlot) Bot: An Accessible AI Chatbot…
<table><tr><td>Feature</td><td>Debate Nature Bot (Altay et al., 2022)</td><td>Aristotle Bot (FlowGPT, 2024)</td><td>Daniel Dennett Bot (Schwitzgeb- el, 2022)</td><td>Peter Singer Bot (Singer, 2024)</td><td>LuFlot Bot</td><td>General LLMs</td></tr><tr><td>Interac- tion Style</td><td>Formal debate format with opening state- ments, rebuttals, and closing statements.</td><td>Conversa- tional, with a focus on philosophical dialogue.</td><td>Conver- sational, mimicking Dennett's style.</td><td>Conver- sational, emulating Singer's style.</td><td>Informative and edu- cational, focusing on ethics and phi- losophy of</td><td>Flexible, adapting to the style and needs of the user.</td></tr><tr><td></td><td>tation techniques; the ability to process and respond to complex debate topics.</td><td>cal insights specific to Aristotelian thought.</td><td>Effective imitation of Dennett's writing style, enabling engaging philosophical discussions</td><td>Interactive dialogue that helps users ar- ticulate and refine ethical viewpoints, grounded in Singer's</td><td>Provides citations from Floridi's manuscripts to connect its dynamic responses to Floridi's original literature.</td><td>Broad knowl- edge, adapt- ability; high- quality language</td></tr><tr><td>Limita- tions</td><td>Struggles with coherence and flow compared to human debaters; perfor- mance is evalu- ated subjectively by audiences. The bot is not free or publicly accessible.</td><td>topics within Aristotle's philosophy. Hosted via FlowGPT, an AI chatbot platform that requires users to sign up for an ac- count to ac-</td><td>inaccuracies and misin- terpretations of Dennett's complex ideas, lacking the depth and nuance of his original work. Heav- ily reliant</td><td>free or publicly accessible (exclusive to paid sub- scribers); it is limited to the beta testing phase as of July 2024.</td><td>the scope of Luciano Floridi's work. The bot will not cover all aspects of AI ethics comprehen- sively.</td><td>produce less spe- cialized or less nuanced content for specific philo- sophi- cal or ethical</td></tr><tr><td>Evalu- ation Method</td><td>Informal audience feedback on debate performance.</td><td>User satis- faction with the depth and relevance of philosophical discussions.</td><td>Participants identified Dennett's an- swer among five options (one real and four GPT- 3-generated), with ac- curacy rates assessing the model's abili- ty to simulate Dennett's responses</td><td>User feed- back during the beta testing phase with paid subscribers.</td><td>Academic and user feedback on the ac- curacy and relevance of citations and ethical discussions. satisfac-</td><td>Perfor- mance metrics like co- herence, rel- evance, and user tion.</td></tr><tr><td>Open Access</td><td>×</td><td>X</td><td>convincingly. X</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Direct Quota- tions from</td><td>X</td><td>X</td><td>X</td><td>X</td><td>√</td><td>X</td></tr><tr><td>Literature Peda- gogical Principles Incorpo- rated</td><td>×</td><td>X</td><td>X</td><td>√</td><td>√</td><td>X</td></tr></table>

## 4 The Purpose, Impact, and Limitations of LuFlot

## 4.1 General Public Exposure to AI Ethics

LuFlot’s broad accessibility invites a diverse audience to engage with and understand the complex ethical issues surrounding AI and digital technologies. By simplifying complex ethical discussions, LuFlot bridges the gap between academic philosophy and lay understanding, making these crucial conversations approachable to the general public. Additionally, LuFlot enhances AI literacy knowledge for individuals—a set of competencies that enables individuals to evaluate AI technologies critically; communicate and collaborate efectively with AI; and use AI as a tool online, at home, and in the workplace (Long & Magerko, 2020)—by providing clear insights into AI’s socioethical implications. Through its straightforward interface and ability to distill complex concepts into easily understandable language, LuFlot contributes to raising awareness and understanding of AI ethics, empowering individuals to make more informed decisions when considering AI’s role in their lives. As of April 2025, LuFlot has reached people in 107 countries, according to data from Vercel analytics. Examples of LuFlot’s ability to distill complex topics surrounding digital ethics into widely understandable information transmission are provided below (Figs. 2, 3, 4 and 5).

![](images/d26b5a0939b0f19d91821c194630da72c09d63592ef6ee44a4644fca27ecd2e8.jpg)  
Fig. 2 LuFlot’s response to “How is AI used in everyday life?”

![](images/1a3c501ea05c114a4889f626c3c561401d77514d31b25c6b40fd5b3d39f2882a.jpg)  
Fig. 3 LuFlot’s response to “What are the benefits of using AI in healthcare and education?”

## 4.2 General Educational and Research Use Cases

The LuFlot Bot can be used in various educational and research settings. For instance, educators can integrate it into philosophy and ethics courses to provide students with instant access to Luciano Floridi’s insights, enhancing classroom discussions around digital ethics. Researchers can employ the bot to quickly reference Floridi’s works, streamlining the literature discovery and review process. Additionally, the bot can serve as a guide for students, helping them navigate the landscape of digital ethics and consider various philosophical perspectives.

![](images/2264d35b4ad012c821147fa226fa96971e9ec43b9ac0037646ffbfecbf27bb2e.jpg)  
Fig. 4 LuFlot’s response to “How can AI be governed to balance innovation with ethical responsibility?”

![](images/832b5f1b81de6a175bf8eb1cd9ec219681e4997b5e1e2c5fde5c6fb25a21338c.jpg)  
Fig. 5 LuFlot’s response to “What is AI ethics?”

## 4.3 Representative User Interactions

To illustrate how LuFlot functions pedagogically, this subsection presents several anonymized, representative user queries alongside LuFlot's responses. These examples were selected to capture the range of user intentions—from clarifying Floridi’s technical vocabulary to exploring conceptual frameworks and engaging in comparative ethical analysis—and to demonstrate how LuFlot structures its explanations while remaining closely grounded in Floridi’s texts. LuFlot's responses are reproduced in their original markdown formatting to reflect how the system structures explanations for readability. The beginning and end of each example are delimited by “###”.   
###

## Example 1: Conceptual Clarification (“Infraethics”)

User: Can you explain what Floridi means by “infraethics”?

LuFlot:

Certainly! The concept of \*\*infraethics\*\*, as articulated by Luciano Floridi, refers to the foundational structures and frameworks that influence moral behavior within a society. It represents a critical layer that operates beneath traditional ethical considerations, acting as a facilitator or hindrance to ethical actions and decisions.

## ### Key Concepts of Infraethics

## 1. \*\*Definition and Role\*\*:

\- Infraethics is described as a \*\*not-yet-ethical but ethically relevant framework\*\*. It encompasses the socio-cultural norms, expectations, and rules that shape moral behavior but are not inherently ethical themselves. This distinction is crucial as it helps clarify that while infraethics can influence ethical outcomes, it does not itself dictate what is ethical or unethical. Instead, it serves as an infrastructure that either supports or obstructs ethical evaluations and actions [1], [2].

## 2. \*\*Dual Nature\*\*:

\- Floridi emphasizes that infraethics possesses a \*\*dual value\*\*. It can facilitate moral behavior or contribute to immoral actions, similar to how a physical infrastructure can support both beneficial and harmful activities in society. Thus, infraethics is not morally neutral; rather, it reflects a tension between ethical and unethical potentials. This analogy is illustrated by comparing it to a taut rope under tension, where the balance between opposing forces can lead to either constructive or destructive outcomes [2], [4].

## 3. \*\*Comparison with Ethics\*\*:

\- The distinction between infraethics and ethics is critical. While ethics deals with moral rights and values—essentially the “water” that flows through the “pipes” of moral frameworks—infratechnology can be seen as the “pipes” themselves. Without a proper infraethical framework, the ethical considerations may struggle to be efectively realized in practical contexts [1], [3]. Floridi argues that recognizing this distinction is essential for understanding how moral behavior is shaped in an increasingly digital and interconnected world.

## ### Practical Implications

\- \*\*Ethical Infrastructure\*\*: In a digitally mature society, efective moral interactions require robust infraethical systems. This means that as we develop and engage with information and communication technologies (ICTs), we must also cultivate the underlying ethical frameworks that will guide their use and impact [5]. For example, the balance between privacy and security in digital contexts reflects an infraethical concern, where both elements must be managed efectively to promote ethical outcomes.

\- \*\*Influence on Society\*\*: Floridi posits that the moral behavior of a society is heavily reliant on its ethical infrastructure. Just as economic systems require physical infrastructures to thrive, so too do our moral interactions depend on welldesigned infraethical frameworks. This insight underscores the importance of developing policies and norms that support ethical behavior in the digital age [4], [5].

## ### Conclusion

In summary, infraethics is a foundational concept within Floridi’s philosophy that highlights the interplay between ethical frameworks and the structures that support them. By understanding infraethics, we can better navigate the complexities of moral behavior in a digital context, ensuring that our ethical considerations are not only well-founded but also efectively implemented in practice. Floridi’s exploration of this concept invites us to reflect on how our socio-cultural infrastructures shape our ethical landscapes, particularly as we engage with the digital world.

\*\*Sources: \*\*

[1]: The Green and the Blue Naive Ideas to Improve Politics in the Digital Age - “occurrence of what is ethically good. At best, infraethics is the oil that lubricates ethical mechanisms to function smoothly and correctly. For this reason, it is easy to conflate infraethics with et…”.

[2]: The Green and the Blue Naive Ideas to Improve Politics in the Digital Age - “understood conceptually, only in terms of a second-order or meta-ethical discourse on ethics. Instead, infraethics is a not-yet-ethical but ethically-relevant framework that can facilitate or hinder e…”.

[3]: The Green and the Blue Naive Ideas to Improve Politics in the Digital Age - “the vital humus for the success of any complex society. As I wrote earlier, infraethics has a fundamental role in human interactions, comparable to that we commonly attribute to good physical infrastr…”.

[4]: The Fourth Revolution How The Infosphere Is Reshaping Human Reality - “the fact that the moral behaviour of a society of agents is also a matter of ‘ethical infrastructure’ or simply infraethics. An important aspect of our moral lives has escaped much of our attention. M…”.

[5]: The Green and the Blue Naive Ideas to Improve Politics in the Digital Age\*\* - “in terms of a platform or infrastructure of social norms, expectations, and rules, often only socio-cultural and unwritten, which facilitate or hinder the moral or immoral behaviour of the agents invo”.

## Example 2: Ontological Inquiry (“Infosphere”)

User: Can you define AI and explain why do you prefer the concept of “agency”?

## LuFlot:

\## Defining AI and the Concept of Agency

Artificial Intelligence (AI) remains a complex and often debated term within both the technological and philosophical domains. As Luciano Floridi highlights, “the best definition of AI remains that propounded by the scientists and mathematicians McCarthy, Minsky, Rochester, and Shannon,” which emphasizes a family of sciences, methods, and technologies rather than a singular definition [5]. This lack of consensus illustrates the multifaceted nature of AI, reflecting its evolution and application in diverse contexts.

## ### The Concept of Agency in AI

Floridi’s preference for the concept of \*\*agency\*\* over a strict definition of intelligence is rooted in the transformative nature of AI as a new form of smart agency. Here are some key insights into this concept:

1. \*\*Decoupling Intelligence from Agency\*\* - Floridi argues that AI represents a divorce between agency and intelligence, where successful agency does not necessarily require intelligence. This means that AI can perform tasks and solve problems efectively without mimicking human-like intelligence [4].

2. \*\*Smart Agency\*\* - In Floridi’s view, AI functions as a “reservoir of smart agency on tap,” capable of executing an increasing array of tasks that traditionally required human cognitive abilities. This perspective shifts the focus from trying to define AI based on intelligence to understanding it as a tool for enhancing human capabilities [1].

3. \*\*Ethical Implications\*\* - The transformation of agency through AI raises significant ethical questions. As Floridi notes, this new form of agency can lead to unintended consequences, such as nudging humanity to adapt to technologies that may not always align with human values [2]. By analyzing AI as agency, we can better address these ethical challenges and ensure responsible use.

4. \*\*Design and Agency\*\* - Floridi posits that design plays a crucial role in shaping AI’s agency. This is because the manner in which AI systems are engineered and implemented reflects our values and priorities, thereby influencing the outcomes they produce [3]. Thus, understanding AI through the lens of agency enables a more comprehensive grasp of its implications for society.

## ### Practical Implications

Understanding AI through the concept of agency has significant implications for how we interact with technology. By focusing on agency:

\- \*\*Enhancing Human Agency\*\*: AI can be developed to complement and enhance human decision-making rather than replace it, empowering individuals and communities.

\- \*\*Ethical Design\*\*: Designers and engineers are encouraged to consider ethical principles in the creation of AI systems, ensuring that they align with human values and societal goals.

\- \*\*Policy Development\*\*: Policymakers can better navigate the complexities of AI regulation by recognizing the agency aspects, fostering frameworks that prioritize ethical considerations.

## ### Concluding Thoughts

In summary, the concept of agency provides a nuanced understanding of AI that transcends mere definitions of intelligence. It emphasizes the autonomy and capabilities of AI systems while also highlighting the ethical responsibilities that accompany their deployment. As Floridi aptly illustrates, recognizing AI as a form of agency allows for a more thoughtful engagement with the challenges and opportunities that this technology presents [1][4].

This perspective invites further exploration into how AI can be designed and utilized to respect and enhance human agency, fostering a digital environment that aligns with our collective values. Would you like to discuss specific ethical implications or examples related to AI agency?

\*\*Sources: \*\*

[1]: The Ethics of Artificial Intelligence Principles, Challenges, and Opportunities - “Both the classic counterfactual definition and the interpretation of AI as a divorce (not a marriage) between agency and intelligence enable one to conceptualise AI as a growing resource of interactiv…”.

[2]: The Ethics of Artificial Intelligence Principles, Challenges, and Opportunities - “the new field of AI in 1955. We already encountered it in the previous chapter, and this is the characterisation that I shall adopt for the rest of the book. I also discuss Turing’s famous question ‘c…”.

[3]: The Ethics of Artificial Intelligence Principles, Challenges, and Opportunities - “of the digital. I illustrate this cleaving power through some concrete examples. Then, I use it to interpret AI as a new form of smart agency brought about by the digital decoupling of agency and inte…”.

[4]: The Green and the Blue Naive Ideas to Improve Politics in the Digital Age - “Let us recall the basic premise: the digital marks a revolution because it cuts, pastes, and hence can more easily design or re-design reality and how we think about it. If this is true, does AI r…”.

[5]: The Ethics of Artificial Intelligence Principles, Challenges, and Opportunities\*\* - “has cut and pasted our realities along with our ideas about our realities, re-ontologising and re-epistemologising modernity. This has led to the development of AI as a new form of agency that can be…”.

Example 3: Comparative Philosophical Question (Floridi and Virtue Ethics)

User: How might Floridi’s ideas coincide with virtue ethics?

LuFlot:

\## Overview of Floridi’s Ideas and Virtue Ethics

Luciano Floridi’s philosophy, particularly his work in information ethics (IE), intersects intriguingly with virtue ethics. Both frameworks share a foundational interest in the well-being of entities, yet they diverge significantly in their approaches and implications, particularly in the context of a globalized information society.

\## Key Concepts

1. \*\*Well-Being of Entities\*\* - Floridi emphasizes that the flourishing of informational entities—whether human or artificial—is paramount. His approach positions well-being as central to ethical considerations in the infosphere, indicating a dialogue with virtue ethics, which also prioritizes the flourishing of individuals as virtuous beings. He states that “the well-being of an entity as well as of the whole infosphere consists in the preservation and cultivation of its properties” [1]. This shared focus suggests a common ground where both philosophies aim to nurture the good qualities in entities.

2. \*\*Patient-Oriented Ethics\*\* - Floridi’s IE adopts a patient-oriented perspective, aligning it with virtue ethics, which emphasizes character and personal development. In this view, ethical considerations are not merely transactional but relational, fostering an environment where entities can cultivate virtues. This contrasts with more functionally driven ethical frameworks that may overlook the intrinsic value of the entities involved.

3. \*\*Construction of the Self\*\* - Floridi posits that both IE and virtue ethics recognize the human being as a “work in progress,” constantly engaged in selfconstruction [1]. This perspective resonates in virtue ethics, where the development of character is seen as a lifelong endeavor. However, Floridi’s broader conception of what constitutes a good entity expands this dialogue beyond human agents to include the ethical implications of artificial agents and information systems.

4. \*\*Challenges of Individualism\*\* - While virtue ethics can foster personal growth, Floridi cautions against its limitations in a globalized context. He argues that such an approach might promote ethical individualism, where agents focus solely on their self-construction, neglecting the interconnectedness of the infosphere and the ethical responsibilities towards others [2]. This critique underscores the necessity for an ethical framework that encompasses collective well-being alongside individual virtue.

## ## Practical Implications

Floridi’s integration of virtue ethics into information ethics suggests several practical implications:

\- \*\*Ethical Design in Technology\*\* - When developing information systems, designers should consider how these systems can foster virtues such as trust, respect, and responsibility. This aligns with Floridi’s call for ethical innovation in technology, ensuring that digital platforms promote the flourishing of all users.

\- \*\*Community and Relational Ethics\*\* - In digital spaces, where community interaction is prevalent, Floridi’s emphasis on the collective good encourages a shift from individualistic approaches to community-oriented ethics. This suggests that online behaviors should reflect a commitment to communal well-being, echoing the virtues espoused by virtue ethics.

\- \*\*Education and Character Development\*\* - Educational frameworks that incorporate Floridi’s insights could focus on cultivating not just technical skills but also ethical sensibilities, promoting the development of character traits that are essential for navigating the complexities of the digital world.

## ## Concluding Thoughts

Floridi’s exploration of information ethics reveals a rich interplay with virtue ethics, emphasizing the importance of well-being and character development in both individual and collective contexts. As we navigate an increasingly complex digital landscape, the integration of these ethical frameworks can guide us toward a more responsible, inclusive, and flourishing information society. This synthesis not only highlights the importance of nurturing virtues but also calls for a broader acknowledgment of our interconnectedness within the infosphere, where ethical considerations extend beyond individual interests to encompass the welfare of all entities involved.

\*\*Sources: \*\*

[1]: The Ethics of Information - “With all due attention and care, we should be ready to innovate. 4.7.3 IE and Virtue Ethics The well-being of an entity as well as of the whole infosphere consists in the preservation and cult…”.

[2]: The Ethics of Information - “in small cyber-communities (comparable to local area networks) and is popular ‘IRL’ or ‘OT’ (in real life or out there). However, the opposite is true. Because virtue ethics remains limited by its sub…”.

[3]: The Ethics of Information.

[4]: The Ethics of Information - “One should still properly object that the kind of egopoiesis promoted by virtue ethics cannot (indeed, was not meant to) scale to very complex and open social contexts; and virtue ethics presu…”.

[5]: The Ethics of Artificial Intelligence Principles, Challenges, and Opportunities.

###

Across these interactions, several qualitative patterns become clear. Users frequently seek clarification of Floridi’s technical vocabulary (e.g., infraethics), ask for explanations of abstract concepts embedded within broader philosophical or ethical frameworks (e.g., AI as agency rather than intelligence), or request comparative analysis that situates Floridi’s ideas within familiar ethical traditions (e.g., virtue ethics). These queries show that users engage LuFlot to navigate conceptual distinctions, interpret foundational principles, and understand how Floridi’s philosophy relates to wider debates in philosophy. LuFlot’s responses demonstrate its capacity to structure multi-layered explanations, introduce conceptual scafolding, and maintain citation-grounded fidelity to the underlying manuscripts. While not a formal evaluation, these interaction patterns provide qualitative evidence that LuFlot functions as an interpretive and pedagogical mediator: it helps non-expert audiences access, contextualize, and meaningfully engage with Floridi’s scholarship in ways that would otherwise require specialized background knowledge.

## 4.4 Limitations

Like any LLM-based system, LuFlot has clear constraints that users should understand. First, its explanations can become reductionist when a concept requires situating within Floridi’s broader argumentative framework. This occurs most noticeably with ideas that depend on long-form textual development—infraethics and ontological design, for example—where a short answer cannot capture the full range of distinctions Floridi draws. In our testing, reductionism was infrequent but predictable in cases where users asked for highly compressed summaries of dense material.

Second, while RAG can reduce hallucinations, it does not eliminate errors. Misquotations or partial interpretations occurred occasionally during development, typically when the retrieved passage was adjacent to, but not identical with, the text most relevant to the query. These errors were usually minor, slight paraphrasing drift rather than fabricated material, but they reinforce the need for users to verify quotations against the primary texts when precision matters.

![](images/bc80e9f9494ae0247c6eec01d6790080ccbeec56a5e47b0f532f404e034af678.jpg)  
Fig. 6 User testimonial from a doctoral student highlighting LuFlot’s value for academic research and philosophical inquiry in digital ethics

A further limitation concerns multilingual use. Because the manuscripts used to build LuFlot are entirely in English, non-English users receive answers in their own language that are generated by the LLM on the basis of English source material, rather than translations of the primary texts themselves. This introduces a philosophical trade-of: the system broadens access while simultaneously mediating the user’s contact with Floridi’s language and conceptual texture. Nuances that hinge on specific terminology—such as Floridi’s distinctions between “information,” “data,” and “semantic content”—can shift subtly in translation, even when the underlying reasoning remains intact. This does not undermine the value of multilingual accessibility, but it does situate it as an interpretive rather than an archival encounter. Users should therefore view these translated outputs as an entry point into Floridi’s work rather than as substitutes for the original formulations.

To mitigate these limitations, users should treat the system as a guide rather than a source of authoritative exegesis: consulting linked passages, asking follow-up questions for clarification, and using LuFlot’s output as a starting point for further reading.

## 4.5 Applications for Students and Researchers

For students and researchers in philosophy or digital ethics, LuFlot can serve as a valuable resource. The bot provides instantaneous access to Floridi’s philosophical insights, proving useful for those investigating the ethical dimensions of technology. As one doctoral student noted in Fig. 6, “[LuFlot] will be useful for us doctoral students to consult LuFlot to have immediate feedback on his thoughts and his texts, fundamental in the field of Artificial Intelligence and digital technologies.” This testimonial highlights the bot’s role in providing quick and easily accessible information about topics within the digital ethics field, thereby enhancing the eficiency of research discovery. Researchers can use the bot to clarify complex concepts, verify interpretations, and inspire new lines of inquiry, making it a valuable tool in their scholarly toolkit.

## 5 Conclusion

The development and deployment of LuFlot marks a significant advancement in democratizing access to complex philosophical discourse in digital ethics. By leveraging GPT-4-Turbo’s capabilities through OpenAI’s Assistants API and implementing RAG, LuFlot has helped bridge the gap between academic philosophy and public understanding, reaching individuals across 107 countries. The system’s implementation of advanced prompt engineering techniques, alongside its multilingual capabilities and adaptable explanation levels, has created an accessible educational tool that maintains scholarly integrity through proper attribution.

This commentary’s central contribution is to demonstrate that a citation-grounded RAG system can function as a reliable pedagogical channel for complex philosophical scholarship, allowing non-specialists to access and interrogate Floridi’s ideas with verifiable interpretive fidelity. LuFlot thus demonstrates how AI systems, when properly constrained and curated, can help bridge the gap between technical academic texts and wider audiences.

Looking ahead, further work could entail expanding LuFlot’s capabilities beyond its current chatbot implementation into an agentic system capable of more sophisticated interactions in research, education, and ethical analysis. As AI continues to propagate throughout society, LuFlot serves as a proof of concept for how AI-powered tools can reshape specialized academic knowledge into insights accessible to the public while maintaining intellectual rigor.

## References

Altay, S., Schwartz, M., Hacquin, A. S., Allard, A., Blancke, S., & Mercier, H. (2022). Scaling up interactive argumentation by providing counterarguments with a chatbot. Nature Human Behaviour, 6(4), 579–592. https://doi.org/10.1038/s41562-021-01271-w

Borenstein, J., & Howard, A. (2021). Emerging challenges in AI and the need for AI ethics education. AI and Ethics, 1(1), 61–65. https://doi.org/10.1007/s43681-020-00002-7

Chen, Z. (2024). Eficient retrieval-augmented generation Master’s thesis. University of Illinois at Urbana-Champaign. Department of Computer Science. https://hdl.handle.net/2142/124428

Day, T. (2023). A preliminary investigation of fake Peer-Reviewed citations and references generated by ChatGPT. The Professional Geographer, 75, 1024–1027. https://doi.org/10.1080/00330124.2023.2 190373

Floridi, L. (2024). The ethics of artificial intelligence: Exacerbated problems, renewed problems, unprecedented problems - Introduction to the special issue of the American philosophical quarterly dedicated to the ethics of AI. SSRN Electronic Journal. https://doi.org/10.2139/ssrn.4801799

FlowGPT (2024). Talk with Aristotle. FlowGPT. https://flowgpt.com/p/talk-with-aristotle.

Lai, V., Ngo, N., Veyseh, A., Man, H., Dernoncourt, F., Bui, T., & Nguyen, T. (2023). ChatGPT beyond english: Towards a comprehensive evaluation of large Language models in multilingual learning. ArXiv. https://doi.org/10.48550/arXiv.2304.05613

Long, D., & Magerko, B. (2020). What is AI Literacy? Competencies and Design Considerations. Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems. https://doi.org/10. 1145/3313831.3376727

McGregor, M. (2023). What is GPT-4? Key facts and features. Semrush. https://www.semrush.com/blog /gpt-4/

OpenAI (2024). GPT-4-Turbo. OpenAI Documentation. https://platform.openai.com/docs/models/gpt-4-t urbo

Restack (2024). Text Chunking With Openai Ada 002. Restack. https://www.restack.io/p/text-chunking-a nswer-openai-text-embedding-ada-002-cat-ai

Sadeq, N., Xu, X., Xie, Z., McAuley, J., Kang, B., Lamba, P., & Gao, X. (2025). Improving In-Context learning with reasoning distillation. https://doi.org/10.48550/arXiv.2504.10647

Schwitzgebel, E. (2022). Results: The computerized philosopher: Can you distinguish Daniel Dennett from a computer? The Splintered Mind. https://schwitzsplinters.blogspot.com/2022/07/results-com puterized-philosopher-can.htm

Singer, P. (2024). Introducing Peter Singer AI: Elevating ethical discourse in the digital age. Bold Reasoning with Peter Singer. https://boldreasoningwithpetersinger.substack.com/p/introducing-peter-singe r-ai-elevating

Vasconcelos, M., & Santos, R. (2023). Enhancing STEM learning with chatGPT and Bing chat as objects to think with: A case study. ArXiv. https://doi.org/10.29333/ejmste/13313

Wei, J., Wang, X., Schuurmans, D., Bosma, M., Chi, E., Xia, F., Le, Q., & Zhou, D. (2022). Chain of thought prompting elicits reasoning in large Language models. ArXiv, abs/2201.11903.

White, J., Fu, Q., Hays, S., Sandborn, M., Olea, C., Gilbert, H., Elnashar, A., Spencer-Smith, J., & Schmidt, D. (2023). A prompt pattern catalog to enhance prompt engineering with ChatGPT. ArXiv. https://doi. org/10.48550/arXiv.2302.11382. abs/2302.11382.

Xu, Z., Jain, S., & Kankanhalli, M. (2025). Hallucination is inevitable: An innate limitation of large Language models (ArXiv:2401.11817). ArXiv. https://doi.org/10.48550/arXiv.2401.11817

Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional afiliations.

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law.