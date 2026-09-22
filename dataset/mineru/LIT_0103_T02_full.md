# AIGC: From Statistical Methods to Cognitive Applications Technological Evolution and Current Challenges

Hongyi Zhou   
Aberdeen Institute of Data Science and Artificial   
Intelligence   
South China Normal University   
Foshan, Guangdong province, China   
Business School   
University of Aberdeen   
Aberdeen, Scotland, United Kingdom   
2963087383@qq.com

Biqing Zeng<sup>∗</sup> Aberdeen Institute of Data Science and Artificial Intelligence South China Normal University Foshan, Guangdong province, China zengbiqing137@163.com

## Abstract

Recent advances in algorithms, computing power, and data have accelerated the development of AI-generated content (AIGC), reshaping a wide range of industries. However, along with the development of technology, many potential problems also emerge continuously. To elucidate the dilemmas in AIGC development and provide guidance for future research, this paper takes a global view and systematically reviews its evolution from statistical models to cognitive breakthroughs. Then, the core technologies are examined, and the major development highlights of AIGC at the current stage are discussed. Building on the above analysis, a three-level AIGC application risk transmission model is proposed, which integrates multi-source evidence chains and reveals information ethics issues and application dilemmas. Furthermore, the model demonstrates how universal benefits can be achieved through progressive logic. Finally, the paper discusses future research directions for these issues.

## CCS Concepts

• Computing methodologies → Artificial intelligence; Natural language processing; Natural language generation.

## Keywords

AIGC; Artificial Intelligence; Information Ethics

## ACM Reference Format:

Hongyi Zhou and Biqing Zeng. 2025. AIGC: From Statistical Methods to Cognitive Applications: Technological Evolution and Current Challenges. In The 18th International Conference on Computer Science and Information Technology (ICCSIT 2025), October 27–29, 2025, Paris, France. ACM, New York, NY, USA, 11 pages. https://doi.org/10.1145/3783862.3783894

## 1 Introduction

The fast-paced evolution of artificial intelligence (AI) is transforming how information is produced and used. As an emerging paradigm, AI-generated content (AIGC) is attracting increasing attention for its innovation potential and its expanding role in research and industry. Specifically, AIGC [1] refers to a multimodal machine learning model driven by a deep neural network architecture that is pre-trained and forms a complete output through Autoregression [19], which is significantly diferent from analytical AI [74].

The multimodal output capability of AIGC is enabled by a range of generative models that have been extensively developed in AI. Based on model design principles, these generative models can be grouped into three stages, conceptual inception and weight simulation, probabilistic approximation, and cognitive development, as summarized in Table 1. During the idea germination and weight simulation stage, the representative MP Model (McCulloch–Pitts Model) produced basic outputs by simulating human brain neurons [4], ofering essential theoretical insights for the development of perceptrons [5] and neural networks [6][7]. In the probability approximation stage, the modeling of data distributions gradually became mainstream. Representative models during this period included the Deep Belief Network (DBN) [8] and the Generative Adversarial Network (GAN) [2]. In the cognitive development stage, the model’s perception, generative, and reasoning capabilities are significantly enhanced, as reflected in the Transformer [10], Difusion Model [11], and DeepSeek-R1 model [12], respectively.

This paper reviews major milestones in AIGC and assesses their impacts across related domains by tracing key technological developments. It also analyzes architectural advances and practical deployment bottlenecks from two complementary perspectives, providing actionable insights for researchers and practitioners, and informing technology governance and future trend analysis. Consequently, this review synthesizes the historical evolution of AIGC and examines future trajectories and associated societal implications.

Beyond the introduction, the structure of this paper is organized as follows. Chapter 2 outlines representative technologies and models in the development of AIGC, including the Transformer and the DeepSeek-R1 model. Chapter 3 examines the current development status of AIGC, including its advantages, open-source strategy, and the three-level risk transfer model for limitations and risks. Chapter

<table><tr><td>Stage</td><td>Year/Mile- stone</td><td>Representative Model</td><td>Key Features</td><td>Role in AIGC Evolution</td></tr><tr><td>Conceptual Inception &amp; Weight</td><td>1940</td><td>MP Model[4]</td><td>Binary threshold neuron model for Boolean function representation</td><td>Established theoretical founda- tion for neural networks</td></tr><tr><td>Simulation Probabilistic</td><td>1950</td><td>SLP[5]</td><td>Trainable single-layer feedforward ar- chitecture with perceptron learning Recurrent architecture with temporal</td><td>Pioneered supervised learning for AIGC model training First to generate sequential</td></tr><tr><td rowspan="4">Approximation</td><td>1980</td><td>RNN[6]</td><td>dependency modeling Hierarchical convolutional feature ex-</td><td>content in AIGC Core support for AIGC visual</td></tr><tr><td>1980 2000</td><td>CNN[7] DBN[8]</td><td>traction with spatial invariance Layer-wise unsupervised pretraining</td><td>content generation Early adopter of unsupervised</td></tr><tr><td>2010</td><td>GAN[2]</td><td>for deep representation learning Adversarial learning framework with generator and discriminator interac-</td><td>deep learning in AIGĆ Dramatically enhanced quality</td></tr><tr><td></td><td></td><td>tion Self-attention based sequence model-</td><td>of generated content in AIGC Significant advance in coherent</td></tr><tr><td rowspan="3"></td><td>2010</td><td>Transformer[10]</td><td>ing with global dependency capture Stochastic diffusion based generative</td><td>text generation for AIGC Leap in image-generation capa-</td></tr><tr><td>2020 2025</td><td>Diffusion Model[11] DeepSeek-</td><td>modeling with iterative denoising Large-scale inference training for en-</td><td>bilities for AIGC Extended AIGC into logic-</td></tr><tr><td></td><td>R1[i2]</td><td>hanced reasoning capability</td><td>intensive domains, boosting practical utility</td></tr></table>

Table 1: Evolutionary stages of AI technologies in AIGC

4 proposes three potential directions for future research. Chapter 5 concludes the paper.

## 2 OVERVIEW OF AIGC RELATED TECHNIQUES

## 2.1 Deep Belief Networks (DBN)

Deep Belief Networks (DBNs) are deep learning models composed of multiple layers of Restricted Boltzmann Machines (RBMs) [8][14][15]. As a probabilistic generative model, the RBM-based architecture captures abstract data features by learning a probability distribution over the input, with weights obtained through unsupervised, greedy layer-wise pre-training [8].

Compared with the Multilayer Perceptron (MLP) [5], which con sists of an input layer, hidden layer, and output layer, the RBM architecture within a Deep Belief Network comprises a visible layer and a hidden layer. During training, each RBM layer must be trained sequentially. Notably, neurons within each RBM layer are unconnected, while inter-layer neurons are fully connected. This architecture promotes intra-layer independence and enhances feature learning. Once training ofa single-layer RBM converges, its weights and biases are fixed, and performance is refined through multiple iterations.

