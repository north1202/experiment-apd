# Research Ethics in the Age of Generative AI: Opportunities and Pitfalls in Engineering and Technology

Seong-Woo Kim

Graduate School of Engineering Practice

Seoul National University

Seoul, Republic of Korea

snwoo@snu.ac.kr

Abstract—This study examines how the rise of generative AI shapes research ethics in science and engineering. As AI increasingly contributes to writing, design optimization, and data analysis, questions of authorship, responsibility, and erosion of human agency take on new significance. Viewing ethics as an adaptive strategy rather than a fixed rulebook, we compare two collaborative production models—the K-pop Song Camp system and Andy Warhol’s Factory. These cases illustrate how creative value can emerge from distributed agency and systemlevel verification instead of individual authorship, reflecting the ethical landscape shaped by generative AI. Cultural differences in AI perception are also discussed as factors that influence researchers’ attitudes. Additionally, a Bayesian analysis conducted in one of our courses shows that even a single instance of unusually similar assignment submissions can raise the inferred probability of generative AI involvement to over 90 percent, reinforcing the need for transparent and collaborative ethical frameworks in academic practice. We argue that research ethics in the age of generative AI should shift from prohibition to an adaptive, system-oriented form of governance grounded in openness and shared responsibility.

Index Terms—Collaborative creativity, cultural perception of AI, generative artificial intelligence, research ethics, transparency and accountability.

## I. INTRODUCTION

In science and engineering, artificial intelligence has become more than a tool that transforms research methodology. Traditionally, research involves iterative experimentation, design, and conceptualization, followed by expression through writing. Today, generative AI can design experiments, organize code, and even draft and review manuscripts. However, despite their fluency, AI-generated texts often feel soulless. Readers do not sense an author presence, making engagement difficult. This form of authorless writing is now proliferating rapidly, prompting academia and industry alike to demand clearer standards and responses. AI can be viewed as a means to an end, but it can also serve as a mirror through which we better understand human cognition itself, forcing us to reconsider the essence of research and what constitutes good scholarship.

## II. THE EVOLUTION OF ETHICS

Ethics is not a static rule, but an adaptive norm developed for collective survival. Thus, what is considered ethical varies between regions [1] and cultures [2]. Just as family ethics have evolved from hierarchical authority to companionshipbased relationships, research ethics must also evolve with the times. The evolution of K-pop offers a telling example of the interaction between technology and ethics. In the past, plagiarism was hard to detect due to limited access to foreign music. However, the internet accelerated the flow of information, making plagiarism immediately traceable. To avoid this, the Korean music industry developed collaborative songwriting systems such as Song Camps, where multiple composers co-create through highly distributed collaboration [3]. This structure has produced a globally distinctive originality which can be regarded as an adaptive evolution of ethics. Similarly, research in the age of generative AI will require a shift from individual-centered ethics to collaborationcentered ethics, as true research quality will depend as much on collective validation and transparency as on individual creativity.

## III. CULTURE AND PERCEPTION

Cultural perceptions of AI shape ethical attitudes. In the United States, robots are often viewed as servants or tools [4]. In Japan, they are seen as family members (Astro Boy) or helpers (Doraemon). Korea lies between these perspectives, balancing efficiency with emotional affinity. Such differences influence how researchers interact with AI. If AI is regarded merely as a machine that writes, ethics becomes an issue of control. But if it is viewed as a partner in thought, ethics becomes a principle of co-existence. For researchers striving for originality, using AI in writing introduces unfamiliar confusion, questioning whether the work reflects their own ideas or those of the AI. However, AI can serve as a valuable icebreaker [5] to initiate ideas or as a collaborator. Recent discussions even explore whether AI systems could be credited as scientific contributors or even listed as authors [6], further complicating the boundary between tool and collaborator.

## IV. OPPORTUNITIES AND PITFALLS

Generative AI is rapidly spreading in science and engineering, and several pitfalls emerge.

