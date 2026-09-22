![](images/3dc5e119fc3fd64cf86ca832abcdfb50ace3f67ff43f64e05bb56e4c6facc29c.jpg)

# Detecting AI-generated essays using fine-tuned XLNet-CNN hybrid techniques: a study of the academic integrity challenge

Manish Prajapati<sup>1</sup> · Santos Kumar Baliarsingh<sup>1</sup> · Prabhu Prasad Dev<sup>1</sup>

Received: 22 January 2025 / Accepted: 11 November 2025 / Published online: 2 February 2026   
© The Author(s), under exclusive licence to Springer-Verlag GmbH Germany, part of Springer Nature 2026

## Abstract

The rapid advancement of large language models (LLMs) such as GPT-3 and GPT-4 has raised serious concerns for academic integrity, as AI-generated essays often bypass conventional plagiarism detection systems and threaten the credibility of student assessments. To address this challenge, we propose XLNet-CNN, a hybrid detection framework that combines XLNet (Generalized Autoregressive Pretraining for Language Understanding) with a convolutional neural network (CNN) for local feature extraction. Using the EnglishQA Essays Corpus containing 161,640 essays from both human and AI sources, we benchmark the model against representative machine learning, deep learning, and transformer-based baselines, as well as widely used external detection tools. The framework achieves accuracy 0.98, recall 0.96, F2 score 0.97, precision 1.00, BLEU (Bilingual Evaluation Understudy) 30.76, and perplexity (PPL) 3.99. Notably, it eliminates false negatives, ensuring that no AI-generated essay is misclassified as human-written, a critical safeguard for high-stakes academic contexts. These results demonstrate the efectiveness of hybrid architectures in capturing both semantic coherence and stylistic artifacts, ofering a reliable and scalable solution for maintaining fairness in academic evaluation while supporting responsible AI use in education.

Keywords AI-generated essays · Academic integrity · Text Detection · NLP tasks · Transformer · XLNet-CNN · Deep learning

## 1 Introduction

In recent years, large language models (LLMs) have advanced significantly, demonstrating the ability to generate text that closely resembles human writing. This progress has introduced new challenges in education, particularly with respect to academic integrity. A central concern is the growing use of LLMs by students to generate essays that appear authentic, thereby undermining the credibility of academic assessments. Since the release of ChatGPT, generative AI has become a mainstream phenomenon, attracting widespread adoption and raising urgent concerns about plagiarism and academic dishonesty [1, 2].

Evidence suggests that existing plagiarism detection systems are insuficient for this challenge. Yeadon [3] found that AI-generated short essays received very low plagiarism detection scores (1–2%) from widely used tools such as Turnitin and Grammarly. Some researchers even argue that eforts to distinguish AI- from human-generated text may be futile [4]. Yet, with universities continuing to rely on plagiarism detection rather than dedicated AI-detection frameworks, academic institutions face increasing risks to credibility and fairness [3].

Recent advancements in natural language processing (NLP), particularly with models such as GPT-3 and GPT-4 [5, 6], have been driven by unsupervised representation learning. Autoregressive (AR) models, which predict the next token in a sequence, and autoencoding (AE) models, which leverage masked token prediction, have provided high-quality pretrained embeddings. These developments have laid the groundwork for building robust detection models. A variety of machine learning and deep learning approaches have also been investigated for related classification tasks, including SVMs [7], CNNs [8], RNNs [9], LSTMs [10], BiLSTMs [11], and GRUs [12]. Hybrid methods such as CNN-LSTM [13] and CNN-Attention-LSTM [14] combine local feature extraction with sequential modeling, while pretrained Transformers, including BERT, RoBERTa [15], and XLNet [16] further enhance contextual understanding.

Despite these advances, detecting AI-generated text remains a dificult problem. Traditional plagiarism tools are not robust to rapidly evolving LLMs, and many detection systems sufer from high false-positive rates, unfairly penalizing genuine student work. This gap highlights the urgent need for methods that can capture both the statistical artifacts of machine-generated text and the nuanced semantic structures of human writing.

Motivated by this challenge, we explore a hybrid architecture that integrates XLNet’s autoregressive pretraining and bidirectional context modeling with the convolutional neural network’s ability to extract local features. The XLNet-CNN framework aims to provide educators with a reliable detection system that balances accuracy with fairness. By equipping institutions with tools that distinguish between student-written and AI-generated essays, our work seeks to preserve academic integrity while acknowledging the constructive potential of LLMs in education.

Our main contributions are as follows:

We propose XLNet-CNN, a hybrid model that combines XLNet’s pretrained contextual embeddings with CNN and LSTM layers.

The model captures both long-range dependencies and local textual features for improved detection accuracy.

We benchmark XLNet-CNN against widely used AI-detection tools (OpenAI Detector, GPTZero, DetectGPT, Copyleaks, Grammarly, Turnitin).

Performance is evaluated using precision, recall, and F2 score, emphasizing both accuracy and fairness.

● Our framework provides a transparent, practical, and adaptable solution to help educators distinguish between AI-generated and student-written essays.

The remainder of this paper is organized as follows: Sect. 2 reviews related literature, Sect. 4.1 describes the dataset, Sect. 3 presents the methodology, Sect. 4 discusses results and experimental setup, Sect. 5 outlines challenges and limitations, and Sect. 6 concludes with future research directions.

## 2 Related work

Research on detecting AI-generated text has grown rapidly with the rise of large language models (LLMs). Two influential studies shaped our approach: Gehrmann et al. [17] and Sadasivan et al. [18], which highlighted both statistical methods and practical challenges in detecting AI-written essays.

## 2.1 Development of language model

The evolution of language models has significantly transformed the field of NLP, enabling the extraction of meaningful insights from vast amounts of unstructured text. The evolution of NLP has been marked by significant milestones, transforming the way machines understand and interpret human language. Initially, NLP models relied on probabilistic approaches, focusing on learning word occurrence probabilities from vast document collections [19]. However, the introduction of Word2Vec in 2013 revolutionized the field by converting text into word embeddings, enabling various NLP tasks such as identifying semantically similar words [20]. Despite its groundbreaking impact, Word2Vec’s limitations in addressing polysemy and capturing contextual nuances became apparent, prompting further innovations [21].

In order to get over these restrictions, scientists looked into pretraining techniques and directed language models, which provide context-based dynamic word representations. This shift enabled more accurate and context-aware language understanding, as seen in the works [22, 23]. These advancements have paved the way for more sophisticated NLP models, capable of capturing the nuances of human language. A significant milestone in this evolution was the development of ELMo, which used a bidirectional LSTM (biLSTM) network to produce context-aware word representations, thus enhancing the handling of word meanings within diferent contexts [22]. The introduction of the Transformer architecture in 2017 [24] marked a breakthrough. This architecture, with its attention mechanism, excelled in managing long-term dependencies more efectively than LSTMs. Building upon this foundation, the Bidirectional Encoder Representations from Transformers (BERT) model was introduced in 2018 [25]. BERT’s bidirectional encoding approach significantly improved the model’s understanding of context and semantics.

The landscape of NLP has undergone a significant transformation with the advent of the Generative Pre-trained Transformer (GPT) model, introduced by OpenAI [26]. This pioneering architecture, focusing on the decoder component of the Transformer, has revolutionized the field by establishing new benchmarks and catalyzing the "pre-training and fine-tuning" paradigm. This paradigm has inspired a new generation of models, including BART [27], RoBERTa [28], and T5 [29], which have further refined the pre-training and fine-tuning approach, expanding its applicability to a wide range of tasks such as question answering, sentiment analysis, and named entity recognition. Recent breakthroughs in computational power and the availability of large datasets have given rise to LLMs, marking a significant departure from traditional language models [30]. Notably, GPT-3 [31] and GPT-4 [32] have demonstrated remarkable capabilities, redefining the interaction between AI and human users. ChatGPT, built on GPT-3 and GPT-4, has exhibited exceptional conversational abilities, setting a new standard for AI-driven dialogue systems. In contrast, LLaMA [33] has focused on enhancing eficiency and reducing resource consumption, making it an attractive option for diverse text generation tasks.

## 2.2 Evolution of prompting techniques in ChatGPT

Supervised learning has long been a staple in NLP, yet it heavily depends on having a suficiently labeled dataset. The emergence of prompt engineering, also known as prompt learning, has revolutionized the field of NLP by providing an innovative solution to the limitations imposed by traditional fine-tuning methods. This approach leverages the capabilities of LLMs, such as ChatGPT, to perform various NLP tasks without the need for extensive labeled data or gradient updates. By crafting specific task descriptions, known as prompts, researchers can guide the model to achieve remarkable results in zero-shot or few-shot settings [34–36]. ChatGPT, in particular, has been extensively explored for its potential in various domains, including healthcare and medical fields, due to its user-friendly interface and impressive ability to generate human-like text. Studies have demonstrated its efectiveness in scientific writing [37, 38], research topic generation [39, 40], and domain report translation [41]. However, despite its promise, challenges such as hallucinations, plagiarism, and research fabrication highlight the need for rigorous human oversight, careful consideration, and regulation [42, 43].

## 2.3 XLNet modeling method

The permutation-based AR modeling has been studied before in [44, 45], although with several important diferences in emphasis. XLNet is intended to allow AR language models to retain bidirectional context, while previous models concentrated on improving density estimation by incorporating an orderless inductive bias into the model. According to the technical details, XLNet does this by explicitly integrating the target location into the hidden state using a two-stream attention method, unlike previous permutation-based AR models that relied on implicit positional awareness in their MLP structures. Notably, for both orderless NADE and XLNet, the term orderless does not mean that the input sequence is randomly permuted; rather, it indicates that the model is capable of supporting various factorization orders for the distribution. Autoregressive denoising is a comparable idea in text generation [46], but it only acts in a given order.

## 2.4 Pre-trained embeddings and hybrid approaches

Early advances in NLP focused on pre-trained embeddings that capture semantic relationships between words. Word-2Vec [20] represented words in a continuous vector space, where semantic similarity corresponded to spatial proximity. This inspired hybrid models such as Word2Vec + CNN [47], which improved feature extraction, and LSTM-based models that integrated Word2Vec to better handle sequential dependencies. GloVe [48] extended this line of work by combining co-occurrence statistics with global vector representations, yielding compact and semantically rich embeddings. However, both Word2Vec and GloVe remain static, unable to handle polysemy or adapt to contextual variation [49, 50]. To address these limitations, recent research has integrated embeddings into hybrid architectures. XLNet [16], building on the Transformer framework [25], introduced a permutation-based autoregressive objective with two-stream attention. This design enables dynamic, contextsensitive representations while maintaining the strengths of autoregressive modeling. By bridging static embeddings and contextual modeling, such hybrid approaches demonstrate strong adaptability and are particularly useful for detecting subtle diferences between human- and AI-generated text.

## 3 Methodology

## 3.1 XLNet model

XLNet is a state-of-the-art NLP model that builds upon the Transformer architecture, introducing a generalized autoregressive pretraining method for language understanding. It addresses the limitations of previous models, such as BERT, by integrating bidirectional context learning with autoregressive pretraining, making it particularly efective for tasks like human and AI-generated essays detection. Detecting whether text has been generated by AI or written by a human has become increasingly relevant as large language models like GPT-3 and GPT-4 become more advanced. Traditional models like BERT provided strong contextual learning but had inherent limitations in handling autoregressive tasks, which are crucial for detecting nuanced diferences in text. XLNet addresses these gaps by combining the strengths of autoregressive language modeling with bidirectional context learning, making it a powerful tool for AI and human-generated text detection.

The core idea behind XLNet is to combine the strengths of AR language modeling and AE methods. While models like BERT use AE for learning bidirectional contexts, XLNet incorporates autoregressive features to model language by considering all permutations of the factorization order of input tokens.

## 3.1.1 Autoregressive language modeling

In the context of detecting AI-generated essays, we compare Autoregressive (AR) Language Modeling with BERT-style pretraining, as illustrated in the Figure. AR-based models (such as GPT) rely on a unidirectional probability distribution, where the probability of a token $y _ { t }$ is conditioned on the preceding words. This can be mathematically represented as (see the Eq. 1):

$$
\operatorname* { m a x } _ { \phi } \sum _ { t = 1 } ^ { T } \log q _ { \phi } ( y _ { t } | y _ { < t } ) = \sum _ { t = 1 } ^ { T } \log \frac { \exp \left( g _ { \phi } ( y _ { 1 : t - 1 } ) ^ { T } v ( y _ { t } ) \right) } { \sum _ { y ^ { \prime } } \exp \left( g _ { \phi } ( y _ { 1 : t - 1 } ) ^ { T } v ( y ^ { \prime } ) \right) }\tag{1}
$$

where $g _ { \phi } \big ( y _ { 1 : t - 1 } \big )$ is the hidden representation of the preceding sequence, and $v ( y )$ represents the token embedding. For AI-generated essays detection, AR models learn sequential dependencies, capturing statistical anomalies that often characterize AI-generated essays. These include repetitive patterns, unnatural token transitions, and over-reliance on high-frequency n-grams key indicators of AI-generated essays.

Conversely, BERT-based detection models use MLM, where some tokens are randomly masked and then predicted based on bidirectional context. This method is described mathematically as (see Eq. 2):

$$
\underset { \phi } { \operatorname* { m a x } } \sum _ { t = 1 } ^ { T } z _ { t } \log q _ { \phi } ( y _ { t } | \tilde { y } ) = \sum _ { t = 1 } ^ { T } z _ { t } \log \frac { \exp \left( G _ { \phi } ( \tilde { y } ) ^ { T } v ( y _ { t } ) \right) } { \sum _ { y ^ { \prime } } \exp \left( G _ { \phi } ( \tilde { y } ) ^ { T } v ( y ^ { \prime } ) \right) }\tag{2}
$$

where $z _ { t } = 1$ if $y _ { t }$ is masked, and $G _ { \phi } ( \tilde { y } )$ represents the learned hidden representation of the masked sequence ${ \tilde { y } } .$ Unlike AR models, BERT-style detectors leverage bidirectional context, making them efective at recognizing contextual inconsistencies and detecting subtle linguistic artifacts in AI-generated essays. Since LLMs often generate text that appears fluent but lacks deep discourse coherence, BERT-based models can highlight semantic and syntactic inconsistencies that diferentiate AI-generated text from human-written essays.