As an example, a DBN composed of two stacked RBM layers is shown in Figure 1. Neurons v1, v2, v3, and v4 represent the visible units of the first RBM layer, while h1, h2, and h3 serve as hidden feature detectors. In the second RBM layer, v5, v6, and v7 are the visible units, with h4 and h5 as the corresponding hidden units. During forward propagation, data are transmitted upward through the hierarchy, with the activations of the first hidden layer directly serving as input to the visible units of the second layer, thereby enabling layer-wise learning.

Moreover, the RBM enables autonomous data reconstruction in the absence of labeled supervision, through backward propagation from the higher to the lower layers as indicated by the red arrow in Figure 1. This process allows multiple iterations of forward and backward propagation between the visible layer and the first hidden layer without increasing the network depth.

As a representative generative model, the introduction of DBNs proposed the innovative concept of pre-training for the development of deep neural networks, efectively addressing the historical problem of vanishing gradients and facilitating the emergence and adoption of discriminative models such as CNNs [21]. Moreover, DBNs demonstrate the strong potential of deep architectures in handling complex data, and their unsupervised feature learning approach ofers key methodological support for the advancement of AIGC-related techniques.

## 2.2 Transformer

The Transformer model [10], based on the self-attention mechanism, is capable of capturing complex global relationships, thereby significantly enhancing AIGC’s capacity to comprehend multimodal content. Transformer models employ architectures similar to the Sequence Transduction Model [19] and the Variational Autoencoder (VAE) [17], in which the overall structure comprises an encoder and a decoder. The self-attention mechanism is introduced as a key innovation enabling this architecture. Consequently, during text generation, the model considers not only the current input but also contextual relevance, assigning attention weights to each token to capture global dependencies.

![](images/6caad7694ccd5ec4e7e56dd1abefc7c84f1d7645a4d82affa4dde21fd4426f34.jpg)  
Figure 1: Example Deep Belief Network (DBN) architecture

Building on the work presented in [19] and [17], [10] proposes the Multi-Head Attention mechanism, which projects the Query, Key, and Value matrices into a lower-dimensional space h times, performs the attention operation h times, and concatenates the resulting outputs, which are then projected through a linear layer to produce the final output. This architecture enables parallel multidimensional feature extraction, allowing adaptation to input sequences of varying lengths. Furthermore, [10] refined Batch Normalization (BN) [16] by replacing it with Layer Normalization, which normalizes each row to have a mean of zero and a variance of one, an operation essentially equivalent to a matrix transpose. This allows independent normalization at each position, improving model stability, reducing internal covariate shift, and thereby accelerating training. At the decoder level, an autoregressive mechanism is employed: when predicting the output at time t, the model must not access inputs corresponding to time steps beyond t, even if they appear later in the sequence. To enforce this constraint, Vaswani et al. [10] introduced the Masked Multi-Head Attention mechanism.

As a cornerstone of AIGC progress, the Transformer’s ability to capture long-range dependencies significantly accelerates generative model development and fosters the diversification of AIGC application scenarios.

## 2.3 Difusion Model

Initially introduced into non-equilibrium thermodynamics theory [18], the difusion model employs a Markov chain to simulate the dynamic evolution of data during the forward process, incrementally adding noise to the original data to produce a distribution approximating standard normality. During the subsequent backward process, Gaussian noise is progressively removed and decoded to generate new data, thereby achieving the transformation from a Gaussian distribution to the target data distribution. This approach outperforms contemporary generative models such as the Deep Convolutional GAN [28] and VAE [17] in both sample quality and training stability. Moreover, Stable Difusion reduces the dimensionality to a latent space, significantly shortening the training period [11], and represents another major innovation in the field of AIGC following the difusion model.

As a core driver of AIGC development, the difusion model significantly enhances output quality by incrementally adding noise and learning the reverse denoising process. Compared with other latent variable generative models, its training stability and controllable generation capabilities lower the barriers to real-world deployment of AIGC technology and promote the widespread adoption of AIGC in creative industries.

## 2.4 DeepSeek family of Large Language Models (LLMs)

2.4.1 DeepSeek-V3. The DeepSeek-v3 large model [23] was launched by the DeepSeek research and development team. This model realizes a multi-dimensional innovation breakthrough, and achieves eficient inference and training while reducing computational complexity.

![](images/7ce14e101ee6d7910016cefdd6e25886bc410030accc9c49babbed59d05a6436.jpg)  
Figure 2: Optimized MoE with shared and routed experts

Innovative hybrid expert architecture. As shown in Figure 2, the model adopts an optimized Mixture of Experts (MoE) architecture [22]. Traditional MoE architectures [26] comprise multiple expert models and handle complex tasks by decomposing them into subproblems, which are routed to corresponding experts via a gating network. However, traditional MoE sufers from low training efficiency due to minimal overlap and over-specialisation among experts. To address this, the team implemented a combination of shared-expert and fine-grained expert segmentation strategies [23].

Specifically, the architecture introduces a fine-grained expert division strategy, which enhances expert specialization by partitioning the original expert set into smaller, more focused units. Simultaneously, a fixed subset of experts is activated at each layer to form a static expert network (as shown in Figure 2), which integrates contextual information and handles general tasks, thereby reducing parameter redundancy among routed experts, enhancing expert specialization, and optimizing the allocation of computational resources. In addition, although the sparse expert activation mechanism is similar to that in GShard [27], the DeepSeek-MoE architecture [22], optimized on this basis, exhibits lower expert knowledge redundancy and higher routing accuracy, thereby im proving the model’s scalability.

No auxiliary loss load balancing. The problem of load balancing has always been a big problem in training MoE architecture mod els. As early as 2021, William Fedus et al. [24] proposed a solution that introduces a load-balancing loss function to ensure that the experts inside the model are trained in a balanced way. However, this scheme has the possibility of overfocusing on the function and ignoring the performance of the model in the optimization iterative process. Therefore, the DeepSeek research team proposed the Auxiliary-Loss-Free Load Balancing strategy (ALFLB) [23], which dynamically adjusts the probability of activation of each expert through model adaptation to achieve eficient and low-cost training efect.

Multi-Token Prediction. The MTP (Multiple Target Prediction) technique [25] employed in the DeepSeek-V3 model significantly improves sample eficiency and accelerates inference. Built upon the Transformer architecture, MTP employs multiple independent output heads to predict several future tokens in parallel, with the final output verified and filtered by a next-token prediction head. Compared to traditional next-token prediction (NTP), MTP provides richer supervision signals [23], thereby improving learning eficiency and enabling adaptation to more complex generation tasks.

2.4.2 DeepSeek-R1-Zero. The DeepSeek-R1-Zero grand model is considered as a transition model from V3 to R1. The innovation of this model lies in the Group Relative Policy Optimization (GRPO) [12], which breaks through the traditional paradigm. That is, Supervised fine tuning (SFT) is required after large model pre-training, and it solves the computational bottleneck problem faced by traditional reinforcement learning algorithms, such as Proximal Policy Optimization (PPO), when optimizing LLMs. For the same input, by training multiple strategies and reference models, the GRPO algorithm will generate the average reward of multiple outputs as the baseline value, and then update the gradient according to the diference between itself and the group’s baseline value, so as to stimulate the reasoning ability of the model autonomously. Com pared with traditional reinforcement learning, it does not need to rely on manually labeled data sets, and guides model optimization in the form of comparing multiple response groups in the same batch.