• First, there is the loss of creative agency. When AIgenerated designs or texts are used verbatim, the sense of authorship becomes diluted. The writing often feels fragmented, as if stitched together by multiple minds.

• Second, there is erosion of verification and trust. When AI output is mistaken for fact, reproducibility collapses. AI can cite fictitious concepts, people, or references, blurring the line between reality and fabrication.

• The third is the ambiguity of responsibility. Although credit for success is easily claimed, accountability for error becomes difficult to assign—should it lie with the human or AI?

Such issues are not new, and similar tensions have surfaced in the arts. Andy Warhol’s Factory system [7], in which he conceived ideas but delegated production to assistants, reinterpreted art as industrialized collaboration rather than individual genius. His Factory anticipated today’s diffusion of authorship under AI. For researchers, the lesson is clear: AI can produce, but interpretation and responsibility remain human. The ethical focus must therefore shift from Who created it? to Who is responsible for it? Furthermore, transparency in the process now matters as much as the quality of the outcome. Warhol never concealed his Factory system, yet he retained final authorship, i.e., an example of controlled openness. Similarly, modern musicians use the term sampling to navigate authorship in collaborative creativity.

## V. DISCUSSION

The ethics of generative AI inevitably returns us to the fundamental question: What is the essence of research itself? Ultimately, research ethics is not only about preventing misconduct, but about safeguarding the very nature of inquiry: How knowledge is produced, validated, embodied, and transmitted. As generative AI becomes increasingly involved in analysis, experimentation, interpretation, and writing, the boundary of authorship becomes porous. It is no longer unthinkable that future AI systems can be recognized as coauthors or even primary authors of scientific work. This shift will trigger methodological innovation. Certain fields may undergo extensive transformation through AI-driven generation and verification, particularly those dependent on tacit physical experience. Others may remain relatively insulated.

These changes require a re-examination of creativity within research training [8]. Human creativity, especially the ability to originate something that does not yet exist in any data set, becomes more critical. In disciplines grounded in physical experimentation, hands-on experience will gain increasing educational value [9], [10], which is direct interaction with instruments, materials, and unpredictable phenomena. Such embodied practices cultivate forms of intuition, judgment, and situational awareness that remain beyond the current capabilities of AI systems.Research ethics, in this emerging landscape, must therefore expand beyond guidelines for writing and data integrity to include the protection and cultivation of human creative processes.

However, the boundary between human experience and artificial capability is not fixed. As AI develops the capacity for multimodal perception through sensors [11]–[13], physical interaction through robotic control [14], [15], and autonomous adaptation in real-world environments [16], [17], even handson experimentation can eventually be partially or fully delegated to intelligent systems. When AI agents can observe the world, manipulate objects, conduct experiments, and make iterative decisions, they will no longer simply generate hypotheses or draft papers. Instead, they will participate in the entire research cycle. The ethical considerations that follow from this are profound: How should responsibility be distributed among human researchers and physically embodied AI agents? What does it mean to experience or validate knowledge when a nonhuman system performs the experiment?

In this transitional era, dual educational innovation becomes necessary [18], [19]. First, researchers need frameworks to understand, audit and guide AI-driven creativity and experimentation. Second, there must be parallel investment in enabling humans to cultivate forms of creativity, interpretation, and embodied judgment that remain uniquely meaningful. Education reforms must therefore address not only AI control, but also the enhancement of human cognitive and physical research skills in ways that complement the growing role of intelligent systems [20].

## VI. CONCLUSION

As AI becomes a creative partner capable of writing, designing, and even conducting experiments, the key question shifts from whether researchers used AI to how they used it. This transformation forces a renewed reflection on the essence of research, highlighting the growing importance of human creativity, interpretation, and hands-on experimentation, even as embodied AI with sensing and control capabilities becomes increasingly integrated into these domains. Just as the K-pop industry turned technological challenges into global competitiveness through collaborative systems, science and engineering must pursue transparency, shared verification, and cooperative authorship.