A major challenge in AI-text detection is handling inference-time discrepancies. BERT models introduce artificial [MASK] tokens, making the training environment diferent from real-world classification scenarios. On the other hand, AR models predict the next word naturally but struggle to capture global coherence. A hybrid detection approach combining AR-based sequential dependency learning with BERT-style bidirectional context modeling can improve classification accuracy by leveraging both local statistical cues and broader linguistic structures present in AI-generated essays.

## 3.1.2 Permutation language modeling

XLNet presents a permutation-based training objective in contrast to models such as BERT, which employ a masked language modeling (MLM) objective. Maximizing the chance of a sequence under every feasible variation of the token order is the main concept. Given an input sequence $x = ( x _ { 1 } , x _ { 2 } , . . . , x _ { n } )$ , XLNet considers a random permutation of the sequence $z = ( z _ { 1 } , z _ { 2 } , . . . , z _ { n } )$ , where each $z _ { i }$ represents a reordering of tokens. The probability of each token $x _ { z _ { t } }$ is conditioned on its preceding tokens in the permutation (see Eq. 3):

$$
P ( x _ { z _ { t } } | x _ { z _ { 1 } } , . . . , x _ { z _ { t - 1 } } )\tag{3}
$$

This objective enables XLNet to capture dependencies in multiple directions, giving it a richer understanding of context a critical aspect for detecting subtle inconsistencies in AI-generated essays compared to human writing.

Permutation language modeling is a technique used by XLNet, a state-of-the-art pre-trained language model. This approach is diferent from traditional autoregressive models, such as GPT, which predict the next word in a sequence based on the previous words. Instead, XLNet generates predictions by considering all possible permutations of the input sequence, allowing it to learn bidirectional context while maintaining autoregressive concepts.

Figure 1 illustrates XLNet’s Permutation Language Modeling, where multiple permutations of input tokens are created to predict the context. It incorporates memory states for better context representation. For example, given the sequence $S = [ X 1 , X 2 , X 3 , X 4 ]$ , permutations like $[ 3  2  4  1 ]$ are modeled. Each token (X3) generates hidden states $( h _ { 3 } ^ { ( 1 ) } , h _ { 3 } ^ { ( 2 ) } )$ based on memory and surrounding tokens. This bidirectional approach enhances understanding by learning dependencies from all directions, improving over traditional language modeling.

Key concept: In permutation language Modeling, the model doesn’t strictly follow a left-to-right or right-to-left

Fig. 1 The illustration depicts the XLNet Permutation Language Modeling approach, showcasing forward factorization and multiple factorization orders. The permutation of token sequences enables bidirectional context learning by modeling all possible factorization orders $( 3  2  4  1 ,$ 2 4 3 1, etc.). Each factorization order processes token dependencies using memory layers (Memory-0, Memory-1) and computes hidden states $( \tilde { h } _ { t } ^ { ( 1 ) } , h _ { t } ^ { ( 2 ) } )$ for a target token $( X _ { 3 } )$ . The example demonstrates how this mechanism allows XLNet to leverage the benefits of both autoregressive models and bidirectional contexts for enhanced performance in natural language understanding tasks

![](images/8e5f3ea641064161fb723ca5f8389969b9abfbddf7205223e7e59000ac89d41b.jpg)

order of word predictions. Equation 4 Instead, it randomly permutes the order in which the words are predicted, allowing the model to learn dependencies across the entire sequence. This approach leads to a deeper understanding of context because the model learns not just to predict the next word, but also to understand relationships between words that appear at diferent positions within the sequence. For example, consider a sentence like "This is a KIIT." XLNet might randomly permute the positions of the words in the sequence and then predict each word based on its surrounding context. The number of possible permutations is calculated as the factorial of the sequence length (for a sentence with four words, the number of permutations is 4! = 24).

Why permutation?: The advantage of permutation over a fixed order (like left-to-right in GPT) is that it allows XLNet to capture more diverse contextual relationships in the text. This model retains the benefits of autoregressive models, where each word is conditioned on others, but it also incorporates the strength of bidirectional models (like BERT), where the context of each word can come from both its left and right.

For a sentence of length S, the number of permutations P(S) is computed as (see Eq. 4):

$$
P ( S ) = S ! = S \times ( S - 1 ) \times ( S - 2 ) \times . . . \times 1\tag{4}
$$

For example, if $S = 4 .$ , the number of possible permutations is $P ( 4 ) = 4 \times 3 \times 2 \times 1 = 2 4$

Impact on Model Performance: This permutation-based approach allows XLNet to capture rich, context-aware representations of language, which often results in better performance on various NLP tasks like text classification, question answering, and, importantly, essay generation and detection. It balances the flexibility of autoregressive models with the bidirectionality of models like BERT, making XLNet particularly efective for complex language tasks.

## 3.1.3 XLNET: attention masks

XLNet uses an attention mask to control which tokens the model should attend to in a sequence, especially for padding tokens or any other tokens that should not contribute to the model’s understanding. The attention mask is particularly useful in tasks like essay generation, where you might need to focus on certain parts of the text (like the essay content) and ignore irrelevant parts (like padding or masked tokens).

Let’s walk through an example of how an attention mask works in the context of detecting AI-generated essays versus human-generated essays using XLNet. XLNet uses the attention mechanism to weigh the importance of diferent tokens in the input sequence. The attention mask plays a crucial role in controlling which tokens the model should focus on while processing input sequences. This is especially important when working with padded sequences. Figure 2 illustrates XLNet’s Attention Masking mechanism. For a sentence like "This is a KIIT," permutations of token order (e.g., [3  2  4  1]) are used to compute probabilities sequentially. Each token can only attend to previous tokens in the permutation order. Attention masks ensure this causality by marking which tokens can be attended (e.g., [0, 0, 1, 0] for Token 2). The mask matrix enforces this rule across the entire sequence, enabling bidirectional context learning without data leakage.

Fig. 2 XLNet’s Attention Masking mechanism enables bidirectional context learning by enforcing causal dependencies through permutation-based factorization orders. The attention mask matrix ensures each token attends only to permissible tokens in the given permutation, preserving context integrity during computation  
![](images/3770c76abd612618c8c035ada330c4cc4786734fdbad1fcbff1843ac3f496205.jpg)

In XLNet, the attention mask is a binary tensor that indicates which tokens should be attended to and which should be ignored. It typically has a shape of (batch\_size, sequence\_length), where each position holds a value of 1 if the corresponding token is real (not padding) and 0 if it’s padding. The attention mask ensures that padding tokens do not interfere with the model’s ability to focus on the actual content of the input text.

For example: if you have the sequence “This is a KIIT" and pad it to a length of 10 with zero-padding, the attention mask would look like this: [1, 1, 1, 1, 0, 0, 0, 0, 0, 0] Here, 1 indicates a token the model should pay attention to, and 0 indicates a padding token to ignore. The attention mask ensures that only the meaningful tokens are attended to during the computation of attention scores, avoiding bias from the padding.

Remark about Permutation: the objective proposed alters only the factorization order while maintaining the sequence order intact. This ensures the preservation of the original sequence order, utilizing the corresponding positional encodings for that order. A suitable attention mask within Transformers guarantees the proper permutation of the factorization order. This method is essential as the model only sees the text patterns in their natural order when it is being fine-tuned.

The token z<sub>3</sub> may be predicted using the same input sequence z, but with diferent factorization ordering, as shown in Fig. 1.

Although the permutation language modeling objective has beneficial characteristics, a simple implementation with a conventional Transformer setup may not perform eficiently. To illustrate the problem, consider modeling the next token distribution $p _ { \theta } ( Y _ { x _ { t } } | Y _ { x _ { < t } } )$ using the typical softmax approach (see Eq. 5):

$$
p _ { \theta } ( Y _ { x _ { t } } = y | Y _ { x _ { < t } } ) = \frac { \exp ( h ( y ) ^ { \top } p _ { \theta } ( Y _ { x _ { < t } } ) ) } { \sum _ { y ^ { \prime } } \exp ( h ( y ^ { \prime } ) ^ { \top } p _ { \theta } ( Y _ { x _ { < t } } ) ) } ,\tag{5}
$$

where the hidden state of $Y _ { x _ { < t } } )$ produced by the shared Transformer network with appropriate masking is represented by $p _ { \theta } ( Y _ { x _ { < t } } )$

Observe that the target location $x _ { t }$ has no bearing on $p _ { \theta } ( Y _ { x _ { < t } } )$ . This hinders the learning of meaningful representations since the same distribution is anticipated regardless of the target position.

In order to get around this, we suggest adjusting the next token distribution to take the intended position into consideration (see Eq. 6):

$$
p _ { \theta } ( Y _ { x _ { t } } = y | Y _ { x _ { < t } } ) = \frac { \exp ( h ( y ) ^ { \top } n _ { \theta } ( Y _ { x _ { < t } } , x _ { t } ) ) } { \sum _ { y ^ { \prime } } \exp ( h ( y ^ { \prime } ) ^ { \top } n _ { \theta } ( Y _ { x _ { < t } } , x _ { t } ) ) } ,\tag{6}
$$

where $n _ { \theta } ( Y _ { x _ { < t } } , x _ { t } )$ introduces a new type of representation that integrates the target position $x _ { t }$ as input.

Two streams of self-attention: it is dificult to define $n _ { \theta } ( Y _ { x _ { < t } } , x _ { t } )$ , even though the idea of target-aware representations helps to clear up the ambiguity in target prediction. Out of all the options, we suggest that we "stand" in the desired location $x _ { t }$ and use it to collect information from the context $Y _ { x _ { < t } }$ by paying attention to everything.

There are two requirements that must be met for this parameterization to function properly:

![](images/8636d1a1efa8924860dc5de3feb047d1a2cb1c7c7e29feac30f1375374916ee9.jpg)  
Fig. 3 Content stream attention, identical to standard self-attention. (c): Query stream attention, which lacks access to information about the content $x _ { y t }$

The target position $x _ { t }$ should be the sole thing used to forecast the token $Y _ { x _ { t } }$ , not the content $Y _ { x _ { < t } ; }$ otherwise, the task becomes simplistic.

The content $Y _ { x _ { < t } }$ must be included in order to forecast other tokens $Y _ { x _ { j } }$ for $j > t , n _ { \theta } ( Y _ { x < t } , x _ { t } )$ and guarantee full contextual information.

To resolve this conflict, we introduce two distinct sets of hidden-representations:

The function of content-representation $p _ { \theta } ( Y _ { x _ { < t } } )$ , represented as $p _ { x _ { t } } ,$ is comparable to that of the typical hidden states in Transformers. This representation encodes $Y _ { x _ { < t } }$ as well as the context.

● Query-representation $n _ { \theta } ( Y _ { x _ { < t } } , x _ { t } )$ , denoted as $n _ { x _ { t } } , \mathrm { r e - }$ lies only on the context $Y _ { x < t }$ and the target position $x _ { t }$ without directly accessing the content $Y _ { x _ { < t } }$

Computationally speaking, the content stream is initialized from the corresponding word embeddings, i.e. $, p _ { j } ^ { ( 0 ) } = g ( y _ { j } )$ whereas the first layer query stream is initialized with a trainable vectors, i.e., $q _ { j } ^ { ( 0 ) } = v$ . For every self-attention layer $n = 1 , \ldots , N$ , the two streams of representations undergo iterative updates in the manner described below:

Using a shared set of parameters, the representation streams evolve as shown in Fig. 3 and Fig. 4.

<sub>q</sub>(n) Self Attention $( Q = q _ { x t } ^ { ( n - 1 ) } , K V = p _ { x < t } ^ { ( n - 1 ) } ; \theta )$ , (query stream: uses $x _ { t }$ but cannot access $y _ { x _ { t } } )$

Here, the query, key, and value in the attention operation are represented by $Q , K , V$ . Similar to the ordinary selfattention procedure, the update rule applies to content representations. The content stream may therefore be used as a conventional Transformer model for fine-tuning, and the

$$
p _ { x t } ^ { ( n ) } \gets \mathrm { S e l f ~ A t t e n t i o n } ( Q = p _ { x t } ^ { ( n - 1 ) } , K V = p _ { x < t } ^ { ( n - 1 ) } ; \theta ) , \quad \mathrm { ( c o n t e n t \_ s t r e a m : ~ u s e s ~ b o t h ~ } x _ { t } \mathrm { ~ a n d ~ } y _ { x t } ) .
$$

query stream can be skipped. In Eq. 6, the next-token prediction is subsequently calculated using the final query representation $q _ { x t } ^ { ( N ) }$

Fig. 4 XLNet’s masked two-stream attention mechanism. The content stream (‘h‘) encodes token representations, while the query stream (‘g‘) maintains autoregressive properties. The factorization order (e.g., $\cdot 3 \gets 2 \gets 4 \gets 1 ^ { \cdot } )$ determines token processing. The attention mask ensures the query stream avoids self-attention, preserving causality. This design enables XLNet to leverage bidirectional context efectively while retaining the benefits of autoregressive modeling for improved language understanding and generation

![](images/c10da506184a1561ffffbc327ace42ae5e1aaf8375c2f417c97b7925674436b3.jpg)

Partially predicted: with standing the obvious advantages of the permutation language modeling goal objective (Eq. 3) has several benefits, the complexity of the permutations makes it an challenging optimization issue, which causes first trials to converge slowly. In order to address this problem, we limit predictions to the last tokens in a specified factorization order.

Specifically, y is divided into a target subsequence $y { > } d$ and a non-target subsequence $y _ { \leq d } ,$ where d is the cutof point. The objective is to maximize the target subsequence’s log-likelihood conditioned on the non-target subsequence (see Eq. 7):

$$
\operatorname* { m a x } _ { \theta } \mathbb { E } _ { y \sim \mathcal { V } _ { T } } \left[ \sum _ { t = d + 1 } ^ { | y | } \log p _ { \theta } ( w _ { y _ { t } } \mid w _ { y _ { \le d } } ) \right] .\tag{7}
$$

Here, $y { > } d$ is chosen as the target, as it incorporates the longest context within the sequence according to the current factorization order y.

To optimize the model’s eficiency, a hyperparameter L is introduced such that approximately $1 / L$ tokens are selected for prediction, i.e., $| y | / ( | y | - d ) \approx L$ . For tokens that are not selected, their query representations are omitted, which leads to gains in both processing speed and memory utilization.

## 3.2 CNN model