2.4.3 DeepSeek-R1. Overall, this large model integrates the advantages presented in [25] and [12]. The DeepSeek-R1-Zero model is trained solely via reinforcement learning. Without supervised fine-tuning, it may be more prone to cross-lingual mixing during generation. Subsequently, the DeepSeek-R1 model incorporates cold start data to provide guidance and enhance early-stage performance. Thereafter, reasoning-oriented reinforcement learning commences, introducing a language consistency reward mechanism to enhance reasoning capabilities on structured tasks while main taining accuracy. Optimization in specific dimensions is achieved through rejection sampling and supervised fine-tuning. Following training in the general alignment reinforcement learning stage, the model’s capacity for multi-scene task processing and its security in open-domain tasks are substantially enhanced. It is worth mentioning that the thinking modes such as self-reflection and Aha Moment spontaneously emerge in the training of the model, which has the rudiment of Artificial General Intelligence (AGI).

In short, the paradigm of DeepSeek series models improving the reasoning ability of the model through reinforcement learning training further improves the rigor of AIGC output content logic. At the same time, its low-cost development features also provide new impetus for the popularization and innovation of AIGC, which has a profound impact on AIGC ecology.

## 3 THE CURRENT DEVELOPMENT STATUS OF AIGC

## 3.1 Highlight of the AIGC Industry Development

The core breakthrough progress of AIGC can be summarized into three key elements, as shown in Figure 3.

![](images/186a314b880815fb1bd61935da275784ccc2c569966a7ebbd522eb3cccbaa7da.jpg)  
Figure 3: Three key highlights in AIGC development

3.1.1 Industry progress driven by hardware upgrades. Over the past five years, hardware technology has improved the parallel computing framework and energy eficiency management strategies, facilitating multi-level optimization of computing power and significantly enhancing model computing power. In 2022, NVIDIA launched the new-generation Hopper architecture GPU chip NVIDIA H100. This chip integrates up to 80 billion transistors and 18,432 cores [37], significantly improving the training eficiency of large models by optimizing the hardware’s parallel computing capability. Additionally, at the SC24 conference, Google launched the new AI accelerator TPU v6e (Trillium) [38], with onboard HBM increasing by 16GB compared to the previous generation, capable of handling higher standards of training task requirements.

3.1.2 Continuous improvement of the performance. Recent advances have shifted how large models generate content. They are moving beyond simply recombining training data [30] to creating novel out puts through reasoning. For instance, the DeepSeek-R1 large model utilized the GRPO strategy [12] to partially replace the manually annotated dataset with the application of group dynamics theory, thereby enhancing the model’s autonomous reasoning ability and achieving breakthroughs in model performance. Additionally, in the optimization of cross-modal capabilities, large models have shown a continuous improvement trend in their cross-modal representation and association modeling abilities for multimodal data such as text and images. For example, the GILL model [36] can generate coherent multimodal outputs based on arbitrary interleaved images and text inputs and outperforms baseline generation models in handling longer and more complex language generation tasks.

3.1.3 Open-source trend. As the industry develops, the number of entities adopting open-source strategies in technology development enterprises is showing a continuous upward trend. They stimulate innovation and transformation by revealing the underlying logic of public projects and expand unlimited possibilities through open cooperation. For instance, Google has made its Gemma 2 model open source [34], ofering two versions with parameter quantities of 9B and 27B, providing convenience for users for secondary development. The DeepSeek technology team has also opened up the DeepSeek-R1 large model and related distillation models in 2025, allowing users to conduct distillation and commercial use.By adopting open-source and free strategies, organizations can boost technical performance, where this approach enables low-cost col laboration that drives model innovation and speeds up local deployment. Moreover, the integration of open-source models into various fields facilitates broad industrial transformation and new economic growth. As the Financial Times puts it, the open-source initiative of the DeepSeek team continues the spirit of Gutenberg’s printing press [33], the proactive open-source measures have broken the technological monopoly and promoted the process of artificial intelligence large models shifting from oligarchic games to mass innovation. In summary, project open-source has become a trend, and it may continue to drive its breakthroughs and achievements.

## 3.2 Analysis and Assessment of AIGC Risks and Construction of Model

AIGC utilizes advanced generative models to generate various multimodal content such as text, images, and audio, significantly enhancing the eficiency of content creation and expanding the scope of creation. However, its application also brings multi-dimensional risks and challenges, covering aspects such as technology, ethics, and employment. Therefore, this paper proposes a three-level ap plication risk transmission model (as shown in Figure 4), aiming to start from the breadth and depth of influence, using a hierarchical analysis framework to systematically introduce and analyze the application dilemmas and risks of AIGC, forming a systematic thinking and examination dimension from problem classification and solution to system-wide governance, and determining the goals and orientations for the governance of AIGC applications.

3.2.1 Technical botleneck. As shown in Figure 4, at the top of the inverted pyramid are the technical bottleneck limitations. These types of problems are among the first to emerge within the industry at that stage. With the deepening of research on AIGC-related technologies, the lack of systematic solutions for these problems will lead to their ripple efects extending beyond a single application field such as academic research and commercial applications, presenting cross-disciplinary and multi-level impacts. The systematic radiation efect at the top level will be vertically transmitted to the downstream levels, transmitting application risks and giving rise to certain negative efects at the social level.

Training cost barrier. The cost barrier constitutes a significant technical bottleneck for AIGC technology. According to the law of scaling [35], which posits that larger models exhibit stronger performance, enterprises must invest substantial funds to stimulate the emergent abilities [40] of large-scale models. The Artificial Intelligence Index Report 2024 [39] highlights that training costs for large models have reached unprecedented heights, approximately 78 million USD were expended on GPT-4, while the Gemini Ultra model required up to 191 million USD for performance enhancement. Although the DeepSeek-R1 model reduces resource demands, supervised datasets remain necessary during pre-training, incurring non-negligible costs.

At the same time, this cost barrier also hinders new startups from entering this industry. The large-scale investment in training funds has concentrated on the research and development and deployment of large models in the leading enterprises of this industry, while small research institutions and enterprises will be marginalized [41]. According to the Theory of Contestable Markets [42], only by continuously lowering the threshold of training cost can the eficiency of the market be further improved and the resource allocation be optimized.