## APPENDIX: BAYESIAN ESTIMATION OF THE PROBABILITY OF USING GENERATIVE AI

## A. Problem Definition

In one of the author’s courses on robot intelligence, the assignments are designed not merely to test correctness, but to encourage students to explore ideas independently and develop creative reasoning. We consider the following question: If a student’s assignment resembles another student’s submission, what is the probability $P ( H \mid E )$ that the student used generative AI? where:

• H: the event that a student used generative AI, and

• E: the event that the student’s submission is similar to another assignment.

## B. Prior Probability and Likelihood Estimation

1) Prior probability of using generative AI: A recent nationwide survey reported that 78% of university students had used generative AI for academic activities, and among them, writing assignments or reports was the most common use case at 88.6% [21]. Assuming independence between these two statistics, we estimate:

$$
P ( H ) = 0 . 7 8 \times 0 . 8 8 6 = 0 . 6 9 1 ,
$$

$$
P ( \neg H ) = 1 - P ( H ) = 0 . 3 0 9 .
$$

2) Likelihood of similarity given AI usage (our experiment): To understand how often generative AI produces similar outputs for identical prompts, we conducted an experiment in our course. Using the GPT-5 model [22], we provided only the assignment template in a session isolated from prior conversation history and generated ten independent outputs.

Among these ten responses, two exhibited a highly similar structure, line of reasoning, and set of results. Thus:

$$
P ( E \mid H ) = { \frac { 2 } { 1 0 } } = 0 . 2 0 .
$$

3) Likelihood of similarity without AI usage: To approximate the natural similarity rate among independently written human assignments, we referred to publicly reported plagiarism statistics from a large introductory university course. In that data set, 8 of 157 students submitted work sufficiently similar to be flagged.

Assuming that (i) generative AI was not involved due to strict prohibitions in that course, and (ii) such similarity rates are representative of large student populations, we estimate:

$$
P ( E \mid \neg H ) = { \frac { 8 } { 1 5 7 } } = 0 . 0 5 1 0 .
$$

Note that no specific institution, field, or semester is referenced; only aggregate publicly available numbers are used.

## C. Posterior Probability Inference

Applying Bayes’ theorem, the probability that a student used generative AI given that their assignment resembles another submission becomes:

$$
P ( H \mid E ) = { \frac { 0 . 2 0 \times 0 . 6 9 1 } { 0 . 2 0 \times 0 . 6 9 1 + 0 . 0 5 1 0 \times 0 . 3 0 9 } } = 0 . 9 0 1 .
$$

Thus, a single observed similarity elevates the posterior probability to approximately 90.1%.

If a second similar assignment is observed at a later time, using the updated prior $P ( H ) = 0 . 9 0 1$ :

$$
P ( H \mid E ) = { \frac { 0 . 2 0 \times 0 . 9 0 1 } { 0 . 2 0 \times 0 . 9 0 1 + 0 . 0 5 1 0 \times 0 . 0 9 9 } } = 0 . 9 7 5 .
$$

Multiple occurrences substantially strengthen the posterior confidence that generative AI was used.

## REFERENCES

[1] E. Awad, S. Dsouza, R. Kim, J. Schulz, J. Henrich, A. Shariff, J.-F. Bonnefon, and I. Rahwan, “The moral machine experiment,” Nature, vol. 563, no. 7729, pp. 59–64, 2018.

[2] C. Rapaille, The Culture Code: An Ingenious Way to Understand Why People Around the World Live and Buy as They Do. Crown Currency, 2007.

[3] D.-h. Kim, Kim Do-hoon’s Composition Method: Professional Guide to Popular Music Composition. 1458music, 2018.

[4] T. Williams, Degrees of Freedom: On Robotics and Social Justice. MIT Press, 2025.

[5] S. Jo, S. Shin, and S.-W. Kim, “Interactive storyboarding system leveraging large-scale pre-trained model,” Available at SSRN 4399439, 2023.