Convolutional Neural Networks (CNNs), originally designed for image processing, have proven to be highly efective in text classification tasks, including the detection of AI-generated text. Their strength lies in their ability to automatically extract local and hierarchical features from sequences of text, enabling the model to recognize patterns such as word n-grams, syntactic structures, and stylistic cues that diferentiate human-written content from machine-generated text (see the Fig. 5).

## 3.2.1 Character embedding and feature representation

The process begins with character-level embedding, where each character in a text is converted into a dense vector representation. As shown in the diagram, characters such as $^ { \mathrm { \tiny ~ * } } \mathrm { K } ^ { \mathrm { \tiny ~ , ~ } } , ^ { \mathrm { \tiny ~ * } } \mathrm { I } ^ { \mathrm { \tiny ~ , ~ } } , ^ { \mathrm { \tiny ~ * } } \mathrm { I } ^ { \mathrm { \tiny ~ , ~ } } , ^ { \mathrm { \tiny ~ * } } \mathrm { T } ^ { \mathrm { \tiny ~ , ~ } } , ^ { \mathrm { \tiny ~ * } } \mathrm { E } ^ { \mathrm { \tiny ~ , ~ } } , ^ { \mathrm { \tiny ~ * } } \mathrm { E } ^ { \mathrm { \tiny ~ , ~ } }$ are mapped into embedding vectors. This representation captures semantic and orthographic information at the most granular level, which is especially useful for handling misspellings, rare words, and stylistic variations commonly observed in both human and AI-generated text. Padding is applied to ensure consistent sequence lengths for convolution operations.

In addition to embeddings, auxiliary character features can be included. These features may capture statistical, syntactic, or frequency-based information that complements the learned embeddings. Together, embeddings and additional features form the initial representation that is fed into the CNN.

Fig. 5 Pipeline of a CNN model for detecting AI-generated text. Character embeddings are processed through convolution and max pooling layers to extract salient features, which are then used for classification  
![](images/c32309adf4b2b4d0a8cf1f559e78301393b660d781278ba1247442c907c005c5.jpg)

## 3.2.2 Convolutional layers for local feature extraction

The convolution layer applies multiple filters across the embeddings, sliding over the input sequence to capture local dependencies and patterns. For instance, a filter of width three might detect common trigrams, while larger filters can capture longer phrases. Each filter produces a feature map that highlights the presence of specific n-gram features in the text. This is crucial in AI-generated text detection, as generative models often leave subtle traces in local word patterns, repetitions, or unnatural phrase constructions.

By stacking multiple convolutional filters, the model can learn a diverse set of features ranging from simple character combinations to complex syntactic structures. These learned patterns serve as discriminative signals to diferentiate between authentic human writing and AI-generated outputs.

## 3.2.3 Max Pooling for Dimensionality Reduction

After convolution, max pooling is applied to reduce the dimensionality of the feature maps while retaining the most informative signals. This process condenses variable-length inputs into fixed-size vectors, making the representation more manageable for downstream layers. Importantly, max pooling ensures that the model focuses on the most salient features, such as unusual word sequences or repetitive structures, which are often indicative of machine-generated text.

The resulting pooled feature vectors are referred to as CNN-extracted character features. These compact, information-rich vectors are highly efective for classification tasks.

## 3.2.4 Classification layer and detection

The extracted features are then passed to one or more dense layers, culminating in a classification layer (often with a sigmoid or softmax activation) that predicts whether the input text is human-written or AI-generated. During training, the model learns to assign higher weights to discriminative patterns such as coherence, grammar consistency, and semantic flow, which are typically more natural in human text but may appear mechanical or inconsistent in AI-generated outputs.

## 3.3 XLNet-CNN hybrid model