Environmental energy consumption. Furthermore, the model training process illustrated in Figure 4 imposes a significant constraint on AIGC development due to its adverse environmental impact. The training and inference of large language models (LLMs) consume substantial energy, resulting in considerable carbon and water footprints with profound environmental consequences [48]. For example, Google’s data centers consumed nearly 24 billion liters of water in 2023 [44], approximately six times that of Meta’s data centers during the same period (3.881 billion liters) [47]. In response, Zhaojian Yu et al. [50] proposed the OpenCarbonEval framework to predict model carbon emissions, thereby contributing to the sustainable development of AI technologies and ecological practices. Additionally, Wang Yuntao et al. [49] introduced the concept of integrating collaborative cloud-edge computing, energy-saving innovations, and AIGC algorithms to design a green AIGC architecture aimed at reducing carbon emissions throughout the lifecycle.

Data noise. The training dataset serves as one of the fuels for the model, and while it enhances the model’s performance, its potential drawbacks are gradually becoming apparent. The massive raw data contains a great deal of noise, so large models trained based on such data have the possibility of performance deviations due to noise interference. Particularly, for some adversarial examples with subtle noise in the dataset [51], deep neural networks are highly prone to misclassifying this data, thereby negatively afecting the robustness of the large model in critical environments. Additionally, due to the characteristics of the storage of large model parameters, even after manual fine-tuning, their outputs based on the incorrect probability distribution between words may further expose the existing biases and discrimination phenomena in the data [45], ultimately causing distortions in user value orientation and generating public cognitive biases.

![](images/2e33a0dbee8a18d8d77123c2f71cfe8b41bc25c98d66bb3a228d057057989dae.jpg)  
Figure 4: Three-tier risk transmission model for AIGC applications

3.2.2 Information ethics issues in risk transmission application. Despite the fact that the application of AIGC technology still faces several obstacles, as shown in Figure 4, the technical bottlenecks have led to the emergence of false content generation and disputes over the ownership of privacy and copyright, which in turn have become the key issues restricting the deep popularization and com mercialization of AIGC.

Spread of false information. The characteristic of large models generating content based on the probability distribution of tokens leads to them sometimes outputting fabricated facts or misleading texts [56], thereby causing users to develop cognitive biases. Specif ically, generative AI will exhibit factual hallucinations and faithful hallucinations during the process of generating new content. Factual hallucinations refer to the content output by the large model that contradicts objective facts, while faithful hallucinations can be generally understood as the output of the large model not matching the context content. Both types of hallucinations will mislead users decisions, resulting in a decline in the credibility of the large model. In addition, apart from the large model possibly fabricating content based on the probability distribution of tokens, the large model can also be deliberately generated with false content by those with ul terior motives, namely the problem of Deepfake abuse. In February 2024, a fraud group used this technology in combination with the public information of a Hong Kong multinational company to use Deepfake to forge the image and voice of the senior management of the company’s British headquarters and defraud the financial staf of 200 million Hong Kong dollars [53]. This behavior seriously violated personal portrait rights and the property security of the enterprise and caused negative social impacts.

Information Privacy Rights Issue. The large-scale datasets used to support the training of large models may violate users’ privacy rights regarding personal information, namely the issue of training data infringement [3]. During the interaction with users, the data obtained by Machine Learning as a Service (MLaaS) may be used by developers as the training data for the next round of large models, thereby posing a risk of exposing users’ personal data. For example, ChatGPT uses this type of interaction data to fine-tune the large model and further improve the service [54]. At the same time, in some cases, attackers can induce the large model to output sensitive information from the external retrieval database of Retrieval-Augmented Generation (RAG) technology [61], which also poses a severe challenge to information privacy protection.

Disputes over the copyright of generated content. Controversy persists within the industry concerning copyright ownership of content generated by generative AI (GAI). If the data employed to train generative AI lacks authorization, the intellectual property status of the generated content becomes ambiguous, potentially constituting copyright infringement of the original authors. For instance, The New York Times sued OpenAI over allegations of "massive copyright infringement" in the training of GPT, asserting that its training processes violated the copyright of Times articles [52]. Consequently, the questions of whether AI can be considered an original author and whether the generated content possesses uniqueness remain central issues in ongoing social debates [59].

Response to Information Ethics Risks. To address the aforementioned risks, an actionable protection system should be constructed at the technical level. Firstly, the watermarking technology [58] can embed invisible identifiers in AI-generated text, images, and videos, enhancing the ability to trace the content and curbing malicious applications such as deepfake. Research institutions like OpenAI and Google DeepMind have integrated such watermarking mechanisms into their generation models for subsequent content identification and platform review. Secondly, diferential privacy [61] provides mathematical guarantees for data usage, enabling the reduction of the risk of individual information being inferred while maintaining the eficiency of data analysis. Many technology enterprises have deployed diferential privacy algorithms in user behavior analysis, advertising placement, and recommendation systems, thereby ensuring data value while safeguarding user privacy rights. In summary, these technical measures can provide a fundamental ethical defense throughout the entire process of AIGC applications.

At the policy and governance level, it is necessary to leverage existing regulations and norms to form a synergy, ensuring the compliance and transparency of AIGC technology development and application. The Chinese Personal Information Protection Law [57] establishes legal boundaries in data processing and cross-border transmission, providing a legal basis for data governance and user rights protection of AIGC systems. Only by integrating technical means with policy regulations can we fundamentally promote the implementation of AIGC information ethics governance from macro principles to practical operational levels.

3.2.3 The employment issues arising from AIGC. Currently, the impact of AIGC technology on employment remains confined to specific sectors within the social system. However, as technical bot tlenecks are addressed and ownership disputes evolve across stages, the hierarchical transmission mechanism shown in Figure 4 is expected to intensify AIGC driven impacts on employment through a dynamic pathway that begins with early signals, spreads through transmission, and culminates in amplified efects. Consequently, the associated risks and impacts warrant serious consideration.

Overall, the AIGC industry has been profoundly transforming the labor market, and the labor force transformation has become an inevitable trend. The McKinsey Company report [55] shows that the rise of AIGC stimulates changes in the labor demand pattern, and by 2030, up to 30% of working hours can be replaced or saved by AI automation. Daron Acemoglu [62] proposed in The Theory of Wages [66] that technological change not only has a bias but is also influenced by price efects and market size efects. Specifically, specific technological changes have a bias towards certain production factors, and the development and popularity of AIGC in the current stage are not only afected by price efects such as the reduction of software and hardware costs, but also by market size efects. Its widespread application will replace most low-skilled labor, promote the redistribution of social assets, exacerbate the technical bias distribution problem in the labor market [64], and generate significant wealth distribution efects.