[6] “Open conference of AI agents for science 2025,” https://agents4science.stanford.edu/, 2025, stanford University. Accessed: 2025-12-02.

[7] A. Warhol, The Philosophy of Andy Warhol: From A to B and Back Again. Houghton Mifflin Harcourt, 1977.

[8] S. Shin and S.-W. Kim, “Exploring creativity education in researchoriented college of engineering,” Journal of Engineering Education Research, vol. 26, no. 1, pp. 45–57, 2023.

[9] J. Lee and S.-W. Kim, “Snu idea factory with integrative approaches: From physical space, education, to culture,” in Proceedings of 1st International Symposium on Academic Makerspaces, 2016, pp. 58–61.

[10] S.-W. Kim, “Hierarchical curriculum structure in academic makerspaces,” IJAMM, 2020.

[11] H.-Y. Kim, B. Park, B. Choi, H. Cho, B. Kim, S. Lee, M. Jeon, S.- W. Seo, and S.-W. Kim, “Radar-based nlos pedestrian localization for darting-out scenarios near parked vehicles with camera-assisted point cloud interpretation,” arXiv preprint arXiv:2508.04033, 2025.

[12] B. Park, H.-Y. Kim, B. Choi, H. Cho, B. Kim, S. Lee, M. Jeon, and S.- W. Kim, “mmwave radar-based non-line-of-sight pedestrian localization at t-junctions utilizing road layout extraction via camera,” arXiv preprint arXiv:2508.02348, 2025.

[13] M. Jeon, J.-K. Cho, H.-Y. Kim, B. Park, S.-W. Seo, and S.-W. Kim, “Non-line-of-sight vehicle localization based on sound,” IEEE Transactions on Intelligent Transportation Systems, 2024.

[14] J.-K. Cho, C. Kim, M. K. M. Jaffar, M. W. Otte, and S.-W. Kim, “Lowlevel controller in response to changes in quadrotor dynamics,” in 2023 IEEE International Conference on Robotics and Automation (ICRA). IEEE, 2023, pp. 5317–5323.

[15] S.-W. Kim and S.-W. Seo, “Cooperative unmanned autonomous vehicle control for spatially secure group communications,” IEEE Journal on selected areas in communications, vol. 30, no. 5, pp. 870–882, 2012.

[16] M. Oh, C. Kim, S.-W. Seo, and S.-W. Kim, “Language as cost: Proactive hazard mapping using vlm for robot navigation,” arXiv preprint arXiv:2508.03138, 2025.

[17] C. Kim, K. Kim, M. Oh, H. Baek, J. Lee, D. Jung, S. Woo, Y. Woo, J. Tucker, R. Firoozi et al., “E2map: Experience-and-emotion map for self-reflective robot navigation with language models,” in 2025 IEEE International Conference on Robotics and Automation (ICRA). IEEE, 2025, pp. 12 811–12 817.

[18] S. W. Kim, “An interdisciplinary capstone course on creative product development with cross-college collaboration,” International Journal of Engineering Education, vol. 36, no. 3, pp. 919–928, 2020.

[19] W. Leung, Y. Wang, S.-W. Kim et al., “Global product development: Project-based multidisciplinary joint course,” in DS 95: Proceedings of the 21st International Conference on Engineering and Product Design Education (E&PDE 2019), University of Strathclyde, Glasgow. 12th-13th September 2019, 2019.

[20] S.-W. Kim, “Kepler vs newton: teaching programming and math to almost all-majors in a single classroom,” in 2020 IEEE International Conference on Teaching, Assessment, and Learning for Engineering (TALE). IEEE, 2020, pp. 956–957.

[21] ITDaily, “78% of university students use generative ai for academic purposes,” http://www.itdaily.kr/news/articleView.html?idxno=228010, Oct. 2024, accessed: 2025-12-02.

[22] OpenAI, “Gpt-5 technical overview,” https://openai.com, 2025, large Language Model documentation. Accessed: 2025-12-02.