The increasing use of LLMs, such as GPT-3 and GPT-4, has raised significant concerns in academic settings regarding the authenticity of student work. Detecting AI-generated essays is crucial for maintaining academic integrity and ensuring the validity of assessments. To address this challenge, this paper presents the XLNet-CNN Algorithm 1 and , a hybrid approach that combines the XLNet transformer model with CNNs for detecting human and AI-generated essays, as shown in Fig. 6. This model is evaluated using the "EnglishQA Essays Corpus", which contains Question(N) = 161,640 (212,479 human-generated; 169,668 AI-generated essays, samples labeled as either human-written or AI-generated.

1: function CREATE\_MODEL   
2: Input: Token IDs and attention mask of shape (256,)   
3: Output: Compiled neural network model   
4: Print("Loading XLNetModel")   
5: Load pre-trained XLNet model xlnetModel   
6: Define shared Conv1D layer: conv1D\_shared ← Conv1D(64, kernel\_size = 7, strides =   
2, regularization = L2(0.01))   
7: Define batch normalization layer: batchN ← BatchNormalization()   
8: Define activation function: activa ← Activation(relu)   
9: Pass input through XLNet model:   
10: xlnetout ← xlnetModel.transformer({input\_ids, attention\_mask})   
11: Extract last hidden state: x ← xlnetout.last\_hidden\_state   
12: Apply Conv1D layer: x ← conv1D\_shared(x)   
13: Apply batch normalization: x ← batchN(x)   
14: Apply activation function: x ← activa(x)   
15: Apply max pooling: x ← MaxPooling1D(3, strides = 2)(x)   
16: Flatten output: x ← Flatten()(x)   
17: Apply dense layer with sigmoid activation: x ← Dense(1, activation = sigmoid)(x)   
18: Apply dropout: x ← Dropout(0.3)(x)   
19: Define model: model ← Model(inputs = [input\_ids, attention\_mask], outputs = x)   
20: Print model summary   
21: Define optimizer: adam ← Adam(learning-rate = 0.00001)   
22: Compile model with binary cross-entropy loss and accuracy, precision, and recall metrics:   
23: model.compile(optimizer = adam, loss = BinaryCrossentropy(from\_logits = False),   
24: metrics = [accuracy, Precision(), Recall()])   
25: return model   
26: end function  
Algorithm 1 Create XLNet-CNN-based model

![](images/615edbde8ffdb6d1e875f7c4d7a351d2e88b88ed1495fddde15fa8c820a90c11.jpg)  
Fig. 6 Proposed methodology: XLNet-CNN hybrid model for AI-generated essays detection

The XLNet-CNN algorithm combines XLNet’s power of generalized autoregressive pretraining with the ability of CNNs to capture local patterns and structures in text. This hybrid model efectively utilizes XLNet’s bidirectional context learning while capturing distinctive stylistic features that can diferentiate human-written text from AI-generated essays.

This paper provides a detailed explanation of the XLNet-CNN algorithm, the steps involved in training and testing the model, and the role of word embeddings in the process. The following sections break down the methodology, data preprocessing, model architecture, training, and fine-tuning processes.

## 3.3.1 XLNet-CNN model architecture overview

The XLNet-CNN model integrates two key components: XLNet: A transformer model that learns bidirectional dependencies between tokens, leveraging generalized autoregressive pretraining. CNNs: Used for feature extraction and capturing local patterns within the text.

XLNet is a transformer-based model designed to overcome limitations of traditional bidirectional transformers like BERT. While BERT relies on a masked language model (MLM) to predict missing tokens, XLNet employs a generalized autoregressive model. Instead of masking tokens, XLNet learns to predict tokens in any possible order, thereby capturing bidirectional context while also benefiting from autoregressive capabilities. Mathematically, the training objective for XLNet is (see Eq. 8):

$$
P _ { \theta } ( x ) = \prod _ { i = 1 } ^ { n } P _ { \theta } ( x _ { i } | x _ { 1 : i - 1 } )\tag{8}
$$

Where: $\mathbf { \Sigma } - \mathbf { \Sigma } x _ { i }$ represents the tokens in a sequence; - $P _ { \theta } ( x _ { i } | x _ { 1 : i - 1 } )$ is the probability of predicting the $i ^ { t h }$ token given all the previous tokens in the sequence; - θ are the model parameters; - n is the sequence length.

This training paradigm allows XLNet to capture richer semantic relationships and bidirectional dependencies, making it ideal for complex NLP tasks like human vs. AIgenerated essays classification.

## 3.3.2 CNN: convolutional layers for feature extraction

After XLNet generates token embeddings, these embeddings are passed through a series of convolutional layers. CNNs are well-known for their ability to capture local patterns and structures in data. In the case of text, CNNs learn to identify characteristic features such as sentence structures, word usage patterns, or stylistic elements typical of human or AI-generated essays.

A convolutional layer applies a filter over the input data to detect patterns. The mathematical operation for the convolution is (see Eq. 9):

$$
y _ { j } = \operatorname* { m a x } \left( \sum _ { i = 1 } ^ { m } w _ { i } x _ { i + j - 1 } + b \right)\tag{9}
$$

Where: $\mathbf { \nabla } - y _ { j }$ is the output at position $j , \cdot w _ { i }$ are the weights $( { \mathrm { f i l t e r s } } ) ; - x _ { i + j - 1 }$ are the input values; - b is the bias term; - m is the size of the filter.

This process is applied repeatedly with diferent filters, resulting in a set of feature maps that highlight important aspects of the text that may distinguish human from AIgenerated essays.

## 3.3.3 Preprocessing for the englishQA essays corpus

The englishQA essays corpus consists of 161,640 essays, each labeled as human-written or AI-generated. Data preprocessing is a critical step to ensure the model receives clean, relevant input. The preprocessing pipeline consists of the following steps:

Text normalization and tokenization

Lowercasing: All text is converted to lowercase to reduce variations in the data caused by capitalization.

Tokenization: SentencePiece, a subword tokenization method, is applied to split the text into smaller units, or tokens. This approach helps the model handle rare or out-of-vocabulary words more efectively.

● Stop-word Removal: Common words (such as "the," $" \mathrm { a } , "$ and "and") that do not carry significant meaning are removed from the text to reduce noise and focus on important content.

● Punctuation Removal: Non-informative punctuation marks (commas, periods, etc.) are eliminated to avoid unnecessary complexity.

Digit Removal: Numbers are removed to prevent irrelevant noise, as they do not add meaningful information for distinguishing between human and AI text.

● Whitespace and Noise Removal: Any extra spaces, special characters, or HTML tags are stripped from the text to ensure clean data input.

Embedding generation: XLNet tokenization and embeddings after preprocessing, the text is tokenized into subword units using XLNet’s pretrained tokenizer. These tokens are then transformed into dense vector representations (embeddings), which capture the semantic meaning of the words and their relationships in context. XLNet embeddings encode both local and global context information, which is critical for detecting AI-generated essays.

## 3.3.4 Model training and fine-tuning

The XLNet-CNN model is trained on the preprocessed EnglishQA Essays Corpus dataset. The dataset is split into training (60%), validation (20%), and testing (20%) sets. The training process follows standard supervised learning principles, where the model learns to distinguish between human-written and AI-generated essays. Once the data is preprocessed and the embeddings are generated, the model enters the training and fine-tuning phases.

Stepwise training process:

1. Input representation: The text is tokenized and fed into XLNet. Each token is represented by a dense embedding vector generated by XLNet’s transformer-based architecture.

2. Feature Extraction with CNN: The embeddings are passed through a series of convolutional layers. These layers apply filters to detect local features, such as syntax or grammar patterns, that are indicative of either human-written or AI-generated essays.

3. Max Pooling Layer: After the convolutional layers, a max-pooling operation is applied to reduce the dimensionality of the feature maps while retaining the most important features. The max-pooling operation selects the most informative values from each feature map.

4. Fully connected Layer: The pooled features are passed through one or more fully connected layers. These layers consolidate the information extracted by the CNN and XLNet and help the model learn complex relationships between the features.

5. Output Layer: A softmax activation function is applied to the final output layer, which produces a probability distribution over the two classes: human-written and AI-generated.

![](images/27c26c48a90eaf074fc881f1748d8199c7ca8933a6d5f48f5afe4e189f967ee9.jpg)  
Algorithm 2 XLNet-CNN algorithm for Human-AI text detection

## 3.3.5 Loss function: cross-entropy loss

The model is trained using cross-entropy loss for binary classification, where the goal is to minimize the diference between predicted and actual class labels (see Eq. 10).

$$
L = - \frac { 1 } { N } \sum _ { i = 1 } ^ { N } \left( y _ { i } \log ( p _ { i } ) + ( 1 - y _ { i } ) \log ( 1 - p _ { i } ) \right)\tag{10}
$$

Where: - N is the number of samples in the batch; - y is the true label (1 for human-written, 0 for AI-generated); $\mathbf { \nabla } - p _ { i }$ is the predicted probability of the sample being human-written.

## 3.3.6 Fine-tuning the model

Fine-tuning is performed to adapt the pretrained XLNet model to the specific task of human vs. AI-generated essays detection. Fine-tuning allows the model to adjust its weights based on the characteristics of the EnglishQA Essays Corpus. The key steps in fine-tuning are:

1. Model initialization: the XLNet-CNN model is initialized with pretrained weights from XLNet. These weights have been learned from large datasets, providing a strong foundation for learning language representations.

2. Hyperparameter optimization: hyperparameters such as the learning rate, batch size, and number of filters in the CNN layers are optimized using grid search or random search. The learning rate controls the size of the weight updates during training, while the batch size determines how many samples are processed in each iteration.

3. Regularization: techniques like dropout and early stopping are applied to prevent overfitting. Dropout randomly disables a fraction of neurons during training, forcing the model to learn more robust features. Early stopping ensures that training halts if the model’s performance on the validation set stops improving.

In the context of regularization, the following equations represent the key techniques:

3.1 Dropout: during training, dropout randomly disables a fraction of neurons, meaning that for each training step, the activations of a subset of neurons are set to zero. Mathematically, this can be represented as (see Eq. 11):

$$
\hat { h } ^ { ( l ) } = \mathrm { D r o p o u t } ( h ^ { ( l ) } ) = h ^ { ( l ) } \odot r\tag{11}
$$

where: - $\it { h ^ { ( l ) } }$ is the vector of activations at layer $l , \cdot r$ is a binary vector sampled from a Bernoulli distribution with probability p (the probability of keeping a neuron active), - represents element-wise multiplication.

3.2 Early stopping: early stopping monitors the validation error and stops training when it starts to increase, preventing overfitting. The stopping criterion can be expressed as (see Eq. 12):

$$
\mathrm { S t o p ~ t r a i n i n g ~ w h e n } ; \quad \frac { 1 } { N } \sum _ { i = 1 } ^ { N } \mathrm { V a l i d a t i o n ~ E r r o r } ( t _ { i } ) > \mathrm { V a l i d a t i o n ~ E r r o r } _ { \operatorname* { m i n } } + \epsilon\tag{12}
$$

where: $\mathbf { \nabla } - t _ { i }$ represents the training epoch; - N is the number of validation samples; - ϵ is a small tolerance indicating when the model’s performance on the validation set no longer improves significantly.

These techniques help to prevent the model from memorizing the training data and improve its ability to generalize to unseen data.

## 3.3.7 Testing and evaluation

After the model is trained and fine-tuned, it is evaluated on a separate test set. The following metrics are used to assess the model’s performance:

Accuracy: The proportion of samples correctly classified as either human-written or AI-generated. Precision: The fraction of AI-generated essays correctly classified by the model. Recall: The fraction of actual AI-generated essays that the model successfully identifies. F2-score: The harmonic mean of precision and recall, providing a balanced measure of the model’s performance.

The XLNet-CNN model is compared to other popular models like SVM, CNN, LSTM, and BiLSTM to demonstrate its superiority in detecting AI-generated essays.

## 3.3.8 N-Gram discrepancy BOW model for detecting AIgenerated essays

The n-gram Discrepancy BOW language model is designed to detect AI-generated essays by analyzing the distribution of n-gram diferences between human and ChatGPT-generated text. Standard Bag-of-Words (BOW) models disregard grammar and word order, representing text as frequencybased vectors. To enhance context capture, we developed an n-gram BOW variant (up to n = 5), integrating word sequence information while accounting for discrepancies between human and AI-generated essays. The vectorized representations were fed into a machine learning classifier trained on essays from the EnglishQA Essays Corpus, continuously updated to track evolving AI-generated essays characteristics.

![](images/0bb7e3a928e6b732bb23ef95912cb1a552a8826f7da7b66ac4ec3473fda05efc.jpg)  
Source(s): Authors own creation

Fig. 7 Training the contextual word embedding language model with human (student) and AI-generated essays and testing the hybrid machine learning (ML) classifier yields ROUGE Score, PERPLEXITY (PPL), BLEU Score, overall accuracy, precision, recall, ROC-AUC, and F2-score  
![](images/069f8e22d3b23342ed71aa48bce9aba6f72b8e7150609f13e7d4c5c85a5bf58b.jpg)  
Fig. 8 Percentage-based distribution of student and AI-generated essay answers

In the testing phase, a 70/30 data split and 10-fold Monte Carlo cross-validation were used to evaluate multiple deep learning and machine learning classifiers, including SVM,

CNN, RNN, LSTM, BiLSTM, GRU, CNN-LSTM, CNN-Attention-LSTM, RoBERTa, and Modern BERT. Additionally, an Ensemble Learning (EL) classifier combined all models via majority voting. Notably, XLNet-CNN was the most discriminative model; by adjusting its cut-of threshold, we eliminated false negatives, achieving a perfect recall score (100%) and optimizing the F1 score, which is crucial for distinguishing student-written from AI-generated essays (see Fig. 7).

Evaluation metrics included ROUGE (text similarity), Perplexity (fluency), BLEU (coherence), Accuracy, Precision, Recall, and F2-score, ensuring robust AI text detection. The model continuously updates itself with real-world essay data, improving generalization across writing styles. By incorporating hybrid models (CNN, LSTM, Transformers) and leveraging diverse classifiers, the system efectively identifies linguistic artifacts in AI-generated essays. This research contributes to academic integrity, preventing AI-generated plagiarism, and enhancing automated content verification in education and professional settings.

Fig. 9 Visualization of the sources of student and AI answers (source: authors’ own creation)  
![](images/7baddc44d774d4f0265629cd19b113e9cf310af0f4cb84d93486df06553f29ac.jpg)

Table 1 Category-wise distribution of questions, human answers, and AI answers
<table><tr><td>Category (sources)</td><td># of questions</td><td># of student answers (0)</td><td># of AI answers (1)</td></tr><tr><td>Persuade corpus [53]</td><td>103,984</td><td>103,984</td><td>98,345</td></tr><tr><td>ChatGPT [51]</td><td>9684</td><td>18,654</td><td>17,337</td></tr><tr><td>LLaMA2-Chat [52]</td><td>9684</td><td>19,587</td><td>7561</td></tr><tr><td>Mistral 7B v2 [52]</td><td>4842</td><td>14,842</td><td>6660</td></tr><tr><td>Mistral 7B v1 [52]</td><td>4842</td><td>4842</td><td>5842</td></tr><tr><td>Original-Moth [52]</td><td>7263</td><td>6842</td><td>6842</td></tr><tr><td>Train-Essays [51]</td><td>4134</td><td>14,134</td><td>3842</td></tr><tr><td>LLaMA 70B v1 [54]</td><td>3516</td><td>3842</td><td>3842</td></tr><tr><td>Falcon 180B v1 [55]</td><td>3165</td><td>3842</td><td>2842</td></tr><tr><td>Claude-v7 [56]</td><td>1000</td><td>1000</td><td>1000</td></tr><tr><td>Claude-v6 [52]</td><td>1000</td><td>942</td><td>942</td></tr><tr><td>GPT–3.5 [57]</td><td>1500</td><td>1500</td><td>1342</td></tr><tr><td>LLaMA-2-7B-Chat [54]</td><td>842</td><td>842</td><td>842</td></tr><tr><td>Cohere-Command [56]</td><td>1000</td><td>942</td><td>1742</td></tr><tr><td>PaLM-Text-Bison1 [58]</td><td>1842</td><td>1842</td><td>2845</td></tr><tr><td>GPT-4 [59]</td><td>4842</td><td>14,842</td><td>6842</td></tr><tr><td>Total</td><td>161,640</td><td>212,479</td><td>169,668</td></tr></table>

## 4 Results and discussion

## 4.1 Dataset

The experiments are conducted on the public EnglishQA Essays Corpus [51–53], which contains 161,640 questions paired with human- and AI-generated responses, including

ChatGPT, LLaMA2, Mistral, Claude, Falcon, and others. The dataset is divided into training (60%), validation (20%), and testing (20%) splits. Figures 8 and 9 illustrate the proportion of human versus AI answers, while Table 1 provides the category-wise distribution. Human responses dominate most categories, although models such as GPT-4 and PaLM-Text-Bison1 contribute a larger share of AI-generated content.

To examine indistinguishability, we compared a postgraduate student’s essay excerpt with a ChatGPT-generated one on the same question. As shown in Table 2, both responses appear stylistically similar, making it dificult for evaluators to diferentiate. This highlights the risks of AIgenerated essays for academic integrity and the necessity of reliable detection methods.

The corpus spans multiple academic levels (middle school to postgraduate), requiring augmentation to balance human- and AI-generated texts. For human essays, we applied synonym replacement, paraphrasing, back-translation, and sentence restructuring to increase stylistic diversity. For AI essays, we varied prompts, adjusted sampling parameters, and applied fine-tuned generation to simulate diferent writing styles. Human-in-the-loop editing further introduced natural variation. These techniques reduced bias, improved balance, and enhanced generalization in detection models.

Standard preprocessing was applied to clean and normalize the corpus, including lowercasing, tokenization, and removal of stop-words, punctuation, digits, and extra spaces [60]. Essays were then tokenized using the XLNet tokenizer, producing subword-level embeddings enriched with positional and segment information. The [CLS] token embedding was used as the sentence-level representation for classification.

<table><tr><td colspan="3">Table 2 Comparison of Former Student&#x27;s and ChatGPT&#x27;s Answers on NLP</td></tr><tr><td>Question</td><td>Student&#x27;s excerpt (answer)</td><td>ChatGPT&#x27;s excerpt (answer)</td></tr><tr><td>What is NLP and write applications?</td><td>NLP is a subfield of artificial intelligence that focuses on enabling computers to inter- pret and process human language. It is used in many areas, such as search engines and voice recognition systems. NLP uses machine learning, statistical models, and deep learning to perform tasks like sentiment analysis, translation, and text summarization. A key challenge is the ambiguity of language, where words may have multiple meanings. Overcoming this is essential for building effective systems</td><td>NLP is a specialized area of AI dealing with the interac- tion between computers and human language. It enables machines to process, under- stand, and generate text and speech. Applications include speech recognition, classifica- tion, translation, and chatbots.</td></tr></table>

## 4.2 Experimental setup

We trained our models on a machine equipped with two NVIDIA GeForce RTX 3060 GPUs. For the base models, using the hyperparameters outlined in the paper, each training step took approximately 0.6 s. We trained the base models for a total of 50,000 steps, which took around 4.9 days. For the larger models (detailed in the bottom row of Table 4), the training step time was 1.0 s. These larger models were trained for 150,000 steps, requiring approximately 12.9 days to complete. This setup allowed us to eficiently process and fine-tune our models within the given time frames. We conduct t-tests, Wilcoxon tests, and ANOVA to compare model performances across diferent evaluation metrics (Test Accuracy, Precision, Recall), and see the Table 6,7,10, and 11.

The Table 5 compares various machine learning and deep learning models used for detecting AI-generated and humangenerated text. It includes traditional methods like SVM, deep learning architectures such as CNN, RNN, LSTM, and GRU, along with hybrid models like CNN-LSTM and CNN-Attention-LSTM. Transformer-based models such as RoBERTa and Modern BERT are also included. The models difer in hyperparameters like epochs, learning rate, batch size, optimizer, activation function, hidden units, dropout rate, and additional parameters. Notably, transformer models (RoBERTa, BERT) use the AdamW optimizer with GELU activation, whereas recurrent models use Adam or RMSprop with Tanh activation. Hybrid models integrate CNNs and attention mechanisms for feature extraction. Transformers leverage large pretrained models, making them more resource-intensive but often more accurate. This Table helps in comparing model architectures and selecting the best approach for AI text detection.

## 4.3 Evaluation metrics

To evaluate model performance, we employed several widely used metrics. ROUGE scores (ROUGE-1, ROUGE-2, ROUGE-L, ROUGE-S) were applied to capture lexical and structural overlaps between generated and reference texts [61]. Perplexity (PPL) was used to assess the predictive quality of models, where lower values indicate better sequence modeling [62]. BLEU scores measured n-gram precision and text similarity, commonly used for machine translation and generation tasks [63]. In addition, classification metrics such as Accuracy, Precision, Recall, and the F2-score were used to quantify detection performance [64]. These complementary metrics provide a comprehensive assessment, balancing surface-level lexical overlap with deeper classification efectiveness, particularly important for distinguishing AI-generated from humanwritten essays.

Table 3 Model performance with existing Methods
<table><tr><td>Model</td><td>Weight type</td><td>Accuracy</td><td>Precision</td><td>Recall</td><td>F2-score</td></tr><tr><td>SVM</td><td>Frozen</td><td>0.90</td><td>0.88</td><td>0.91</td><td>0.89</td></tr><tr><td>SVM</td><td>Unfrozen</td><td>0.99</td><td>0.99</td><td>1.00</td><td>0.99</td></tr><tr><td>CNN</td><td>Frozen</td><td>0.95</td><td>0.93</td><td>0.96</td><td>0.94</td></tr><tr><td>CNN</td><td>Unfrozen</td><td>0.97</td><td>1.00</td><td>0.99</td><td>1.00</td></tr><tr><td>RNN</td><td>Frozen</td><td>0.94</td><td>0.92</td><td>0.97</td><td>0.95</td></tr><tr><td>RNN</td><td>Unfrozen</td><td>0.96</td><td>0.99</td><td>0.99</td><td>1.00</td></tr><tr><td>LSTM</td><td>Frozen</td><td>0.93</td><td>0.93</td><td>0.96</td><td>0.95</td></tr><tr><td>LSTM</td><td>Unfrozen</td><td>0.96</td><td>0.98</td><td>1.00</td><td>1.00</td></tr><tr><td>Bi-LSTM</td><td>Frozen</td><td>0.94</td><td>0.95</td><td>0.97</td><td>0.99</td></tr><tr><td>Bi-LSTM</td><td>Unfrozen</td><td>0.96</td><td>1.00</td><td>1.00</td><td>1.00</td></tr><tr><td>GRU</td><td>Frozen</td><td>0.95</td><td>0.97</td><td>0.95</td><td>0.96</td></tr><tr><td>GRU</td><td>Unfrozen</td><td>0.96</td><td>1.00</td><td>0.99</td><td>1.00</td></tr><tr><td>CNN-LSTM</td><td>Frozen</td><td>0.93</td><td>0.96</td><td>0.96</td><td>0.96</td></tr><tr><td>CNN-LSTM</td><td>Unfrozen</td><td>0.96</td><td>0.99</td><td>1.00</td><td>1.00</td></tr><tr><td>CNN-Attention-LSTM</td><td>Frozen</td><td>0.94</td><td>0.98</td><td>0.96</td><td>0.92</td></tr><tr><td>CNN-Attention-LSTM</td><td>Unfrozen</td><td>0.98</td><td>1.00</td><td>1.00</td><td>1.00</td></tr><tr><td>Modern BERT</td><td>Frozen</td><td>0.94</td><td>0.99</td><td>0.99</td><td>0.99</td></tr><tr><td>Modern BERT</td><td>Unfrozen</td><td>0.97</td><td>0.99</td><td>1.00</td><td>0.96</td></tr><tr><td>RoBERTa</td><td>Frozen</td><td>0.95</td><td>0.96</td><td>0.96</td><td>0.94</td></tr><tr><td>RoBERTa</td><td>Unfrozen</td><td>0.975</td><td>1.00</td><td>1.00</td><td>1.00</td></tr><tr><td>XLNet</td><td>Frozen</td><td>0.95</td><td>0.99</td><td>0.95</td><td>0.98</td></tr><tr><td>XLNet</td><td>Unfrozen</td><td>0.98</td><td>1.00</td><td>1.00</td><td>1.00</td></tr><tr><td>XLNet-CNN</td><td>Frozen</td><td>0.96</td><td>0.99</td><td>0.99</td><td>0.94</td></tr><tr><td>XLNet-CNN</td><td>Unfrozen</td><td>0.99</td><td>1.00</td><td>1.00</td><td>1.00</td></tr></table>

## 4.4 Experiments

We trained 10 variations of our LLM model, dividing them into two groups: 5 with frozen parameters and 5 with unfrozen parameters. Each model was trained using datasets split into training (60%), validation (20%), and testing (20%) portions, and the results were recorded in a comprehensive table. To evaluate the performance of these models, we employed several widely recognized metrics, including Precision, recall, F2-score, and support. Precision measures the proportion of positive predictions that are correctly classified as belonging to the positive class. Recall evaluates the number of positive predictions made out of all actual positive instances in the dataset. The F2-score balances precision and recall, with values ranging from 0 to 1, where a score closer to 1 indicates higher model accuracy. Additionally, we considered BLEU Score and PPL to further assess the models’ performance and linguistic quality.

Table 3 presents the performance comparison of various machine learning and deep learning models trained on

100% of the dataset, evaluating their Testing Accuracy, Precision, Recall, and F2-score under both Frozen and Unfrozen weight settings. Generally, Unfrozen models (where pre-trained weights are fine-tuned) outperform Frozen models (where pre-trained weights remain fixed), demonstrating higher accuracy and recall. Traditional models like SVM and CNN perform well, but transformer-based models such as Modern BERT, RoBERTa, XLNet, and XLNet-CNN show superior performance, especially in the Unfrozen state, achieving nearly perfect scores across all metrics. Hybrid models like CNN-LSTM and CNN-Attention-LSTM also exhibit strong classification capabilities, benefiting from both convolutional feature extraction and sequential modeling. XLNet-CNN (Unfrozen) achieves the highest performance, indicating its efectiveness in AI-generated text detection by leveraging both bidirectional context learning (XLNet) and feature extraction (CNN). The results highlight the importance of fine-tuning deep learning models for optimal performance in detecting AI-generated text.

## 4.4.1 Variations in model design

In our analysis, we compare XLNet-CNN hybrid variants to understand how architectural modifications afect model eficiency, perplexity, and human-perceived fluency. We find that the base configuration (6 layers, $d _ { m o d e l }$ 512, d<sub>ff</sub> 2048, 8 heads, 128 CNN filters, 3 3 kernels) serves as a strong benchmark, achieving balanced scores across PPL,

<table><tr><td>Table 4 Performance comparison of XLNET-CNN hybrid language model variants under different configurations</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>CNN Filters</td><td>Kernel Size</td><td></td><td></td><td>BLEU</td><td></td><td></td></tr><tr><td>Config N</td><td></td><td>dmodel</td><td>dff</td><td>h</td><td>dk</td><td>dv</td><td>Pdrop</td><td>∈ls</td><td></td><td></td><td>Train Steps</td><td>PPL</td><td></td><td>ROUGE</td><td>Human Eval</td></tr><tr><td>Base</td><td>6</td><td>512</td><td>2048</td><td>8</td><td>64</td><td>64</td><td>0.1</td><td>0.1</td><td>128</td><td>3x3</td><td>10K</td><td>4.92</td><td>28.8</td><td>0.85</td><td>8.3</td></tr><tr><td>(1)</td><td></td><td>512</td><td>512</td><td>4</td><td>128</td><td>128</td><td>0.1</td><td></td><td>64</td><td>5x5</td><td></td><td>6.29</td><td>27.9</td><td>0.77</td><td>7.5</td></tr><tr><td></td><td></td><td>128</td><td>128</td><td>16</td><td>32</td><td>32</td><td>0.1</td><td></td><td>64</td><td>3x3</td><td></td><td>4.91</td><td>27.8</td><td>0.69</td><td>6.8</td></tr><tr><td></td><td></td><td>32</td><td>32</td><td>32</td><td>16</td><td>16</td><td>0.1</td><td></td><td>32</td><td>3x3</td><td></td><td>5.01</td><td>28.4</td><td>0.80</td><td>7.9</td></tr><tr><td>(2)</td><td>16</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>32</td><td>3x3</td><td></td><td>5.16</td><td>28.1</td><td>0.71</td><td>7.9</td></tr><tr><td></td><td>32</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>64</td><td>3x3</td><td></td><td>5.01</td><td>28.4</td><td>0.73</td><td>7.7</td></tr><tr><td>(3)</td><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>32</td><td>3x3</td><td></td><td>6.11</td><td>26.7</td><td>0.76</td><td>7.5</td></tr><tr><td></td><td>4</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>32</td><td>5x5</td><td></td><td>5.19</td><td>27.3</td><td>0.76</td><td>7.4</td></tr><tr><td></td><td>8</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>64</td><td>5x5</td><td></td><td>5.12</td><td>27.4</td><td>0.77</td><td>7.9</td></tr><tr><td></td><td>256</td><td>32</td><td>32</td><td>128</td><td>128</td><td>128</td><td>0.2</td><td></td><td>128</td><td>7x7</td><td></td><td>5.12</td><td>28.4</td><td>0.79</td><td>7.5</td></tr><tr><td>(4)</td><td>0.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>64</td><td>3x3</td><td></td><td>5.77</td><td>28.6</td><td>0.82</td><td>8.2</td></tr><tr><td></td><td>0.2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>64</td><td>3x3</td><td></td><td>5.47</td><td>28.7</td><td>0.69</td><td>6.8</td></tr><tr><td>(5)</td><td></td><td>Positional embedding instead of sinusoids</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>3x3</td><td></td><td>4.92</td><td></td><td></td><td>8.9</td></tr><tr><td>Large</td><td>6</td><td>768</td><td>3072</td><td>12</td><td>64</td><td>64</td><td>0.2</td><td>0.1</td><td>256</td><td>7x7</td><td>100K</td><td>4.33</td><td>29.9</td><td>0.91</td><td>9.2</td></tr></table>

BLEU, ROUGE, and human evaluation. When we reduce the feed-forward dimensions or the Transformer depth, we observe higher perplexity and lower fluency, confirming that depth and representation capacity are critical for semantic richness. We also note that adjustments to CNN filter size and kernel width can partially recover performance, where wider kernels (5 5, 7 7) capture longer-range dependencies and improve BLEU and ROUGE scores.

We further investigate the role of regularization and embedding choices. We observe that lower dropout improves coherence and human evaluation, while excessive dropout reduces fluency despite similar BLEU scores. When we replace sinusoidal with learnable positional embeddings, we achieve the highest human evaluation, suggesting that learned embeddings capture contextual continuity more efectively. Finally, when we scale the model (larger d , $d _ { f f } .$ and CNN filters), we obtain the best overall results (PPL 4.33, BLEU 29.9, ROUGE 0.91, human eval 9.2). These findings demonstrate that deeper architectures with suficient training scale and expressive CNN layers enable superior generalization and naturalness.

## 4.4.2 Model comparison

The comparative analysis between traditional machine learning models, deep learning architectures, hybrid neural approaches, and Transformer-based models presented in Table 6, and the latest AI-generated text detection tools shown in Table 7, highlights both the progress in algorithmic sophistication and the nuanced trade-ofs across precision, recall, test accuracy, and robustness in detecting AI-generated versus human-authored text. Starting with the models in Table 6, the classical SVM baseline achieves an accuracy of 85% with high recall (0.96), reflecting its ability to detect AI-generated texts efectively, yet its relatively low precision (0.79) underscores a vulnerability to false positives, meaning it often misclassifies human text as AI-generated, which could create issues in educational or evaluative contexts where fairness is paramount.

Moving towards CNNs, the CNN model raises overall accuracy slightly to 85.8% and shows better balance between precision (0.80) and recall (0.92), reflecting convolutional networks’ ability to extract local n-gram-like features from essays, but their inability to fully capture long-range dependencies limits performance. The RNN model achieves 92% accuracy with very high precision (0.95), demonstrating strong sequential modeling capabilities, but its recall drops slightly to 0.90, indicating it may miss some AI-generated cases. Traditional sequential models like LSTM and BiL-STM show accuracies between 86–87%, with BiLSTM ofering stronger precision (0.92) but lower recall (0.82), while GRU balances both precision and recall at 0.82 but remains weaker overall. These results show that while recurrent architectures can model dependencies across words, their limited capacity and training ineficiencies prevent them from competing with newer approaches. Hybrid models like CNN-LSTM and CNN-Attention-LSTM bridge this gap, achieving 92–93% accuracy, leveraging convolutional feature extraction for local cues and LSTMs with attention for contextual focus, which improves both precision and recall, demonstrating the benefit of combining architectures. However, the most significant improvements emerge with Transformer-based models, where ModernBERT achieves 94% accuracy, RoBERTa 95%, BERT 96%, GPT 97%, and XLNet 95% with superior recall (0.97). Importantly, the proposed XLNet-CNN hybrid delivers the best results with 98% accuracy, perfect precision (1.00), and near-perfect recall (0.96), minimizing both false positives and false negatives. Its BLEU score of 30.76 and low perplexity of 3.99 also indicate its outputs are closer to human-like reference distributions and are highly confident in predictions, showing how combining XLNet’s permutation-based contextual embeddings with CNN’s local feature learning produces a superior hybrid detector.

Table 5 Hyperparameter settings for various models
<table><tr><td>Model</td><td>Learning rate</td><td>Batch size</td><td>Optimizer</td><td>Activation</td><td>Hidden units</td><td></td><td>Dropout Additional parameters</td></tr><tr><td>SVM</td><td>0.01</td><td>N/A</td><td>SGD</td><td>N/A</td><td>N/A</td><td>N/A</td><td>Kernel: RBF, C: 1.0</td></tr><tr><td>CNN</td><td>0.001</td><td>32</td><td>Adam</td><td>ReLU</td><td>128</td><td>0.3</td><td>Kernel: (3×3), Pooling: Max (2x2)</td></tr><tr><td>RNN</td><td>0.0005</td><td>64</td><td>RMSprop</td><td>Tanh</td><td>256</td><td>0.2</td><td>2 Layers</td></tr><tr><td>LSTM</td><td>0.0003</td><td>64</td><td>Adam</td><td>Tanh</td><td>512</td><td>0.2</td><td>3 Layers, bidirectional: No</td></tr><tr><td>BiLSTM</td><td>0.0003</td><td>64</td><td>Adam</td><td>Tanh</td><td>512</td><td>0.3</td><td>3 Layers, bidirectional: Yes</td></tr><tr><td>GRU</td><td>0.0003</td><td>64</td><td>Adam</td><td>Tanh</td><td>256</td><td>0.2</td><td>2 Layers</td></tr><tr><td>CNN-LSTM</td><td>0.001</td><td>32</td><td>Adam</td><td>ReLU/Tanh</td><td>256</td><td>0.3</td><td>CNN Kernel: (3x3), MaxPool: (2x2)</td></tr><tr><td>CNN-Attn-LSTM 0.001</td><td></td><td>32</td><td>Adam</td><td>ReLU/Softmax/Tanh</td><td>256</td><td>0.3</td><td>Attention Heads: 2</td></tr><tr><td>RoBERTa</td><td>2e-5</td><td>16</td><td>AdamW</td><td>GELU</td><td>768</td><td>0.1</td><td>Pretrained: roberta-base</td></tr><tr><td>Modern BERT</td><td>2e-5</td><td>16</td><td>AdamW</td><td>GELU</td><td>768</td><td>0.1</td><td>Pretrained: bert-large-uncased</td></tr></table>

Table 6 Performance comparison of models for AI-generated and human-generated text detection
<table><tr><td>Proposed model</td><td>TP</td><td>TN</td><td>FP</td><td>FN</td><td>Precision</td><td>Recall</td><td>Test accuracy</td><td>F2-score</td><td>BLEU</td><td>PPL</td></tr><tr><td>SVM</td><td>81</td><td>64</td><td>21</td><td>3</td><td>0.79</td><td>0.96</td><td>0.85</td><td>0.92</td><td>24.5</td><td>4.33</td></tr><tr><td>CNN</td><td>79</td><td>73</td><td>19</td><td>6</td><td>0.80</td><td>0.92</td><td>0.858</td><td>0.90</td><td>24.67</td><td>4.56</td></tr><tr><td>RNN</td><td>78</td><td>71</td><td>4</td><td>8</td><td>0.95</td><td>0.90</td><td>0.92</td><td>0.91</td><td>25.67</td><td>5.43</td></tr><tr><td>LSTM</td><td>77</td><td>77</td><td>12</td><td>11</td><td>0.86</td><td>0.87</td><td>0.870</td><td>0.87</td><td>24.56</td><td>5.22</td></tr><tr><td>BiLSTM</td><td>69</td><td>68</td><td>6</td><td>15</td><td>0.92</td><td>0.82</td><td>0.86</td><td>0.83</td><td>25.66</td><td>4.87</td></tr><tr><td>GRU</td><td>71</td><td>71</td><td>15</td><td>15</td><td>0.82</td><td>0.82</td><td>0.82</td><td>0.82</td><td>25.65</td><td>4.66</td></tr><tr><td>CNN-LSTM</td><td>82</td><td>77</td><td>5</td><td>7</td><td>0.94</td><td>0.92</td><td>0.92</td><td>0.92</td><td>24.56</td><td>5.00</td></tr><tr><td>CNN-Attention-LSTM</td><td>79</td><td>75</td><td>3</td><td>7</td><td>0.96</td><td>0.91</td><td>0.93</td><td>0.92</td><td>24.56</td><td>5.89</td></tr><tr><td>ModernBERT</td><td>82</td><td>79</td><td>4</td><td>6</td><td>0.95</td><td>0.93</td><td>0.94</td><td>0.93</td><td>25.64</td><td>5.33</td></tr><tr><td>RoBERTs</td><td>76</td><td>78</td><td>0</td><td>7</td><td>1.00</td><td>0.91</td><td>0.95</td><td>0.93</td><td>24.56</td><td>5.56</td></tr><tr><td>BERT</td><td>81</td><td>71</td><td>1</td><td>5</td><td>0.98</td><td>0.94</td><td>0.96</td><td>0.95</td><td>24.56</td><td>5.56</td></tr><tr><td>GPT</td><td>75</td><td>68</td><td>1</td><td>2</td><td>0.98</td><td>0.97</td><td>0.97</td><td>0.97</td><td>24.56</td><td>5.56</td></tr><tr><td>XLNET</td><td>71</td><td>68</td><td>5</td><td>2</td><td>0.93</td><td>0.97</td><td>0.95</td><td>0.96</td><td>24.56</td><td>5.56</td></tr><tr><td>XLNET-CNN</td><td>61</td><td>83</td><td>0</td><td>2</td><td>1.00</td><td>0.96</td><td>0.98</td><td>0.97</td><td>30.76</td><td>3.99</td></tr></table>

Table 7 Performance evaluation of the proposed classification model algorithms (see Table 6) and the latest trending AI-generated text detection software tool
<table><tr><td>LLM model</td><td>TP</td><td>TN</td><td>FP</td><td>FN</td><td>Precision</td><td>Recall</td><td>Test accuracy</td><td>F2-score</td><td>BLEU</td><td>PPL</td></tr><tr><td>OpenAI-Detector</td><td>71</td><td>63</td><td>1</td><td>5</td><td>0.986</td><td>0.934</td><td>0.957</td><td>0.95</td><td></td><td></td></tr><tr><td>GPTZero</td><td>82</td><td>77</td><td>4</td><td>1</td><td>0.953</td><td>0.987</td><td>0.969</td><td>0.980</td><td></td><td></td></tr><tr><td>DetectGPT</td><td>83</td><td>69</td><td>5</td><td>3</td><td>0.943</td><td>0.965</td><td>0.95</td><td>0.960</td><td></td><td></td></tr><tr><td>Copyleaks</td><td>86</td><td>69</td><td>2</td><td>4</td><td>0.977</td><td>0.955</td><td>0.962</td><td>0.959</td><td></td><td></td></tr><tr><td>Fast-DetectGPT</td><td>85</td><td>70</td><td>1</td><td>2</td><td>0.988</td><td>0.977</td><td>0.981</td><td>0.979</td><td></td><td></td></tr><tr><td>Grammarly</td><td>82</td><td>77</td><td>4</td><td>0</td><td>0.953</td><td>0.987</td><td>0.966</td><td>0.980</td><td></td><td></td></tr><tr><td>Turnitin</td><td>82</td><td>77</td><td>3</td><td>1</td><td>0.953</td><td>0.987</td><td>0.964</td><td>0.980</td><td></td><td></td></tr><tr><td>GTLR</td><td>82</td><td>77</td><td>2</td><td>2</td><td>0.97</td><td>0.97</td><td>0.97</td><td>0.97</td><td></td><td></td></tr></table>

Turning to Table 7, which evaluates widely used LLMbased detection tools, we see that real-world detectors are generally strong but vary in balance between precision and recall. OpenAI Detector demonstrates high precision (0.986)

Table 8 Efect of data augmentation on XLNet+CNN Model
<table><tr><td>Setting</td><td>TP</td><td>TN</td><td>FP</td><td>FN</td><td>Precision</td><td>Recall</td><td>Test accuracy</td><td>F2-score</td><td>BLEU</td><td>PPL</td></tr><tr><td>Without augmentation</td><td>58</td><td>80</td><td>3</td><td>5</td><td>0.95</td><td>0.92</td><td>0.94</td><td>0.93</td><td>28.45</td><td>4.22</td></tr><tr><td>With augmentation</td><td>61</td><td>83</td><td>0</td><td>2</td><td>1.00</td><td>0.96</td><td>0.98</td><td>0.97</td><td>30.76</td><td>3.99</td></tr></table>

Fig. 10 Models Performance and BLEU/PPL Score Comparison

![](images/58bc0ee3cab9bfbf76760fe0a5791c4924863db1ab295f1f07258c6a6ea7a263.jpg)

but a slightly lower recall (0.934), yielding 95.7% accuracy, which means it confidently flags AI text when detected but can miss certain generative cases, leading to false negatives. GPTZero, one of the most widely used detectors in education, achieves a recall of 0.987 and accuracy of 96.9%, indicating its efectiveness in capturing nearly all AI-generated essays while maintaining a precision of 0.953, which is strong but suggests occasional false positives. DetectGPT ofers comparable performance (95% accuracy) with precision of 0.943 and a recall of 0.965, showing it is slightly less precise but still highly efective. Copyleaks balances well with 96.2% accuracy, precision of 0.977, and recall of 0.955, reflecting strong reliability and reduced false positives. Fast-DetectGPT stands out with 98.1% accuracy, precision of 0.988, and recall of 0.977, rivaling the top-performing research models in Table 6 and validating how algorithmic optimizations can yield state-of-the-art real-world detectors. Grammarly, Turnitin, and GTLR also perform competitively, with accuracies around 96–97% and high recall values (0.987 for Grammarly and Turnitin, 0.97 for GTLR), underscoring their reliability in practical academic and professional settings. Interestingly, Grammarly achieves perfect recall (1.000) while maintaining a precision of 0.953, meaning it successfully identifies all AI-generated samples in the dataset without missing any, but with a small trade-of of increased false positives. Turnitin balances slightly better with 0.965 precision and 0.988 recall, while GTLR provides an even balance at 0.97 for both precision and recall, ofering robustness and consistency across test cases.

When comparing Table 6 models with Table 7 detection tools, several insights emerge. First, while advanced detectors like Fast-DetectGPT and Grammarly rival or even exceed the accuracy of many proposed deep learning models, they are still slightly outperformed by the researchgrade hybrid XLNet-CNN model, which reaches 98% accuracy with perfect precision. This suggests that while commercial detectors are optimized for broad usability, custom hybrid architectures tailored for the detection task can achieve higher discriminative power. Second, the trade-of between precision and recall is central: tools like OpenAI Detector prioritize precision, reducing false accusations against human authors but risking missed detections, while tools like Grammarly prioritize recall, ensuring AI cases are caught at the cost of higher false positives. Academic contexts might prefer higher recall to prevent AI misuse, while professional or creative domains may prefer higher

Table 9 Ten-fold cross-validation results (Mean ± Std) for AI vs Human text detection models
<table><tr><td>Model</td><td>Precision</td><td>Recall</td><td>Accuracy</td><td>F2-score</td><td>BLEU</td><td>PPL</td></tr><tr><td>SVM</td><td> $0 . 7 8 6 \pm 0 . 0 0 7$ </td><td> $0 . 9 6 2 \pm 0 . 0 1 0$ </td><td> $0 . 8 5 0 \pm 0 . 0 1 0$ </td><td> $0 . 9 2 3 \pm 0 . 0 0 9$ </td><td> $2 4 . 5 0 1 \pm 0 . 0 0 7$ </td><td> $4 . 3 3 3 \pm 0 . 0 0 8$ </td></tr><tr><td>CNN</td><td> $0 . 8 0 1 \pm 0 . 0 1 0$ </td><td> $0 . 9 2 3 \pm 0 . 0 0 9$ </td><td> $0 . 8 6 1 \pm 0 . 0 1 0$ </td><td> $0 . 9 0 2 \pm 0 . 0 0 9$ </td><td> $2 4 . 6 7 1 \pm 0 . 0 1 2$ </td><td> $4 . 5 6 2 \pm 0 . 0 0 7$ </td></tr><tr><td>RNN</td><td> $0 . 9 4 7 \pm 0 . 0 0 8$ </td><td> $0 . 8 9 7 \pm 0 . 0 1 0$ </td><td> $0 . 9 2 3 \pm 0 . 0 0 8$ </td><td> $0 . 9 1 2 \pm 0 . 0 1 2$ </td><td> $2 5 . 6 6 8 \pm 0 . 0 1 0$ </td><td> $5 . 4 3 2 \pm 0 . 0 0 7$ </td></tr><tr><td>LSTM</td><td> $0 . 8 6 5 \pm 0 . 0 0 9$ </td><td> $0 . 8 6 9 \pm 0 . 0 0 7$ </td><td> $0 . 8 6 8 \pm 0 . 0 0 7$ </td><td> $0 . 8 7 0 \pm 0 . 0 0 8$ </td><td> $2 4 . 5 6 1 \pm 0 . 0 0 8$ </td><td> $5 . 2 1 7 \pm 0 . 0 0 8$ </td></tr><tr><td>BiLSTM</td><td> $0 . 9 1 3 \pm 0 . 0 0 8$ </td><td> $0 . 8 2 2 \pm 0 . 0 0 8$ </td><td> $0 . 8 6 1 \pm 0 . 0 1 3$ </td><td> $0 . 8 2 9 \pm 0 . 0 0 9$ </td><td> $2 5 . 6 5 6 \pm 0 . 0 0 8$ </td><td> $4 . 8 6 8 \pm 0 . 0 0 7$ </td></tr><tr><td>GRU</td><td> $0 . 8 1 8 \pm 0 . 0 0 8$ </td><td> $0 . 8 2 2 \pm 0 . 0 0 7$ </td><td> $0 . 8 1 8 \pm 0 . 0 1 0$ </td><td> $0 . 8 2 1 \pm 0 . 0 0 7$ </td><td> $2 5 . 6 5 2 \pm 0 . 0 1 0$ </td><td> $4 . 6 5 4 \pm 0 . 0 0 9$ </td></tr><tr><td>CNN-LSTM</td><td> $0 . 9 4 3 \pm 0 . 0 0 9$ </td><td> $0 . 9 1 7 \pm 0 . 0 0 9$ </td><td> $0 . 9 1 9 \pm 0 . 0 0 8$ </td><td> $0 . 9 1 7 \pm 0 . 0 0 9$ </td><td> $2 4 . 5 6 1 \pm 0 . 0 1 4$ </td><td> $5 . 0 0 0 \pm 0 . 0 1 1$ </td></tr><tr><td>CNN-AttentionLSTM</td><td> $0 . 9 5 9 \pm 0 . 0 0 9$ </td><td> $0 . 9 1 0 \pm 0 . 0 0 9$ </td><td> $0 . 9 3 3 \pm 0 . 0 0 6$ </td><td> $0 . 9 1 7 \pm 0 . 0 0 7$ </td><td> $2 4 . 5 6 4 \pm 0 . 0 0 8$ </td><td> $5 . 8 8 9 \pm 0 . 0 1 0$ </td></tr><tr><td>ModernBERT</td><td> $0 . 9 5 2 \pm 0 . 0 0 8$ </td><td> $0 . 9 2 7 \pm 0 . 0 0 7$ </td><td> $0 . 9 4 2 \pm 0 . 0 0 8$ </td><td> $0 . 9 2 6 \pm 0 . 0 0 9$ </td><td> $2 5 . 6 4 0 \pm 0 . 0 1 0$ </td><td> $5 . 3 2 7 \pm 0 . 0 0 9$ </td></tr><tr><td>RoBERTs</td><td> $0 . 9 9 7 \pm 0 . 0 1 2$ </td><td> $0 . 9 1 0 \pm 0 . 0 0 7$ </td><td> $0 . 9 5 0 \pm 0 . 0 0 9$ </td><td> $0 . 9 2 0 \pm 0 . 0 0 7$ </td><td> $2 4 . 5 5 8 \pm 0 . 0 1 1$ </td><td> $5 . 5 6 2 \pm 0 . 0 1 0$ </td></tr><tr><td>BERT</td><td> $0 . 9 7 7 \pm 0 . 0 0 7$ </td><td> $0 . 9 4 5 \pm 0 . 0 1 5$ </td><td> $0 . 9 6 4 \pm 0 . 0 0 9$ </td><td> $0 . 9 4 5 \pm 0 . 0 0 8$ </td><td> $2 4 . 5 5 8 \pm 0 . 0 1 2$ </td><td> $5 . 5 6 5 \pm 0 . 0 1 1$ </td></tr><tr><td>GPT</td><td> $0 . 9 7 9 \pm 0 . 0 0 8$ </td><td> $0 . 9 7 0 \pm 0 . 0 1 2$ </td><td> $0 . 9 6 8 \pm 0 . 0 0 7$ </td><td> $0 . 9 7 0 \pm 0 . 0 1 3$ </td><td> $2 4 . 5 6 3 \pm 0 . 0 1 0$ </td><td> $5 . 5 6 1 \pm 0 . 0 1 0$ </td></tr><tr><td>XLNet</td><td> $0 . 9 3 2 \pm 0 . 0 1 0$ </td><td> $0 . 9 6 9 \pm 0 . 0 0 9$ </td><td> $0 . 9 5 2 \pm 0 . 0 0 8$ </td><td> $0 . 9 6 3 \pm 0 . 0 1 3$ </td><td> $2 4 . 5 6 4 \pm 0 . 0 1 0$ </td><td> $5 . 5 5 7 \pm 0 . 0 0 7$ </td></tr><tr><td>XLNet-CNN</td><td> $1 . 0 0 0 \pm 0 . 0 1 1$ </td><td> $0 . 9 6 3 \pm 0 . 0 1 5$ </td><td> $0 . 9 8 2 \pm 0 . 0 0 4$ </td><td> $0 . 9 6 7 \pm 0 . 0 0 8$ </td><td> $3 0 . 7 5 6 \pm 0 . 0 0 9$ </td><td> $3 . 9 9 6 \pm 0 . 0 1 1$ </td></tr></table>

Table 10 Pairwise significance tests (accuracy vs. XLNet-CNN)
<table><tr><td>Model</td><td>t test p value</td><td>Wilcoxon p value</td></tr><tr><td>SVM</td><td>2.1e-11</td><td>0.0019</td></tr><tr><td>CNN</td><td>5.1e-11</td><td>0.0019</td></tr><tr><td>RNN</td><td>4.7e-09</td><td>0.0019</td></tr><tr><td>LSTM</td><td>2.1e-11</td><td>0.0019</td></tr><tr><td>BiLSTM</td><td>6.9e-10</td><td>0.0019</td></tr><tr><td>GRU</td><td>1.8e-11</td><td>0.0019</td></tr><tr><td>CNN-LSTM</td><td>1.5e-09</td><td>0.0019</td></tr><tr><td>CNNAttnLSTM</td><td>1.4e-09</td><td>0.0019</td></tr><tr><td>ModernBERT</td><td>4.3e-07</td><td>0.0019</td></tr><tr><td>RoBERTs</td><td>5.7e-06</td><td>0.0019</td></tr><tr><td>BERT</td><td>3.1e-04</td><td>0.0019</td></tr><tr><td>GPT</td><td>3.6e-04</td><td>0.0039</td></tr><tr><td>XLNet</td><td>1.7e-05</td><td>0.0019</td></tr><tr><td>XLNet-CNN</td><td>一</td><td>一</td></tr></table>

Table 11 ANOVA results across all models

Change the bold font in Table 6 to normal Font. In summary, the dual comparison across Tables 6 and 7 illustrates how both research-driven and commercially deployed approaches to AI-generated text detection have reached a maturity where accuracies above 95% are common, but the best-performing systems diferentiate themselves through their handling of precision-recall trade-ofs, interpretability, and adaptability across datasets. While Transformer-based hybrids like XLNet-CNN push the frontier of performance with unmatched precision and robustness, detection software like GPTZero, Copyleaks, and Fast-DetectGPT ofer scalable, user-friendly tools already widely adopted in education and industry. Ultimately, this comparison reveals that future progress may not hinge solely on accuracy improvements but also on integrating explainability, fairness, and adaptability, ensuring detection systems not only perform well under controlled experiments but also align with realworld ethical and practical demands where both false positives and false negatives carry significant consequences.

<table><tr><td>Metric</td><td>F score</td><td>p value</td></tr><tr><td>Precision</td><td>608.38</td><td>6.74e-107</td></tr><tr><td>Recall</td><td>218.19</td><td>1.16e-79</td></tr><tr><td>Accuracy</td><td>325.64</td><td>3.37e-90</td></tr><tr><td>F2-score</td><td>216.96</td><td>1.63e-79</td></tr><tr><td>BLEU</td><td>236948</td><td>1.25e-269</td></tr><tr><td>PPL</td><td>34533</td><td>6.09e-217</td></tr></table>

precision to avoid unfair penalization of genuine authors. Third, the perplexity and BLEU scores in Table 6 reveal a deeper interpretability layer absent from most commercial tools, showing how linguistic similarity to human references and model confidence influence classification. Notably, XLNet-CNN’s exceptionally high BLEU and low PPL demonstrate not only detection strength but also nuanced understanding of text coherence and fluency, a capability that real-world tools do not explicitly report but could integrate in future iterations.

Table 8 compares the performance of the proposed XLNet+CNN model trained with and without data augmentation techniques (back-translation and paraphrasing). The results indicate that augmentation provides a measurable benefit. Without augmentation, the model achieves a test accuracy of 0.94 and an F2-score of 0.93, with recall at 0.92. After introducing augmentation, performance improves to a test accuracy of 0.98, an F2-score of 0.97, and recall rises to 0.96. Precision also reaches 1.00, meaning the augmented model makes no false positive classifications in the evaluated test set. In addition, BLEU scores increase (28.45 30.76), while perplexity decreases (4.22  3.99), suggesting that augmentation contributes to generating more linguistically diverse yet consistent representations.

Overall, the comparison confirms that data augmentation strengthens the robustness and generalization of the hybrid

XLNet+CNN model, improving both classification accuracy and language quality metrics (Fig. 10).

## 4.4.3 Ten-fold cross-validation

The results of the comparative evaluation across multiple deep learning and machine learning models for the task of distinguishing between AI-generated and human-written text are summarized in Tables 9, 10, and 11. These tables report not only the direct performance metrics of the models under a ten-fold cross-validation (CV) scheme but also provide statistical significance testing through pairwise comparisons and global variance analyses. Together, these findings ofer a comprehensive picture of how the diferent architectures perform, where they excel, and where significant performance diferences exist.

Table 9 reports the mean and standard deviation of six metrics: Precision, Recall, Accuracy, F2-score, BLEU, and Perplexity (PPL)for each of the evaluated models under a ten-fold CV setup. This experimental design is important because it provides a robust estimate of performance by averaging across multiple folds of the dataset, reducing the likelihood of results being biased by a particular split. In terms of performance trends, several observations can be made. First, traditional machine learning baselines such as SVM show reasonable recall $( 0 . 9 6 2 \pm 0 . 0 1 0 )$ and F2-score $( 0 . 9 2 3 \pm 0 . 0 0 9 )$ but struggle with accuracy $( 0 . 8 5 0 \pm 0 . 0 1 0 )$ confirming the limitations of shallow approaches compared to more complex neural architectures. Among simpler deep models, CNNs and RNNs ofer notable improvements, with the RNN in particular achieving strong precision (0.947 ± 0.008) and accuracy $( 0 . 9 2 3 \pm 0 . 0 0 8 )$ . However, recurrent architectures such as LSTM, BiLSTM, and GRU show variability in their trade-ofs: while BiLSTM achieves relatively high precision $( 0 . 9 1 3 \pm 0 . 0 0 8 )$ , its recall drops to $0 . 8 2 2 \pm$ 0.008, suggesting that it struggles with sensitivity to AIgenerated texts. In contrast, GRU achieves balanced but overall lower scores, highlighting its limitations in this specific classification task.

Moving to hybrid architectures, CNN-LSTM and CNN-Attention-LSTM demonstrate significant gains, particularly in accuracy (0.919 ± 0.008 and $0 . 9 3 3 \pm 0 . 0 0 6$ , respectively) and F2-score (both around $0 . 9 1 7 \pm 0 . 0 0 7 )$ . The inclusion of attention mechanisms appears to provide consistent improvements by allowing the network to focus on important features of the text selectively. However, the most striking improvements are observed in Transformer-based architectures. ModernBERT, RoBERTa (denoted as RoB-ERTs), BERT, GPT, and XLNet all achieve accuracy above 0.94, with GPT $( 0 . 9 6 8 \pm 0 . 0 0 7 )$ and XLNet $( 0 . 9 5 2 \pm 0 . 0 0 8 )$ showing particularly strong balance between precision and recall. Notably, BERT and GPT demonstrate near-perfect precision $( 0 . 9 7 7 \pm 0 . 0 0 7$ and $0 . 9 7 9 \pm 0 . 0 0 8$ , respectively), making them highly efective at minimizing false positives. Finally, the proposed XLNet-CNN hybrid outperforms all others, with an accuracy of $0 . 9 8 2 \pm \ : 0 . 0 0 4$ , precision of $1 . 0 0 0 \pm 0 . 0 1 1$ , and the lowest perplexity $( 3 . 9 9 6 \pm 0 . 0 1 1 )$ The significant increase in BLEU score $( 3 0 . 7 5 6 \pm 0 . 0 0 9 )$ also indicates that this model is better aligned with linguistic structures, suggesting that its combined architecture is able to capture both contextual and structural properties of text. Taken together, Table 9 demonstrates clear stratification between simpler models, hybrid approaches, and advanced Transformer-based methods, with the XLNet-CNN hybrid consistently outperforming others.

While mean performance provides insight, statistical testing is necessary to determine whether these diferences are truly significant. Table 10 addresses this by reporting pairwise significance tests comparing the accuracy of each model to the XLNet-CNN. Both paired t tests and Wilcoxon signed-rank tests were conducted, ofering complementary parametric and non-parametric perspectives. The results show that for nearly all models, the p-values are extremely small (often< 1e-09 for the t-test and consistently< 0.01 for the Wilcoxon test). This indicates that the improvements of XLNet-CNN over other models are not only numerically superior but also statistically significant. The only exception is when comparing XLNet-CNN to itself, where no values are reported, as expected. Importantly, even state-of-the-art models such as GPT, BERT, and XLNet show statistically significant diferences when compared against XLNet-CNN, with p-values as low as 3.6e–04 and 1.7e–05. These findings reinforce the robustness of the proposed hybrid architecture, confirming that the observed gains are unlikely to be due to random variation.

To provide a global perspective, Table 11 presents the results of ANOVA (Analysis of Variance) across all models for each evaluation metric. ANOVA tests whether there are statistically significant diferences in the means of multiple groups. The results are striking: all metrics show extremely high F-scores and vanishingly small p-values (well below 0.001). For example, Precision has an F-score of 608.38 $( \mathsf { p } = 6 . 7 4 \mathsf { e } { - } 1 0 7 )$ , Accuracy has an F-score of 325.64 (p $= 3 . 3 7 \mathrm { e } { - 9 0 } )$ , and BLEU reaches a staggering F-score of 236,948 (p = 1.25e–269). These results confirm that diferences across models are not only present but also highly statistically significant across all dimensions of evaluation. The extremely low p-values further validate the claim that model architecture has a profound efect on performance in AI-generated text detection.

In summary, the results from Tables 9, 10 and 11 provide strong empirical and statistical evidence of the superiority of the proposed XLNet-CNN model. Table 9 demonstrates its numerical dominance across all key metrics, Table 10 confirms that these improvements are statistically significant compared to other baselines, and Table 11 shows that diferences across models are globally significant. The findings highlight three important trends: (1) traditional models like SVM and basic deep models lag significantly behind in this task, (2) hybrid approaches such as CNN-Attention-LSTM show noticeable improvements due to their ability to model sequential and hierarchical text features, and (3) Transformer-based architectures, particularly XLNet-CNN, achieve state-of-the-art performance by combining contextual richness with local feature extraction. These results underscore the importance of hybrid deep learning strategies in tackling the challenges of AI-generated text detection and contribute evidence that architectural innovations yield meaningful and statistically reliable improvements.

Table 12 Comparison of ROUGE scores for diferent models in detecting AI-generated essays
<table><tr><td>Model</td><td>ROUGE-1</td><td>ROUGE-2</td><td>ROUGE-L</td><td>ROUGE-S</td></tr><tr><td>SVM</td><td>0.55</td><td>0.42</td><td>0.50</td><td>0.38</td></tr><tr><td>CNN</td><td>0.65</td><td>0.52</td><td>0.60</td><td>0.48</td></tr><tr><td>RNN</td><td>0.60</td><td>0.48</td><td>0.55</td><td>0.43</td></tr><tr><td>LSTM</td><td>0.68</td><td>0.55</td><td>0.62</td><td>0.50</td></tr><tr><td>BiLSTM</td><td>0.70</td><td>0.58</td><td>0.65</td><td>0.53</td></tr><tr><td>GRU</td><td>0.67</td><td>0.54</td><td>0.61</td><td>0.49</td></tr><tr><td>CNN-LSTM</td><td>0.72</td><td>0.60</td><td>0.68</td><td>0.57</td></tr><tr><td>CNN-Attention-LSTM</td><td>0.75</td><td>0.63</td><td>0.70</td><td>0.60</td></tr><tr><td>RoBERTa</td><td>0.80</td><td>0.68</td><td>0.76</td><td>0.65</td></tr><tr><td>Modern BERT</td><td>0.82</td><td>0.70</td><td>0.78</td><td>0.67</td></tr><tr><td>XLNet</td><td>0.83</td><td>0.71</td><td>0.79</td><td>0.68</td></tr><tr><td>XLNet-CNN</td><td>0.85</td><td>0.73</td><td>0.81</td><td>0.70</td></tr></table>

![](images/8c0b4116ba79b8802a9d7e3d9bd1d7055c556b96652648f902d79b758a44ed25.jpg)  
Fig. 11 Comparison of ROUGE scores across models

## 4.4.4 Visualization hybrid models comparison of ROUGE scores

Visualization of Hybrid Models’ Comparison of ROUGE Scores provides a graphical representation of how diferent hybrid models perform in terms of their ROUGE scores. In the context of detecting AI-generated versus humangenerated essays, hybrid models (e.g., combining CNN with LSTM or Transformer models) are compared to assess how well they capture linguistic features and overall text quality. The visualization ofers insights into which hybrid models achieve higher ROUGE scores across diferent metrics (ROUGE-1, ROUGE-2, ROUGE-L, and ROUGE-S), which are used to measure the quality and relevance of text generation in question-answering systems. By comparing these scores, one can evaluate the efectiveness of hybrid models for this specific task.

Table 12 and Fig. 11 compare the ROUGE scores (ROUGE-1, ROUGE-2, ROUGE-L, and ROUGE-S) for various models used to detect AI-generated versus humangenerated essays. The comparison of diferent models based on ROUGE scores reveals the varying strengths and weaknesses of traditional machine learning models versus modern deep learning architectures. The traditional SVM model performs relatively modestly, with an ROUGE-1 score of 0.55 and an ROUGE-2 score of 0.42, which are considerably lower than those of more advanced models. SVM’s performance is highly dependent on feature extraction methods, and it struggles to capture complex patterns in sequential data. On the other hand, CNNs, which focus on local patterns, outperform SVM by a significant margin, achieving a ROUGE-1 score of 0.65 and a ROUGE-2 score of 0.52. This indicates that CNNs are better at identifying useful features in text, particularly for shorter sequences. Recurrent Neural Networks (RNNs), with a ROUGE-1 score of 0.60 and ROUGE-2 score of 0.48, show an improvement over SVM and CNNs, particularly in handling sequential data. However, they still struggle with long-term dependencies, limiting their performance in more complex tasks.

Long Short-Term Memory (LSTM) networks significantly improve upon RNNs, handling long-term dependencies better, and score higher with ROUGE-1 of 0.68 and ROUGE-2 of 0.55.

Bidirectional LSTMs (BiLSTM) further enhance accuracy by capturing both forward and backward context, achieving the highest performance among traditional deep learning architectures, with a ROUGE-1 score of 0.70 and a ROUGE-2 score of 0.58. Gated Recurrent Units (GRU), while less powerful than LSTMs, ofer a simplified version with competitive performance (ROUGE-1 of 0.67 and ROUGE-2 of 0.54). The combination of CNN and LSTM (CNN-LSTM) increases performance even further, with ROUGE-1 reaching 0.72. Attention mechanisms incorporated into CNN-LSTM models (CNN-Attention-LSTM) boost performance, particularly in ROUGE-L, achieving a score of 0.70. The pretrained models, such as RoBERTa (ROUGE-1 of 0.80) and modern BERT (ROUGE-1 of 0.82), excel in contextual understanding, with XLNet (ROUGE-1 of 0.83) showing even better results. The XLNet-CNN hybrid combines the best of both worlds, with the highest ROUGE scores of all models, particularly excelling in both contextual accuracy and pattern extraction, indicating its superior performance in complex text generation and understanding tasks.

## 5 Challenges and limitations

Despite the strong performance of the proposed XLNet-CNN hybrid model, several challenges and limitations remain:

1. Evolving nature of AI-generated text: With the rapid advancement of large language models (LLMs) such as GPT-4, AI-generated text increasingly resembles human writing. This makes it dificult for detection systems like XLNet-CNN to consistently identify subtle linguistic artifacts, requiring continuous retraining and adaptation.

2. Generalization and adaptability: although the XLNet-CNN model demonstrates robust results on the EnglishQA Essays Corpus, its ability to generalize across diferent domains, academic subjects, and multilingual contexts is limited. The reliance on domain-specific datasets may restrict its efectiveness when applied to unseen or diverse text sources.

3. Need for robust training strategies: high accuracy on benchmark datasets does not eliminate the risk of overfitting. Future work must incorporate adversarial training, dynamic learning strategies, and real-time monitoring to improve adaptability and resilience against increasingly sophisticated AI-generated essays.

## 6 Conclusion

This paper presented a fine-tuned XLNet-CNN hybrid framework for detecting AI-generated essays, addressing the pressing challenge of maintaining academic integrity in the era of large language models (LLMs). By combining XLNet’s generalized autoregressive pretraining and bidirectional context learning with the convolutional neural network’s strength in local feature extraction, the proposed approach consistently outperformed traditional classifiers and transformer-based baselines on the EnglishQA Essays Corpus. Experimental results demonstrated strong detection capability, with the model achieving accuracy of 0.98, recall of 0.96, F2-score of 0.97, and precision of 1.00, while eliminating false negatives. These findings underscore the efectiveness of hybrid architectures in capturing both semantic coherence and stylistic artifacts that distinguish humanwritten from AI-generated text. Comparative evaluations against widely used detection tools further confirmed the adaptability and reliability of the framework across diverse writing styles and contexts. Overall, the XLNet-CNN model ofers a scalable and practical solution for safeguarding educational integrity in high-stakes academic settings.

## 7 Future research directions

Building upon the identified challenges, several directions for future research can be explored:

1. Cross-domain and multilingual expansion: extending the XLNet-CNN model to handle multilingual datasets and domain-specific academic writing (e.g., scientific, technical, and humanities essays) will enhance its generalization ability and make it more applicable in global educational contexts.

2. Integration of hybrid architectures: combining XLNet-CNN with emerging architectures such as state space models (SSMs) or attention-free transformers can further improve both eficiency and detection accuracy. Exploring hybrid ensembles may also help balance robustness and inference speed.

3. Adversarial and real-time training: future research should incorporate adversarial training and real-time monitoring frameworks to adapt to evolving LLMs. This will enable the detection system to remain resilient against novel generative models that continuously refine their outputs.

4. Explainability and educational tools: enhancing the interpretability of model predictions will provide educators with actionable insights, helping them understand why a text is flagged as AI-generated. Integrating explainable AI (xAI) techniques could increase trust and adoption in academic environments.

5. Ethical and policy considerations: beyond technical development, future work should also address ethical concerns and collaborate with institutions to formulate guidelines that balance the responsible use of AI tools in education while safeguarding academic integrity.

Author contributions MP conceptualized and designed the study, performed the analysis, and wrote the original draft. PPV contributed to data collection and interpretation and critically reviewed the manuscript. SKB AND PPV supervised the project and was involved in the final editing of the manuscript. All authors read and approved the final manuscript.

Data availability The data that support the findings of this study are available from the corresponding author upon reasonable request.

## Declarations

Conflict of interest The authors declare no conflict of interest.

## References

1. Saul D (2023) ChatGPT parent Open AI Gets ‘game changing’multibillion-dollar boost from Microsoft. Forbes, Jersey

2. Fyfe P (2023) How to cheat on your final paper: assigning ai for student writing. AI & Soc 38(4):1395–1405

3. Yeadon W, Inyang O-O, Mizouri A, Peach A, Testrow CP (2023) The death of the short-form physics essay in the coming ai revolution. Phys Educ 58(3):035027

4. Sharples M (2022) Automated essay writing: an AIED opinion. Int J Artif Intell Educ 32(4):1119–1126

5. Waisberg E, Ong J, Masalkhi M, Kamran SA, Zaman N, Sarker P, Lee AG, Tavakkoli A (2023) Gpt-4: a new era of artificial intelligence in medicine. Ir J Med Sci (1971) 192(6):3197–3200

6. Floridi L, Chiriatti M (2020) Gpt-3: its nature, scope, limits, and consequences. Mind Mach 30:681–694

7. Yadagiri A, Pakray P (2025) Deep learning strategies for identifying machine-generated text. 2025 19th International conference on ubiquitous information management and communication (IMCOM). IEEE, Geneva, pp 1–8

8. Lin C-Y, Chien T-W, Chen Y-H, Lee Y-L, Su S-B (2022) An app to classify a 5-year survival in patients with breast cancer using the convolutional neural networks (CNN) in Microsoft excel: development and usability study. Medicine 101(4):28697

9. Sherstinsky A (2020) Fundamentals of recurrent neural network (RNN) and long short-term memory (LSTM) network. Physica D 404:132306

10. Song X, Liu Y, Xue L, Wang J, Zhang J, Wang J, Jiang L, Cheng Z (2020) Time-series well performance prediction based on long short-term memory (LSTM) neural network model. J Petrol Sci Eng 186:106682

11. Liu G, Guo J (2019) Bidirectional LSTM with attention mechanism and convolutional layer for text classification. Neurocomputing 337:325–338

12. Rana R (2016) Gated recurrent unit (gru) for emotion classification from noisy speech. arXiv preprint arXiv:1612.07778

13. Alhussein M, Aurangzeb K, Haider SI (2020) Hybrid CNN-LSTM model for short-term individual household load forecasting. Ieee Access 8:180544–180557

14. Saqware GJ (2024) Hybrid deep learning model integrating attention mechanism for the accurate prediction and forecasting of the cryptocurrency market. Operations research forum. Springer, Cham, p 19

15. Semary NA, Ahmed W, Amin K, Pławiak P, Hammad M (2023) Improving sentiment classification using a Roberta-based hybrid model. Front Hum Neurosci 17:1292010

16. Yang Z (2019) Xlnet: generalized autoregressive pretraining for language understanding. arXiv preprint arXiv:1906.08237

17. Gehrmann S, Strobelt H, Rush AM (2019) Gltr: statistical detection and visualization of generated text. arXiv preprint arXiv:1906.04043

18. Sadasivan VS, Kumar A, Balasubramanian S, Wang W, Feizi S (2023) Can ai-generated text be reliably detected? arXiv preprint arXiv:2303.11156

19. Goldberg Y, Hirst G (2017) Neural network methods in natural language processing. Morgan and Claypool Publishers, San Rafael, p 69

20. Mikolov T, Chen K, Corrado G, Dean J (2013) Eficient estimation of word representations in vector space. arXiv preprint arXiv:1301.3781

21. Ling W, Dyer C, Black AW, Trancoso I (2015) Two/too simple adaptations of word2vec for syntax problems. In: Proceedings of the 2015 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, pp 1299–1304

22. Neumann M, Iyyer M, Gardner M, Clark C, Lee K, Zettlemoyer L (2018) Deep contextualized word representations. arXiv preprint arXiv:1802.05365

23. Howard J, Ruder S (2018) Universal language model fine-tuning for text classification. arXiv preprint arXiv:1801.06146

24. Vaswani A, Shazeer N, Parmar N, Uszkoreit J, Jones L, Gomez AN, Kaiser Ł, Polosukhin I (2017) Attention is all you need. Adv Neural Inf Process Syst 30

25. Devlin J, Chang M-W, Lee K, Toutanova K (2018) Bert: pretraining of deep bidirectional transformers for language understanding. arXiv preprint arXiv:1810.04805

26. Radford A, Narasimhan K, Salimans T, Sutskever I (2018) Improving language understanding with unsupervised learning. 2018. URL: https://openai. com/research/language-unsupervised

27. Lewis M, Liu Y, Goyal N, Ghazvininejad M, Mohamed A, Levy O, Stoyanov V, Zettlemoyer L (2019) Bart: denoising sequenceto-sequence pre-training for natural language generation, translation, and comprehension. arXiv preprint arXiv:1910.13461

28. Liu Y, Ott M, Goyal N, Du J, Joshi M, Chen D, Levy O, Lewis M, Zettlemoyer L, Stoyanov V (2019) Roberta: a robustly optimized bert pretraining approach. arXiv preprint arXiv:1907.11692

29. Rafel C, Shazeer N, Roberts A, Lee K, Narang S, Matena M, Zhou Y, Li W, Liu PJ (2020) Exploring the limits of transfer learning with a unified text-to-text transformer. J Mach Learn Res 21(140):1–67

30. Hou X, Zhao Y, Liu Y, Yang Z, Wang K, Li L, Luo X, Lo D, Grundy J, Wang H (2023) Large language models for software engineering: a systematic literature review. arXiv preprint arXiv:2308.10620

31. Brown T, Mann B, Ryder N, Subbiah M, Kaplan JD, Dhariwal P, Neelakantan A, Shyam P, Sastry G, Askell A et al (2020)

Language models are few-shot learners. Adv Neural Inf Process Syst 33:1877–1901

32. Achiam J, Adler S, Agarwal S, Ahmad L, Akkaya I, Aleman FL, Almeida D, Altenschmidt J, Altman S, Anadkat S, et al (2023) Gpt-4 technical report. arXiv preprint arXiv:2303.08774

33. Touvron H, Lavril T, Izacard G, Martinet X, Lachaux M-A, Lacroix T, Rozière B, Goyal N, Hambro E, Azhar F, et al (2023) Llama: open and eficient foundation language models. arXiv preprint arXiv:2302.13971

34. Reynolds L, McDonell K (2021) Prompt programming for large language models: beyond the few-shot paradigm. In: Extended abstracts of the 2021 CHI conference on human factors in computing systems, pp 1–7

35. Trummer I (2022) Codexdb: synthesizing code for query processing from natural language instructions using GPT-3 codex. Proc VLDB Endow 15(11):2921–2928

36. White J, Fu Q, Hays S, Sandborn M, Olea C, Gilbert H, Elnashar A, Spencer-Smith J, Schmidt DC (2023) A prompt pattern catalog to enhance prompt engineering with chatgpt. arXiv preprint arXiv:2302.11382

37. Cascella M, Montomoli J, Bellini V, Bignami E (2023) Evaluating the feasibility of Chatgpt in healthcare: an analysis of multiple clinical and research scenarios. J Med Syst 47(1):33

38. Levin G, Meyer R, Kadoch E, Brezinov Y (2023) Identifying chatgpt-written OBGYN abstracts using a simple tool. Am J Obstet Gynecol MFM 5(6):100936

39. Gupta R, Pande P, Herzog I, Weisberger J, Chao J, Chaiyasate K, Lee ES (2023) Application of chatgpt in cosmetic plastic surgery: ally or antagonist? Aesthetic Surg J 43(7):587–590

40. Lahat A, Shachar E, Avidan B, Shatz Z, Glicksberg BS, Klang E (2023) Evaluating the use of large language model in identifying top research questions in gastroenterology. Sci Rep 13(1):4164

41. Lyu Q, Tan J, Zapadka ME, Ponnatapura J, Niu C, Myers KJ, Wang G, Whitlow CT (2023) Translating radiology reports into plain language using chatgpt and gpt-4 with prompt learning: promising results, limitations, and potential. arXiv preprint arXiv:2303.09038

42. Thorp HH (2023) ChatGPT is fun, but not an author. American Association for the Advancement of Science, Washington

43. Van Dis EA, Bollen J, Zuidema W, Van Rooij R, Bockting CL (2023) Chatgpt: five priorities for research. Nature 614(7947):224–226

44. Germain M, Gregor K, Murray I, Larochelle H (2015) Made: masked autoencoder for distribution estimation. In: International Conference on Machine Learning, PMLR. pp 881–889.

45. Uria B, Côté M-A, Gregor K, Murray I, Larochelle H (2016) Neural autoregressive distribution estimation. J Mach Learn Res 17(205):1–37

46. Fedus W, Goodfellow I, Dai AM (2018) Maskgan: better text generation via filling in the\_. arXiv preprint arXiv:1801.07736

47. Ouyang X, Zhou P, Li CH, Liu L (2015) Sentiment analysis using convolutional neural network. In: 2015 IEEE international conference on computer and information technology; ubiquitous computing and communications; dependable, autonomic and secure computing; pervasive intelligence and computing, pp. 2359–2364. IEEE

48. Pennington J, Socher R, Manning CD (2014) Glove: global vectors for word representation. In: Proceedings of the 2014 conference on empirical methods in natural language processing (EMNLP), pp. 1532–1543

49. Li W (2020) Analysis of semantic comprehension algorithms of natural language based on robot’s questions and answers. In: 2020 IEEE International conference on advances in electrical engineering and computer applications (AEECA), IEEE pp. 1021–1024.

50. Deguang C, Jinlin M, Ziping M, Jie Z (2021) Review of pre-training techniques for natural language processing. J Front Comput Sci Tech 15(8):1359

51. Essays Corpus datasets (2023) https://www.kaggle.com/competit ions/llm-detect-ai-generated-text/data. Accessed 31 Oct 2023

52. EnglishQA Essays Corpus datasets (2023) https://www.kaggle.co m/datasets/thedrcat/daigt-proper-train-dataset. Accessed 11 May 2023

53. Crossley SA, Tian Y, Bafour P, Franklin A, Benner M, Boser U (2024) A large-scale corpus for assessing written argumentation: persuade 2.0. Assess Writ 61:100865

54. EnglishQA Essays Corpus datasets. https://www.kaggle.com/da tasets/nbroad/daigt-data-llama-70b-and-falcon180b. Accessed 11 May 2024

55. Abbas HM (2025) A novel approach to automated detection of ai-generated text. J Al-Qadisiyah Comput Sci Math 17(1):1–17

56. EnglishQA Essays Corpus datasets (2024) https://www.kaggle.c om/datasets/darraghdog/hello-claude-1000-essays-from-anthropi c. Accessed 11 May 2024

57. EnglishQA Essays Corpus datasets (2023) (https://www.kaggle .com/datasets/alejopaullier/daigt-external-dataset). Accessed 11 May 2023

58. EnglishQA Essays Corpus datasets. https://www.kaggle.com/da tasets/kingki19/llm-generated-essay-using-palm-from-google-ge n-ai. Accessed 11 May 2024

59. EnglishQA Essays Corpus datasets. https://www.kaggle.com/data sets/radek1/llm-generated-essays. Accessed 11 May 2024

60. Naseem S, Mahmood T, Asif M, Rashid J, Umair M, Shah M (2021) Survey on sentiment analysis of user reviews. In: 2021 International Conference on Innovative Computing (ICIC), IEEE pp 1–6.

61. Chen A, Stanovsky G, Singh S, Gardner M (2019) Evaluating question answering evaluation. In: Proceedings of the 2nd Workshop on Machine Reading for Question Answering, pp 119–124

62. Jelinek F (1998) Statistical methods for speech recognition. MIT press, Cambridge

63. Papineni K, Roukos S, Ward T, Zhu W-J (2002) Bleu: a method for automatic evaluation of machine translation. In: Proceedings of the 40th mof the association for computational linguistics, pp 311–318

64. Sokolova M, Lapalme G (2009) A systematic analysis of performance measures for classification tasks. Inf Process Manag 45(4):427–437

Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional afiliations.