3.2.4 Three-level risk transmission model: case mapping analysis. To enhance the practical relevance of this research model, a representative case of Deepfake abuse within the AIGC domain was selected for mapping analysis. Firstly, at the technical bottleneck level, despite advances in deep learning generation technologies such as GANs and difusion models that produce nearly indistinguishable faces and voices, detection mechanisms remain incomplete. Numerous open-source and commercial Deepfake tools lack a unified digital watermarking or source traceability mechanism, rendering source authentication highly challenging. Secondly, the application risk transmission pathway manifests as follows: upon obtaining original materials, perpetrators can easily generate synthetic videos of political figures or celebrities, which are rapidly disseminated via social media and community channels. For instance, a fraud group exploited this technology to impersonate senior managers of a Hong Kong multinational corporation, facilitating fraudulent transfers and resulting in substantial financial losses. Due to limited risk management expertise among managers and the deliberate circumvention of platform reviews by some perpetrators, Deepfake content often spreads unchecked, accelerating the transition from technical vulnerabilities to broader social risks. Finally, at the social impact level, Deepfake abuse substantially undermines public trust in video evidence. By forging faces and voices of acquaintances or authoritative figures, it enables fraud via videos or phone calls, rapidly eroding trust in online audiovisual evidence. As real person images become unreliable, users struggle to verify authenticity when receiving remote requests from relatives or staf, leading to frequent financial fraud and significant harm. Furthermore, the exploitation of facial templates belonging to women, the elderly, and other vulnerable groups exacerbates psychological harm and financial losses, while amplifying a chain reaction of privacy violations, identity risks, and cyber violence on social networks, thereby further eroding social trust. In summary, the Deepfake abuse case exemplifies the logical progression of the three-stage mechanism including technical bottleneck, application risk transmission, and social impact, where it ofers targeted practical validation for the theoretical model proposed herein.

## 4 THE FUTURE RESEARCH PROSPECTS OF AIGC

Although the development of the AIGC industry is currently facing numerous risks and challenges, looking to the future, the prospects of this industry in the research and application fields remain broad. The future research directions can be divided into three stages based on the Technology Readiness Level (TRL): short-term (1-2 years), medium-term (2-4 years), and long-term (more than 5 years). In the short term, eforts should be focused on improving the controllable generation efect and establishing a multi-dimensional evaluation system in vertical domain applications to achieve practical implementation. In the medium term, attention should be given to the integration of diferent AI schools of thought, through the Hybrid Controllable Generation Framework and unified evaluation standards, to enhance the generation quality and logical interpretability. In the long term, the focus can be on building a model value system, introducing a value control module at the bottom and formulating quantitative evaluation indicators to ensure ethical compliance and social responsibility.

## 4.1 Widespread application in vertical fields

As a general-purpose technology with universal applicability, continuous improvement, and complementary innovation characteristics [64][65], GAI had the potential to combine with various industries to create greater commercial value from the very beginning of its development and is expected to become a strategic driving force for the next round of industrial transformation. Nowadays, GAI has gone beyond the fields of artistic creation, product design, and assisted learning [76] and has further developed towards multi-dimensional research-oriented applications:

In medical guidance, Cristobal Pais et al. [71] proposed using pharmacological knowledge to train the Claude model and integrating it into the innovative concept of the MEDIC system. This system improves the accuracy and eficiency of pharmacy operations by simulating the reasoning of pharmacists. In legal document extraction, Hannes Westermann et al. [72] demonstrated that multimodal

LLMs can assist in solving the information extraction problems faced by non-professionals when handling paper legal documents, providing a new direction for judicial acquisition tools. In the field of news media, Mingzhe Li et al. [69] integrated AIGC-related technologies to design the first multimodal task model Dual-Interactionbased Multi-modal Summarizer (DIMS), which handles both news video cover selection and text summary generation simultaneously, providing a new path for handling the semantic relationship between news text and video. In the financial field, Qianqian Xie et al. [73] proposed the PIXIU framework, including the first financial large language model FinMA that is fine-tuned through multi-task and multimodal instruction data, as well as related datasets and evaluation benchmarks, demonstrating its superior performance in financial tasks such as stock movement prediction.

![](images/dd8df71b0a1750984b30ef8b8fe86474d6948e7c3b69f5424569c8cedf20a26b.jpg)  
Figure 5: Challenges and risk intensity in high-risk AIGC applications

Although the aforementioned applications have demonstrated the great potential of AIGC, its application in practical scenarios still needs further optimization. Especially in diferent fields and complex scenarios, the instability of generated content has become the main bottleneck hindering its wider and deeper popularization. For instance, the diagnostic accuracy of medical reports has not reached the application requirements, making it impossible to be put into practical use. The generalization ability ofnews multimodal models for complex data is still limited. To address these challenges, in the short term (1-2 years, TRL 4-5), future research should focus on optimizing controllable generation technology and building a multi-dimensional evaluation system to improve the accuracy and domain applicability of generated content.

Furthermore, for high-risk fields such as finance, healthcare, and law, the challenges posed by the application of AIGC technology are particularly unique. As illustrated in Figure 5, it imposes higher requirements on data privacy, model interpretability, compliance, and ethical issues. In the healthcare sector, due to the sensitivity of patient data and the possibility that AIGC misdiagnosis could endanger patients’ lives, its application faces extremely high risks. Therefore, it occupies the largest proportion of risk assessment. The financial sector follows, with its strict compliance requirements and protection of financial data privacy remaining the main obstacles to the application of AIGC technology. This is quite diferent from the general AIGC domain, which is widely applied, has a higher tolerance for errors, and has a relatively relaxed regulatory environment. Therefore, advancing AIGC requires iterative model design, expert knowledge, regulatory compliance, and transparent algorithms to ensure safe, fair, and reliable applications.

In conclusion, the future application of AIGC in vertical fields will rely on the continuous breakthroughs of controllable generation technology and the improvement of diversified evaluation systems, continuously enhancing the professionalism, accuracy, and practical value of content generation, and promoting the intelligent development of the industry to a new height.

## 4.2 The Ideas of the Artificial Intelligence School: Continuous Integration

At present, AIGC integrates concepts and technologies from diverse schools, including connectionism and behaviorism, to enhance performance. In the future, it is expected to continue integrating and innovating with concepts from other paradigms. Studying human brain intelligence through an integrative paradigm has become a consensus within cognitive science and AI [74]. Despite their distinct strengths across diferent tasks, the integration of symbolic, statistical, deep, and reinforcement learning methods is still exploratory.

In the medium-term stage (2-4 years, TRL 5-7), under the multiparadigm joint modeling framework, for specific generation tasks, a mixed controllable generation module can be introduced to achieve fine control of the content. By integrating multiple paradigms such as neural networks, symbolic logic, knowledge graphs, and physical simulation, for example, neuro-symbolic AI (Neuro-Symbolic AI) [67][63], structured knowledge and process constraints can be injected into the generation model, significantly improving the reliability, interpretability, and diversity of complex tasks. Logical support can be provided through symbolic reasoning, where reliable control of the generated content can be achieved through constraint sampling and prompt engineering, balancing model flexibility and output quality, laying the foundation for applications in fields such as medical reports, intelligent manufacturing, and financial risk control.

Future research directions should focus on standardization and interoperability of interfaces between paradigms, exploring multiobjective joint optimization and trade-of mechanisms, and improving the interpretability and traceability of generation models. Additionally, for diferent fields, an evaluation system and public benchmark covering reliability, logical consistency, and interpretability indicators need to be constructed to support the integration of AIGC technology school ideas and the realization of controllable generation technology from concept validation to industrialization implementation. Combined with edge, cloud and local collaboration solutions, the actual efects can be tested in pilot projects.

## 4.3 Construction of the model’s value system

As large models permeate diverse societal domains, ethical risks, bias concerns, and security hazards have become increasingly salient. Currently, both academic and industrial communities are increasingly focusing on value systems. However, a unified solution has yet to emerge.

Research by Liyuan Lu et al. [70] indicates that the values em bedded in large models vary according to the enterprises’ national and socio-cultural backgrounds. These value discrepancies may arise from factors including training data diversity and developers’ design preferences. However, specific causes remain underexplored. At the architectural level, assessments of human cognitive tendencies towards large models predominantly focus on surface-level interaction analysis, neglecting deeper exploration of the mechanisms underlying value formation. Moreover, at the output level, large models currently tend to produce content that contravenes moral and ethical standards, largely due to training data deficien cies and other factors, underscoring the urgent need for a robust value system.

In the long-term phase (beyond five years, TRL 7–8), research should prioritize optimizing model architectures to establish a value system aligned with universal human principles. In terms of model development, it is advisable to explore embedding a value control module within the model infrastructure. For instance, LLM4QA has demonstrated how a large language model can be harnessed to perform eficient knowledge-graph reasoning via SPARQL queries, suggesting that similar mechanisms could be extended to enforce value constraints at inference time [75]. Jiaming Ji et al. [68] developed the Align Anything multimodal alignment framework, trained on multimodal human preference data (align-anything-200k) and optimized via a loop of generate, evaluate and regenerate, significantly enhancing the command-following capability of multimodal large models. This framework can be extended to encompass the value dimension by integrating ethical constraints between symbolic rules and neural networks, enabling bias suppression, realtime interception of sensitive topics, and compliance prompting, where it dynamically corrects inappropriate content and enhanccs the ethical and legal reliability of model outputs.

Regarding model evaluation, as values are dificult to define by a unified standard and human feedback is inherently biased, value assessment criteria remain under development and require urgent refinement. Researchers are thus encouraged to construct more inclusive evaluation systems by integrating cross-cultural value datasets, multilingual data, and regionally diverse feedback. Moreover, recent benchmarks on retrieval-augmented generation such as evaluations of open-source LLMs on code-switched Tagalog English tasks, which highlight the importance of testing on linguistically and culturally varied corpora to stress-test both factuality and value alignment [77]. Additionally, the use ofautomated evaluation tools, such as statistical and machine learning based sentiment and semantic analysis, may help mitigate human subjectivity in evaluation.

In summary, researchers need to attach importance to the continuous research in this field to promote the optimization and iteration of large models, and jointly construct AGI that conforms to human morality, providing support for technological breakthroughs and social well-being.

## 5 CONCLUSION

Based on a staged review of AI evolution, this study synthesizes representative models and architectures, including DBN, Transformer, difusion models, and the DeepSeek family, and summarizes two current industry shifts, hardware upgrades and the move toward open-source ecosystems. By combining application cases with a three-level risk transmission model, the analysis clarifies how technical and industrial factors interact to shape practical risks, with particular attention to training cost pressures, energy consumption, training data noise, and information ethics challenges. A case study on deepfake abuse further demonstrates the model’s explanatory value in tracing risk emergence, propagation, and amplification.

Looking ahead, this study integrates the maturity of controllable generation techniques and evaluation standards to outline research priorities across diferent time horizons. Three futuristic directions are highlighted, expanding vertical domain applications, integrating academic paradigms, and constructing model value in a way that aligns technical progress with governance needs. Overall, this review consolidates the evolution of AIGC, identifies its key benefits and deployment bottlenecks, and provides a structured reference for both future research and responsible development.

## References

[1] Cao, Y., Li, S., Liu, Y., Yan, Z., Dai, Y., Yu, P. S., and Sun, L. 2025. A survey of AI-generated content (AIGC). ACM Computing Surveys 57, 5, 1–38. 16

[2] Goodfellow, I. J., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair, S., Courville, A., and Bengio, Y. 2014. Generative adversarial nets. In Proceedings ofthe 27th International Conference on Neural Information Processing Systems (NIPS’14), Montreal, Canada, Dec 8–13. MIT Press, 2672–2680. 49

[3] Hacker, P., Engel, A., and Mauer, M. 2023. Regulating ChatGPT and other large generative AI models. arXiv preprint. Retrieved Apr. 5, 2025 from https://doi.org/ 10.48550/arXiv.2302.02337.

[4] McCulloch, W. S. and Pitts, W. H. 1943. A logical calculus of the ideas immanent in nervous activity. Bulletin ofMathematical Biology 5, 4, 115–133.

[5] Rosenblatt, F. 1958. The perceptron: A probabilistic model for information storage and organization in the brain. Psychological Review 65, 6, 386–392.

[6] Rumelhart, D. E., Hinton, G. E., and Williams, R. J. 1986. Learning representations by back-propagating errors. Nature 323, 6088, 533–536.

[7] LeCun, Y., Boser, B., Denker, J. S., Henderson, D., Howard, R. E., Hubbard, W., and Jackel, L. D. 1989. Backpropagation applied to handwritten zip code recognition. Neural Computation 1, 4, 541–551.

[8] Hinton, G. E., Osindero, S., and Teh, Y. W. 2006. A fast learning algorithm for deep belief nets. Neural Computation 18, 7, 1527–1554.

[9] Goodfellow, I. J., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair, S., Courville, A., and Bengio, Y. 2014. Generative adversarial nets. In Proceedings ofthe 27th International Conference on Neural Information Processing Systems, Montreal, Dec 8–13, 2014. Cambridge: MIT Press, 2672–2680.

[10] Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Kaiser, Ł., Gomez, A. N., Polosukhin, I., and Jones, L. 2017. Attention is all you need. In Proceedings ofthe 31st International Conference on Neural Information Processing Systems, Long Beach, Dec 4–9, 2017. Red Hook: Curran Associates, 5998–6008.

[11] Ho, J., Jain, A., and Abbeel, P. 2020. Denoising difusion probabilistic models. In Proceedings ofthe 34th Conference on Neural Information Processing Systems, Virtual, Dec 6–12, 2020. 6840–6851

[12] DeepSeek-AI, Guo, D., Yang, D. J., et al. 2025. DeepSeek-R1: incentivizing reasoning capability in LLMs via reinforcement learning. Technical Report. Retrieved Apr. 5, 2025 from https://github.com/deepseek- ai/DeepSeek-R1/blob/main/DeepSeek\_R1.pdf.

[13] Huang, P. 2025. Risk types and legal regulation of training data for large AI models. Political Science and Law Review 1, 23–37. 2

[14] Ackley, D. H., Hinton, G. E., and Sejnowski, T. J. 1985. A learning algorithm for Boltzmann machines. Cognitive Science 9, 1, 147–169.

[15] Hinton, G. E. 2002. Training products of experts by minimizing contrastive divergence. Neural Computation 14, 8, 1771–1800.

[16] Iofe, S. and Szegedy, C. 2015. Batch normalization: Accelerating deep network training by reducing internal covariate shift. In Proceedings ofthe 32nd International Conference on Machine Learning (ICML’15), Lille, France, Jul 6–11. PMLR, 448–456.

[17] Kingma, D. P. and Welling, M. 2014. Auto-encoding variational Bayes. In Proceedings of the 2nd International Conference on Learning Representations (ICLR’14), Banf, Canada, Apr 14–16. arXiv, 14.

[18] Sohl-Dickstein, J., Weiss, E. A., Maheswaranathan, N., and Ganguli, S. 2015. Deep unsupervised learning using nonequilibrium thermodynamics. In Proceedings of the 32nd International Conference on Machine Learning (ICML’15), Lille, France, Jul 6–11. JMLR.org, 2256–2265.

[19] Sutskever, I., Vinyals, O., and Le, Q. V. 2014. Sequence to sequence learning with neural networks. In Proceedings ofthe 27th International Conference on Neural Information Processing Systems (NIPS’14), Montreal, Canada, Dec 8–13. MIT Press, 3104–3112.

[20] Zhang, R., Li, W., and Mo, T. 2018. A survey on deep learning. Information and Control 47, 4, 385–397.

[21] Zhou, F., Jin, L., and Dong, J. 2017. Survey on convolutional neural networks. Journal ofComputer Science and Technology 40, 6, 1229–1242.

[22] Dai, D., Deng, C., Zhao, C., et al. 2024. DeepSeekMoE: Towards ultimate expert specialization in mixture-of-experts language models. In Proceedings ofthe 62nd Annual Meeting ofthe Association for Computational Linguistics (ACL’24), Bangkok, Thailand, Aug 11–16. Association for Computational Linguistics, 1280– 1297.

[23] DeepSeek-AI, Al, B., Bei, F., et al. 2024. DeepSeek-V3 technical report. Technical Report. Retrieved Apr. 5, 2025 from https://github.com/deepseek-ai/DeepSeek-V3.

[24] Fedus, W., Zoph, B., and Shazeer, N. 2022. Switch transformers: Scaling to trillion parameter models with simple and eficient sparsity. Journal of Machine Learning Research 23, 1–39.

[25] Gloeckle, F., Idrissi, B. Y., Rozière, B., et al. 2024. Better & faster large language models via multi-token prediction. In Proceedings ofthe 41st International Conference on Machine Learning (ICML’24), Honolulu, HI, Jul 21–27. PMLR, 15706–15734.

[26] Jacobs, R. A., Jordan, M. I., Nowlan, S. J., et al. 1991. Adaptive mixtures of local experts. Neural Computation 3, 1, 79–87.

[27] Lepikhin, D., Lee, H., Xu, Y., et al. 2021. GShard: Scaling giant models with conditional computation and automatic sharding. In Proceedings of the 9th International Conference on Learning Representations (ICLR’21), Virtual Event, May 3–7. OpenReview.

[28] Radford, A., Metz, L., and Chintala, S. 2016. Unsupervised representation learning with deep convolutional generative adversarial networks. In Proceedings ofthe 4th International Conference on Learning Representations (ICLR’16), San Juan, Puerto Rico, May 2–4. arXiv:1511.06434.

[29] Shao, Z., Wang, P., Zhu, Q., et al. 2024. DeepSeekMath: Pushing the limits of mathematical reasoning in open language models. arXiv preprint. Retrieved Apr. 5, 2025 from https://arxiv.org/abs/2402.03300.

[30] Zhai, Y. and Li, J. 2022. Reflections on the development path of AIGC: New opportunities in the popularization of large model tools. Internet World 11, 22–27.

[31] Zhang, H. 2025. How DeepSeek-R1 was developed? Journal of Shenzhen University (Science and Technology Edition). Retrieved Apr. 5, 2025 from https://link.cnki.ne t/urlid/44.1401.N.20250210.1628.002.

[32] Chen, Y. 2023. Beyond ChatGPT: Opportunities, risks and challenges of generative AI. Journal ofShandong University (Philosophy and Social Sciences) 3, 127–143.

[33] Financial Times. 2025. DeepSeek’s success will undermine the US-China tech war. Online Article. Retrieved Apr. 5, 2025 from https://www.ft.com/content/3549cc33- e04d-41da-8c58-525d5bb2ba4c.

[34] Google. 2025. Gemma 2 is now available to researchers and developers. Technical Announcement. Retrieved Apr. 5, 2025 from https://blog.google/technology/dev elopers/google-gemma-2/.

[35] Kaplan, J., McCandlish, S., Henighan, T., et al. 2020. Scaling laws for neural language models. arXiv preprint. Retrieved Apr. 5, 2025 from https://arxiv.org/ab s/2001.08361.

[36] Koh, J. Y., Fried, D., and Salakhutdinov, R. R. 2023. Generating images with multi modal language models. In Advances in Neural Information Processing Systems 36 (NeurIPS’23), New Orleans, LA, Dec 10–16. Curran Associates, 21487–21506.

[37] NVIDIA. 2022. NVIDIA H100 Tensor Core GPU Architecture Overview: WHITEPAPER-08949-001\_v10.2. Technical Report. Santa Clara: NVIDIA. Re trieved Apr. 5, 2025 from https://resources.nvidia.com/en-us-tensor-core/gtc22- whitepaper-hopper.

[38] Smith, E. 2024. Google Cloud TPU v6e Trillium Shown at SC24. Online Article. Retrieved Apr. 5, 2025 from https://www.servethehome.com/google-cloud-tpuv6e-trillium-shown-at-sc24/.

[39] Stanford University. 2024. Artificial intelligence index report 2024. Research Report. Stanford, CA. Retrieved Apr. 5, 2025 from https://aiindex.stanford.edu/r eport/.

[40] Wei, J., Tay, Y., Bommasani, R., et al. 2022. Emergent abilities of large language models. Transactions on Machine Learning Research.

[41] Wen, X., Zhang, C., Guo, R., et al. 2024. Challenges and recommendations for building open source innovation ecosystem for large-models in China. Bulletin of Chinese Academy of Sciences 39, 8, 1313–1326.

[42] Baumol, W. J. 1982. Contestable markets: An uprising in the theory of industry structure. American Economic Review 72, 1, 1–15.

[43] Chen, C. and Zhang, M. 2023. Data determinism? Ethical issues in AIGC. Journalism and Writing 4, 15–23.

[44] Google. 2024. 2024 Environmental Report: Carbon Emissions and AI Development. Technical Report. Mountain View, CA: Google Sustainability. Retrieved Apr. 5, 2025 from https://sustainability.google/reports/google-2024-environmentalreport/.

[45] Huang, P. 2024. Challenges and risk regulation of generative AI in personal information protection. Modern Law Science 46, 4, 101–115.

[46] Jiazi Guangnian. 2024. 2024 open-source large model ecosystem research report. Technical Report. Retrieved Apr. 5, 2025 from https://runwise.co/245861.html.

[47] Meta. 2024. 2024 Sustainability Report: Water and Energy Consumption in Data Centers. Technical Report. Menlo Park, CA: Meta Sustainability. Retrieved Apr. 5, 2025 from https://sustainability.atmeta.com/2024-sustainability-report/.

[48] Rillig, M. C., Ågerstrand, M., Bi, M., et al. 2023. Risks and benefits oflarge language models for the environment. Environmental Science & Technology 57, 9, 3464–3466.

[49] Wang, Y., Pan, Y., Yan, M., et al. 2023. A survey on ChatGPT: AI-generated contents, challenges, and solutions. IEEE Open Journal ofthe Computer Society 4, 280–302.

[50] Yu, Z., Wu, Y., Deng, Z., et al. 2024. OpenCarbonEval: A unified carbon emission estimation framework in large-scale AI models. arXiv preprint. Retrieved Apr. 5, 2025 from https://arxiv.org/abs/2405.12843.

[51] Yuan, X., He, P., Zhu, Q., et al. 2019. Adversarial examples: Attacks and defenses for deep learning. IEEE Transactions on Neural Networks and Learning Systems 30, 9, 2805–2824.

[52] Browne, R. 2023. The New York Times sues Microsoft, ChatGPT maker OpenAI over copyright infringement. Online Article. CNBC. Retrieved Apr. 5, 2025 from https://www.cnbc.com/2023/12/27/new-york-times-sues-microsoft-chatgptmaker-openai-over-copyright-infringement.html.

[53] Chen, X. 2024. Shocking! "Face-Changing" Impersonates CFO, Defrauds Two Billion! Details of Hong Kong’s Largest AI Scam Exposed. Online Article. Securities China. Retrieved May 9, 2025 from https://mp.weixin.qq.com/s?\_\_biz=MzA3NjM 5MjIwOQ==&mid=2652131382&idx=1&sn=f23751b5d507be6d1227f98a74dd34 5f.

[54] Harbin Institute of Technology Natural Language Processing Research Institute. 2023. ChatGPT research report. Technical Report. Retrieved Apr. 5, 2025 from https://www.modb.pro/doc/110341

[55] Hazan, E., Madgavkar, A., Chui, M., et al. 2024. A new future of work: The race to deploy AI and raise skills in Europe and beyond. Research Report. McKinsey & Company.

[56] Huang, L., Yu, W., Ma, W., et al. 2024. A survey on hallucination in large language models: Principles, taxonomy, challenges, and open questions. ACM Transactions on Information Systems 1, 1, Article 1.

[57] Personal Information Protection Law of the People’s Republic of China. 2021. Legal Document. Retrieved Jun. 3, 2025 from http://www.gov.cn/xinwen/2021- 08/20/content\_5632486.htm.

[58] Sharma, S., Zou, J. J. Q., Fang, G., et al. 2024. A review of image watermarking for identity protection and verification. Multimedia Tools and Applications 83, 31829–31891.

[59] Thorp, H. H. 2023. ChatGPT is fun, but not an author. Science 379, 6630, 313.

[60] Van Dis, E. A. M., Bollen, J., Zuidema, W., et al. 2023. ChatGPT: five priorities fo research. Nature 614, 7947, 224–226.

[61] Zeng, S., Zhang, J., He, P., et al. 2024. The good and the bad: exploring privacy issues in retrieval-augmented generation (RAG). arXiv preprint. Retrieved Apr. 5, 2025 from https://arxiv.org/abs/2402.16893.

[62] Acemoglu, D. 2002. Directed technical change. The Review of Economic Studies 69, 4, 781–809.

[63] Bougzime, O., Cruz, C., André, J.-C., et al. 2025. Neuro-symbolic artificial intelligence in accelerated design for 4D printing: Status, challenges, and perspectives. Materials & Design 252, 113737.

[64] Bresnahan, T. and Trajtenberg, M. 1995. General purpose technologies "engines of growth"? Journal of Econometrics 65, 1, 83–108.

[65] Crafts, N. 2021. Artificial intelligence as a general-purpose technology: An historical perspective. Oxford Review ofEconomic Policy 37, 3, 521–536.

[66] Hicks, J. R. 1963. The Theory of Wages (2nd ed.). London: Palgrave Macmillan.

[67] Hitzler, P., Eberhart, A., Ebrahimi, M., et al. 2022. Neuro-symbolic approaches in artificial intelligence. National Science Review 9, 6, nwac035. Retrieved Jun. 4, 2025 from https://doi.org/10.1093/nsr/nwac035.

[68] Ji, J., Zhou, J., Lou, H., et al. 2024. Align Anything: Training All-Modality Models to Follow Instructions with Language Feedback. arXiv preprint. Retrieved May 9, 2025 from arXiv:2412.15838.

[69] Li, M., Chen, X., Gao, S., et al. 2020. VMSMO: Learning to generate multimodal summary for video-based news articles. In Proceedings ofthe 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP’20), Online, Nov 16–20. Association for Computational Linguistics, 9360–9369.

[70] Lv, L., Li, Y., Wang, J., et al. 2025. Research on the values of large language models: Concept framework and empirical evaluation. Electronic Government 1, 15–28.

[71] Pais, C., Liu, J., Voigt, R., et al. 2024. Large language models for preventing medication direction errors in online pharmacies. Nature Medicine 30, 6, 1574– 1582.

[72] Westermann, H. and Savelka, J. 2024. Analyzing images of legal documents: Toward multi-modal LLMs for access to justice. In Proceedings ofthe AIfor Access to Justice Workshop, co-located with the 37th International Conference on Legal Knowledge and Information Systems (JURIX’24), Brno, Czechia, Dec 11.

[73] Xie, Q., Han, W., Zhang, X., et al. 2023. PIXIU: A large language model, instruction data and evaluation benchmark for finance. In Proceedings ofthe 37th International Conference on Neural Information Processing Systems (NeurIPS’23), New Orleans, LA, Dec 10–16. Curran Associates Inc., Article 1454, 16 pages.

[74] Zhang, B., Zhu, J., and Su, H. 2020. Toward the third generation of artificial intelligence. Scientia Sinica Informationis 50, 1281–1302.

[75] Lan, M., Xia, Y., Zhou, G., Huang, N., Li, Z., and Wu, H. 2024. LLM4QA: Leveraging large language model for eficient knowledge graph reasoning with SPARQL query. Journal ofAdvances in Information Technology 15, 10, 1157–1162.

[76] Zhang, Z., Zhang, J., Zhang, X., et al. 2025. A comprehensive overview of Generative AI (GAI): Technologies, applications, and challenges. Neurocomputing 632, 129645.

[77] Adoptante, A. J. M., Castro, J. A. D. V., Medrana, M. L. B., Ocampo, A. P. B., Peramo, E. C., and Miranda, M. R. M. 2025. Benchmarking open-source large language models on code-switched Tagalog-English retrieval augmented generation. Journal ofAdvances in Information Technology 16, 2, 233–242. https: //doi.org/10.12720/jait.16.2.233-242.