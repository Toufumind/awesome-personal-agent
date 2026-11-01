# Personal agent papers & benchmarks

[中文](PAPERS.md) · [Main list](../README.en.md)

**Understand what was measured before comparing scores.** This guide separates evaluations / benchmarks from methods / systems, and distinguishes direct personal-context research, transferable general memory / execution capabilities, and specific privacy / security risks.

Literature and resource check: **2026-10-31**. **176 distinct papers**: 86 evaluation entries, 105 method entries, and 9 human-study entries. Proactive Agent, MemoProAgent, PbP/InTU, Ask-before-Plan/CEP, PersonalAlign/HIM-Agent, PEToolLLM/PEToolLLaMA, MemGuide/MS-TOD, Me-Agent/User FingerTip, PPP/UserVille, PUMA/PersonalWAB, MPR/HybridMem, PrivacyLens-Live/PrivacyChecker, PTBench/PTool, PAL-Bench/H²Memory, PENGUIN/RAISE, Searching for Privacy Risks, THEANINE/TeaFarm, Operationalizing Contextual Integrity, ImplexConv/TaciTree, Context-Time Memory, EvoArena/EvoMem, DAM/DABench, DuLeMon/PLATO-LTM, and ActMem/ActMemEval each contribute a benchmark and a method; each paper is counted once. Sources are paper abstracts and the explicitly identified passages below, author project pages, official repositories, and dataset cards. **No installation, independent benchmark run, model training, or security audit was performed.** This is a selective reading guide, not a comprehensive survey, latest-paper feed, or product ranking.

**Entry checks:** B25–B86, M16–M105, and H1–H9 were checked on 2026-11-01; earlier entries retain their original check dates.

**Reading scope:** Each entry records the abstract, relevant passages, and resource pages actually consulted. No claim is made that every paper was read end to end. Translation is not an additional verification.

Years and versions identify the listed paper, not the current project. Original task counts may differ from current code. Branches, dataset cards, and resource status are observations on the check date, not pinned reproduction snapshots. “Public” means an official entry point was found, not that commercial reuse is permitted, dependencies install, weights are complete, or results reproduce.

## Contents

- [Start with a research question](#reading-paths)
- [Evaluation: User profiles and preferences](#user-profile-evaluation)
- [Evaluation: Long-term personal memory](#personal-memory-evaluation)
- [Evaluation: Personalized planning and action](#planning-action-evaluation)
- [Evaluation: Proactivity and clarification](#proactive-clarification-evaluation)
- [Evaluation: Privacy, authorization and safety](#safety-evaluation)
- [Evaluation: Transferable memory and sequential tasks](#transferable-memory-evaluation)
- [Evaluation: Transferable execution and interaction](#execution-evaluation)
- [Methods: User understanding, profiles, and preference learning](#user-understanding-methods)
- [Methods: Memory and persistent state](#memory-methods)
- [Methods: Planning, tools, and action](#planning-action-methods)
- [Methods: Proactivity and clarification](#proactive-clarification-methods)
- [Methods: Privacy, authorization, and safety](#privacy-safety-methods)
- [Human studies](#human-studies)
- [Comparison and reproducibility](#reproducibility)
- [Sources and rights](#sources-and-rights)

**Evaluation navigation:** Groups follow the question primarily measured, not keywords in the title. Each B entry has one home; scope and overlapping questions remain in the entry and cross-links. Personal-context, transferable and risk evidence must still be distinguished. IDs, benchmark/method boundaries and dedicated human studies stay unchanged. **No single benchmark evaluates an entire personal agent.**

**Method navigation:** The five themes below are this guide’s editorial reading map, not the papers’ own taxonomy or one implemented architecture. Each M entry has one primary home; overlapping capabilities remain described in the entry. IDs and entry links stay stable, and dedicated human-study entries remain separate; method entries may also include human evidence. These are research mechanisms, not certified personal-assistant products.

<a id="reading-paths"></a>
## Start with a research question

| Research question | Start here | Still needs separate testing |
| --- | --- | --- |
| Do revised plans retain preferences? | [PDEU-Bench](#benchmark-pdeu-bench) | Real services, full execution, and authorization |
| Does the agent elicit preferences for later? | [ATRBench](#benchmark-atrbench) | Evolving real preferences and asking costs |
| Are unreliable claims stored and reused? | [PASB](#benchmark-pasb) | Population risk and longitudinal use |
| Does it remember user statements and updates? | [LongMemEval](#benchmark-longmemeval), [LoCoMo](#benchmark-locomo); [MemoryAgentBench](#benchmark-memoryagentbench) for general incremental memory | Erasure, correction, user isolation, real longitudinal use |
| Does the answer fit this person's preferences? | [LaMP](#benchmark-lamp), [PersonaMem](#benchmark-personamem-v1) / [PersonaMem-v2](#benchmark-personamem-v2), [PersonaBench](#benchmark-personabench), [PrefEval](#benchmark-prefeval) | Human satisfaction, safe private-document deployment; compare QA / generation / MCQ protocols separately |
| Does memory change tool arguments and subsequent actions? | [Mem2ActBench](#benchmark-mem2actbench), [MemoryArena](#benchmark-memoryarena) | Real execution, side-effect authorization, interrupted-task recovery |
| When should it help, clarify, or stay quiet? | [ProactiveBench](#benchmark-proactivebench-lu) / [Proactive Agent](#method-proactive-agent), [KnowU-Bench](#benchmark-knowu-bench), [MemoProBench](#benchmark-memoprobench) / [MemoProAgent](#method-memoproagent), [π-Bench](#benchmark-pi-bench) | Human acceptance, interruption cost, restraint after rejection, undo, authorization |
| Can it complete multi-app tasks? | [AppWorld](#benchmark-appworld), [WebArena](#benchmark-webarena), [OSWorld](#benchmark-osworld), [AndroidWorld](#benchmark-androidworld) | Real accounts, environment changes, irreversible actions |
| Does it reliably follow workflows across repeated runs? | [τ-bench](#benchmark-tau-bench) | Simulated versus real users and process-level safety |
| Should accessible information be shared outward? | [PrivacyLens](#benchmark-privacylens), [AgentCIBench](#benchmark-agentcibench); [AgentDojo](#benchmark-agentdojo) separately tests indirect prompt injection | Full privacy compliance, cross-user / multi-agent isolation, all attack surfaces |
| How can individual feedback teach preferences? | [P-RLHF](#method-p-rlhf) | Cold start, preference changes, longitudinal human utility; not memory storage |
| How should persistent memory and its lifecycle be managed? | [MemGPT](#method-memgpt), [MemoryBank](#method-memorybank), [A-MEM](#method-a-mem), [Mem0](#method-mem0), [Zep](#method-zep), [MemOS](#method-memos) | Invalidation or non-use is not physical erasure; permissions, scheduling, observability |
| How can experience, skills, and agent coordination be reused? | [ReAct](#method-react), [Reflexion](#method-reflexion), [Voyager](#method-voyager), [ExpeL](#method-expel), [AutoGen](#method-autogen) (historical) | Longitudinal human utility, single-agent controls, stale experience, operating cost |


**Personal-planning reading route:** Start with [TravelPlanner+](#benchmark-travelplanner-plus) for turning profiles and personal concepts into plan conditions; [PbP](#benchmark-pbp) / [InTU](#method-intu) for inferring unstated preferences from behavior; [Ask-before-Plan](#benchmark-ask-before-plan) / [CEP](#method-cep) for clarification; [PDEU-Bench](#benchmark-pdeu-bench) for retaining preferences through plan updates; and [AuthorizationBench](#benchmark-authorizationbench) for distinguishing completion from authorized action. This question-based sequence is not evidence of one complete system. Cross-session state, longitudinal utility, and changes in authorization need separate testing.

<a id="user-profile-reading-path"></a>
### User profiles: four questions to read by

This cross-cutting route **preserves the benchmark / method distinction; a paper can appear in several rows**. “Profile” includes user histories, preference summaries and learned user representations—not necessarily a fixed profile card. This is the list's synthesis, not the papers' own taxonomy.

| Question | Start here; what to look for | What this does not establish |
| --- | --- | --- |
| **1. How do we understand the user?** | [MemoryBank](#method-memorybank): summarize user information from past interactions. [P-RLHF](#method-p-rlhf): learn user representations from explicit preference text and individual comparison feedback. [PrefEval](#benchmark-prefeval): test recognition and following of explicit / implicit preferences. | A user representation is not a complete, accurate personality model. PrefEval tests capability; it is not a profiling system. |
| **2. How do we store and update it?** | [MemoryBank](#method-memorybank): store, retrieve, reinforce and fade memories. [Zep](#method-zep): handle conflicting relations with timestamps while retaining history. Then use [LongMemEval](#benchmark-longmemeval) to test answers after updates. | Fading or invalidation is not physical deletion. P-RLHF training is not a continual memory-update mechanism either. |
| **3. How do we apply it?** | [LaMP](#benchmark-lamp): use user history for personalized classification / generation. [P-RLHF](#method-p-rlhf): condition generation on learned user preferences. For actions, continue to [Mem2ActBench](#benchmark-mem2actbench): memory-to-tool arguments. | Retrieving history and learning user representations are different approaches. Preference-aligned answers or correct tool arguments do not establish real task completion. |
| **4. How do we evaluate it?** | [LaMP](#benchmark-lamp): personalized task quality. [PrefEval](#benchmark-prefeval): following known preferences. [PersonaMem (v1)](#benchmark-personamem-v1): recognizing changing preferences and transferring them to new situations. | These are not interchangeable metrics. PersonaMem's synthetic histories and four-choice protocol cannot substitute for open-ended response quality or long-term satisfaction of real users. |

<a id="evaluation-a-personal-context-memory-and-proactivity"></a>
<a id="personal-evaluation"></a>
<a id="user-profile-evaluation"></a>
## Evaluation: User profiles and preferences

Does the response fit this person? Read profile inference, preference following and personalized response quality here. These protocols are not interchangeable: static survey evidence (B80), synthetic personas and constructed dialogues are not longitudinal assistant use. For eliciting unknown preferences, continue to [proactivity and clarification](#proactive-clarification-evaluation).

<a id="benchmark-lamp"></a>
### B1. LaMP · Personalized language tasks

[LaMP: When Large Language Models Meet Personalization](https://aclanthology.org/2024.acl-long.399/) — ACL 2024.

**Checked / reading scope:** 2026-10-31; Paper abstract and §2.3 metric passages; official README licensing notes and data-download page.

- **Input → output:** Task input and the user's historical items → a personalized label or text. The paper covers three classification and four generation tasks.
- **Measures:** Accuracy / F1, rating MAE / RMSE, and generation ROUGE; user-based and time-based splits distinguish generalization settings.
- **Limits:** Tests personalized retrieval and generation, not multi-step tool execution or longitudinal use with real users.
- **Resources:** [Official code](https://github.com/LaMP-Benchmark/LaMP), [data](https://lamp-benchmark.github.io/download). Code and construction methods use CC BY-NC-SA 4.0; underlying datasets retain their own licenses.

<a id="benchmark-personamem-v1"></a>
### B4. PersonaMem · Evolving user profiles

[Know Me, Respond to Me: Benchmarking LLMs for Dynamic User Profiling and Personalized Responses at Scale](https://arxiv.org/abs/2504.14225) — COLM 2025; this entry covers the original benchmark / v1 data.

**Checked / reading scope:** 2026-10-31; Original-paper revision: §2 task definition and relevant §4 results passages; official README data format and v1 dataset card.

- **Input → output:** Synthetic multi-session history with changing preferences and a new-scenario question → one of four candidate responses.
- **Measures:** Selection accuracy across seven query types, context lengths, and distances from preference mentions; separates recall, updates, and preference transfer.
- **Limits:** Four-choice accuracy is not open-ended personalized response quality. Synthetic personas are not longitudinal human participants. Do not mix with PersonaMem-v2 data.
- **Resources:** [Official code](https://github.com/bowen-upenn/PersonaMem), [v1 data](https://huggingface.co/datasets/bowen-upenn/PersonaMem-v1), including 32k, 128k, and 1M context settings.

<a id="benchmark-personabench"></a>
### B7. PersonaBench · Understanding users through private documents

[PersonaBench: Evaluating AI Models on Understanding Personal Information through Accessing (Synthetic) Private User Data](https://aclanthology.org/2025.findings-acl.49/) — Findings of ACL 2025; inspected text: [arXiv v2, 2025-08-20](https://arxiv.org/html/2502.20616v2).

**Checked / reading scope:** 2026-10-31; Abstract, §5.3 metrics, and official README examples and licensing.

- **Input → output:** Timestamped synthetic private documents, such as chats and purchase records, plus a personal question → a factual answer, such as a music preference found in chat.
- **Measures:** Retrieval Recall / NDCG and end-to-end answer Recall / F1; report these separately.
- **Limits:** Personal-context QA, not autonomous execution or privacy protection. Synthetic social context does not establish real-user personalization. The v1.0 public examples describe two communities of three people each, not the full paper dataset.
- **Resources:** [Official code, public evaluation data, and README](https://github.com/SalesforceAIResearch/personabench). CC BY-NC-SA 4.0, with additional usage restrictions in the README; inspect both before reuse.

<a id="benchmark-prefeval"></a>
### B8. PrefEval · Remembering is not following preferences

[Do LLMs Recognize Your Preferences? Evaluating Personalized Preference Following in LLMs](https://arxiv.org/html/2502.09597v1) — ICLR 2025; inspected v1, 2025-02-13.

**Checked / reading scope:** 2026-10-31; Abstract, §§2.2, 2.5, and 3.4, official README and LICENSE.

- **Input → output:** Explicit or implicit preferences, distractor turns, and a later request → free-form responses or four-choice answers; for example, restaurant advice reflecting an earlier dietary preference. Three expression forms derive from 1,000 base preference–question pairs, not 3,000 independent users.
- **Measures:** Four binary judge checks aggregated into error types for generation; accuracy for classification. Report separately.
- **Limits:** Directly tests preference following. Here personalization proactiveness means applying known preferences without reminders, not background monitoring or independently launching tasks, nor actual user satisfaction.
- **Resources:** [Official code and complete formats](https://github.com/amazon-science/PrefEval), [explicit-preference data](https://huggingface.co/datasets/siyanzhao/prefeval_explicit). The [repository license](https://github.com/amazon-science/PrefEval/blob/main/LICENSE) is CC BY-NC 4.0. The linked HF data is only the explicit subset, not all three forms.

<a id="benchmark-personamem-v2"></a>
### B9. PersonaMem-v2 · Implicit preferences, ownership, and non-use

[PersonaMem-v2: Towards Personalized Intelligence via Learning Implicit User Personas and Agentic Memory](https://arxiv.org/html/2512.06688v1) — 2025 preprint; inspected v1, 2025-12-07. Distinct from the original PersonaMem paper in B4.

**Checked / reading scope:** 2026-10-31; Abstract, §§2.3–2.4 and 4.1, official dataset card and family README.

- **Input → output:** Synthetic multi-session histories and a current question → open-ended or four-choice answers, covering implicit, changing, third-party, sensitive, and ask-to-forget information.
- **Measures:** Correct-option matching for MCQ; aggregated judgments from three judges for open responses. Keep protocols separate.
- **Limits:** Not using a fact after a forget request does not prove erasure from storage, backups, or model weights. The paper also trains a readable-memory system; those results are not generic deployed-agent capabilities. This entry covers text settings.
- **Resources:** [Official data](https://huggingface.co/datasets/bowen-upenn/PersonaMem-v2): CC BY 4.0; [family repository](https://github.com/bowen-upenn/PersonaMem): MIT. The current card includes later multimodal resources. Pin text revision, split, 32k / 128k setting, and evaluation mode. A complete v2 RL reproduction package was not confirmed.

<a id="benchmark-pdr-bench"></a>
### B40. PDR-Bench · Research reports tailored to an individual

[Towards Personalized Deep Research: Benchmarks and Evaluations](https://arxiv.org/html/2509.25106v3) — ICLR 2026; inspected v3, March 4, 2026.

**Verified / actual reading scope:** 2026-11-01; v3 §3 construction, relevant §4 PQR evaluation passages, Appendix A limitations, and B.1–B.2 settings/subset selection; author README, repository root, and LICENSE. Selected passages, not a line-by-line full-paper review; no installation, execution, or experimental reproduction.

- **Evaluation:** Fifty tasks and 25 volunteer-grounded profiles produce 250 task–user pairs. PQR separately measures personalization, content quality and factual/citation reliability.
- **Limits:** Structured personas are real-user grounded, but annotators simulate dynamic interactions. Collection is Chinese-centered with English translations. Appendix selection proceeds 250→150→50; benchmark size is not full experimental coverage. Report quality does not demonstrate safe execution or long-term human utility.
- **Resources:** [Author code/data](https://github.com/OPPO-PersonalAI/PersonalizedDeepResearchBench), verified Apache-2.0 root license; model/search APIs and upstream asset terms remain separate requirements.

<a id="benchmark-personalens"></a>
### B41. PersonaLens · Personalized dialogue across domains

[PersonaLens](https://aclanthology.org/2025.findings-acl.927/) — Findings ACL 2025; inspected [arXiv v1](https://arxiv.org/html/2506.09902v1), June 11, 2025.

**Verified / actual reading scope:** 2026-11-01; v1 §2 profiles/tasks/simulation protocol, §3 experimental setup, relevant §4 evaluation passages, and Limitations; ACL publication record, author README, and LICENSE.md. Selected passages, not a line-by-line full-paper review; no installation, execution, or experimental reproduction.

- **Evaluation:** 111 tasks across 20 domains, with simulated users and judges assessing personalization, task completion, naturalness and coherence.
- **Limits:** The 1,500 profiles use real PRISM demographics but generated preferences, histories and contexts—not 1,500 real assistant users. Section 3 states that all reported experiments use a random subset of 50 profiles, comprising 3,283 single-domain and 813 multi-domain dialogues; construction scale is not evaluation coverage. Bookings and purchases are simulated dialogue, not executed actions. Demographic conditioning can reproduce stereotypes.
- **Resources:** [Author code/data](https://github.com/amazon-science/PersonaLens), verified **CC-BY-NC-4.0** `LICENSE.md`; execution requires Amazon Bedrock access.

<a id="benchmark-pal-bench"></a>
### B52. PAL-Bench · Requirements and preferences from long-term personal histories

[Mem-PAL: Towards Memory-based Personalized Dialogue Assistants for Long-term User-Agent Interaction](https://arxiv.org/html/2511.13410v2) — v2, 2025-11-26; AAAI 2026 Oral. Same paper as M47.

**Actual reading scope:** PAL-Bench construction/tasks, H²Memory framework and Experiments, including external validation; repository README and file listing. Appendices were sampled, not comprehensively read.

- **Input → output:** behavioral logs plus dialogue history → restated requirements, proposed/selected solutions, multi-turn responses.
- **Measures:** BLEU, GPT-4 implicit-need judgments, solution-selection scores and pairwise dialogue judgments.
- **Boundary:** PAL-Set has 100 synthetic users, approximately 29 sessions and 9.4 simulated months each; human verification does not make this a longitudinal user study. Multi-turn users are simulated by an LLM. External validation covers only LongMemEval’s single-session-preference subset and uses the dialogue components (Topic Outline + Principle), not the complete four-component system.
- **Resources/language:** [official code/data](https://github.com/hzp3517/Mem-PAL). README identifies the English version as a DeepSeek-V3 translation without item-by-item human verification. Appendix B states an intended PAL-Set release under CC BY-NC 4.0; this author statement uses future-release wording and is separate from verifying the distributed dataset’s terms or the implementation’s license. Repository reuse-license verification remains incomplete.

<a id="benchmark-personafeedback"></a>
### B59. PersonaFeedback · Response selection with explicit personas

[PersonaFeedback: A Large-scale Human-annotated Benchmark For Personalization](https://arxiv.org/html/2506.12915v1) — arXiv v1, 2025-06-15, work in progress.

Evaluates binary response selection given explicit personas using selection accuracy against labels, with 8,298 human-labelled cases—not 8,298 real participants. Twenty real seed profiles underpin constructed personas; 200 are used for benchmarking. Model-generated material is human-filtered, with majority labels from nine evaluators. This is not a longitudinal user study or evidence that RAG generally fails. Subjective labels and persona simplification constrain conclusions. The [public dataset](https://huggingface.co/datasets/PersonalAILab/PersonaFeedback) declares Apache-2.0; its viewer currently reports incompatible schemas. No formal privacy guarantee was established.

**Reading scope:** §3 construction/annotation, §4 evaluation setup, limitations; official dataset card and viewer status. Targeted construction, evaluation and limitations; dataset card/viewer, not a full dataset audit.

<a id="benchmark-personaconvbench"></a>
### B69. PERSONA-Bench · Multi-user conversational history

[A Personalized Conversational Benchmark: Towards Simulating Personalized Conversations](https://arxiv.org/html/2505.14106v2) — [NeurIPS 2025 MTI-LLM workshop (not main conference)](https://research.adobe.com/publication/a-personalized-conversational-benchmark-towards-simulating-personalized-conversations/); methods and experiments reviewed in arXiv v2, 2025-05-25.


- **Scope**: §§2–4, appendix C; official `Latest` README/data card.
- **Input → output**: prior conversational/user trajectories constructed from raw Reddit posts in ten domains → binary label, community-score forecast or next-user text.
- **Measures**: accuracy/F1/MCC, regression errors and generation similarity; separate protocols. Temporal access and target masking are reported, not independently audited.
- **Comparison protocol**: §C.3 generates 10 candidates for every model except Claude and selects the highest-SBERT candidate; Claude uses one candidate. Cross-model generation scores therefore do not represent single-response performance under equal sampling budgets.
- **Boundary**: “sentiment” is score-derived, not validated personal emotion. Historical evaluation is not deployed-assistant or mental-health effectiveness evidence.
- **Resources**: [code](https://github.com/PERSONA-bench/PERSONA/tree/Latest) / [data](https://huggingface.co/datasets/PERSONABench/PERSONA-Bench). HF says MIT; repository says research-only/Reddit TOS. Resolve this discrepancy before reuse; do not describe data as unrestricted MIT.

<a id="benchmark-personal-laps"></a>
### B71. Doing Personal LAPS · Human-involved multi-session preference data

[Doing Personal LAPS: LLM-Augmented Dialogue Construction for Personalized Multi-Session Conversational Search](https://arxiv.org/abs/2405.03480v1) — SIGIR 2024; [proceedings DOI](https://doi.org/10.1145/3626772.3657815).

**Checked / reading scope:** 2026-11-01; construction §3, recommendation/evaluation §4, results §5 including Tables 7–8, and repository resource/license documentation.

- **Construction / input → output:** One worker writes both dialogue roles with LLM guidance, expressing actual preferences. Histories support preference extraction and personalized recommendation across recipe and movie domains, totaling 1,406 dialogues.
- **Measurement:** Dialogue quality/diversity, extraction, preference utilization, and human judgments of recommendations and rationales.
- **Boundary / counterexample:** Constructed self-dialogues are not deployment logs. Preference memory improves recipe recommendations and rationales in both domains, but not movie recommendation quality; movie utilization F1 is numerically slightly lower (.424 to .419); the paper does not support inferring a statistically significant decrease.
- **Resources:** The [MIT-labelled repository](https://github.com/informagi/laps) includes data, collection and evaluation code, and downstream resources. Listed as data/evaluation evidence, not general autonomous action capability.

<a id="benchmark-lamp-qa"></a>
### B72. LaMP-QA · Personalized long-form answers

[LaMP-QA: A Benchmark for Personalized Long-form Question Answering](https://aclanthology.org/2025.emnlp-main.60/) — EMNLP 2025 Main; arXiv `2506.00137v2` is the same work.

**Checked / reading scope:** 2026-11-01; formulation, construction, metrics, baselines and experiments §§2–5, limitations, repository documentation and dataset card.

- **Input → output:** Real StackExchange question histories plus a current title → personalized long-form answers. The current post narrative is withheld from generation and used for evaluation.
- **Measurement:** Rubric-based requirement coverage and human comparisons; PlanPers/RAG wins are 35%/26% over 100 comparisons, with the remainder tied.
- **Boundary / counterexample:** Real posts are not assistant deployment logs. Narratives may omit needs; annotators are not the original users. Requirement coverage is not deployment satisfaction, privacy protection or action execution.
- **Resources:** [Code](https://github.com/LaMP-Benchmark/LaMP-QA) and [data](https://huggingface.co/datasets/alireza7/LaMP-QA) are accessible. The paper identifies upstream SE-PQA as CC-BY-SA 4.0; a separate downstream code/data license was not verified. Do not substitute the article license. LaMP-QA is distinct from LaMP and LongLaMP.

<a id="benchmark-hicupid"></a>
### B73. HiCUPID · Synthetic personalized dialogue and proxy evaluation

[Exploring the Potential of LLMs as Personalized Assistants: Dataset, Evaluation, and Analysis](https://aclanthology.org/2025.acl-long.504/) — ACL 2025 Main. HiCUPID is the resource name; arXiv `2506.01262v1` is the same paper.

**Checked / reading scope:** 2026-11-01; construction §3, evaluation §4, results §5/Tables 3–4, license Appendix A12, and official repository/data/model cards.

- **Input → output:** Synthetic preference, profile and schedule dialogues → personalized single-/multi-information answers for 1,500 synthetic users, not real interaction logs.
- **Measurement:** GPT-4o and distilled Llama-3.2 evaluators, separate seen-user/unseen-question and unseen-user/unseen-question settings, and human evaluation of four LLMs’ zero-shot outputs on 100 persona QA pairs sampled from Test Set 1—not 100 responses in total.
- **Boundary / counterexample:** DPO alone does not consistently improve personalization in the reported settings; multi-information reasoning remains difficult. Proactiveness means suggestions in responses, not autonomous initiation or external actions.
- **Resources:** [Code](https://github.com/12kimih/HiCUPID), [data](https://huggingface.co/datasets/12kimih/HiCUPID) and [evaluator](https://huggingface.co/12kimih/Llama-3.2-3B-HiCUPID) cards claim Apache-2.0; the Llama-3.2 base-model Community License remains a separate consideration. The project label does not establish that every component is free of additional restrictions.

<a id="benchmark-implexconv"></a>
### B76. ImplexConv: cross-session implicit reasoning

Tests personalized QA through supportive/opposed implicit scenarios; the paper reports 2,500 examples of roughly 100 sessions. Generated reasoning scenarios are combined with existing-dataset distractors and selective human verification, not a field study. Separate generation/evaluation models do not establish contamination freedom.

- Paper/version: [Toward Multi-Session Personalized Conversation: A Large-Scale Dataset and Hierarchical Tree Framework for Implicit Reasoning, 2503.07018v1](https://arxiv.org/html/2503.07018v1), 2025-03-10.
- Cross-reference: M74; same paper, counted once. Internal IMPersona/IMPACT naming remnants are not separate papers.
- Assets: [Official repository](https://github.com/Kaylee0501/ImplexConv) contains framework/evaluation files; code license unverified. Current cards list [opposed](https://huggingface.co/datasets/Kaylee0501/ImplexConv-opposed) 1,550 + [supportive](https://huggingface.co/datasets/Kaylee0501/ImplexConv-supportive) 814 = 2,364 examples, unlike the paper’s total. Their MIT data label does not establish code licensing.
- Inspected: §§3–6, limitations, README, dataset cards, repository root.

<a id="benchmark-evoarena"></a>
### B79. EvoArena · PersonaMem-Evo subset

**Conditionally direct evaluation: synthetic preference evolution**

[Paper](https://arxiv.org/html/2606.13681v2) · arXiv v2, 2026-06-17. Method: M79; count the shared paper once.

PersonaMem-Evo generates interaction histories and evolving preferences from synthetic personas, testing four-way single-pattern transfer, multi-pattern synthesis, conflict resolution, and temporal-trajectory inference, with persona-only/no-context shortcut filtering. It is not a real-user longitudinal study. Terminal-Bench-Evo and SWE-Chain-Evo supply adjacent, transferable evidence.

**Resources:** The [official data card](https://huggingface.co/datasets/Aiden0526/PersonaMem-Evo) reports 10 personas/505 examples, empty 128k links, a broken viewer, and no license metadata. The [repository](https://github.com/Aiden0526/EvoArena) is not a verified complete release; its license remains pending. The paper’s CC BY 4.0 does not establish asset permissions.

**Verification date / actually read:** 2026-11-01; version page, §§3–6, relevant Appendices A/E, repository README/root, and PersonaMem-Evo data card. No reproduction run.

<a id="benchmark-indievaluecatalog"></a>
### B80. Benchmark — IndieValueCatalog

[Can Language Models Reason about Individualistic Human Values and Preferences?](https://aclanthology.org/2025.acl-long.336/) — ACL 2025 main-conference long paper; examined [arXiv:2410.03868v2, May 31, 2025](https://arxiv.org/html/2410.03868v2).

**Checked / reading scope**: November 1, 2026; relevant §§2–4, limitations/ethics, Appendix B, official README/root listing.

- **Task and metrics**: Predict unseen individual value choices from WVS statements; accuracy and inequity metrics.
- **Evidence**: 93,279 real survey respondents; 800 held out, not interactive-agent users.
- **Limits**: Adjacent individual-value modeling; static surveys/single-prompt limitations; demographics cannot replace individual evidence. Privacy, manipulation and autonomy remain concerns.
- **Resources and rights**: [Official repository](https://github.com/liweijiang/indievalue) provides conversion/metadata code and links converted labels. WVS research-use, non-redistribution terms remain separate from the paper's CC BY license; no root code license observed.

<a id="benchmark-dulemon"></a>
### B84.  Benchmark

**DuLeMon**, from **Long Time No See! Open-Domain Conversation with Long-Term Persona Memory** | [Findings of ACL 2022](https://aclanthology.org/2022.findings-acl.207/); [2203.05797v2](https://arxiv.org/html/2203.05797v2), 2022-03-14, following March 11 v1. Same-paper method: **M95**.

Chinese mutual-persona conversation with supplied role descriptions and persona grounding: 27,501 crowdsourced role-play dialogues, not natural longitudinal user histories. Human evaluation rates bot–bot conversations using PLATO-LTM as the user simulator: ten episodes × four sessions × sixteen rounds per chatbot. Human rating is not longitudinal human use.

**Resources/license:** the [official directory](https://github.com/PaddlePaddle/Research/tree/master/NLP/ACL2022-DuLeMon) supplies a dataset download script. Parent repository [Apache 2.0](https://github.com/PaddlePaddle/Research/blob/master/LICENSE); separate terms for externally downloaded data unverified. **Inspected:** §3 construction, §5 evaluation, ethics, Appendices A/B, version history, official README/directory and parent license; dataset not downloaded/unpacked.

<a id="personal-memory-evaluation"></a>
## Evaluation: Long-term personal memory

What can the agent retrieve, update and reason about across sessions? Keep retrieval, factual QA and response judgments separate. ActMemEval (B85) tests memory-dependent constraints through QA, not executed actions; memory-to-tool and embodied tasks belong under [planning and action](#planning-action-evaluation).

<a id="benchmark-locomo"></a>
### B2. LoCoMo · Long-term conversational memory

[Evaluating Very Long-Term Conversational Memory of LLM Agents](https://aclanthology.org/2024.acl-long.747/) — ACL 2024.

**Checked / reading scope:** 2026-10-31; Paper abstract, §4 QA metrics, relevant §6 summary-evaluation and §8 limitations passages; official README data notes and LICENSE.

- **Input → output:** Timestamped, multi-session conversations → QA, event summaries, or multimodal dialogue continuation. Model-generated dialogues are human-checked and edited.
- **Measures:** Category-level QA F1; ROUGE and atomic-fact measures for summaries; separate multimodal relevance measures. These are not one interchangeable “memory score.”
- **Limits:** The current official release contains **10 long conversations**, not the earlier 50-conversation release. Offline history is not months of real assistant use.
- **Resources:** [Code / data](https://github.com/snap-research/locomo). Original images are not distributed; URLs and related information are provided. [License](https://github.com/snap-research/locomo/blob/main/LICENSE.txt): CC BY-NC 4.0.

<a id="benchmark-longmemeval"></a>
### B3. LongMemEval · Cross-session recall, updates, and abstention

[LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://arxiv.org/abs/2410.10813) — 2024 preprint; ICLR 2025.

**Checked / reading scope:** 2026-10-31; Paper abstract and §3.3 evaluation passages; official README data-format/evaluation notes and cleaned dataset card.

- **Input → output:** Timestamped user–assistant history and a question → an answer or abstention. Its 500 questions cover extraction, cross-session / temporal reasoning, updates, and abstention.
- **Measures:** LLM-judged answers, with optional retrieval Recall@k / NDCG@k. S, M, and oracle expose different history lengths and evidence.
- **Limits:** Retrieval recall is not answer accuracy; constructed-history QA does not establish task execution, deletion, or continuous availability.
- **Resources:** [Evaluation code](https://github.com/xiaowu0162/LongMemEval), [official cleaned data](https://huggingface.co/datasets/xiaowu0162/longmemeval-cleaned). Pin the data revision and judge version.

<a id="benchmark-memsim"></a>
### B36. MemSim / MemDaily · Synthetic personal-memory evaluation

[MemSim: A Bayesian Simulator for Evaluating Memory of LLM-based Personal Assistants](https://arxiv.org/abs/2409.20163) — 2024 preprint; v1, 2024-09-30.

**Verification / reading scope**: 2026-11-01; relevant passages in [v1](https://arxiv.org/html/2409.20163v1) §3 methods, §4 data quality, and §5 benchmark; official README and root listing.

- **Input → output**: Synthetic user-message streams and personal questions → text or multiple-choice answers; supporting-message annotations also enable retrieval evaluation.
- **Measures**: Answering and retrieval are separate; question types cover single-/multi-hop, comparison, aggregation, post-processing, and noise. Full, recent, retrieved, absent, and oracle memory are compared, primarily with GLM-4-9B. Do not pool MemDaily settings with different irrelevant-post ratios.
- **Limits**: Bayesian profiles and structured hints improve consistency, but sampled human checks do not guarantee error-free data. Synthetic factual QA does not establish real-user preference understanding or tool execution.
- **Resources**: [Official code/data](https://github.com/nuster1128/MemSim) includes generation, benchmarking, and `data_generation/final_dataset/memdaily.json`; README reports 2,954 trajectories/questions and 26,003 messages. Code/data licensing was not verified; the paper's CC BY 4.0 does not automatically cover them.

<a id="benchmark-mpr"></a>
### B46. MPR · Multi-hop personalized factual reasoning

[Explicit v.s. Implicit Memory: Exploring Multi-hop Complex Reasoning Over Personalized Information](https://arxiv.org/html/2508.13250v1) — arXiv v1, 2025-08-18; method in M38. Count the paper once.

**Verification date / reading scope:** 2026-11-01; §3–6; official README, complete file tree and release metadata.

- **Input → output:** Synthetic user graphs, generated single-hop statements and questions → 2–10-hop personalized factual answers; not observed human histories.
- **Measurement:** Normalized answer exact match; experiments use a balanced 2,700-question subset. Report oracle and ordinary retrieval separately.
- **Boundary:** Not tool execution, online preference changes or longitudinal satisfaction. Table 2 says 108,000 QA but §3.3.3 says 10,800; retain the discrepancy rather than silently correcting it.
- **Resources:** [official repository](https://github.com/nuster1128/MPR), master, last pushed 2025-08-24; no releases or declared repository license. README links a Drive dataset, but its archive was inaccessible during verification. Paper CC BY 4.0 does not establish code/data reuse rights.

<a id="benchmark-realmem"></a>
### B56. RealMem

**Benchmark: long-term project state and cross-session memory**

[RealMem: Benchmarking LLMs in Real-World Memory-Driven Interaction](https://aclanthology.org/2026.findings-acl.703/) · **Findings of ACL 2026**, with arXiv:2601.06966v1 as the earlier version.

Evaluates evolving state, temporal reasoning and goal alignment using over 2,000 **synthetic** cross-session dialogues across 11 scenarios—not longitudinal deployment logs. Final Table 2 reports memory-only GPT-4o QA of 0.567 for MemoryOS versus 0.804 for the oracle. Human validation covers 30 instances and two NLP-background annotators, not user outcomes. Prefer the final paper, which adds LightMem, full-context baselines and evaluation details. Synthetic data and model-based judging limit generalization. [Official code/data](https://github.com/AvatarMemory/RealMemBench) are available; **LICENSE states Apache-2.0; README badge says MIT**. **Read:** arXiv methods/results, final PDF results/limitations/human protocol, repository README/LICENSE; no reproduction.

<a id="benchmark-atm-bench"></a>
### B60. ATM-Bench · Multi-source personal referential memory QA

[According to Me: Long-Term Personalized Referential Memory QA](https://arxiv.org/html/2603.01990v1) — arXiv v1, 2026-03-02, preprint.

Uses roughly four years of human-origin multimodal memories and 1,038 human-annotated QA/evidence pairs. Structured memory supports retrieval and grounded answering. QS selects its scorer by answer type: EM for numbers, Jaccard for list recall, and an LLM judge for open-ended answers. Retrieval separately reports Recall@k and Recall@k_GT (k equals the ground-truth evidence count); Joint@k = QS × Recall@k. Consent, visual redaction, email paraphrasing and synthetic identifier replacement are not formal anonymity guarantees. The paper’s below-20% Hard finding belongs to its original evaluation. [Code](https://github.com/JingbiaoMei/ATM-Bench) and [data](https://huggingface.co/datasets/Jingbiao/ATM-Bench) are now released: MIT code and CC BY-NC 4.0 data. Later repository benchmarks can use different release sets and must not be merged with preprint results.

**Reading scope:** §3–5, Appendix A privacy/licensing and Appendix B annotation; official repository timeline, result-version notes and dataset card. Targeted methods/evaluation/ethics/annotation plus release records; no raw personal-data inspection.

<a id="benchmark-convomem"></a>
### B66. ConvoMem · Full context as a strong memory baseline

[ConvoMem Benchmark: Why Your First 150 Conversations Don't Need RAG](https://arxiv.org/html/2511.10523v1) — arXiv 2511.10523v1, 2025-11-13.

75,336 QA pairs cover user/assistant facts, abstention, preferences, changing facts and implicit connections. Synthetic enterprise personas feed scenario, evidence and conversation generation; evidence and filler share a pipeline with multi-model validation. Full context, Mem0 and two-stage extraction are compared for accuracy, cost and latency, with histories tested up to 300 conversations.

**Limits:** The title's 150-conversation threshold is conditional on the data, models and costs, not universal. These are not longitudinal real-user logs. Missing-information abstention is not privacy/permission refusal; consent, deletion, access isolation and leakage protection are untested.

**Read:** v1 §§2–3, §5 and Appendix A. Paper-provided code/data links; no independent reproduction or reuse-license verification.

<a id="benchmark-perltqa"></a>
### B68. PerLTQA · Personal-memory QA

[PerLTQA: A Personal Long-Term Memory Dataset for Memory Classification, Retrieval, and Synthesis in Question Answering](https://arxiv.org/html/2402.16288v1) — reviewed v1, 2024-02-26; the [SIGHAN-10 2024 published version](https://aclanthology.org/2024.sighan-1.18/) uses “Fusion” in the final part of the title.


- **Scope**: §§3–5, generation/validation appendices; README/LICENSE.
- **Input → output**: synthetic profiles, relationships, events, dialogues and questions → memory classes, retrieved memories and answers. GPT-3.5 generation uses ChatGPT/Wikipedia seeds with human checks. 8,593 QA items cover 30 fictional characters, not longitudinal participants.
- **Measures**: classification P/R/F1/accuracy, Recall@K, anchor MAP and model-judged correctness/coherence.
- **Boundary**: not real-user utility, action execution or privacy/security validation.
- **Resources**: [code / data repository](https://github.com/Elvin-Yiming-Du/PerLTQA); [dataset license CC BY-NC 4.0](https://github.com/Elvin-Yiming-Du/PerLTQA/blob/main/LICENSE.txt). README records a 2025-12-22 consistency update: pin the revision rather than equating current data with the paper snapshot.

<a id="benchmark-teafarm"></a>
### B70. TeaFarm · Counterfactual memory stress test

[Towards Lifelong Dialogue Agents via Timeline-based Memory Management](https://arxiv.org/html/2406.10996v3) — NAACL 2025; reviewed v3, 2025-01-29. Method: **M65**; same paper.


- **Scope**: §§3–5, appendices D/E/J; official resources.
- **Input → output**: five-session MSC/Conversation Chronicles histories, synthetic continuations and counterfactual questions → answers. TeaBag has 100 source episodes, 200 QA pairs and 200 GPT-4-generated sixth sessions.
- **Measure**: successful recall despite false premises, distinct from ordinary response quality.
- **Boundary**: constructed stories, not lifelong participant observation; counterfactual QA is not comprehensive security certification.
- **Resources**: [code](https://github.com/kimnamssya/Theanine) / [data](https://huggingface.co/datasets/LangAGI-Lab/teafarm); current dataset has 200 rows. Appendix J specifies academic/non-commercial use; check upstream terms separately.

<a id="benchmark-context-time-memory"></a>
### B77. Context- and time-sensitive memory evaluation

Adds padding and simulated timestamps to 12 simulated, human-edited LoCoMo logs; tests temporal, temporal-plus-content, and ambiguous temporal queries. Recall/F2 measure retrieved response IDs, not answer accuracy or real-user task success.

- Paper/version: [Toward Conversational Agents with Context and Time Sensitive Long-term Memory, 2406.00057v2](https://arxiv.org/html/2406.00057v2), 2024-06-04. Reversed Time/Context wording in the resource citation is an alias.
- Cross-reference: M75; same paper, counted once.
- Assets: [TemporalMemoryDataset](https://github.com/Zyphra/TemporalMemoryDataset) exposes conversation/test data; method code and explicit repository license unverified. The paper’s CC BY 4.0 does not establish repository licensing.
- Inspected: §§3–6, Appendix A.1–A.3, README, repository root.

<a id="benchmark-dabench"></a>
### B81. Benchmark — DABench

[DABench / Dynamic Affective Memory Management](https://arxiv.org/html/2510.27418v1) — arXiv:2510.27418v1, October 31, 2025 preprint; conference acceptance not verified. Same paper as [DAM-LLM](#method-dam-llm).

**Checked / reading scope**: November 1, 2026; relevant §§3–6, Appendix A.3–A.4 and arXiv metadata.

- **Composition**: 2,500 observation sequences; 100 simulated sessions/1,000 turns; 500 query-memory pairs. All dialogue/memory explicitly GPT-4-generated.
- **Measurement and limits**: GPT-4 ratings of accuracy, coherence, memory reference, emotional resonance, personalization and fluency do not establish real emotional improvement, clinical benefit or an unbiased judge.
- **Resources**: Appendix prompts/parameters are partial: A.3.2 does not supply the complete simulated-session generation prompt, so full reproducibility is not established. No official code/data release or artifact license located. Method/benchmark entries count as one paper.

<a id="benchmark-actmemeval"></a>
### B85.  Benchmark: ActMemEval

[ActMem: Bridging the Gap Between Memory Retrieval and Reasoning in LLM Agents](https://arxiv.org/html/2603.00026v2) — 2603.00026v2, revised 2026-06-17; preprint, venue unverified.

- **Task:** Memory-dependent implicit constraints across safety/health, feasibility, time-space-procedure, availability, preferences and reuse opportunities; not executed actions.
- **Samples:** 327 synthetic questions, averaging 67.25 sessions and 120k tokens. Gemini generation, Claude validation and three researcher checks; not longitudinal human users.
- **Measurement:** Evidence recall and QA accuracy judged by DeepSeek-V3, with sampled human-agreement checks. Scores do not establish execution safety, authorization enforcement or causal identification.
- **Resources/rights:** [Official repository](https://github.com/nju-websoft/ActMem) exposes `dataset/ActMemEval.json` (96,837,216 bytes); only directory metadata was checked, not individual records. Root MIT differs from Appendix G's dataset CC BY 4.0 plus academic-research-only wording; reuse scope remains unresolved.
- **Reading scope:** arXiv metadata, relevant §§3–5 text, Tables 1–2 and Appendices F/G. No experiment execution or complete visual figure inspection. Same paper as the method entry below.

<a id="benchmark-engramabench"></a>
### B86.  Benchmark: EngramaBench

[EngramaBench: Evaluating Long-Term Conversational Memory with Structured Graph Retrieval](https://arxiv.org/html/2604.21229v1) — 2604.21229v1, 2026-04-23; preprint, venue unverified.

- **Samples/tasks:** Five entirely synthetic personas, 100 conversations, 150 queries: factual, cross-space, temporal, abstention and synthesis. No real user data.
- **Evidence:** Shared GPT-4o answering model. Global composite: full context 0.6186, Engrama 0.5367, Mem0 0.4809. Engrama leads full context on the cross-space slice only: 0.6532 versus 0.6291, n=30, with limited statistical power—not global superiority.
- **Limits:** Token-F1 synthesis scoring; incomplete runtime evidence-provenance auditing; costs are query-time only, excluding memory construction. Not production validation.
- **Resources/rights:** [Repository](https://github.com/julianacunadc/engramabench/blob/main/README.md) provides data, scorer, public baselines and canonical results; [MIT license text](https://github.com/julianacunadc/engramabench/blob/main/LICENSE) verified. **Proprietary Engrama is excluded.** DOI `10.5281/zenodo.19697774` is linked by the paper/repository; the Zenodo record could not be inspected.
- **Reading scope:** Metadata, relevant §§3–8, limitations/ethics and cost appendix text; repository README/LICENSE. No scorer execution, record-by-record data audit or proprietary-system reproduction.

<a id="planning-action-evaluation"></a>
## Evaluation: Personalized planning and action

Do personal context and preferences change plans, tool arguments or actions? Distinguish itinerary quality, generated calls, task-oriented dialogue and executed trajectories; embodiment and mobile settings retain their own boundaries. Clarification overlaps with B50 and ETAPP (B34), but the primary home follows the planning/tool outcome. Completion never substitutes for [authorization and safety](#safety-evaluation).

<a id="benchmark-mem2actbench"></a>
### B5. Mem2ActBench · From memory to tool arguments

[Mem2ActBench: A Benchmark for Evaluating Long-Term Memory Utilization in Task-Oriented Autonomous Agents](https://aclanthology.org/2026.acl-long.370/) — ACL 2026.

**Checked / reading scope:** 2026-10-31; Paper abstract, relevant §4.1 experimental-setup and §5.4 tool-selection passages; official README (including its License statement), root listing, and data-directory entry points.

- **Input → output:** Historical memory, an implicitly constrained request, and tool schemas → tool selection and arguments. The paper constructs 400 memory-dependent tasks.
- **Measures:** Argument matching / F1, tool selection, and whole-call matching. Main experiments supply the correct tool; separate experiments add distractor tools.
- **Limits:** Correct arguments are not a completed real transaction. Main results should not be presented as open-ended tool-selection performance.
- **Resources:** [Official construction code / data directories](https://github.com/Cantaloupe-M/Mem2ActBench). The [README License section](https://github.com/Cantaloupe-M/Mem2ActBench#license) declares MIT License, but no separate LICENSE file was observed in the root listing. Confirm the full license text and scope before reuse. Check upstream ToolACE, BFCL, and OASST1 terms separately; this declaration does not establish MIT licensing for all data.

<a id="benchmark-pdeu-bench"></a>
### B25. PDEU-Bench · Preferences across plan revisions

[PDEU-Bench: Benchmarking the Personalized Planning Lifecycle of Tool-Calling LLM Agents](https://arxiv.org/html/2609.34930v1) — 2026 preprint; v1, 2026-09-28.

**Checked / reading scope:** 2026-11-01; abstract and relevant passages in Environment Construction, Preference and Task Construction, Task Evaluation, and Error Analysis.

- **Input → output:** Synthetic user histories and tasks → initial plans, tool calls, and updates after every attempt; 214 tasks, 12 domains, 94 tools.
- **Measures:** A fixed judge applies binary preference/quality rubrics; strict success requires all relevant stages to pass. Execution scores preference-sensitive arguments only.
- **Limits:** Synthetic preferences and an offline sandbox do not establish real transactions or longitudinal user benefit.
- **Resources:** The abstract points to code/data in an appendix, but no verifiable official release was located in the consulted HTML or search. Licensing and runnability remain unconfirmed.

<a id="benchmark-travelplanner-plus"></a>
### B28. TravelPlanner+ · How profiles change plans

[Personal Large Language Model Agents: A Case Study on Tailored Travel Planning](https://aclanthology.org/2024.emnlp-industry.37/) — EMNLP 2024 Industry Track. Title follows ACL metadata; the PDF ends with Tailored Travel Planners.

**Checked / reading scope:** 2026-11-01; abstract, §1, §4.2 and result tables; not reproduced.

- **Input → output:** User models, personal queries and travel information → personalized itineraries.
- **Measures:** Delivery, constraint and final pass rates; separately, judge preference between personal and generic plans.
- **Limits:** Judge preference is neither human satisfaction nor constraint satisfaction; some personalized settings reduce constraint scores. Not longitudinal planning.
- **Resources:** [Paper](https://aclanthology.org/2024.emnlp-industry.37.pdf). No verified official TravelPlanner+ release located; the original TravelPlanner repository is not a substitute.

<a id="benchmark-pbp"></a>
### B29. PbP · Inferring planning preferences from demonstrations

[Inferring the Unspoken: Aligning Embodied Agents with Implicit Preferences](https://arxiv.org/abs/2502.00858v4) — First submitted 2025; v4, 2026-09-08, marked EMNLP 2026 on arXiv. Earlier title: Learning to Plan with Personalized Preferences. Method: M17.

**Checked / reading scope:** 2026-11-01; v4 abstract and version history only; preliminary review.

- **Input → output:** Demonstrations and new situations → preference-aligned embodied plans; 5,000 evaluation groups, 290 preferences.
- **Measures:** Compares given versus inferred preferences; exact metrics remain unverified.
- **Limits:** Embodied setting, not office-agent deployment. PDF exceeded retrieval size; HTML unavailable.
- **Resources:** No verified official release located; availability and reproducibility unconfirmed.

<a id="benchmark-androidintent"></a>
### B32. AndroidIntent · Inferring implicit GUI intent from long-term records

[PersonalAlign: Hierarchical Implicit Intent Alignment for Personalized GUI Agent with Long-Term User-Centric Records](https://aclanthology.org/2026.acl-long.1669/) — ACL 2026; inspected [arXiv v2](https://arxiv.org/html/2601.09636v2), May 13, 2026. Method: M21.

**Verified / reading scope:** 2026-11-01; task and construction passages, §6.1 metrics, Appendix A.3; official README and root listing. Not a full-paper read.

- **Input → output:** mobile-use history and a vague instruction or current state → GUI actions or proactive suggestions; 775 preference cases and 215 routine cases.
- **Measures:** offline action-type accuracy, step-wise success and weighted CSR; suggestions separately use semantic/judge alignment, precision, recall, false alarms and F1.
- **Limits:** primary evaluation compares offline trajectories. CSR is not real-device task completion; an appropriate suggestion does not authorize execution.
- **Resources:** [official code/data directories](https://github.com/iLearn-Lab/ACL26-PersonalAlign). Requires external FingerTip-20k. README describes restoration after disk failure; completeness unverified. No standalone root license found; upstream data terms require separate checking.

<a id="benchmark-petoolbench"></a>
### B33. PEToolBench · Inferring tool preferences from past calls

[PEToolLLM: Towards Personalized Tool Learning in Large Language Models](https://aclanthology.org/2025.findings-acl.1107/) — Findings of ACL 2025; inspected [arXiv v1](https://arxiv.org/html/2502.18980v1), February 26, 2025. Method: M22.

**Verified / reading scope:** 2026-11-01; §3 task, construction and metrics, §4 method overview; official README, LICENSE and dataset file listing. Not a full-paper read.

- **Input → output:** instruction, candidate tools and past user calls → tool and arguments. Synthetic histories encode preferred-only, rating-integrated and chronological preferences. Paper: 12,000 examples, split into 9,000 training and 3,000 test examples.
- **Measures:** separate tool-selection and parameter accuracies.
- **Limits:** a correct generated call is not an executed service; synthetic preferences do not establish longitudinal real-user performance.
- **Resources:** [official code](https://github.com/travis-xu/PEToolBench), [dataset files](https://huggingface.co/datasets/travisxu/PEToolBench/tree/main). [Repository license](https://github.com/travis-xu/PEToolBench/blob/main/LICENSE): Apache-2.0; this does not establish identical terms for upstream tool material.

<a id="benchmark-etapp"></a>
### B34. ETAPP · Personalized tool interaction and additional assistance

[Evaluating Personalized Tool-Augmented LLMs from the Perspectives of Personalization and Proactivity](https://aclanthology.org/2025.acl-long.1064/) — ACL 2025; inspected [arXiv v1](https://arxiv.org/html/2503.00771v1), March 2, 2025.

**Verified / reading scope:** 2026-11-01; §2 environment, memory and sample construction, §3 evaluation; official README/root. Not a full-paper read.

- **Input → output:** profile, tool preferences, current state, history and request → sandbox tool interactions and response. The 800 cases combine 50 instructions with 16 synthetic profiles—not 800 users.
- **Measures:** human key points assist an LLM judge scoring procedure, personalization and proactivity separately from 0–5. Tool-given and tool-retrieval settings differ.
- **Limits:** proactivity here means useful assistance beyond an initiated request, not necessarily autonomous background initiation. Judge scores do not establish real-world service execution, safety or authorization.
- **Resources:** [official code, data and tools](https://github.com/hypasd-art/ETAPP), with inference/evaluation instructions. No standalone root license found; dependencies and API availability untested.

<a id="benchmark-toolspectrum"></a>
### B35. ToolSpectrum · Selecting tools using profiles and environment

[ToolSpectrum: Towards Personalized Tool Utilization for Large Language Models](https://aclanthology.org/2025.findings-acl.1063/) — Findings of ACL 2025; inspected [arXiv v1](https://arxiv.org/html/2505.13176v1), May 19, 2025.

**Verified / reading scope:** 2026-11-01; §3 task, construction and statistics, §4.1 metrics; official README/root. Not a full-paper read.

- **Input → output:** request, explicit profile, environment and overlapping toolset → application, API, required and personalized optional parameters, or `None` under application policies.
- **Measures:** separate F1 at four levels. Its 1,000 cases comprise 450 profile, 220 environment and 330 combined cases.
- **Limits:** evaluates selection/arguments given profiles, not learning profiles from history or executing transactions. The environment-only subset is not itself individual preference learning.
- **Resources:** [official repository](https://github.com/BUAA-IRIP-LLM/ToolSpectrum) contains `api`, `data` and `prompts`. README does not document a complete evaluation workflow; no standalone root license found.

<a id="benchmark-ms-tod"></a>
### B37. MS-TOD · Cross-session intent and slot tracking

[MemGuide: Intent-Driven Memory Selection for Goal-Oriented Multi-Session LLM Agents](https://ojs.aaai.org/index.php/AAAI/article/view/40313) — AAAI 2026; published 2026-03-14. Same paper as M25.

**Verification / reading scope**: 2026-11-01; relevant Dataset, MemGuide, and Experiments passages in [arXiv v2](https://arxiv.org/html/2505.20231v2); proceedings metadata/PDF resource link; official README and root listing.

- **Input → output**: User history, current dialogue, and QA memories → a response advancing or confirming the current task.
- **Measures**: GPT-4 judging, Joint Goal Accuracy, completion turns, success rate, and human quality ratings. The paper reports 132 personas and 956 task goals; the official README reports 2,860 sessions.
- **Limits**: SGD-seeded, GPT-4-generated dialogues use three temporally ordered sessions per task with human validation; each session is simplified to one service/intent. Slot-based confirmation success is not a completed real booking, payment, or longitudinal user benefit.
- **Versions/resources**: 2505.20231v1 (2025-05-26), *Bridging the Long-Term Gap: A Memory-Active Policy for Multi-Session Task-Oriented Dialogue*, was renamed MemGuide in v2 (2025-08-13); count once. [Official code/data](https://github.com/Elvin-Yiming-Du/MS_TOD_Memory); no root license observed, and reuse terms remain unverified.

<a id="benchmark-user-fingertip"></a>
### B42. User FingerTip · Resolving ambiguous app and content requests

[Me-Agent](https://arxiv.org/html/2601.20162v1) — arXiv v1, January 28, 2026; same paper as M29.

**Verified / actual reading scope:** 2026-11-01; v1 §3 User FingerTip construction/statistics, §5.1–5.2 metrics/results and Table 3, and Limitations; arXiv version history, repository root, and README. Selected passages, not a line-by-line full-paper review; no installation, execution, or experimental reproduction.

- **Evaluation:** Extends FingerTip by removing app names or obscuring requested content. Reports 60 users, 33 apps, 300 Type-I and 267 Type-II instructions.
- **Limits:** Counts versus “15 training/5 test instructions per user” need clarification; this is not established held-out-user evaluation. Table 3’s perfect app selection accompanies task-success rates of 80%/50%, not universal success. Long-term human deployment is unproven.
- **Resources:** [Author repository](https://github.com/Gianthaha/personal-mobile-agent) is MIT-labeled and contains implementation directories, but README still promises updates; complete benchmark packaging remains unverified.

<a id="benchmark-personalwab"></a>
### B44. PersonalWAB · Shopping-history-conditioned function tasks

Same paper as M31; do not count twice. [Original paper](https://arxiv.org/html/2410.17236v2); reading scope and resource limitations as above.

- **Data/environment:** Real histories/reviews from 1,000 sampled Amazon users; model-synthesized profiles, requests and interactive users. Search, recommendation and review-generation tasks expose simplified functions, not browser GUI or live transactions. Successful calls assume review posting.
- **Interpretation:** Function accuracy assesses tools/parameter formatting; result accuracy uses product rank or review-embedding similarity. These are not a universal success measure.
- **Boundary:** Histories are described as split 80/10/10, while profiles use “entire history.” Inspect preprocessing before replication; leakage is not established here. Simulator dependence, inferred profiles and unverified privacy protection constrain real-assistant claims.

<a id="benchmark-triptailor"></a>
### B45. TripTailor · Personalized travel planning

[TripTailor: A Real-World Benchmark for Personalized Travel Planning](https://aclanthology.org/2025.findings-acl.503/) — Findings of ACL 2025, July.

**Verification date / reading scope:** 2026-11-01; Paper §3, §4, Appendix B.1 and limitations; official repository README, complete file tree and release metadata.

- **Input→output:** Single-turn preferences and a Chinese travel sandbox → itinerary. Most experiments receive pre-searched information, including reference-plan POIs; these scores are not end-to-end open-search-and-planning results.
- **Data/metrics:** Real POIs/itineraries are supplemented and LLM-rewritten; queries are generated. An LLM first extracts key entities and activities from natural-language plans; scripts then check feasibility/rationality against the sandbox. This is not purely deterministic evaluation of raw plans. LLM and reward-model judges separately compare personalization with reference plans.
- **Boundary:** Not thousands of participant requests; China-only, single-turn and model biases limit generalization. No booking/execution validation.
- **Resources:** Public code/data.7z; main last pushed 2025-10-22, no releases. No declared repository license or license file; reuse permission remains unverified.

<a id="benchmark-familytool"></a>
### B47. FamilyTool · Multi-hop personal knowledge to tool arguments

[FamilyTool](https://arxiv.org/html/2504.06766v2) — 2025 preprint; inspected v2, May 26, 2025.

**Checked / reading scope:** November 1, 2026; §§4–6, §9, Appendix C.2; official README, repository license metadata and root LICENSE lookup.

- **Input → output:** synthetic family/preference graph, speaker-specific request and candidate tools → tool call and arguments. KGETool retrieves a relevant subgraph first.
- **Measures:** 483 base / 455 extended examples; 102 tools; 1–4 / 2–6 relational hops. Separate graph extraction metrics, call exact match, tool selection and argument accuracy; distinguish oracle from retrieved subgraphs.
- **Limits:** synthetic data undergo model-based and human checks; evaluation focuses on static generated calls, not completed transactions, longitudinal household deployment or open-ended multi-turn execution. Longest-hop cases are sparse; argument correctness proves neither authorization nor execution.
- **Resources:** [official code/data](https://github.com/yxzwang/FamilyTool). Root LICENSE returned 404 and repository license metadata was null: **reuse license unconfirmed**. Check upstream MTU-Bench / UnifiedToolHub terms separately.

<a id="benchmark-compass"></a>
### B49. Feasibility versus preference optimization

[COMPASS](https://arxiv.org/html/2510.07043v2) — inspected v2, April 16, 2026; venue unverified.

**Read:** §§3–6, Appendix H and repository documentation/license; not executed.

- Evaluates 281 travel-planning tasks with tools and simulated users.
- FR measures hard-constraint feasibility; OR-A% measures whether a solution ranks within the top A% of feasible solutions by utility. These are distinct, and OR-A% need not mean exact optimality. Real-source catalogs and simulator annotation do not demonstrate real bookings or user benefit.
- [Repository](https://github.com/sunnytqin/compass) has an MIT root license; database completeness and third-party rights remain unaudited.
- **Deduplication:** Repository acronym expansion denotes the same work; no separate method entry needed.

<a id="benchmark-aware-us"></a>
### B50. Preference-aware infeasible-query repair

[AWARE-US](https://arxiv.org/html/2601.02643v2) — inspected v2, March 1, 2026; acceptance unverified.

**Read:** §§3–7, Tables 1–5, repository and dataset card; not executed.

- Tests clarification and repair on 122 synthetic-persona car queries.
- In Table 5, the SFT+DPO-trained Qwen3-8B local-weighting method achieves 48% Car match. This metric is gated on correct constraint relaxation; that does not establish that correctly relaxed cases form its denominator. It is not satisfaction. Conflicting S2/S3 labels require reconciliation before quoting subgroup results. Testing is limited to structured car queries and static preferences; preference drift is outside scope.
- [Code](https://github.com/mhtkrmz/Infeasible-task) and [dataset](https://huggingface.co/datasets/MehmetKurmaz/AWARE-US) are accessible; reuse licenses unconfirmed.
- **Deduplication:** Weighting/ranking methods may cross-link here; count the paper once. Inferred preferences do not authorize relaxing real hard constraints.


<a id="benchmark-ptbench"></a>
### B51. PTBench · Personal preferences in tool selection and parameters

[Advancing and Benchmarking Personalized Tool Invocation for LLMs](https://arxiv.org/html/2505.04072v1) — preprint, v1, 2025-05-07. Same paper as M46; count once.

**Actual reading scope:** §§3–4 and §5.1–5.3, especially Tables 1–2; official repository file listing and README. Remaining appendices not comprehensively inspected.

- **Input → output:** user profile/behavior, query and candidate APIs → preferred platform and parameterized calls.
- **Measures/evidence:** 1,083 human-verified synthetic test examples; 80 profiles, 360 APIs, five domains; six held-out profiles. Separately measures platform, query/profile parameters and complete output accuracy.
- **Limits:** human checking is not naturalistic user interaction. Static generated calls do not establish successful transactions, authorization or longitudinal adaptation. Table 1 is internally inconsistent: its train 7,096 plus test 1,083 equals 8,179, not the printed total 8,197. Dataset-total prose is also inconsistent. Preserve labeled split counts and flag the unresolved total; do not treat the whole table as reconciled ground truth.
- **Resources:** [official code/test data](https://github.com/hyfshadow/PTBench); training/model release and reuse license unverified.

<a id="benchmark-memento"></a>
### B53. MEMENTO · Applying personal memories to embodied tasks

[Embodied Agents Meet Personalization: Investigating Challenges and Solutions Through the Lens of Memory Utilization](https://arxiv.org/html/2505.16348v4) — v4, 2026-02-13; ICLR 2026.

**Actual reading scope:** §§3–4, overview of memory-design contribution, Appendix A.1–A.2; author project and repository README. Detailed §6 algorithm/ablations and extended Appendix E were not comprehensively read; method cross-index remains provisional.

- **Input → output:** personal object meanings/routines and episodic memories → object-rearrangement actions.
- **Measures:** matched acquisition/utilization goals, single/joint memories, percent complete, success rate and planning cost; 438 episodes across 12 Habitat scenes with generated personal knowledge.
- **Boundary:** main setting guarantees gold memories among retrieved candidates and oracle perception/motor skills. It isolates memory utilization, not unconstrained retrieval or real-world robot reliability. Synthetic users, no conversational clarification. GPT-4o joint-memory success drops 30.5 percentage points relative to its matched acquisition baseline.
- **Resources/identity:** [official repository](https://github.com/Connoriginal/MEMENTO), MIT repository with Habitat/PARTNR dependencies. README’s older subtitle “Exploring Memory Utilization for Personalized Assistance” denotes the same paper.

<a id="benchmark-personal"></a>
### B57. PersONAL

**Benchmark: ownership-conditioned navigation and grounding**

[PersONAL: Towards a Comprehensive Benchmark for Personalized Embodied Agents](https://arxiv.org/abs/2509.19843) · **ICRA 2026**, verified by the [University of Padova institutional record](https://unifind.unipd.it/resource/item/894811?language=en-US), matching title and authors. The version read here is **arXiv v1, September 24, 2025**; its results are not automatically attributed to the final conference version.

Contains **2,020 simulated episodes in HM3D/Habitat** with explicit ownership descriptions, testing active navigation and grounding after exploration. Five humans provide a navigation reference; a separate three-room LoCoBot pilot succeeds on **5/15** grounding queries. Neither establishes household deployment or lifelong adaptation. Human grounding uses interactive GLB scenes rather than the models’ map representation. The POG narrative’s 25% conflicts with Table V’s 16.8% aggregate. [Repository](https://github.com/ZiliottoFilippoDev/PersONAL) data/generation code and a populated [baselines branch](https://github.com/ZiliottoFilippoDev/PersONAL/tree/baselines) are available under **CC-BY-4.0**; HM3D has separate access/terms. **Read:** arXiv v1 §§III–VII, result tables, repository and baseline documentation/tree, and University of Padova publication metadata; final conference full text not checked; no execution.

<a id="benchmark-pin"></a>
### B58. PIN / PInNED — User-specific object navigation
- **Paper:** *Personalized Instance-based Navigation Toward User-Specific Objects in Realistic Environments*, NeurIPS 2024 Datasets and Benchmarks; reviewed arXiv v2 (2025-02-19). PIN is the task and PInNED its dataset: count one paper.
- **Setting/evidence:** Habitat simulations test locating a referenced instance among same-category distractors, using images/manual descriptions; 338 objects across 18 categories support modular and end-to-end baseline comparisons. No household-user or physical-robot trial.
- **Boundary:** Controlled simulated recognition/navigation is not deployed personal-assistant reliability. Small objects, distant details and rendering degradation remain challenges.
- **Licensing/reading scope:** [Paper](https://arxiv.org/html/2410.18195v2) §§3–5, Appendices B/G/I, [project](https://aimagelab.github.io/pin/) and [repository](https://github.com/aimagelab/pin) reviewed. Code: MIT; episodes/descriptions: CC BY; HM3D: noncommercial academic conditions; objects: mixed CC licenses. No blanket commercial-use claim.

<a id="benchmark-triptide"></a>
### B65. TripTide · Personalized itinerary revision after disruption

[TripTide: A Benchmark for Adaptive Travel Planning under Disruptions](https://arxiv.org/html/2510.21329v1) — arXiv 2510.21329v1, 2025-10-24; no verified conference publication.

Extends 1,000 TripCraft plans of 3/5/7 days with model-generated, human-selected disruptions and human-revised reference plans, severity levels and two tolerance profiles. GPT-4o, Qwen2.5-7B and Phi-4-mini are evaluated for constraints, semantic/spatial/sequential changes and disruption response; Llama judging assesses GPT-4o outputs only; three experts reviewing 100 revisions supplement metrics.

**Limits:** §4.2 evaluates the entire dataset without a predefined train/test split; results diagnose planning behavior rather than establish held-out generalization. Simulated disruptions and predefined personas are not real travel deployment. Responsiveness is not measured latency; minimal edits do not establish executability. Perceived quality and hard constraints can disagree. Live inventory, transaction authorization and user satisfaction are untested. Residual 2018 venue/DOI template text is not publication evidence.

**Read:** v1 §§3–6 and relevant appendix passages; paper-provided anonymous code link, no reproduction.

<a id="benchmark-tripcraft"></a>
### B82. Persona-conditioned travel planning

**TripCraft: A Benchmark for Spatio-Temporally Fine Grained Travel Planning** — ACL 2025 Long Papers; version: 2025.acl-long.834 (arXiv alias 2502.20508). [Publication](https://aclanthology.org/2025.acl-long.834/) | [Code and access terms](https://github.com/Soumyabrata2003/TripCraft)

**Benchmark.** Evaluates persona-conditioned itineraries using temporal, spatial, ordering and preference metrics. Reviewed §3–4, limitations and official README. Its 1,000 queries combine real-world place data with constructed queries/personas and adjusted flight dates; human-refined references are not real-traveler validation. Embedding-based persona similarity does not establish satisfaction. No booking execution or authorization is tested. Data require application; internal research/commercial use and modification are permitted. Modifications must retain the paper citation and README; redistribution outside the requesting organization is prohibited. No root code license confirmed.

<a id="proactive-clarification-evaluation"></a>
## Evaluation: Proactivity and clarification

When should the agent help, ask or stay quiet? Separate timely offers, hidden-intent discovery, preference elicitation and clarification before planning. Ask-before-Plan (B30) is adjacent planning/clarification evidence, not longitudinal profiling. Asking well does not grant permission to act; see [authorization](#benchmark-authorizationbench).

<a id="benchmark-proactivebench-lu"></a>
### B6. ProactiveBench (Lu et al.) · When to offer help

[Proactive Agent: Shifting LLM Agents from Reactive Responses to Active Assistance](https://arxiv.org/abs/2410.12361) — 2024 preprint; ICLR 2025.

**Checked / reading scope:** 2026-10-31; Paper abstract and evaluation-metric passages; official README system overview, data statistics, and evaluation entry points.

- **Input → output:** User activity and environment events → a proposed assistance task, or no proposal. The paper includes 6,790 events across coding, writing, and daily-life settings.
- **Measures:** Precision, recall, F1, and false alarms under acceptance / rejection judgments; automated evaluation uses a learned reward model.
- **Limits:** Appropriate offers are not long-term human satisfaction or task completion. A proactive suggestion does not authorize execution.
- **Resources:** [Code, data, evaluation](https://github.com/thunlp/ProactiveAgent). Other papers use the same benchmark name; this entry specifically means Lu et al. See M11 for the method.

<a id="benchmark-knowu-bench"></a>
### B10. KnowU-Bench · Clarification, consent, and restraint

[KnowU-Bench: Towards Interactive, Proactive, and Personalized Mobile Agent Evaluation](https://arxiv.org/html/2604.08455v1) — 2026 preprint; inspected v1, 2026-04-09.

**Checked / reading scope:** 2026-10-31; Abstract, §3.4 and relevant experimental discussion, official repository.

- **Input → output:** Behavioral logs, vague requests or proactive triggers, and Android state → GUI actions, clarification, consent requests, or abstention. The profile is hidden, but a profile-grounded user simulator can answer questions.
- **Measures:** 42 general, 86 personalized, and 64 proactive tasks. Rules check recipients, order / calendar / setting states, and post-rejection violations; judges evaluate semantic preference alignment.
- **Limits:** Directly studies personalized and proactive mobile agents. Simulator, rubric, and judge dependence preclude interpreting scores as human acceptance rates. The environment was not downloaded or execution-tested.
- **Resources:** [Official project](https://zju-real.github.io/KnowU-Bench/), [environment, tasks, and code](https://github.com/ZJU-REAL/KnowU-Bench). Repository: Apache-2.0; third-party Android apps, images, and models have separate terms.

<a id="benchmark-memoprobench"></a>
### B11. MemoProBench · When to speak, what to say, and when not to

[MemoProAgent: Toward Memory-Driven Proactive Assistance](https://arxiv.org/html/2610.22671v2) — 2026 preprint; inspected v2, 2026-10-21. Earlier indexes may use ProPerAgent / ProPerMem; this entry uses v2 names. See M12 for the method.

**Checked / reading scope:** 2026-10-31; v2 abstract, §3.3 metrics, method overview, official README and LICENSE.

- **Input → output:** Egocentric video streams and long personal histories, without an explicit query → grounded, timely reminders or silence.
- **Measures:** Perfect requires exactly one correct intervention within the allowed window. Also report Hit, early, late, repeated, and negative-case false triggers; Hit alone hides unwanted interruptions.
- **Limits:** Direct personal-memory-driven proactivity, but constructed histories are not a year-long human study. It does not evaluate authorized transaction completion or establish all-day usability.
- **Resources:** [Official inference code](https://github.com/facebookresearch/Memo-Pro-Agent): CC BY-NC 4.0; [history data (restricted)](https://huggingface.co/datasets/facebook/MemProBench). The official [README data notes](https://github.com/facebookresearch/Memo-Pro-Agent#data-and-reproducibility) state that `facebook/MemProBench` histories are currently private and require authorized Hugging Face access. Download access was not obtained in this review; independent dataset licensing remains unconfirmed and cannot be inferred from the code license. Videos require separate [Ego4D](https://ego4d-data.org/) access and terms; an inference harness is not a complete RL reproduction package.

<a id="benchmark-pi-bench"></a>
### B23. π-Bench · Hidden intents and proactive clarification across sessions

[π-Bench: Evaluating Proactive Personal Assistant Agents in Long-Horizon Workflows](https://arxiv.org/html/2605.14678v1) — 2026 preprint; initial reading of v1, 2026-05-14. The official README announces NeurIPS 2026 acceptance; this is not an independently checked proceedings record.

**Checked / reading scope:** 2026-10-31; v1 abstract, evaluation discussion and relevant §4 passages; official project-page metric definitions and README resource / acceptance notes. Initial literature reading, not installation or testing.

- **Input → output:** Underspecified requests, earlier sessions and a persistent workspace → targeted clarification, tool actions and artifacts; five personas each have 20 sessions, totaling 100 tasks.
- **Measures:** Proc counts hidden intents proactively satisfied or elicited through targeted clarification; Comp scores checklist requirements across the full trajectory, tool records and artifacts. Eventual completion is not proactive requirement discovery; report both separately.
- **Limits:** Proactivity means reducing specification burden during interaction, not initiating background tasks or granting permission to act. Simulated users and model grading do not establish longitudinal human satisfaction.
- **Resources:** [Official code / data](https://github.com/Simplified-Reasoning/Pi-Bench), [project and metric definitions](https://simplified-reasoning.github.io/Pi-Bench/). Repository Apache-2.0; AppWorld, NanoBot and other dependencies retain their own terms. Pin paper, code, model and judge configurations before comparing.

<a id="benchmark-atrbench"></a>
### B26. ATRBench · Ask now, use later

[Ask Now, Use Later: Benchmarking the Proactivity Gap in Long-Lived LLM Agents](https://arxiv.org/html/2605.28108v3) — v3, 2026-09-15; author metadata lists EMNLP 2026 Main.

**Checked / reading scope:** 2026-11-01; abstract, §§3.1–3.2, Limitations, Ethical Considerations; official README and NOTICE.

- **Input → output:** Ordinary simulated-user tasks → eliciting preferences useful later, not needed now. History is then frozen; test users are offline.
- **Measures:** TSAcc deterministically checks the first relevant tool decision, macro-averaged by user; asking, acquisition, and application are reported separately.
- **Limits:** Twenty synthetic personas, fixed rules, and model routing do not establish changing real preferences or interruption costs. More questions need not help.
- **Resources:** [Official code/data](https://github.com/BUPT-GAMMA/ATRBench). Code: Apache-2.0; NOTICE separately attributes source personas under CC BY 4.0. Do not assume one license covers every asset. Not run.

<a id="benchmark-ask-before-plan"></a>
### B30. Ask-before-Plan · Clarification before commitment

[Ask-before-Plan: Proactive Language Agents for Real-World Planning](https://aclanthology.org/2024.findings-emnlp.636/) — Findings of EMNLP 2024; method: M18.

**Checked / reading scope:** 2026-11-01; abstract, evaluation in §5.1–5.2 and Appendix B.2–B.3; official README.

- **Input → output:** Dialogue and environment feedback → questions, calls and travel plans.
- **Measures:** Clarification, call correctness and plan constraint / final pass rates, separately.
- **Limits:** Component tests supply correct upstream outputs; integral-framework final planning also receives ground-truth conversation (Appendix B.3). Neither establishes fully free-running end-to-end performance or longitudinal profiling.
- **Resources:** [Code](https://github.com/magicgh/Ask-before-Plan), [data](https://huggingface.co/datasets/magicgh/Ask-before-Plan). README declares MIT code and CC BY 4.0 data / environment. Separate environment download; not installed.

<a id="benchmark-prefdisco"></a>
### B38. PrefDisco · Proactively discovering communication preferences

[PrefDisco: Benchmarking Proactive Personalized Reasoning](https://arxiv.org/html/2510.00177v2) — [ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/82d50077a0e140b524a18f380c95d55a-Abstract-Conference.html); inspected arXiv v2, March 4, 2026. V1 used the *Personalized Reasoning* title.

**Verified / actual reading scope:** 2026-11-01; v2 §2 preference modeling/metrics, §3 benchmark construction, relevant §4 experimental-setting passages, and Limitations; arXiv version history and author README. Selected passages, not a line-by-line full-paper review; no installation, execution, or experimental reproduction.

- **Evaluation:** Converts static reasoning questions into cold-start interactions with generated personas and passive simulated users. Preference alignment and factual correctness remain separate outcomes.
- **Limits:** Primarily communication preferences—not content preferences, longitudinal change or demonstrated human utility. Over-personalization and sycophancy are outside scope.
- **Resources:** [Author repository](https://github.com/stellalisy/PrefDisco) provides construction and evaluation tools; repository reuse license remains unconfirmed. Its newer PEP documentation should not automatically be attributed to the inspected v2. An earlier workshop-version relationship remains unverified.

<a id="benchmark-latent-information"></a>
### B39. Latent Information Discovery · Eliciting hidden preferences

[Do LLMs Recognize Your Latent Preferences?](https://arxiv.org/html/2510.17132v1) — arXiv v1, October 20, 2025.

**Verified / actual reading scope:** 2026-11-01; v1 §3 tasks/evaluation protocol, relevant Appendix A judge/user-comparison descriptions, and Appendix D data sources; arXiv version history. Selected passages, not a line-by-line full-paper review; no installation, execution, or experimental reproduction.

- **Evaluation:** A User–Assistant–Judge setup covers 20 Questions, personalized QA and summarization. Reports all-preference success and average stopping turns, counting failures at the maximum turn budget.
- **Limits:** GPT-4o simulates both user and judge; preferences are fixed and user answers truthful. Object guessing is a diagnostic, not itself a personal-assistant task. Judge approval does not establish human satisfaction.
- **Resources:** Appendix documents generation and source datasets. PrefEval-derived generation code carries CC-BY-NC-4.0 restrictions; document-source terms vary. An original complete code/data release was not verified.

<a id="benchmark-userville"></a>
### B43. UserVille · Hidden tasks and interaction preferences

Same paper as M30; do not count twice. [Original paper](https://arxiv.org/html/2511.02208v2); reading scope and resource limitations as above.

- **Automated component:** Obscures task descriptions and uses preference-conditioned LLM users; 20 interaction preferences include eight held out. Code localization uses F1, BrowseComp-Plus uses EM; personalization covers only sessions containing a question.
- **Human component:** v2 includes 33 programmers and 300 evaluations on SWE-Bench tasks. Participants could see descriptions and gold patches; this is not natural longitudinal deployment. Satisfaction is PPP 3.75 versus GPT-5 3.79, but reported resolution is 71% versus 85%. Do not report satisfaction alone.
- **Interpretation:** Table 1 composite means are 62.04 versus Seed-OSS-36B 45.32. The +16.72 comparison is against Seed, not GPT-5, and is not task-success percentage points.

<a id="evaluation-d-privacy-norms-and-adversarial-safety"></a>
<a id="safety-evaluation"></a>
## Evaluation: Privacy, authorization and safety

What may be shared or done, and what can go wrong? Contextual disclosure, authorization violations, persistent sycophancy and adversarial extraction are different questions. This group includes direct personal-context risks and transferable attack environments, plus ecosystem measurement (B63), not only conventional benchmarks. Interpret low violation rates alongside task utility. No single score establishes compliance or security.

<a id="benchmark-privacylens"></a>
### B21. PrivacyLens · Leakage without an attacker

[PrivacyLens: Evaluating Privacy Norm Awareness of Language Models in Action](https://arxiv.org/html/2409.00138v3) — NeurIPS 2024 Datasets and Benchmarks; inspected v3, 2025-03-14.

**Checked / reading scope:** 2026-10-31; Abstract, §1 risk example, §3.3, official multi-level evaluation README and dataset card.

- **Input → output:** Communication instructions and a privacy-sensitive simulated tool trajectory → the final send / post action. Access to private job-search plans, for example, does not authorize disclosure to a manager.
- **Measures:** Privacy-norm probing accuracy, final-action leakage, and helpfulness separately. Refusing everything is not a useful privacy solution.
- **Limits:** Contextual privacy in personal communication without requiring an attacker. Primarily completes supplied trajectories, not full autonomous execution. U.S.-centered norms, synthetic scenarios, and model judges limit generalization; this is not full privacy compliance.
- **Resources:** [Official code and construction pipeline](https://github.com/SALT-NLP/PrivacyLens): MIT; [official data](https://huggingface.co/datasets/SALT-NLP/PrivacyLens): CC BY 4.0. Code and data licenses differ.

<a id="benchmark-agentdojo"></a>
### B22. AgentDojo · Untrusted instructions in tool results

[AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://arxiv.org/html/2406.13352v3) — NeurIPS 2024; inspected v3, 2024-11-24.

**Checked / reading scope:** 2026-10-31; Abstract, §3.4 metrics, official README and license metadata.

- **Input → output:** Legitimate tasks, tools, and attacker-modifiable tool results → actions and final state in email, banking, or travel sandboxes. The paper has 97 user tasks and 629 security cases.
- **Measures:** Benign utility, utility under attack, and targeted ASR together. Avoiding an attack while failing the legitimate task is not assistant success.
- **Limits:** A general tool-agent indirect-injection environment, not personalization evaluation. It does not cover every privacy, authorization, persistent-memory, or multi-agent risk. No attacks were generated or run for this review.
- **Resources:** [Official environment, tasks, and evaluation](https://github.com/ethz-spylab/agentdojo), MIT. The extensible project and API evolve; pin suites, attacks, tool schemas, models, and budgets before comparisons.

<a id="benchmark-agentcibench"></a>
### B24. AgentCIBench · Cross-app disclosure and recipient boundaries

[Capable but Careless: Do Computer-Use Agents Follow Contextual Integrity?](https://arxiv.org/html/2606.23189v2) — Initial reading of v2, 2026-09-10; [author-submitted arXiv metadata](https://arxiv.org/abs/2606.23189) identifies EMNLP 2026 Main.

**Checked / reading scope:** 2026-10-31; v2 abstract, §3 metric and failure-taxonomy passages; official README and dataset-card resource / license notes. Initial literature reading, not installation or testing.

- **Input → output:** Personal-app state, an underspecified task and a recipient → an outward-facing message, event or post; targets visual co-location, task-ambiguity oversharing and recipient misalignment.
- **Measures:** Utility U, leakage L, refusal R and engagement-conditioned leakage L/(1−R). §3 explicitly combines deterministic matching with LLM paraphrase detection; the abstract's “deterministically scored” wording does not make the complete evaluation purely deterministic.
- **Limits:** Contextual privacy can fail without an attacker. Curated disclosure stress tests do not establish real-world prevalence or comprehensive legal compliance. Keep final-disclosure and end-to-end UI settings separate; blanket refusal is not useful privacy protection.
- **Resources:** [Official code](https://github.com/UKPLab/emnlp2026-agentcibench), [official data](https://huggingface.co/datasets/UKPLab/agentcibench). Code Apache-2.0; data / scenario pool CC BY 4.0. Older arxiv2026-agentcibench paths differ from the current repository name; pin versions. No environment or attack generation was run.

<a id="benchmark-pasb"></a>
### B27. PASB · Sycophancy written into persistent state

[Agents Don't Just Agree, They Remember: Benchmarking Persistent Sycophancy in Self-Improving Personal Agents](https://arxiv.org/html/2607.10526v5) — 2026 preprint; v5, 2026-10-10.

**Checked / reading scope:** 2026-11-01; abstract, §§3.3, 4, 5.1, Appendices A.8/A.10; official README and LICENSE.

- **Input → output:** Five-turn claim-bearing chats → three fresh-session answers using retained state; 1,600 tasks across Hermes-Agent/OpenClaw.
- **Measures:** Commit% tracks whether the tested claim was saved in persistent state available to the follow-up. Judge-based Max-FR@3 flags any failing answer; downstream failure averages Max-FR@3 across the four per-answer dimensions, not all six metrics.
- **Limits:** Controlled stress tests are not population risk estimates. Low failure can reflect weak tool use. Reported 88% human agreement allows ±1 Likert point, not exact matching.
- **Resources:** [Official code/data entry](https://github.com/henrymao2004/agent-sycophancy). Code: MIT. The paper labels PASB CC BY 4.0; README requires upstream PersistBench/ELEPHANT terms. Data licensing needs reconciliation. Not run.

<a id="benchmark-authorizationbench"></a>
### B31. AuthorizationBench · Completion is not authorization

[Act on Your Behalf, Beyond Your Authorization: Benchmarking LLM Agent Authorization Alignment](https://arxiv.org/html/2610.27548v2) — 2026 preprint; v2, 2026-10-21.

**Checked / reading scope:** 2026-11-01; abstract, §4.1 metrics and official README.

- **Input → output:** Scoped delegation and sandbox state → action trajectories; 286 tasks.
- **Measures:** Completion and authorization violations, using trajectories and state evidence.
- **Limits:** Delegation benchmark, not a personalized planning method; simulated services and judges do not establish deployment risk.
- **Resources:** [Official repository](https://github.com/PEACH-Research-Lab/AuthorizationBench). README declares MIT for original artifacts, excluding third-party sources. Released verdicts cover 6,864 runs, but only 4,981 original trajectories remain. Not run.

<a id="benchmark-privacylens-live"></a>
### B48. PrivacyLens-Live · Disclosure in dynamic tool and multi-agent workflows

[Privacy in Action](https://aclanthology.org/2025.findings-emnlp.925/) — Findings of EMNLP 2025; inspected [arXiv v1, September 22, 2025](https://arxiv.org/html/2509.17488v1). Same paper as M41; count once.

**Checked / reading scope:** November 1, 2026; §§3–4.5 and Limitations; ACL metadata and author resource link.

- **Input → output:** reconstructed benchmark private content and requests → final actions through MCP tools / two-agent interactions.
- **Measures:** 493 static cases; initially 150 Gmail/Notion live cases, plus 36 three-tool cases. Distinguish leakage, helpfulness and helpfulness-adjusted leakage; label model, deployment strategy and static/live setting.
- **Limits:** test-account API execution is real, but content is benchmark-derived—not naturalistic user deployment. A2A reproduces selected components. Residual complex-workflow leakage remains; this is neither comprehensive compliance nor injection resistance testing.
- **Resources:** [author release shortlink](https://aka.ms/privacy_in_action) fetch was denied by robots.txt. **Released contents and implementation/data licenses remain unverified.** This is a distinct paper extending PrivacyLens, not a duplicate entry for the original benchmark.

<a id="benchmark-privacybench"></a>
### B54. PrivacyBench · Leakage versus over-secrecy in personal conversation

[PrivacyBench: A Conversational Benchmark for Evaluating Privacy in Personalized AI](https://arxiv.org/html/2512.24848v1) — preprint, v1, 2025-12-31.

**Actual reading scope:** §§3–8, Table 2, Appendix C.3; Table 2 additionally checked in [PDF p.8](https://arxiv.org/pdf/2512.24848); official code/data repository listings and READMEs.

- **Input → output:** synthetic social profiles, documents and secrets → multi-turn RAG responses under direct/indirect probing.
- **Measures:** leakage, over-secrecy, inappropriate retrieval and persona consistency; 48 synthetic users, 31,972 documents, five assistants, up to ten rounds.
- **Numerical warning:** printed direct averages 16.31%→5.43% do not equal simple means of displayed model rows, 17.064%→7.38%. Overall 15.80%→5.12% is author-reported, not reconciled. 26.56% is a worst-model direct result, not the baseline average. Prompting is not uniformly beneficial: Kimi-K2 direct-probe leakage increases from 14.58% to 18.13%.
- **Limits:** explicit/full-secret leakage excludes hints and partial disclosures; standard RAG only, not universal agent privacy/compliance. Human judge validation is not a real-user deployment. Distinct from PrivacyLens/PrivacyLens-Live/PrivacyChecker.
- **Resources:** [code](https://github.com/sri-ja/privacy-bench), [data](https://github.com/sri-ja/privacy-bench-dataset); reuse licenses unverified. No separate method paper for the prompt mitigation.

<a id="benchmark-penguin"></a>
### B55. PENGUIN · Safety conditioned on individual context

[Personalized Safety in LLMs: A Benchmark and A Planning-Based Agent Approach](https://arxiv.org/html/2505.18882v5) — v5, 2026-01-13; [NeurIPS 2025](https://papers.nips.cc/paper_files/paper/2025/hash/8c2bb821410066459be64d03a4dc5719-Abstract-Conference.html). Same paper as M48.

**Actual reading scope:** §§3–4, §5 method overview/results, Limitations and Ethical Statement; official project/repository README. MCTS mathematical appendices and all additional experiments not comprehensively inspected.

- **Input → output:** query with/without structured user background → context-sensitive answer.
- **Measures:** risk sensitivity, empathy and user-specific alignment; 14,000 scenarios, equally Reddit-derived/synthetic, seven domains. GPT-4o judging checked against three annotators on 350 cases.
- **Limits:** proxy response scores, not measured harm reduction. Rich-context Reddit selection, manually defined attributes and equal acquisition costs constrain generalization.
- **Resources:** [official implementation](https://github.com/yuchenlwu/PersonalizedSafety), [project](https://personalized-safety.github.io/); README contains stale clone/runner references. Availability checked, reproduction not attempted; README’s MIT claim was not independently checked against a license file.

<a id="benchmark-agentdam"></a>
### B61. AgentDAM · Unnecessary disclosure during web execution

[AgentDAM: Privacy Leakage Evaluation for Autonomous Web Agents](https://arxiv.org/html/2503.09780v3) — arXiv v3, 2025-10-01; [NeurIPS 2025 Datasets & Benchmarks](https://arxiv.org/abs/2503.09780).

Executes 246 tasks on self-hosted web replicas with synthetic user data derived from human seeds. Final-state checks measure utility; GPT-4o judges action-text disclosure. Leakage rate is the fraction of instances with leakage; privacy performance equals 1 minus leakage rate. The 98% human agreement validates only one GPT-4o/axtree run. Its threat model excludes malicious actors and external attacks: this is inadvertent data minimization, not prompt-injection defense. Prompting reduces leakage without guaranteeing privacy. [Official resources](https://github.com/facebookresearch/ai-agent-privacy) combine CC BY-NC 4.0, MIT components and additional Llama 3.1-derived data terms.

**Reading scope:** v3 §3 threat model, data, metrics and mitigation; §4–5 evaluation/discussion; arXiv venue metadata and official README licensing section. Targeted methods, evaluation and discussion plus venue/resource records; environments not deployed.

<a id="benchmark-privacy-risk-search"></a>
### B62. Searching for Privacy Risks — multi-turn impersonation and forged consent
- **Paper/cross-reference:** ICLR 2026 / arXiv v3; method: **M59**.
- **Evidence:** Training-5 and Testing-100 configurations, default ten simulations per test configuration; Gemini judge agrees with human labels on 98.5% of 200 actions. Primarily synthetic agent interactions, not a human-subject study. v3 adds an Atlas/GPT-5.1/live-Outlook-interface case study: three successful attacks in five trials.
- **Limits:** Not product-wide incidence. Simulated subjects grant no subsequent consent, leaving legitimate sharing untested. Judge agreement is not a security guarantee. Distinguish v3’s leak velocity from leak rate; do not mix older metric names/results.
- **Resources/read scope:** Same paper/version and licensing boundaries as **M59**. Authors state no human subjects or personally identifiable data; the real email interface does not imply real victim data.

<a id="benchmark-personal-data-flows"></a>
### B63. Third-party GPT data flows and policy traceability

[Personal Data Flows and Privacy Policy Traceability in Third-party LLM Apps in the GPT Ecosystem](https://petsymposium.org/popets/2026/popets-2026-0015.pdf) — PoPETs 2026(1), 273–295; DOI 10.56553/popets-2026-0015.

**Ecosystem measurement, not a conventional task benchmark.** GPTStore.ai's April 2024 crawl and BeeTrove supply 5,286 GPTs with extractable Action schemas and 44,102 parameters. Personal-information classification and policy parsing assess disclosure traceability: approximately 35% of parameters fall into sensitive/identifying categories; 792 GPTs, about 15% of the overall sample, have complete traceability. Of those, 753 have relevant Action parameters classified entirely as NON_PI, with no personal-information transmission identified through those parameters. Thus 15% is not the complete-disclosure rate among personal-data-collecting apps (§4.4.5).

**Limits:** Large-scale findings concern schema-indicated flows, not observed production traffic for every GPT. Three controlled endpoints provide a separate active audit. Disclosure is not authorization or a privacy guarantee. Subsequent processing is outside scope; English-policy restrictions, classifier error and platform specificity remain.

**Read:** Published PDF §§3.1–3.5, 4.1/4.4 and 5.3; targeted reading, no independent reproduction.

<a id="benchmark-privaci"></a>
### B64. PrivaCI-Bench · Context understanding and compliance classification

[PrivaCI-Bench: Evaluating Privacy with Contextual Integrity and Legal Compliance](https://aclanthology.org/2025.acl-long.518/) — ACL 2025 Long Papers, July 2025, 10544–10559.

6,351 compliance-classification samples and 147,840 multiple-choice questions draw on legal/enforcement cases, OPP-115/APP-350 policies, and AI Act checker-derived synthetic scenarios. Three authors and two law-school students correct parsing errors; three authors conduct sampled quality checks of LLM-assisted CI annotation. Evaluation covers permitted/prohibited/not-applicable classification and context understanding, comparing direct prompting, CoT, RAG and annotated CI/legal context. Classification reports accuracy, precision, recall and F1; multiple-choice probing reports accuracy.

**Limits:** Treating policies as permitted examples is a construction assumption, not an independent legal audit. Legal norms omit personal, cultural and ethical expectations. Results use single runs and fixed prompts without sensitivity testing. This is neither runtime authorization enforcement nor professional legal judgment.

**Read:** ACL paper §§3–5, Limitations and Ethical Considerations. Code link is supplied by the paper; installation and reuse licensing were not verified.

<a id="benchmark-mextra"></a>
### B67. MEXTRA · Memory extraction risk

[Unveiling Privacy Risks in LLM Agent Memory](https://arxiv.org/html/2502.13172v2) — ACL 2025 main; reviewed v2, 2025-06-03.


- **Scope**: §§2–6, limitations, appendices B–C; official README/root listing.
- **Input → output**: black-box queries and varying implementation knowledge → historical queries extracted from retrieved query–solution memories. Main tests use EHRAgent and RAP/WebShop with static 200-record memories.
- **Measures**: extraction count/efficiency, retrieval count, complete/any extraction rates; up to three attempts per prompt. Dataset queries plus generated solutions are not a survey of live multi-user services.
- **Boundary**: no user/session memory isolation in the studied setup; not evidence that properly isolated products share the vulnerability, nor proof of comprehensive privacy compliance.
- **Resources**: [official code](https://github.com/wangbo9719/MEXTRA); no overarching root/README license observed. Check upstream terms separately.

<a id="benchmark-operationalizing-ci"></a>
### B74. Operationalizing Contextual Integrity in Privacy-Conscious Assistants

**Evaluation: form-filling disclosure** · Unique paper key: `CI`

[Paper](https://arxiv.org/html/2408.02373v2) · v2, 2024-09-13

126 synthetic forms across 14 scenarios with eight human norm annotators, not live delegated submissions. Structured data, a single sharing action, and fieldwise processing constrain the evaluation. Ask-user outputs are labels, not demonstrated interactive consent. Leakage counts non-refusal in fields that should not be filled, even if the generated value is wrong. Societal norms are not individualized authorization or comprehensive compliance.

**Assets and reproduction：** Article: CC BY 4.0. Official standalone data/runnable benchmark release and formal venue were not verified; reproduction is not established.

**Actual reading scope：** Sections 2–6, Appendix C label aggregation, version metadata.

Method entry: [M70](#method-contextual-integrity-supervisor); same paper, not counted again.

<a id="tmp-m-ci"></a>

<a id="benchmark-execution-prompt-injection"></a>
### B75. Simple Prompt Injection Attacks Can Leak Personal Data Observed by LLM Agents During Task Execution

**Evaluation: runtime personal-data exfiltration** · Unique paper key: `EXFIL`

[Paper](https://arxiv.org/html/2506.01055v1) · v1, 2025-06-01

Attacks runtime-observed data in a fictional AgentDojo banking environment: 16 original tasks and 48 in the extension. Not training-data extraction or real customer research. User/system instructions are trusted; attackers control external input and have white-box access **or** knowledge of the retrieval system (alternative assumptions, not necessarily both). Any sensitive disclosure counts toward aggregate ASR, not necessarily passwords. Zero ASR in the small setting does not generalize to the expanded suite.

**Assets and reproduction：** Article: CC BY 4.0. Checklist promises the new dataset after acceptance; official release was not verified. AgentDojo availability does not establish reproduction of added assets. NeurIPS formatting style is not acceptance.

**Actual reading scope：** Sections 3–4, data construction, threat model, metrics, reproducibility checklist, version page.

<a id="tmp-m-pearl"></a>

<a id="benchmark-ci-bench"></a>
### B78. CI-Bench

**Direct risk evaluation: context-sensitive personal-information disclosure**

[Paper](https://arxiv.org/html/2409.13903v1) · arXiv v1, 2024-09-20.

Contains 44,100 synthetic cases across eight domains and dialogue/email formats, testing context understanding, norm identification, appropriateness judgments, and response generation. Distinct from PrivaCI-Bench and the software-engineering namesake. It focuses on social norms rather than learned individual privacy preferences. Gemini 1.0 Ultra/Pro/Nano are evaluated with stage-specific AUC: norm identification trails context-parameter identification; explicit norms improve appropriateness judgments; response-generation AUC is approximately 0.3–0.5, not an overall benchmark score.

**Limits:** Two-expert labeling, subjective/cultural variation, binary labels, stateless single-context samples, no context transitions, and assumed honest identities. Not an end-to-end agent-security or injection-resistance test.

**Resources:** Official downloadable code/data and asset licenses remain unverified. Paper license: CC BY-NC-SA 4.0.

**Verification date / actually read:** 2026-11-01; version page; Benchmark, Dataset, Experiments, Limitations; relevant response-evaluation appendix passages. No reproduction run.

<a id="benchmark-confaide"></a>
### B83. Contextual privacy

**Can LLMs Keep a Secret? Testing Privacy Implications of Language Models via Contextual Integrity Theory** — ICLR 2024 Spotlight; reviewed version: arXiv 2310.17884v2 (2024-06-28). [Paper v2](https://arxiv.org/html/2310.17884v2) | [Code and data](https://github.com/skywalker023/confaide) | [MIT license](https://github.com/skywalker023/confaide/blob/main/LICENSE)

**Benchmark.** Four tiers assess sensitivity, contextual information flow, secret sharing and meeting-output disclosure. Reviewed §3–5, annotation/metric appendices and repository license. Scenarios are templated/model-generated; tiers 1–3 have human annotations, while Tier 4 uses synthetic meeting transcripts rather than private meeting records. The 39%/57% GPT-4/ChatGPT result is **mean Tier-4 summary leakage across 10 runs with privacy-preserving instructions**, not worst-case leakage. Relevant to personal-assistant privacy, but not a personalization method, access-control mechanism or consent guarantee. Official repository: MIT.

<a id="evaluation-b-transferable-memory-and-sequential-tasks"></a>
<a id="transferable-memory-evaluation"></a>
## Evaluation: Transferable memory and sequential tasks

Can general memory and cross-session dependencies support later tasks? These are useful neighboring capabilities, not evidence of learning an individual user. Compare with [personal-memory evaluation](#personal-memory-evaluation), without pooling their scores.

<a id="benchmark-memoryagentbench"></a>
### B12. MemoryAgentBench · Incremental memory and conflicting updates

[Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions](https://arxiv.org/html/2507.05257v1) — 2025 preprint; the repository identifies ICLR 2026. This entry pins v1, 2025-07-07.

**Checked / reading scope:** 2026-10-31; Abstract, incremental construction, Appendix A / Table 5 tasks and metrics, official README and dataset card.

- **Input → output:** Incrementally ingested material followed by queries → factual answers, intent labels, recommendations, or summaries; examples include updating conflicting facts and learning banking intent labels from examples.
- **Measures:** v1 groups accurate retrieval, test-time learning, long-range understanding, and conflict resolution. Subtasks use SubEM, Recall, accuracy, ROUGE, or model judgments.
- **Limits:** General memory-component evaluation, not a complete personal assistant. Chunked ingestion is not longitudinal human interaction; conflict resolution is not privacy erasure. Later selective-forgetting terminology must not silently replace v1 settings or results.
- **Resources:** [Official code](https://github.com/HUST-AI-HYZ/MemoryAgentBench), [dataset card](https://huggingface.co/datasets/ai-hyz/MemoryAgentBench): both mark MIT. Check upstream terms for repackaged datasets separately.

<a id="benchmark-memoryarena"></a>
### B13. MemoryArena · Cross-session action dependencies

[Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks](https://arxiv.org/html/2602.16313v2) — inspected v2, 2026-09-17; project name: MemoryArena.

**Checked / reading scope:** 2026-10-31; Abstract, §3.1 task construction, §4.2 metrics, project page, repository root, and dataset card.

- **Input → output:** Session-separated dependent subtasks, observations, and previous experience → subsequent actions and answers, such as compatible follow-up purchases or accumulating group-travel constraints. v2 has 701 task groups across shopping, travel, progressive search, math, and physics.
- **Measures:** Overall success rate (SR), subtask progress (PS), and constraint-level soft progress (sPS). Partial progress is not full-chain success.
- **Limits:** General sequential tasks, partly relevant to personal assistants. It couples memory to action rather than only historical QA, but does not establish months-long real-user reliability.
- **Resources:** [Project](https://memoryarena.github.io/), [official code](https://github.com/ZexueHe/MemoryArena), [data](https://huggingface.co/datasets/ZexueHe/memoryarena). Data: CC BY 4.0. Code: preview; no explicit root LICENSE observed. Data licensing does not license code; parity between preview code and paper v2 is unverified.

<a id="evaluation-c-task-execution-and-interaction"></a>
<a id="execution-evaluation"></a>
## Evaluation: Transferable execution and interaction

Can the agent solve tasks and operate tools, apps or interfaces? Web research, sandbox function calls and GUI trajectories are distinct protocols. AppWorld’s simulated personal apps and people are not longitudinal personalization with real users. Personal-looking environments do not by themselves test learned preferences; see [personalized planning and action](#planning-action-evaluation) for that question.

<a id="benchmark-assistantbench"></a>
### B14. AssistantBench · Realistic web information tasks

[AssistantBench: Can Web Agents Solve Realistic and Time-Consuming Tasks?](https://aclanthology.org/2024.emnlp-main.505/) — EMNLP 2024.

**Checked / reading scope:** 2026-10-31; Paper abstract and relevant §3.4 automatic-evaluation passages; official project page, code entry point, and dataset card.

- **Input → output:** A task requiring web search and synthesis → a string, number, or structured answer. The original benchmark has 214 tasks.
- **Measures:** Answer accuracy, answer rate, precision, and exact match, rather than an agent's own completion claim.
- **Limits:** Primarily information gathering, not writes to real accounts. Web changes and answer freshness affect reproducibility; persistent preferences are not tested.
- **Resources:** [Project](https://assistantbench.github.io/), [code](https://github.com/oriyor/assistantbench), [data](https://huggingface.co/datasets/AssistantBench/AssistantBench).

<a id="benchmark-gaia"></a>
### B15. GAIA · General-assistant problem solving

[GAIA: a benchmark for General AI Assistants](https://arxiv.org/abs/2311.12983) — 2023 preprint.

**Checked / reading scope:** 2026-10-31; Paper abstract and relevant §3.2 evaluation passages; official dataset-card task, split, gating, and redistribution notes.

- **Input → output:** A natural-language question, sometimes with files / multimodal material → a short, verifiable answer. The paper contains 466 questions at three difficulty levels.
- **Measures:** Type-aware normalized, near-exact answer matching; tasks involve browsing, tools, multimodality, and reasoning.
- **Limits:** Single-question correctness is not personalization, background proactivity, or long-horizon reliability. Development and hidden-answer test sets differ.
- **Resources:** [Official dataset card and leaderboard entry point](https://huggingface.co/datasets/gaia-benchmark/GAIA). Access is gated; the authors prohibit resharing the dataset in crawlable form.

<a id="benchmark-appworld"></a>
### B16. AppWorld · A sandbox for cross-app personal tasks

[AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents](https://arxiv.org/abs/2407.18901) — ACL 2024.

**Checked / reading scope:** 2026-10-31; Paper task overview and relevant §3.2 evaluation / §7 limitations passages; official project page, README, and licensing notes.

- **Input → output:** User instruction, simulated initial app state, and API documentation → interactive code / calls changing state. The paper has 750 tasks across nine apps.
- **Measures:** Database-state tests; TGC requires all tests for a task, while SGC requires success on every task variant in a scenario.
- **Limits:** Simulated APIs are not live services or GUIs. The original benchmark differs from later AppWorld-UL user-in-the-loop tasks.
- **Resources:** [Project](https://appworld.dev/appworld/), [code / data download workflow](https://github.com/StonyBrookNLP/appworld). Protected content has additional encrypted-redistribution requirements: [license notes](https://github.com/StonyBrookNLP/appworld#-license).

<a id="benchmark-tau-bench"></a>
### B17. τ-bench · Tools, users, and domain rules

[τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](https://arxiv.org/abs/2406.12045) — 2024 preprint.

**Checked / reading scope:** 2026-10-31; Paper abstract, §3 reward/pass^k definitions, and relevant §6 discussion passages; official README outdated-task and migration warnings.

- **Input → output:** Simulated user dialogue, domain policies, and APIs → conversation and tool actions. Original domains are airline and retail services.
- **Measures:** Final database versus target state, plus required information in replies. **pass^k measures success on all k repeated trials, unlike pass@k's at-least-one-success criterion.**
- **Limits:** Service-agent workflows are not persistent personal assistance. Correct final state does not establish process-level compliance; user simulation affects results.
- **Resources:** [Original code / data](https://github.com/sierra-research/tau-bench). The official README now labels these tasks outdated and directs readers to τ³-bench. Distinguish historical reproduction from newer versions.

<a id="benchmark-webarena"></a>
### B18. WebArena · Reproducible web interaction

[WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854) — 2023 preprint, revised 2024.

**Checked / reading scope:** 2026-10-31; Paper abstract and relevant §3 task/evaluation passages; official README version, environment, and implementation notes.

- **Input → output:** High-level intent and web observations → browser actions, final page state, or an answer. The paper contains 812 tasks.
- **Measures:** Functional outcomes: answers, navigation destinations, or page state, rather than a fixed click sequence.
- **Limits:** Self-hosted sites support reproducibility but do not cover every live website, login obstacle, or ongoing personalization. Results are not universal browser success rates.
- **Resources:** [Official code, environments, evaluation](https://github.com/web-arena-x/webarena). Pin task revisions and site images before comparing runs.

<a id="benchmark-osworld"></a>
### B19. OSWorld · Desktop and cross-app workflows

[OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://arxiv.org/abs/2404.07972) — 2024.

**Checked / reading scope:** 2026-10-31; Paper abstract and introduction task/state-evaluation overview; official project-page version and resource notes.

- **Input → output:** A task, initial desktop / file state, and screenshots or accessibility trees → computer actions and final artifacts. The paper has 369 tasks.
- **Measures:** Task-specific execution-based evaluators; observation modes, action spaces, and step budgets affect comparability.
- **Limits:** Not a long-term user-relationship test; depends on VM / software versions. Original OSWorld, OSWorld-Verified, and OSWorld 2.0 differ; some cloud-document tasks require extra setup.
- **Resources:** [Official project and version links](https://os-world.github.io/), [code / tasks](https://github.com/xlang-ai/OSWorld).

<a id="benchmark-androidworld"></a>
### B20. AndroidWorld · Parameterized mobile tasks

[AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents](https://arxiv.org/abs/2405.14573) — 2024 preprint, revised 2025.

**Checked / reading scope:** 2026-10-31; Paper abstract, §3.4 state-based rewards, and Appendix A limitations passages; official project page and README.

- **Input → output:** Natural-language task, emulator state, and screen / UI tree → Android actions. There are 116 base tasks across 20 apps with randomized parameters.
- **Measures:** Initialization, success checks, and teardown inspect device state; parameter variation supports robustness testing.
- **Limits:** 116 is not the total number of randomized instances. Primarily open-source / system apps; generalization to commercial apps, other devices, or Chinese interfaces is unproven.
- **Resources:** [Project](https://google-research.github.io/android_world/), [environment / task code](https://github.com/google-research/android_world).

<a id="personalization-methods"></a>
<a id="methods-c-personalization-and-preference-learning"></a>
<a id="user-understanding-methods"></a>
## Methods: User understanding, profiles, and preference learning

How are user representations and preferences inferred or learned? Personalized retrieval and response generation also belong here when persistent memory or external action is not the central contribution.

<a id="method-p-rlhf"></a>
### M16. P-RLHF · Learning preferences from individual feedback

[Personalized Language Modeling from Personalized Human Feedback](https://arxiv.org/html/2402.05133v3) — 2024 preprint; first submitted 2024-02-06; consulted v3, 2024-12-09.

**Checked / reading scope:** 2026-11-01; abstract, §4.1–4.4 user models / P-DPO, relevant §5 experiment passages; official README data, training, and evaluation instructions. No installation or training.

- **Core:** Jointly learns a lightweight user model and LLM. User embeddings combine explicit textual preferences with implicit preferences learned from individual comparison feedback. User embeddings enter generation through soft prompting, and P-DPO conditions preference optimization on the user.
- **Relevance and limits:** A personalization method, not a benchmark or long-term memory system. Experiments include synthetic, semi-synthetic, and PRISM human feedback; model-judged response comparisons do not establish longitudinal human satisfaction, changing-preference tracking, or tool execution. An unknown user without textual information receives a non-personalized response.
- **Resources:** [Official implementation](https://github.com/HumainLab/Personalized_RLHF) includes user models and data-processing, training, and evaluation entry points. Public code does not establish reproduced training; upstream data and base-model terms require separate checks.

<a id="method-intu"></a>
### M17. InTU · Verbalize preferences before planning

[Inferring the Unspoken](https://arxiv.org/abs/2502.00858v4) — Same paper as B29; count once.

**Checked / reading scope:** 2026-11-01; v4 abstract only; preliminary review.

- **Mechanism:** Express preferences inferred from multimodal demonstrations in language, then condition action plans on them.
- **Limits:** An interpretable intermediate representation does not guarantee correct inference. Evaluation, resources and reading limitations: [B29](#benchmark-pbp).

<a id="method-personaagent"></a>
### M19. PersonaAgent · Connecting memory and action through an adaptable personal prompt

[PersonaAgent: Bridging Memory and Action for Personalized LLM Agents](https://aclanthology.org/2026.findings-acl.1315/) — Findings of ACL 2026; [arXiv v2](https://arxiv.org/html/2506.06254v2), May 27, 2026. The earlier title, *When Large Language Model Agents Meet Personalization at Test Time*, is the same paper, not an additional work.

**Verified / reading scope:** 2026-11-01; v1 method passages, v2 §3.1 and Appendices E–G, publication record. Not a full-paper read.

- **Mechanism:** retrieves individual experiences and summarizes stable preferences; a user-specific system prompt guides actions and is optimized at test time using textual feedback from recent historical examples.
- **Evidence:** LaMP classification, rating and generation tasks, measured with accuracy/F1, MAE/RMSE and ROUGE—not one combined action score.
- **Limits:** implemented tools are Wikipedia search and personal-memory retrieval. Main evaluation selects 100 active users, with single-run experiments; this does not validate multi-app transactions or longitudinal deployment.
- **Resources:** paper verified; no author implementation entry point confirmed in this pass. Unrelated repositories with the same name are not substitutes.

<a id="method-rlpa"></a>
### M20. RLPA · Learning to infer and use profiles across dialogue turns

[Teaching Language Models to Evolve with Users: Dynamic Profile Modeling for Personalized Alignment](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2fbc1ea60e215275e823c86338417162-Abstract-Conference.html) — NeurIPS 2025; inspected [arXiv v2](https://arxiv.org/html/2505.15456v2), December 11, 2025.

**Verified / reading scope:** 2026-11-01; §2–3 method passages, §4.1 and Table 1; official README/root/LICENSE. Not a full-paper read.

- **Mechanism:** PPO trains Qwen2.5-3B through simulated-user interactions, combining profile-matching and personalized-response rewards. The trained model is Qwen-RLPA.
- **Evidence:** ALOE same-schema and cross-schema settings; average alignment, normalized improvement and normalized coefficient of determination.
- **Limits:** a dialogue method, not tool execution or deployed continual learning. Table 1 gives GPT-4o a higher raw Extended alignment score than RLPA; avoid blanket “beats GPT-4o” claims.
- **Resources:** [official training code](https://github.com/XingYuSSS/RLPA), [Apache-2.0](https://github.com/XingYuSSS/RLPA/blob/main/LICENSE). A complete checkpoint/data/evaluation package was not confirmed.

<a id="method-him-agent"></a>
### M21. HIM-Agent · Keeping preferences and routines distinct

[PersonalAlign](https://aclanthology.org/2026.acl-long.1669/) — ACL 2026; same paper as B32.

**Verified / reading scope:** 2026-11-01; [v2](https://arxiv.org/html/2601.09636v2) method overview, §6.1 and Appendix A.3; official README/root. Not a full-paper read.

- **Mechanism:** streaming record aggregation, followed by execution-based preference filtering and state-based routine filtering, produces separate intent memories.
- **Evidence:** AndroidIntent offline GUI metrics and proactive suggestion alignment; see B32 for evaluation scope.
- **Limits:** recognizing routines does not imply permission to execute them. Real-device end-to-end completion, safe authorization and longitudinal user benefit remain unestablished.
- **Resources:** [official HIM-Agent and scripts](https://github.com/iLearn-Lab/ACL26-PersonalAlign). B32's data dependencies, restoration/completeness and missing-root-license caveats apply. The later skills-beta is not evidence of paper-validated cross-platform capability.

<a id="method-dpl"></a>
### M34. DPL · Representing users through inter-user differences

[Measuring What Makes You Unique](https://aclanthology.org/2025.findings-acl.1095/) — Findings ACL 2025; [arXiv v3](https://arxiv.org/html/2503.02450v3), 2025-06-11.

**Actual reading scope:** relevant v3 §§2–4, Table 1 and Appendices A–F; published PDF limitations/ethics/Appendix A, author preprocessing, README/root listing and data cards. Not a line-by-line review; no execution.

- **Mechanism:** Compares writing, emotional and semantic differences between the target and other reviewers, then combines these with personal history to condition generation: a user-representation method.
- **Evidence/boundary:** Offline generation from real Amazon/Yelp reviews also receives target rating/title; not multi-turn dialogue, unconstrained preference prediction or tool execution. Main results average five temperatures, not five same-configuration seeds. Cross-user information requires privacy/consent safeguards.
- **Consistency issue:** Paper Appendix A says third-most-recent review for testing; current code uses the latest. This discrepancy is not proof of demonstrated leakage; audit data before replication.
- **Resources:** [Author code](https://github.com/SnowCharmQ/DPL) has no observed root license. [DPL-main](https://huggingface.co/datasets/SnowCharmQ/DPL-main) and [DPL-meta](https://huggingface.co/datasets/SnowCharmQ/DPL-meta) specify **CC BY-NC 4.0**; do not propagate the paper ethics paragraph’s broad MIT claim. Check upstream terms separately.

<a id="method-guided-profile-generation"></a>
### M35. Guided Profile Generation · Guided user profiling

[Guided Profile Generation Improves Personalization with LLMs](https://arxiv.org/html/2409.13093v1) — arXiv v1, 2024-09-19.

**Verification date / reading scope:** 2026-11-01; §3–6: methods, task definitions, metrics, results and limitations.

- **Method:** Task-specific context digestion produces a readable profile for downstream responses; raw history remains in the main experiments.
- **Evaluation:** Amazon four-option purchase prediction, LaMP-7 tweet rewriting and PER-CHAT Reddit response generation use different accuracy, overlap and semantic metrics.
- **Boundary:** Offline tasks derived from human histories, not longitudinal participants; single-source text and mainly one GPT-3.5 snapshot. No validated profile truth, continual updating or action execution; fewer abstentions partly explain purchase gains. PER-CHAT generation gains are weak/inconsistent.
- **Resources:** No verified official code/new-data release. Paper CC BY 4.0 does not license upstream data.

<a id="method-rlpf"></a>
### M43. Prediction-guided user-profile compression

[RLPF](https://arxiv.org/html/2409.04421v2) — AAAI 2025; inspected v2, January 17, 2025.

**Read:** §§2–5, Appendix I task definitions, version record and resource search; not executed.

- Trains a history summarizer using future-activity prediction and length rewards; prediction selects the actual next item against three randomly selected negative options, rather than searching an unrestricted catalog.
- Offline evaluation uses MovieLens 2015/2003, Amazon reviews and Google Local reviews; some transfer tasks regress. It does not establish continual profile updating, action execution or privacy protection.
- Official implementation/new-data release not verified; paper licensing does not license upstream assets.
- **Deduplication:** Conference and arXiv versions count once.

<a id="method-aloe"></a>
### M45. Interactive individual-preference alignment

[Aligning LLMs with Individual Preferences via Interaction](https://aclanthology.org/2025.coling-main.511/) — COLING 2025; method inspected in [v2](https://arxiv.org/html/2410.03642v2), December 15, 2024.

**Read:** §§2–5, publication metadata and repository; no full version comparison or execution.

- Uses generated preference conversations for SFT and DPO.
- Evaluation uses 100 personas and ten-turn interactions with GPT-4o as both simulated user and alignment judge. Human rating checks are not longitudinal user trials; this does not validate continual online training or tool execution.
- [Code/data directories](https://github.com/ShujinWu-0814/ALOE) are accessible; no root license found; checkpoints unverified.
- **Deduplication:** ALOE is the same paper’s benchmark. Cross-link if needed; do not count twice.

<a id="method-prelude"></a>
### M49. PRELUDE / CIPHER · Learning context-dependent preferences from edits

- **Paper/version:** [Aligning LLM Agents by Learning Latent Preference from User Edits](https://arxiv.org/html/2404.15269v3), NeurIPS 2024; arXiv v3, 2024-11-23. PRELUDE is the framework and CIPHER its algorithm: one paper.
- **Mechanism:** Infer textual preferences from output edits, retrieve and aggregate preferences associated with similar contexts, and condition future generation without fine-tuning.
- **Evidence:** Summarization and email tasks use 200 rounds with GPT-4 simulated editing users and three seeds. Best configurations reduce cumulative token edit distance by approximately 31%/73% against no learning. On summarization only, seven human judges assess 15 pairs per comparison; three human editors follow assigned preferences.
- **Limits:** These human assessments are not natural longitudinal online personalization. Preferences are prescribed by source category; edit distance is not measured time saved or satisfaction. An oracle gap remains.
- **Resources/read scope:** [Official repository](https://github.com/gao-g/prelude), MIT; underlying dataset rights remain separate. Read v3 §§4.1–4.4, mechanism/metric passages, proceedings metadata and repository resource page. No reproduction.

<a id="method-alignxplore"></a>
### M54. AlignXplore · Updating explicit preferences from behavioral signals

[Extended Inductive Reasoning for Personalized Preference Inference from Behavioral Signals](https://arxiv.org/html/2505.18071v2) — arXiv v2, 2025-07-07; venue unverified.

Converts behavioral examples into explicit preferences using synthetic cold-start training and GRPO; streaming inference reuses the previous summary. AlignX/P-Soups tests mainly use preference pairs. Metrics distinguish Acc_jud (preference judging), Acc_gen (preference-guided generation), and GPT-4 win rate; “online evaluation” uses GPT-4 judgments, not live users. The main setting uses two four-example rounds; §4.4 also tests simulated reversals among eight pairs, and §4.5 extends efficiency testing to round four, totaling 16 signals. These do not establish lifelong adaptation; real-user validation is missing. Privacy statements provide no formal guarantee. [Official code](https://github.com/AntResearchNLP/AlignXplore) is accessible, but a project root license was not confirmed; the paper’s CC BY-NC-ND license does not establish code licensing.

**Reading scope:** v2 §3, §4 evaluation setup and streaming experiments, Appendices C–D; official README and root listing. Targeted methods, evaluation and limitations reading; official README/root, not an exhaustive full-paper review.

<a id="method-plus"></a>
### M61. PLUS — co-training textual user summaries and personalized rewards
- **Paper:** *Learning to summarize user information for personalized reinforcement learning from human feedback*, ICLR 2026; arXiv v4 (2026-08-26).
- **Method and evidence:** PPO optimizes summaries while a summary-conditioned reward model is alternately trained. Pets/UltraFeedback use constructed preferences; PRISM contains existing human conversations. Training uses 1,000 PRISM users; known-user reward accuracy is 62.9% versus BTL's 59.8%, while unseen-user prediction remains difficult.
- **Limits:** GPT-4o's 72% win rate is assessed by an oracle reward model trained on self-reported preferences, not human votes or deployed satisfaction. Main-text “308 users × two prompts” conflicts with appendix “906 prompts”; do not merge denominators. Online co-adaptation means the training loop, not continuous learning from deployed users. Editable summaries are future work. Hyperparameter sensitivity and sensitive-profile exposure remain concerns.
- **Resources and reading:** [v4](https://arxiv.org/html/2507.13579v4), §§4–7, ethics/reproducibility and Appendix F; [official project](https://sites.google.com/stanford.edu/plus/home) and linked [code](https://github.com/nam630/pluralistic_user_summary_public). Code Apache-2.0; paper CC BY-NC-SA 4.0. Complete weights/data release not verified.

<a id="method-user-profile-ablation"></a>
### M62. Understanding the Role of User Profile — historical responses and context ordering
- **Paper:** *Understanding the Role of User Profile in the Personalization of Large Language Models*, arXiv v1 (2024-06-22); publication venue not confirmed.
- **Method and evidence:** Ablations on six LaMP tasks (excluding LaMP-6) vary historical inputs, responses, mappings and ordering. Main experiments use fine-tuned Flan-T5-base, with frozen Llama2-7B-chat checks. Results use validation sets because hidden tests were unavailable; no newly recruited user study. Historical responses generally contribute more, output-only contexts fit more records, and earlier profiles matter more in these settings.
- **Limits:** An analysis of profile conditioning, not a new general-purpose execution agent. Findings are specific to tested models, tasks, prompts and context budgets; they do not justify universally discarding inputs/mappings or assuming a universal position effect. Automatic task scores do not establish user satisfaction or longitudinal adaptation.
- **Resources and reading:** [Paper](https://arxiv.org/html/2406.17803v1), §§3–5 and Appendices A/B; [official code](https://github.com/Bingo-W/Personalisation-in-LLM). Code MIT; paper CC BY 4.0. LaMP is an existing resource, not a newly released dataset from this paper.

<a id="method-ariel"></a>
### M66. ARIEL · EEG-assisted emotional adaptation

[ARIEL: Brain-Computer Interfaces meet Large Language Models for Emotional Support Conversation](https://iris.uniroma1.it/handle/11573/1727073) — UMAP **Adjunct** ’24, pp.601–609; DOI 10.1145/3631700.3665193.


- **Scope**: institutional record and attached published PDF §§3–5.
- **Mechanism**: EEG-classified emotion labels and messages enter hard-prompt templates for LLaMA 2 Chat.
- **Evidence**: component study collected Muse 2 EEG from 30 subjects over 40 music-video trials each; consent/anonymization reported. LOSO with five-fold tuning yields SVM per-emotion accuracies of Happy .77, Angry .78, Sad .76 and Relaxed .80. End-to-end dialogue evidence is a controlled real-session example.
- **Boundary**: classifier accuracy is not emotional-support efficacy; in-vivo system evaluation remains future work. Inferred labels do not establish reliable access to actual mental states or clinical benefit.
- **Resources**: institutional PDF marked all rights reserved; no official code/data release identified. Reported privacy handling is not an independent security audit.

<a id="tmp-b-exfil"></a>

<a id="method-pearl"></a>
### M71. Pearl

**Adjacent method: writing-retrieval calibration** · Unique paper key: `PEARL`

[Paper](https://arxiv.org/html/2311.09180v2) · v2, 2024-11-05; CustomNLP4U 2024

Calibrates retrieval by historical documents’ benefit to personalized generation, also supporting poor-retrieval detection and revision. WorkSm evaluation requests are author-written, while its training requests are synthesized by GPT-4; AITA lacks timestamps. Evaluation on both datasets is offline. Reference/stance metrics and LLM judging do not establish live-user satisfaction, authorized sending, or privacy controls.

**Assets and reproduction：** [Publication](https://aclanthology.org/2024.customnlp4u-1.16/): CustomNLP4U workshop, not ACL main. Private WorkSm and closed APIs limit reproduction; official code/weights unverified. Read arXiv article: CC BY-NC-ND 4.0, not a license to underlying data.

**Actual reading scope：** Sections 4–5, Appendix E, version and publication records.

<a id="tmp-m-personax"></a>

<a id="method-personax"></a>
### M72. PersonaX

**Adjacent method: cached recommendation personas** · Unique paper key: `PERSONAX`

[Paper](https://aclanthology.org/2025.findings-acl.300.pdf) · Findings ACL 2025, pp. 5764–5787

Clusters/samples long histories and generates cached persona snippets offline. Amazon CDs/Vinyl and Books ranking uses the last interaction plus nine sampled negatives. Offline ranking is not live satisfaction or general assistance. Streaming freshness remains untested; latency analysis assumes a persona refresh every ten calls.

**Assets and reproduction：** [Author repository](https://github.com/Ancientshi/PersonaX) includes MIT code and data subsets, but README explicitly disclaims full AgentCF/Agent4Rec reproduction by its EasyRec client. The [license scope](https://github.com/Ancientshi/PersonaX/blob/master/LICENSE) explicitly excludes Amazon data, notebook outputs, EasyRec, and third-party code, dependencies, and weights; project MIT terms do not authorize those assets. This scope was supplied by independent review; the original NOTICE fetch for this entry encountered a cache miss.

**Actual reading scope：** PDF sections 4–5, limitations/ethics, official README/file tree.

<a id="method-prime"></a>
### M76. PRIME: personal semantic memory and personalized thinking

Studies episodic/semantic memory configurations and self-distills personalized thinking; **the main reported PRIME configuration excludes episodic memory**. CMV uses real Reddit histories from 41 authors, 133 evaluation queries, and 7,514 historical interactions, but evaluates offline reply ranking—not live human-agent interaction. Llama-3.1-8B Hit@3 is 45.79 versus 36.77 without personalization; this does not establish action success or online adaptation.

- Paper/version: [PRIME: Large Language Model Personalization with Cognitive Dual-Memory and Personalized Thought Process, 2507.04607v3](https://arxiv.org/html/2507.04607v3), 2025-09-26. The repository’s shortened title is an alias.
- Assets: [Official repository](https://github.com/launchnlp/LM_Personalization) exposes README and data; framework code is marked as being cleaned; license unverified. The paper’s arXiv non-exclusive distribution license is not a code license.
- Inspected: §§3–7, limitations, README, repository root.

Verification boundary: Only the specified paper sections and resource pages were inspected. No installation, training, independent benchmarking, or security audit was performed. Resource status checked on 2026-11-01.

<a id="method-lc-rag-copa"></a>
### M81. Method with human evidence — LC-RAG / Copa

[Personalizing Student-Agent Interactions Using Log-Contextualized Retrieval-Augmented Generation (RAG)](https://arxiv.org/html/2505.17238v3) — AIED25 Workshop on Epistemics and Decision-Making in AI-Supported Education; arXiv v3, April 18, 2026. Not an AIED main-conference paper.

**Checked / reading scope**: November 1, 2026; relevant §§3–5 passages, arXiv metadata, official supplement README/root listing.

- **Mechanism**: RQ1 uses GPT-3.5-Turbo to summarize student discourse/logs for retrieval; Copa also compares student and expert computational models.
- **Evidence**: RQ1: 18 consented student contributors and 216 segments across five embedding configurations, with GPT-4o judging retrieval comparisons. RQ2: 18 unique Copa participants in qualitative classroom/focus-group studies, including two who also participated in RQ1; these samples must not be added as disjoint populations.
- **Limits**: Adjacent education personalization, not persistent personal memory; one of five embeddings substantially underperforms, with incorrect advice/overreliance and no causal learning-gain proof.
- **Resources and rights**: IRB approval, student assent and parental consent reported. The [official supplementary repository](https://github.com/claytoncohn/AIED25_Supplementary_Materials) contains six prompt files and a README; no raw student data or root license observed.

<a id="method-alignx"></a>
### M87. User-level preference alignment

**From 1,000,000 Users to Every User: Scaling Up Personalized Preference for User-level Alignment** — ACL 2026 Long Papers, 2026.acl-long.1391; also reviewed arXiv 2503.15463v3 (2025-05-22). [Publication](https://aclanthology.org/2026.acl-long.1391/) | [arXiv v3](https://arxiv.org/html/2503.15463v3) | [New code repository](https://github.com/AntResearchNLP/AlignX-Family) | [Standalone repository](https://github.com/JinaLeejnl/AlignX) | [Dataset card](https://huggingface.co/datasets/JinaLeejnl/AlignX)

**Method/data.** AlignX supports persona-conditioned and preference-bridged AlignXpert alignment. Reviewed arXiv v3 §3–7 and limitations/ethics appendices, final ACL 2026 results/limitations/ethics, repositories and dataset card. Over 1.3M constructed examples are not that many verified users; forum/alignment sources underpin assembled/generated personas. Offline accuracy and model judging do not establish longitudinal adaptation or action authorization. Identifier removal/PII filtering are not consent or privacy guarantees. HF advertises MIT for data; root code licensing remains unconfirmed. Keep paper totals separate from current viewer counts.

<a id="method-safari"></a>
### M90. SAFARI / KBP

**Large Language Models as Source Planner for Personalized Knowledge-grounded Dialogues (SAFARI)** | Findings of EMNLP 2023, pp. 9556–9569; inspected arXiv 2310.08840v1 (2023-10-13). **Scope: knowledge-source planning under persona–knowledge dependencies; KBP is the accompanying dataset, not a separate paper.** Source selection, retrieval and response assembly use dependency relationships supplied in advance. KBP contains 2,477 Chinese dialogues and 24,554 utterances; annotators author both roles using assigned system personas and knowledge, rather than recording natural personal-user deployment. Human evaluation covers 100 responses per model with three annotators and excludes planning effects from that comparison. **The automated metrics have a separate test-selection risk: Appendix C evaluates the NLI model on the KBP test set every 500 training iterations, retains the checkpoint with the highest test performance, and uses it to compute P.C/K.C. Automated consistency scores may therefore be optimistic; this is not an untouched-test evaluator. This caveat concerns NLI-based metrics, not the separately reported human ratings above.** Limitations include cascading errors, retrieval noise, outdated knowledge and untested source types. **Source calls are not external actions or authorization validation.** The author repository contains data and implementation directories, but no root license was found and GitHub license metadata is null. Reuse permission remains unverified; no reproduction was run.

Sources:
- [Formal venue, canonical plural title and DOI 10.18653/v1/2023.findings-emnlp.641](https://aclanthology.org/2023.findings-emnlp.641/)
- [Exact arXiv version; abstract-page title uses singular Dialogue](https://arxiv.org/abs/2310.08840v1)
- [Original data collection, method, evaluation and limitations, §§3–6, Limitations, Ethics Statement and Appendices C/E](https://arxiv.org/html/2310.08840v1)
- [Author repository, default branch master](https://github.com/hrwise-nlp/SAFARI)

Actual inspection: formal publication metadata; arXiv data-collection, method, evaluation and limitation sections, plus Appendix C on NLI checkpoint selection and Appendix E on human/NLI evaluation differences; repository root, README and GitHub license metadata. Verified the presence of kbp.zip, lora, tools and unsupervised; did not unpack the dataset or execute the implementation.

<a id="method-unims-rag"></a>
### M91. UniMS-RAG

**UniMS-RAG: A Unified Multi-source Retrieval-Augmented Generation for Personalized Dialogue Systems** | 2024, arXiv 2401.13256v3 (2024-11-26; formal venue unverified). **Scope: unified source selection, relevance evaluation and personalized response generation.** Acting/evaluation tokens support joint training; relevance and NLI consistency guide iterative evidence/response refinement. Evaluation uses DuLeMon Both and KBP, involving user personas, system personas and external knowledge—not uniformly personal-user memory. “Acting” selects retrieval sources; **it does not demonstrate authorized external execution.** Human evaluation uses 100 responses per dataset/model and three annotators, with approximately 82% agreement. **Important caveat: §V-D selects the NLI evaluator checkpoint by its highest KBP test-set performance. Automated consistency scores may therefore be optimistic; this is not an untouched-test evaluator.** A dedicated official implementation and its license were not verified. Training details and upstream code links are provided; reproduction was not executed.

Sources:
- [Exact version and metadata](https://arxiv.org/abs/2401.13256v3)
- [Original method, datasets and metrics, §§IV–V; evaluator selection §V-D; human evaluation §VII-D](https://arxiv.org/html/2401.13256v3)

Actual inspection: version page; original method, datasets, metrics, training/evaluator-selection, main-result and human-evaluation passages; targeted searches for an official implementation and venue. No dedicated official implementation was verified; this does not establish that none exists. No evaluator retraining or independent score reproduction was performed.

<a id="methods-a-memory-and-persistent-state"></a>
<a id="method-persistent-user-profiles"></a>
### M93.  Method

**Enabling Personalized Long-term Interactions in LLM-based Agents through Persistent Memory and User Profiles** | [2510.07925v1](https://arxiv.org/html/2510.07925v1), 2025-10-09. Only v1 in inspected history; formal venue unverified.

Coordinated retrieval, validation and generation combine short-term context, summaries, persistent memory and incremental JSON user profiles. Offline evaluation uses GVD, LoCoMo and LongMemEval. A separate five-day smartphone pilot enrolled seven people; four completed and three left after day one, with approximately ten minutes of daily interaction. Completers valued recall; three criticized long/generic responses and three reported ambiguous-follow-up failures, without establishing whether these were the same participants.

Results do not uniformly beat RAG: GPT-4o/LongMemEval correctness is 72.8% versus RAG’s 77.7%; some Gemini 2 coordinator-removal ablations perform better. Short duration, attrition and subjective feedback do not establish long-term benefit; proactivity remains future work.

**Resources/license:** paper CC BY 4.0; dedicated official code/data and software licensing unverified. **Inspected:** §§3–5, Table 1, pilot setup/results, conclusion/future work and version history; implementation not run.

<a id="method-ai-persona"></a>
### M99.  Method: AI PERSONA — WIP

[AI PERSONA: Towards Life-long Personalization of LLMs](https://arxiv.org/html/2412.13103v1) — 2412.13103v1, 2024-12-17; arXiv still marks **Work in progress**; venue unverified.

- **Mechanism:** Historical-session management, tool simulation/interfaces and periodic persona-profile updates without retraining.
- **Samples:** PersonaBench has 200 profiles and over 6,000 synthetic points. Volunteer profiles are seeds, not a longitudinal human-interaction cohort.
- **Evaluation:** LLM-judged helpfulness/personalization, profile similarity and utterances needed to satisfy a simulated user. GPT-4o uses the full benchmark; other models use ten-persona subsets.
- **Limits:** Chinese-native-speaker seed/annotation bias; “life-long” names the task, not observed lifetime effectiveness.
- **Resources/rights:** [Official repository](https://github.com/tml1026/Lifelong-Personalized-Agent) contains public code, generation scripts and data files. No LICENSE observed in root/README; reuse rights, full-benchmark completeness and reproduction remain unverified. Do not repeat the abstract's future-release promise as the current state.
- **Reading scope:** Metadata, relevant §§3–4, Tables 1–2, §6, repository README/root/data listings; no code execution, record-by-record audit or volunteer seed-consent verification.

<a id="method-finpersona"></a>
### M101. FinPersona: financial preference-dialogue demo

**Type: method/system; financial research prototype with limited human-evaluation evidence.** Elicits investment preferences, builds a profile and contextualizes discussion of one target stock. Big Five settings control the advisor’s personality, not inferred user personality. A preliminary evaluation with 20 external users lacks detailed protocol and quantitative reporting. It does not establish investment returns, emotional-health benefits or deployment safety. Historical financial context requires updating; RAG is an extension. Authors advise verification and professional consultation. Code, data licensing and detailed privacy governance remain unverified.

**Version/resources:** ECIR 2025 conference demonstration, Volume V, pp.13–18, DOI [10.1007/978-3-031-88720-8_3](https://doi.org/10.1007/978-3-031-88720-8_3). The [author publication record](https://javiersanzcruza.github.io/pubs) provides manuscript, video and poster. Publisher DOI access failed through this tool; author manuscript and venue record were verified. Do not merge unrelated projects sharing the FinPersona name.

**Actual reading:** [Six-page author manuscript](https://javiersanzcruza.github.io/assets/papers/ecir2025_demo.pdf), especially §§2–3 and footnotes 4–5; author publication record. Not treated as investment-return or clinical-efficacy evidence.

<a id="method-cue-cot"></a>
### M103. Cue-CoT: user-status inference

[Cue-CoT: Chain-of-thought Prompting for Responding to In-depth Dialogue Questions with LLMs](https://arxiv.org/html/2305.11792v2) — inspected arXiv v2, 2023-10-15; published in [Findings of EMNLP 2023](https://aclanthology.org/2023.findings-emnlp.806/).

**Inspected:** Abstract, relevant §§3–5 and limitations passages; official README/root listing.

- **Method:** Infer personality, emotional and psychological cues before responding; joint O-Cue or staged M-Cue with demonstration selection.
- **Evidence:** Six Chinese/English datasets and five models. Personality dialogues were synthesized by ChatGPT from Quora/Zhihu question–answer seeds, including inferred personality and generated continuations; the other four datasets reuse existing corpora. Evaluation mainly uses ChatGPT pairwise win rates for helpfulness and acceptability. Three master's-student raters assessed 100 response pairs per dataset to check agreement with automated evaluation.
- **Limits:** Intermediate inference correctness was not directly validated; prompt/order sensitivity remains. This does not establish persistent-profile accuracy, personality diagnosis or clinical efficacy.
- **Resources/rights:** The [official repository](https://github.com/hrwise-nlp/Cue-CoT) provides benchmark/demo material. Its 3k-public-data description also excludes PsyQA; generation/evaluation code remains advertised as forthcoming. Research-only and upstream restrictions apply; forum-user consent is not established.

<a id="method-pag"></a>
### M104. Summary-augmented personalization (survey shorthand: PAG)

[Integrating Summarization and Retrieval for Enhanced Personalization via Large Language Models](https://arxiv.org/html/2310.20081v1) — v1, 2023-10-30. The [official publication page](https://www.amazon.science/publications/integrating-summarization-and-retrieval-for-enhanced-personalization-via-large-language-models) lists the CIKM 2023 Personalized Generative AI workshop. PAG is not an explicit method name in the inspected paper.

**Inspected:** Abstract, §§2–4, Tables 1–3 and official publication page.

- **Method:** Offline task-aware summaries plus runtime BM25 retrieval and fine-tuned FlanT5-base.
- **Evidence:** Six public LaMP tasks, user-separated split, private LaMP-6 excluded; three-run means. The 75% reduction means retrieved items decrease from four to one—not total tokens or cost. Five tasks are comparable/better; LaMP-4 underperforms.
- **Limits:** Narrow benchmark; voice-assistant motivation is not deployment or real-user benefit evidence. Cross-application profiling consent and clinical validation are not established.
- **Resources/rights:** No paper-specific official code verified. Reuses LaMP rather than introducing a benchmark. Paper CC BY-SA 4.0 does not establish data/model rights.

<a id="memory-methods"></a>
## Methods: Memory and persistent state

How is personal context stored, updated, retrieved, or forgotten? This includes conversational and multimodal memory; retrieval accuracy does not establish authorized action or secure erasure.

<a id="method-memorybank"></a>
### M1. MemoryBank · Updating, reinforcement, and forgetting

[MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://arxiv.org/abs/2305.10250) — 2023 preprint.

**Checked / reading scope:** 2026-10-31; Paper abstract; official README mechanism, evaluation-data, and model notes, plus the LoRA release page.

- **Idea:** Store / retrieve conversations, summarize user information, and strengthen or fade memories using a forgetting-curve-inspired mechanism.
- **Relevance and limits:** Directly targets long-term conversational companionship. SiliconFriend is not a tool-execution system, and its experiments are not clinical evidence for psychological services.
- **Resources:** [Code and Chinese / English evaluation data](https://github.com/zhongwanjun/MemoryBank-SiliconFriend), [ChatGLM / BELLE LoRA checkpoint release](https://github.com/zhongwanjun/MemoryBank-SiliconFriend/releases/tag/LoRA_checkpoint). Adapters and base models are different artifacts with separate permissions.

<a id="method-memgpt"></a>
### M2. MemGPT · Hierarchical memory and context management

[MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) — 2023 preprint, revised 2024.

**Checked / reading scope:** 2026-10-31; Paper abstract; research project page, data entry point, Letta README current-source/historical-version notes, and the letta-code entry point.

- **Idea:** Borrow OS-style memory hierarchies to move information between limited context and external memory, with control flow for continued execution.
- **Relevance and limits:** Includes multi-session chat and long-document experiments. Virtual context does not mean infinite, lossless, or cost-free memory.
- **Resources:** [Research page / experimental data entry point](https://research.memgpt.ai/), [historical MemGPT / Letta entry point](https://github.com/letta-ai/letta), [current Letta Code source](https://github.com/letta-ai/letta-code). The legacy entry point directs readers to letta-code and keeps the retired V1 server on its archive branch. Reproduction requires locating the original version; neither the current product nor retired V1 automatically matches the paper implementation.

<a id="method-a-mem"></a>
### M3. A-MEM · Linked notes and evolving memory

[A-MEM: Agentic Memory for LLM Agents](https://arxiv.org/abs/2502.12110) — NeurIPS 2025.

**Checked / reading scope:** 2026-10-31; Paper abstract and relevant §4.2 dataset/metric passages; purpose statements in the two official repositories.

- **Idea:** Organize memory as Zettelkasten-inspired notes, generate attributes and links, and revise existing memory representations as information arrives.
- **Relevance and limits:** A structure for associative assistant memory. Long-dialogue QA does not establish real task completion or consistently correct memory edits.
- **Resources:** [Paper evaluation code](https://github.com/WujiangXu/A-mem), [integrable system](https://github.com/WujiangXu/A-mem-sys). These repositories have different purposes; this is an external-memory method, not a new foundation model.

<a id="method-mem0"></a>
### M4. Mem0 · Extraction, consolidation, and retrieval

[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://arxiv.org/abs/2504.19413) — 2025 arXiv paper version.

**Checked / reading scope:** 2026-10-31; 2025 paper abstract; current official README and research page, used to distinguish the paper from later project changes.

- **Idea:** Extract important conversational information, consolidate updates, and retrieve it; the paper also explores graph memory.
- **Relevance and limits:** Supports cross-session personal context. LoCoMo accuracy, latency, and token measurements cannot be generalized to every task or deployment.
- **Resources:** [Official project code](https://github.com/mem0ai/mem0). Code, hosted services, and algorithms continue evolving. This entry covers the 2025 approach, not current marketing scores presented as independent reproduction.

<a id="method-zep"></a>
### M5. Zep / Graphiti · Temporal validity and historical records

[Zep: A Temporal Knowledge Graph Architecture for Agent Memory](https://arxiv.org/html/2501.13956v1) — 2025 preprint; inspected v1, 2025-01-20.

**Checked / reading scope:** 2026-10-31; Abstract, §2.2.3, §3 retrieval interface, §4 evaluation overview, official repository README and license.

- **Idea:** Convert conversations or business events into timestamped entities and relationships. Conflicting new facts invalidate old edges while retaining history. Queries return time-qualified context for an answer model.
- **Relevance and limits:** Supports versioning of personal facts and preferences. DMR and LongMemEval measure QA accuracy and latency. Models can misjudge conflicts; invalidation is not physical erasure, and QA gains do not establish tool-task success.
- **Resources:** [Official Graphiti code](https://github.com/getzep/graphiti), Apache-2.0; [official Zep / Graphiti distinction](https://help.getzep.com/zep-vs-graphiti). The public engine, full hosted service, and 2025 paper configuration are not interchangeable, nor is this a new foundation-model release.

<a id="method-memos"></a>
### M6. MemOS · Memory as a governed resource

[MemOS: A Memory OS for AI System](https://arxiv.org/html/2507.03724v1) — this entry pins the 2025 preprint v1, 2025-07-04.

**Checked / reading scope:** 2026-10-31; v1 abstract, §4.2 metadata, §5.5 governance-interface excerpts, §6 evaluation overview, current official README and license.

- **Idea:** MemCube packages content with provenance, versions, access policies, and lifecycle metadata, proposing unified management of plaintext, activation, and parameter memory. Histories, queries, and memory operations produce updated resources and inference context.
- **Relevance and limits:** An architecture for persistent-assistant memory governance. v1 evaluates LoCoMo QA, retrieval, and KV acceleration. Governance design is not proof of erasure, permissions, or tenant isolation; architectural goals are not automatically implemented features.
- **Resources:** [Official repository](https://github.com/MemTensor/MemOS), Apache-2.0. The current README describes MemOS 2.0 Stardust, not frozen paper code. Locate the MemOS-0630 configuration for reproduction rather than adopting current marketing scores. LoCoMo and other upstream data have separate terms.

<a id="method-secom"></a>
### M23. SeCom · Topic segmentation and compression-based denoising

[On Memory Construction and Retrieval for Personalized Conversational Agents](https://arxiv.org/abs/2502.05589) — ICLR 2025; the conference title adds SeCom, but this is the same paper. First submitted 2025-02-08; current v3 dated 2025-03-03.

**Verification / reading scope**: 2026-11-01; relevant [v1](https://arxiv.org/html/2502.05589v1) §2–3 method/experiment passages and appendix evaluation notes; official project page, README, and LICENSE. No exhaustive v1–v3 comparison.

- **Mechanism**: Segment historical conversations into coherent topics, then use LLMLingua-2 compression to denoise retrieval units.
- **Evidence/limits**: Offline answering on LOCOMO and Long-MT-Bench+, plus separate segmentation experiments. The main LOCOMO table uses author-generated QA; official QA appears separately in the appendix. These are not interchangeable with other papers' standard benchmark scores and do not establish real-user longitudinal utility or execution.
- **Resources**: [Official implementation](https://github.com/microsoft/SeCom); [MIT LICENSE](https://github.com/microsoft/SeCom/blob/main/LICENSE) verified. Upstream models and datasets require separate checks.

<a id="method-rmm"></a>
### M24. RMM · Prospective organization and retrospective retrieval adaptation

[In Prospect and Retrospect: Reflective Memory Management for Long-term Personalized Dialogue Agents](https://aclanthology.org/2025.acl-long.413/) — ACL 2025; 2503.08026 first submitted 2025-03-11, v2 dated 2025-07-28.

**Verification / reading scope**: 2026-11-01; relevant [v1](https://arxiv.org/html/2503.08026v1) §4–8 method, setup, and results passages; arXiv history and ACL metadata. Description is grounded in v1, not an exhaustive comparison with v2.

- **Mechanism**: Extract/merge topic memories after sessions; adapt a lightweight reranker through online RL using the generator's memory citations as feedback.
- **Evidence**: MSC response similarity and LongMemEval retrieval/answer metrics; main generator Gemini-1.5-Flash. In v1 Table 1, GTE-based answer accuracy is 63.6% for RAG and 70.4% for RMM: +6.8 percentage points, not an unconditional “+10 points.”
- **Limits/resources**: Self-generated citation rewards are neither human feedback nor a guarantee of faithful attribution. Real deployment and permission safety are not established. An official implementation and its license were not verified; this is not a claim that no code exists.

<a id="method-memguide"></a>
### M25. MemGuide · Select memories by intent and missing slots

[MemGuide](https://arxiv.org/html/2505.20231v2) — AAAI 2026; same paper as B37, counted once.

**Verification / reading scope**: 2026-11-01; v2 MemGuide and Experiments passages and Table 3; version, dataset, and resource checks are recorded under B37.

- **Mechanism**: Retrieve intent-aligned QA memories, then rerank with missing-slot reasoning and a fine-tuned LLaMA-8B filter to reduce redundant questions.
- **Evidence/limits**: On MS-TOD, GPT-4o-mini improves from 88% to 99% success (+11 percentage points) and from 6.03 to 3.19 turns versus full-context prompting. This is one setup, not a universal model or real-transaction improvement. Historical candidate values do not authorize new actions.
- **Resources**: [Author code/data](https://github.com/Elvin-Yiming-Du/MS_TOD_Memory). The unrelated embodied MemAdapter dataset also called MemGuide is not this paper's asset; licensing limits are recorded under B37.

<a id="method-rgmem"></a>
### M28. RGMem · Hierarchical user-profile evolution

[RGMem: Renormalization Group-inspired Memory Evolution for Language Agents](https://arxiv.org/html/2510.16392v3) — arXiv records ICML 2026 acceptance; inspected v3, June 2, 2026. The earlier “…Group-based…User Profile” title is the same paper.

**Verified / actual reading scope:** 2026-11-01; v3 relevant §3 methodology passages and Appendix B.1 evaluation protocol; arXiv version/acceptance record, author README, and repository root. Selected passages, not a line-by-line full-paper review; no installation, execution, or experimental reproduction.

- **Mechanism:** Aggregates episodic facts and user inferences into a hierarchical graph, separating rapidly changing evidence from slower traits through thresholded updates and multi-scale retrieval.
- **Evidence/limits:** LOCOMO uses model judging; PersonaMem-128k uses multiple-choice accuracy, averaged over three runs. External-memory evolution is not continual backbone training; neither benchmark proves profile truth, privacy or long-term human utility.
- **Resources:** [Author implementation](https://github.com/fenhg297/RGMem), MIT-labeled; requires components including Elasticsearch, Neo4j and Redis. Not executed.

<a id="method-premem"></a>
### M32. PREMem · Reasoning across sessions before storage

[Pre-Storage Reasoning for Episodic Memory](https://aclanthology.org/2025.findings-emnlp.1204/) — Findings EMNLP 2025; [arXiv v1](https://arxiv.org/html/2509.10852v1), 2025-09-13.

**Actual reading scope:** v1 §§3–5, Tables 1/5, Limitations; publication record, author README/root listing. No complete publication-version comparison or execution.

- **Mechanism:** Extracts factual, experiential and subjective fragments, then clusters, temporally links and derives cross-session inferences for retrieval.
- **Evidence:** Offline LoCoMo, 1,986 questions, and LongMemEval-S, 500 questions. LoCoMo conversations are model-generated and human-edited; LongMemEval sessions are simulated and human-edited, not longitudinal records of real-user use. Metrics include text similarity, LLM judging and abstention accuracy for unanswerable questions.
- **Boundary:** Authors acknowledge weaker single-hop performance, loss of original linguistic nuances and no forgetting mechanism. Inferred information is neither user-confirmed fact nor action authorization.
- **Resources:** [Code/instructions](https://github.com/sangyeop-kim/PREMem) are public, but no root LICENSE was found; code reuse rights remain unconfirmed. README identifies upstream LoCoMo as CC BY-NC 4.0 and LongMemEval as MIT, not PREMem code licensing. Linked dataset-zip access/integrity was not verified.

<a id="method-nemori"></a>
### M33. NEMORI · Distilling memory through prediction error

[What Deserves Memory: Adaptive Memory Distillation for LLM Agents](https://arxiv.org/html/2508.03341v4) — v4, 2026-04-16; venue not confirmed in this inspection. Earlier *Nemori: Self-Organizing Agent Memory Inspired by Cognitive Science* has the same arXiv ID and is not another paper.

**Actual reading scope:** v4 §§3–4.7, Tables 2/7/8, Limitations; version record, author README, evaluation instructions and MIT LICENSE. No complete revision comparison or execution.

- **Mechanism:** Organizes interactions into narrative episodes and distills differences between observed content and predictions from existing knowledge, without updating backbone parameters.
- **Evidence:** Offline LoCoMo, 1,540 questions, and LongMemEval-S, 500. LoCoMo conversations are model-generated and human-edited; LongMemEval sessions are simulated and human-edited, not longitudinal records of real-user use. With GPT-4.1-mini as method backbone/answer generator and GPT-4o-mini as judge, LoCoMo averages 80.8 versus full-context 80.6. With a GPT-4o-mini backbone, LongMemEval knowledge-update scores are worse, 61.5 versus 78.2. Avoid claims of uniform superiority.
- **Boundary:** Simple management/retrieval and bespoke integration are acknowledged limitations; safe deletion and longitudinal human utility are not demonstrated. Its LoCoMo subset differs from PREMem, preventing direct score ranking.
- **Resources:** [Implementation](https://github.com/nemori-ai/nemori) is MIT. The rewrite is incompatible with the legacy MVP and depends on PostgreSQL, Qdrant and model APIs. Download evaluation data separately under upstream terms; README V5 scores are not v4 paper scores.

<a id="method-knowledge-graph-tuning"></a>
### M36. Knowledge Graph Tuning · Feedback-driven factual updates

[Knowledge Graph Tuning: Real-time Large Language Model Personalization based on Human Feedback](https://arxiv.org/html/2405.19686v1) — arXiv v1, 2024-05-30.

**Verification date / reading scope:** 2026-11-01; §4, §5.1–5.4 and §6: method, experimental setup, metrics, ablations and limitations.

- **Method:** Extract query/feedback triples and add/remove external KG facts while freezing LLM weights.
- **Evaluation:** Sequential counterfactual QA on CounterFact and GPT-4-assisted CounterFactExtension; efficacy/paraphrase scores, latency and GPU memory.
- **Boundary:** A factual-personalization proxy, not real-user preference evolution. GPT-4 simulates relation feedback. Instruction following and extraction matter; answer-probability comparisons are not unrestricted task success.
- **Resources:** No verified official available release or software/data license; paper CC BY 4.0. A direct GitHub connector GET of https://api.github.com/repos/W-R-Liu/KGT returned explicit NOT_FOUND / HTTP 404 during this audit. This secondary-source link is not a verified official implementation; the response does not establish permanent nonexistence.

<a id="method-emg-rag"></a>
### M37. EMG-RAG · Editable personal memory graphs

[Crafting Personalized Agents through Retrieval-Augmented Generation on Editable Memory Graphs](https://aclanthology.org/2024.emnlp-main.281/) — EMNLP 2024; methods checked in [arXiv v1, 2024-09-28](https://arxiv.org/html/2409.19401v1).

**Verification date / reading scope:** 2026-11-01; arXiv §4–5.2 and §7; ACL publication metadata and PDF method overview.

- **Method:** Editable hierarchical memory graphs and RL-based memory selection feed a frozen LLM.
- **Evaluation:** Real assistant conversations/screenshots with GPT-4-derived memories/QA labels; QA overlap metrics, entity exact match, and four-week edits.
- **Human evidence:** A separate month-long online A/B adaptation uses real questions and manual answers; not wholly synthetic/offline. Metrics still do not establish satisfaction or executed services.
- **Boundary/resources:** Repeated LLM calls make training costly; graph deletion is not backup/log erasure. No verified public business dataset or official implementation; arXiv CC0 concerns the paper, not private data.

<a id="method-hybridmem"></a>
### M38. HybridMem · Retrieval and clustered parametric memory

[Explicit v.s. Implicit Memory: Exploring Multi-hop Complex Reasoning Over Personalized Information](https://arxiv.org/html/2508.13250v1) — arXiv v1, 2025-08-18; benchmark in B46. Count the paper once.

**Verification date / reading scope:** 2026-11-01; §3 experimental settings, §4–5 comparisons and §6 hybrid memory; official README, complete file tree and release metadata.

- **Method:** Cluster user statements and train separate LoRA adapters; retrieve statements at inference time and select the relevant adapter by voting.
- **Evaluation:** Multi-hop QA over synthetic personalized facts in MPR, using normalized exact match to compare explicit, implicit and hybrid memory across reasoning structures; do not conflate settings.
- **Boundary:** Does not establish sustained real-user benefit, online memory updating, privacy deletion or action execution. Dataset counts conflict between prose and table; see B46.
- **Resources:** [official repository](https://github.com/nuster1128/MPR), master, last pushed 2025-08-24; no releases or declared repository license. The linked Drive archive was inaccessible. Paper CC BY 4.0 does not license code/data automatically; no installation or reproduction performed.

<a id="method-ld-agent"></a>
### M44. Event memory and personas for long-term dialogue

[Hello Again!](https://aclanthology.org/2025.naacl-long.272/) — NAACL 2025; publication PDF; arXiv alias `2406.05925`.

**Read:** §§3–4, limitations, Appendix A, official README and license; not executed.

- Combines event memory, topic retrieval and user/agent personas.
- MSC role-play and generated CC dialogues do not establish authentic longitudinal utility. Text-overlap metrics, persona-classification accuracy and human response-quality ratings are separate measures, not action-success rates.
- [Implementation](https://github.com/leolee99/LD-Agent) is MIT; linked Drive assets unverified; CC release remains a README TODO.
- **Deduplication:** One publication, including its arXiv version.

<a id="method-h2memory"></a>
### M47. H²Memory · Concrete and abstract personal memory

Same [paper](https://arxiv.org/html/2511.13410v2) and reading scope as B52; count once, including PAL-Set alias.

- **Mechanism:** four components—Log Graph, Background, Topic Outline and Principle—with updates and linked retrieval.
- **Evidence/boundary:** improves the listed PAL-Bench baselines; simulated/judge-rated performance is not demonstrated real-user satisfaction or autonomous action success.

<a id="method-grounded-memory"></a>
### M51. A Grounded Memory System · Visual observations into entity memory

- **Paper/version:** [A Grounded Memory System For Smart Personal Assistants](https://arxiv.org/html/2505.06328v1), arXiv v1, 2025-05-09; ESWC 2025 TEXT2KG workshop, not the ESWC main conference.
- **Mechanism:** GPT-4o captions overlapping video windows and labels entities; Neo4j stores embedded memory notes and temporal/entity relationships. A retrieval agent selects semantic search, PageRank expansion or text-to-Cypher.
- **Evidence:** An iPhone home-video prototype with illustrative question/answer outputs—not a controlled comparison, participant study or benchmark. Author-labeled correct examples do not establish 100% evaluated accuracy.
- **Limits:** Does not demonstrate superiority over standard RAG, reliable long-term entity consistency or validated dementia care. Scaling, long-term disambiguation and additional modalities remain future work.
- **Resources/read scope:** Official code/data release and artifact licenses not verified. Read §§3–5 and arXiv version/workshop metadata. No reproduction.


<a id="method-encode-store-retrieve"></a>
### M56. Encode–Store–Retrieve — language-encoded egocentric memory
- **Paper:** *Encode-Store-Retrieve: Augmenting Human Memory through Language-Encoded Egocentric Perception*, ISMAR 2024; arXiv `2308.05822` v3, 2024-10-18. An author page also uses the “Enhancing Memory Augmentation” title variant.
- **Evidence:** ego-LLaVA video-to-text, Chroma retrieval and GPT-4. Alongside QA-Ego4D, 12 participants completed controlled household tasks using HoloLens 2, with recall tested 5–7 days later. Participant ratings: system 4.1/5 versus human responses 2.5/5.
- **Limits:** Framewise encoding loses temporal actions/counting; no longitudinal real-world deployment. Device independence does not establish synchronization. Server uploads/text encoding are not privacy or isolation guarantees.
- **Resources/read scope:** [Author PDF](https://pokristensson.com/pubs/ShenEtAlISMAR2024a.pdf), §§3–7; [version record](https://arxiv.org/abs/2308.05822). No official implementation, weights or software/data reuse license confirmed. QA-Ego4D is an existing dataset, not a new release here.

<a id="method-livia"></a>
### M57. Livia — AR emotional companionship and compressed memory
- **Paper:** *Livia: An Emotion-Aware AR Companion Powered by Modular AI Agents and Progressive Memory Compression*, AIVR 2025 author-accepted manuscript; arXiv v1, 2025-08-12.
- **Evidence:** Emotion/dialogue/memory/orchestration modules, TBC/DIMF compression and AR. §8 reports 200 excerpts from 50 users, 38 participants over four weeks, 24 interviewees and 11,504 conversation turns; these denominators must not be combined.
- **Limits:** Young North American English-speaking sample; comparison allocation insufficiently described. Evaluation supplies no corresponding loneliness scale, pre/post statistics or significance test supporting the abstract’s efficacy claim. **No clinical/mental-health efficacy conclusion.** Facial-expression sensing is future work; encryption/consent/storage are requirements, not verified guarantees.
- **Resources/read scope:** [Manuscript](https://arxiv.org/pdf/2509.05298), §§3–10; [venue/version](https://arxiv.org/abs/2509.05298). Manuscript CC BY-NC-ND 4.0; no official code/data release or software license confirmed.

<a id="method-scrapmem"></a>
### M64. ScrapMem — visual compression and event-graph multimodal memory
- **Paper:** *ScrapMem: A Bio-inspired Framework for On-device Personalized Agent Memory via Optical Forgetting*, arXiv v2 (2026-05-25); publication venue not confirmed.
- **Method and evidence:** Multimodal records become scrapbook pages, indexed by an event graph and degraded through age-dependent JPEG quality/resolution. On ATM-Bench's existing four-year personal archive, No-Forget scores 51.0 Joint@10/70.3 Recall@10; Table 1's forgetting setting scores 46.9/66.1. The 93% storage saving belongs to Timed-Gentle (4302.9→299.5 MiB; Joint@10 46.3), not the 51.0 setting.
- **Limits:** Four years of source data do not establish four years of agent deployment. Qwen3-VL-2B processes memory; GPT-5-mini API judges results. The inspected experiments do not report specific endpoint hardware, latency, energy or end-to-end offline-device validation. Compression loses dates, times and addresses and can induce incorrect inference; it is not secure deletion or a privacy guarantee.
- **Resources and reading:** [v2](https://arxiv.org/html/2605.03804v2), §§4–5, Appendix B and metadata. No official code/weights release confirmed in the paper or targeted search. Its arXiv perpetual non-exclusive distribution license is not an open-source software license.

<a id="method-theanine"></a>
### M65. Theanine · Timeline-based memory

[Towards Lifelong Dialogue Agents via Timeline-based Memory Management](https://arxiv.org/html/2406.10996v3) — NAACL 2025; reviewed v3, 2025-01-29. Evaluation: **B70**; same paper.


- **Scope**: §§2–6, appendices D/E/J; official README/root listing.
- **Mechanism**: retain old memories, link graph nodes by time and relations, retrieve complete timelines, then refine them for current dialogue and response generation.
- **Evidence**: automatic, model and human evaluation plus ablations on MSC/Conversation Chronicles; TeaFarm separately stresses counterfactual recall.
- **Boundary**: “lifelong” is an architectural aim, not lifelong human evidence. Retention does not establish consent withdrawal, deletion or permission isolation.
- **Resources**: [official code](https://github.com/kimnamssya/Theanine); no standalone root code LICENSE observed. Non-commercial dataset terms and website-template licensing should not be substituted for code authorization.

<a id="method-memory-r1"></a>
### M69. Memory-R1

**Method: learned memory management** · Unique paper key: `R1`

[Paper](https://arxiv.org/html/2508.19828v5) · v5, 2026-01-14

Separately RL-trained memory operations and retrieval filtering/answering. Training uses LoCoMo, with MSC and LongMemEval evaluation. Offline dialogue QA does not establish live use, tool execution, or secure erasure. Reported 152/81/1307 split counts disagree with the stated 1:1:8 ratio; user/dialogue-disjointness was not established. Appendix B says 24 preceding turns whereas Algorithm 1 says 50; do not silently reconcile them.

**Assets and reproduction：** [Author repository](https://github.com/yansikuan/memory-r1): Apache-2.0, but README/assets only and code still marked coming soon. LoCoMo derivatives retain CC BY-NC 4.0; article uses the arXiv nonexclusive license. Not a runnable author release.

**Actual reading scope：** Sections 3–4, limitations, Appendices B/D, version metadata, repository README/file tree.

<a id="method-plum"></a>
### M73. PLUM: sequential parametric conversation memory

Augments conversations into positive/negative QA and sequentially trains a per-user LoRA with weighted cross-entropy. Evaluation starts from 100 human-written OpenAssistant prompts but uses generated replies and QA—not longitudinal deployment. Llama-3-8B-Instruct closed-question accuracy with a system prompt is 81.5%, below the best conversation-RAG baseline’s 86.5%. Evidence concerns history retention, not task execution; repeated/conflicting topics remain untested.

- Paper/version: [On the Way to LLM Personalization: Learning to Remember User Conversations, 2411.13405v1](https://arxiv.org/html/2411.13405v1), 2024-11-20.
- Assets: No author code/data release verified. The paper’s arXiv non-exclusive distribution license is not a code license.
- Inspected: §§3–6, limitations/ethics, data-generation description.

<a id="method-tacitree"></a>
### M74. TaciTree: hierarchical fact retrieval

Clusters facts, summarizes hierarchically, and selects relevant subtrees. On ImplexConv’s generated reasoning scenarios with existing-dataset distractors and selective human verification, supportive QA reaches 70.8%; opposed QA reaches only 29.70% even with o1. Better retrieval is not robust reasoning, longitudinal human use, or action success.

- Paper/version: [Toward Multi-Session Personalized Conversation: A Large-Scale Dataset and Hierarchical Tree Framework for Implicit Reasoning, 2503.07018v1](https://arxiv.org/html/2503.07018v1), 2025-03-10.
- Cross-reference: B76; same paper, counted once. See that entry for released-data count differences.
- Assets: [Official repository](https://github.com/Kaylee0501/ImplexConv) exposes framework/evaluation files; code license unverified. Neither the paper’s CC BY 4.0 nor the cards’ MIT data label automatically licenses the code.
- Inspected: §§3–6, limitations, README, dataset cards, repository root.

<a id="method-context-time-memory"></a>
### M75. Rewriting, metadata routing, and chain-of-table retrieval

Combines query disambiguation, metadata/semantic routing, table operations, and vector retrieval. On simulated conversations, GPT-3.5 averages 90.32 recall/55.27 F2 across the two unambiguous categories: retrieval metrics, not answer or action success. Evidence covers two LLMs, one embedder, and mainly single-hop queries; ambiguous temporal-plus-content queries are untested.

- Paper/version: [Toward Conversational Agents with Context and Time Sensitive Long-term Memory, 2406.00057v2](https://arxiv.org/html/2406.00057v2), 2024-06-04.
- Cross-reference: B77; same paper, counted once.
- Assets: [TemporalMemoryDataset](https://github.com/Zyphra/TemporalMemoryDataset) exposes data; method code and explicit repository license unverified. A promised code release is not an observed release; the paper’s CC BY 4.0 does not establish repository licensing.
- Inspected: §§3–6, Appendix A.1–A.3, README, repository root.

<a id="method-memweaver"></a>
### M77. MemWeaver

**Direct method: behavioral and long-term preference memory**

[Paper](https://arxiv.org/html/2510.07713v2) · arXiv v2, 2026-01-26; WWW 2026.

Combines query-guided walks over temporal/semantic behavior graphs with phase-level summaries synthesized into a global preference memory. Evaluation uses time-split LaMP-1–5/7 with Qwen3-8B and Llama-3.1-8B-Instruct; Qwen3-8B LaMP-1 accuracy is 0.6733 versus CFRAG’s 0.6566; v2 additionally reports OpinionQA, Amazon Reviews, and ChangeMyView. These are offline personalization experiments, not longitudinal deployment, tool execution, or privacy guarantees.

**Resources:** [Official code](https://github.com/fishsure/MemWeaver) includes processing, generation, evaluation, and runner files. No explicit code license was found in the root or README; the paper’s CC BY 4.0 does not license code or upstream data.

**Verification date / actually read:** 2026-11-01; version page, §§3–4, relevant Appendix C experiments, official README and root listing. No reproduction run.

<a id="method-sgmem"></a>
### M78. SGMem

**Direct method: sentence-graph retrieval for conversational memory**

[Paper](https://arxiv.org/html/2509.21212v1) · arXiv v1, 2025-09-25.

Combines sentence graphs, vector retrieval, graph expansion, and generated summaries/facts/insights. Avoiding entity-relation extraction does not eliminate LLM-generated memory. Evaluates 500 LongMemEval questions and 500 sampled LoCoMo questions, with Qwen2.5-32B-Instruct answering and serving as LLM judge. LoCoMo full-context accuracy is 0.558, above SGMem-SF Top-10 at 0.542: not a win over every baseline. Constructed-dialogue QA is not evidence of longitudinal real-user use, action completion, or contextual-integrity protection.

**Resources:** No official implementation/data release or corresponding license verified. The paper uses the arXiv perpetual non-exclusive license.

**Verification date / actually read:** 2026-11-01; version page, §§3–5, Appendix A dataset descriptions, and paper-linked resources. No reproduction run.

<a id="method-evomem"></a>
### M79. EvoMem

**Conditionally direct method: evidence-bearing memory patches**

[Paper](https://arxiv.org/html/2606.13681v2) · arXiv v2, 2026-06-17. Same paper as B79.

Records append-only patches only for non-additive revisions, overwrites, or reinterpretations, preserving before/after states, rationales, and evidence; purely additive observations can remain in base memory. Personal-agent evidence comes from A-Mem on synthetic PersonaMem-Evo: average step accuracy rises from 47.3 to 49.0 and chain accuracy from 40.0 to 43.2, step scores individual questions while chain requires every linked question correct; GLM-5.1 regresses on both; gains are not universal. Historical retention does not establish disclosure authorization or privacy boundaries.

**Resources:** [Repository](https://github.com/Aiden0526/EvoArena) contains PersonaMem and Terminal directories; the advertised SWE directory was absent. README retains pending-release/license statements. Paper CC BY 4.0 does not establish asset permissions.

**Verification date / actually read:** 2026-11-01; §§4–6, main results, Appendix A, README/root. No reproduction run. Internal table warning: SWE Qwen chain 12.2→10.1 is labeled +2.1.

<a id="method-evolving-conditional-memory"></a>
### M80. Method — Evolving Conditional Memory

[Personalized Large Language Model Assistant with Evolving Conditional Memory](https://aclanthology.org/2025.coling-main.254/) — COLING 2025; the same work as arXiv:2312.17257 (first submitted in 2023; v2 October 13, 2024). Count once.

**Checked / reading scope**: November 1, 2026; relevant passages in §§3–5, limitations/ethics, Appendix A.1/Table 7 and construction details, and arXiv version history.

- **Mechanism**: Select utterances worth retaining; store contextual conditions separately from knowledge, with reflective retrieval/query expansion.
- **Evidence**: 300 knowledge, 200 feedback and 200 continuation cases; GPT-4-constructed evaluation using existing source datasets and pseudo-human feedback, scored using ROUGE/GPT-4. Three annotators also checked 50 samples/task; knowledge/feedback/continuation qualified rates were 60%/84%/81%.
- **Limits**: Direct personal-memory research, not longitudinal real-user deployment; GPT-4-only experiments, without resolved timestamp/forgetting mechanisms.
- **Resources**: Prompts/construction described; no official code/data release located or artifact license established.

<a id="method-dam-llm"></a>
### M82. Method — DAM-LLM

[Dynamic Affective Memory Management for Personalized LLM Agents](https://arxiv.org/html/2510.27418v1) — arXiv:2510.27418v1, October 31, 2025 preprint; conference acceptance not verified.

**Checked / reading scope**: November 1, 2026; relevant §§3–6, Appendix A.3–A.4 and arXiv metadata.

- **Mechanism**: Object/aspect sentiment-confidence weights, Bayesian-inspired updates, entropy compression, metadata filtering and semantic reranking.
- **Evidence and limits**: Direct affective-memory method; Qwen-Max system, synthetic data/GPT-4 judging, not real-user or clinical efficacy evidence; synchronous update overhead remains a limitation.
- **Resources**: Appendix prompts/parameters are partial: A.3.2 does not supply the complete simulated-session generation prompt, so full reproducibility is not established. No official code/data release or artifact license located. See [DABench](#benchmark-dabench); count this paper once.

<a id="method-bi-mem"></a>
### M83. Bi-Mem: Calibrating local memories against a global persona

[Bi-Mem: Bidirectional Construction of Hierarchical Memory for Personalized LLMs via Inductive-Reflective Agents](https://arxiv.org/html/2601.06490v1) — arXiv v1, 2026-01-10.

**Type / capability:** A personalized conversational-memory method combining bottom-up fact–scene–persona construction, top-down calibration and associative retrieval.

**Evidence / boundaries:** LoCoMo is human-refined, LLM-generated dialogue—not longitudinal natural-user evidence. GPT-4o-mini F1 is 49.74 versus Mem0’s 45.08; adversarial questions are excluded. Reported results average at least three seeds. The authors identify dependence on backbone reasoning and relatively stable personas. The paper describes the original 50-dialogue corpus, while the repository supplies `locomo10.json`; the evaluated sample scope needs reconciliation.

**Resources / actual reading:** [Code and data](https://github.com/tohsaka-sb/Bi-Mem) are accessible, but no root LICENSE was found. The paper’s CC BY 4.0 does not establish artifact licensing. Read: methods, experiments, limitations, Appendix B.2, repository README and directory listing. No reproduction run.

<a id="method-memgas"></a>
### M84. MemGAS: Query-adaptive memory granularity and association

[From Single to Multi-Granularity: Toward Long-Term Memory Association and Selection of Conversational Agents](https://arxiv.org/html/2505.19549v2) — arXiv v2, 2025-09-29; author repository reports ICLR 2026 acceptance. The v1 title (2025-05-26) was *Towards Multi-Granularity Memory Association and Selection for Long-Term Conversational Agents*. Stable ID `2505.19549`: count once.

**Type / capability:** Conversational memory using session, turn, summary and keyword representations, GMM associations, entropy routing, Personalized PageRank and LLM filtering.

**Evidence / boundaries:** Evaluation covers LongMemEval-s/m, LoCoMo and Long-MT-Bench+. These are constructed or reconstructed benchmarks, not a longitudinal natural-user study. [LongMemEval](https://arxiv.org/html/2410.10813) mixes natural-source and synthetic sessions; LoCoMo is human–LLM co-created. LongMemEval-s GPT-4o-judge performance reaches 60.20; however, LoCoMo’s GPT-4o-judge score (not F1) of 41.07 trails SeCom’s 44.21 and HippoRAG2’s 45.62. Some expensive large-context baselines are missing.

**Resources / actual reading:** The [author repository](https://github.com/quqxui/MemGAS) provides reference Python code and dataset-download instructions; no root LICENSE was found. Its later TypeScript plugin is distinct from the experimental implementation. Read: §§2–3, Appendices A/G, version records, README and directory listing, plus LongMemEval construction passages. OpenReview required browser verification; acceptance is confirmed only through the author repository. No reproduction run.

<a id="method-o-mem"></a>
### M85. O-Mem: Dynamic persona, event and multi-channel memory

[O-Mem: Omni Memory System for Personalized, Long Horizon, Self-Evolving Agents](https://arxiv.org/html/2511.13593v3) — arXiv v3, 2025-12-10. Use the [arXiv version record](https://arxiv.org/abs/2511.13593), not the anomalous August 2026 date rendered in HTML.

**Type / capability:** Personal-context memory that updates user attributes and events and retrieves persona-, topic- and clue-related context.

**Evidence / boundaries:** Offline evaluation uses human–LLM-created LoCoMo, [simulated PERSONAMEM conversations](https://arxiv.org/html/2504.14225) and a curated PDR-Bench subset of 50 queries from 25 users. The latter derives from real-user interactions but is not evidence of longitudinal deployment. With GPT-4.1, reported LoCoMo F1 is 51.67 and PERSONAMEM accuracy 62.99. The report explicitly presents an initial design: single runs, no fixed seed or uncertainty statistics, variable shared infrastructure and some proprietary baselines copied from publications. Token-controlled comparison is limited to LoCoMo/GPT-4.1. PDR-Bench is already B40; do not count the subset as a new benchmark.

**Resources / actual reading:** [O-Mem](https://github.com/OPPO-PersonalAI/O-Mem) and [PDR-Bench](https://github.com/OPPO-PersonalAI/PersonalizedDeepResearchBench) have Apache-2.0 repository licenses; upstream data rights remain separate. The paper’s Hugging Face link is a paper page. Read: §§3–5, evaluation caveats, version history, repository README / directory / licensing, and PERSONAMEM’s simulation description. No reproduction run.

<a id="method-caffeine"></a>
### M88. Context-aware persona refinement

**Commonsense-augmented Memory Construction and Management in Long-term Conversations via Context-aware Persona Refinement** — EACL 2024 Short Papers, 2024.eacl-short.11; reviewed arXiv 2401.14215v3 (2024-02-12). [Publication](https://aclanthology.org/2024.eacl-short.11/) | [Paper v3](https://arxiv.org/html/2401.14215v3) | [Code](https://github.com/ktio89/Caffeine-Persona-Refinement)

**Method.** COMET expansion, an NLI contradiction graph and LLM resolution/disambiguation/preservation refine persona memory. Reviewed §2–3 methods/experiments, §6–7 limitations/ethics, human-evaluation appendix and repository. MSC/Persona-Chat contains human-authored benchmark dialogues, not verified autobiographical histories. Response judging samples 50 responses; refinement judging retains 89 pairs after screening. Commonsense/NLI errors create a plausible false-profile risk; user confirmation, memory-disclosure permissions and external actions are not evaluated. Code is accessible, but no root license is confirmed; paper licensing does not license code.

<a id="method-memochat"></a>
### M89. MemoChat

**MemoChat: Tuning LLMs to Use Memos for Consistent Long-Range Open-Domain Conversation** | 2023, arXiv 2308.08239v2 (2023-08-23; formal venue unverified). **Scope: transferable conversational memory, not an external-action agent.** Structured topic/summary/dialogue memos support iterative memorization, retrieval and response generation. Its 54 MT-Bench+ checks are expert-constructed from expanded and combined MT-Bench dialogues; downstream consistency is GPT-4 judged, not longitudinal evidence from personal users or completed tasks. Experiments use a 2k context setting; reported challenges include prompt copying, catastrophic forgetting and prompt-order sensitivity. Code, data, training/testing/judging scripts and weight links are available. **Code is MIT; model weights are declared CC-BY-NC-SA-4.0.** Reproduction was not executed.

Sources:
- [Exact version and metadata](https://arxiv.org/abs/2308.08239v2)
- [Original method and evaluation, §§3–4 and Appendix C](https://arxiv.org/html/2308.08239v2)
- [Author repository: artifacts and distinct code/model licenses](https://github.com/LuJunru/MemoChat)

Actual inspection: version page; original method, training-instruction, experimental-setup, evaluation and challenge passages; repository directory and README workflow, weights and licensing statements. Weights were not downloaded/validated, scripts were not run, and training data were not audited item by item.

<a id="method-plato-ltm"></a>
### M95.  Method

**PLATO-LTM** | Same [Findings of ACL 2022 paper](https://aclanthology.org/2022.findings-acl.207/) / [2203.05797v2](https://arxiv.org/html/2203.05797v2), 2022-03-14. Cross-index: **B84**; do not count as another paper.

Persona filtering, separate user/bot stores, similarity-based deduplication/replacement and contextual retrieval condition response generation without long-session training data. Simulated-dialogue consistency is 0.87 versus PLATO-FT’s 0.40. However, coherence (0–2 scale) is 1.67 versus PLATO-2’s 1.70; PLATO-FT scores 1.59, and the paper discusses small-dataset fine-tuning hurting coherence. Not every quality dimension improves.

An earlier direct personal-memory foundation, not a tool-executing agent. Similarity replacement does not establish full contradiction or temporal-state handling. **Resources/license:** despite the paper’s release claim, the [official README](https://github.com/PaddlePaddle/Research/tree/master/NLP/ACL2022-DuLeMon) still marks the PLATO-LTM framework **Coming soon**; do not claim a complete released implementation. Parent repository Apache 2.0 does not establish external-data terms. **Inspected:** §4 extraction/read-write/generation, §5.3.3, Table 5, Appendix B and official resources; model not run.

<a id="method-xmemory"></a>
### M96.  Method

**Beyond RAG for Agent Memory: Retrieval by Decoupling and Aggregation (xMemory)** | [2602.02007v4](https://arxiv.org/html/2602.02007v4), 2026-05-12; earlier versions February 2, February 25 and April 11. The [official README](https://raw.githubusercontent.com/HU-xiaobai/xMemory/main/README.md) announces NeurIPS 2026 acceptance on 2026-09-24: verified as an author-repository claim, not independently against official conference records.

Segment messages, decouple fact/update components, aggregate a revisable hierarchy, incrementally split/merge, select complementary evidence top-down and expand source text using uncertainty. Offline QA on LoCoMo and PerLTQA uses three readers. Qwen3-8B/LoCoMo F1 is 43.98 versus naive RAG’s 36.48; inference tokens/query are 4,711 versus 8,633. **This comparison excludes construction costs.**

No new human trial or broad task-execution validation. Limitations include construction overhead, extraction errors and potentially unfavorable costs with few future queries. Privacy/deletion/correction safeguards are recommendations, not verified guarantees.

**Resources/license:** [official implementation](https://github.com/HU-xiaobai/xMemory) and [MIT license](https://github.com/HU-xiaobai/xMemory/blob/main/LICENSE) verified; paper CC BY 4.0. Quick Start identifies a released Llama implementation; exact v4 correspondence unverified. MIT software licensing does not override PerLTQA’s noncommercial terms. **Inspected:** v4 §§3–5, main/ablation results, Appendix B asset licensing, selected Appendix C results, E/F limitations/impact, history and official README/directory/LICENSE; no reproduction run.

<a id="method-actmem"></a>
### M97.  Method: ActMem

[ActMem: Bridging the Gap Between Memory Retrieval and Reasoning in LLM Agents](https://arxiv.org/html/2603.00026v2) — 2603.00026v2, revised 2026-06-17; preprint, venue unverified. Cross-entry, not another paper.

- **Mechanism:** Atomic facts and clustering; semantic/inferred-causal graph, PMI filtering and counterfactual commonsense-assisted secondary retrieval.
- **Evidence:** With DeepSeek-V3, QA is 76.52% versus NaiveRAG 61.79%, but evidence recall is lower: 71.66% versus 85.57%. QA gains do not imply superior recall. This is the synthetic ActMemEval setting described above, not executed user tasks.
- **Limits:** Inferred links and commonsense can fail; synthetic QA does not establish reliable real-world execution.
- **Resources/rights:** [Repository](https://github.com/nju-websoft/ActMem) root shows dataset/LICENSE/.gitignore/README; README contains only the title, with no implementation directory observed. Dataset release exists, full implementation release is unverified. Root MIT and paper dataset CC BY 4.0/academic-only wording must remain distinct.
- **Reading scope:** Metadata, relevant §§3–5, Tables 1–2, Appendices F/G and repository listings/README; no code execution, full dataset audit or complete figure inspection.

<a id="method-caim"></a>
### M98.  Method: CAIM

[CAIM: Development and Evaluation of a Cognitive AI Memory Framework for Long-Term Interaction with Intelligent Agents](https://arxiv.org/html/2505.13044v1) — 2505.13044v1, 2025-05-19: version actually inspected.

- **Mechanism:** Memory Controller, ontology/tag retrieval and Post-Thinking maintenance.
- **Evidence:** GVD synthetic ten-day histories for 15 simulated users, 100 English questions, three human annotators—not a ten-day human-user deployment. GPT-3.5 retrieval is 83.3% versus MemoryBank 76.3%; GLM trails some baselines, so gains are not universal.
- **Limits:** Detailed lists/recipes, relative-time references and split-fact connections can fail; query learning and real-user validation remain future work in this version.
- **Resources:** [Official repository](https://github.com/rebeccawesthaeusser/CAIM) documents implementation/evaluation entrypoints and MIT licensing; not executed or reproduced.
- **Reading scope:** v1 metadata, relevant §§3–6 methods/evaluation/limitations and result-table text, official README. IUI 2026 full text was not read.

#### Version and follow-on distinction

The [official IJCAI-26 doctoral-consortium paper](https://ijcai.org/proceedings/2026/953) distinguishes short CAIM (IUI Companion 2025, pp.22–25), full-title CAIM (IUI 2026, pp.134–143), and [2510.07925v1](https://arxiv.org/html/2510.07925v1), the personalization extension—not an arXiv revision or duplicate.

2510.07925v1 reports a **five-day pilot**; the later IJCAI account describes a **three-week exploratory study**. Do not transfer durations/significance claims or merge the reports without verification. **Participant overlap is unverified.** Here, only 2510 metadata, abstract/§2.2 and relevant IJCAI webpage passages were read; the later cohort/statistics were not independently established.

IUI 2026 DOI lead: `10.1145/3742413.3789222`. Publisher fetch returned 403; the official IJCAI reference supports venue, not a claim of having inspected the published full text or established version equivalence.

<a id="method-hltm"></a>
### M100. HLTM: enterprise-adjacent personalized semantic memory

**Type: method/system; enterprise recruiting, not a general personal-life assistant.** Combines business-scoped memory trees, multi-view retrieval, provenance and incremental updates. Evidence includes expert-labelled production-log data and LongMemEval-s; online feedback comparisons are not established randomized evidence. Tenant-isolation findings apply to the reported test, not a general privacy guarantee. Distinguish query latency from complete incremental-index refresh time; architectural minute-scale update windows are not measured whole-index refresh times.

**Version/resources:** [arXiv 2604.26197v3](https://arxiv.org/abs/2604.26197v3), 2026-05-30; KDD 2026 Applied Data Science track. The paper’s CC BY-NC-ND 4.0 license is not a software license. Public implementation/internal hiring dataset availability was not verified in inspected material.

**Actual reading:** [Original](https://arxiv.org/html/2604.26197v3) §§3–6, Tables 1–3/6–8, Appendices C–D; version/venue metadata. No claim of page-by-page full-text audit.

<a id="method-comedy"></a>
### M102. COMEDY / Dolphin: long-term dialogue compression

**Type: method/system; memory compression and personalized dialogue.** One model performs memory extraction, compression and response generation through mixed-task training and DPO. Dolphin originates from real X Eva user–character interactions, but annotations/responses are generated with GPT-4-Turbo and human-refined—not wholly natural human data. Offline memory metrics and dialogue ratings do not demonstrate production efficiency or health benefits. De-identification is author-reported; explicit consent procedures remain unestablished, and author statements are not independent privacy validation.

**Version:** [COLING 2025 record](https://aclanthology.org/2025.coling-main.51/), pp.755–773, is titled “Compress to Impress: Unleashing the Potential of Compressive Memory in Real-World Long-Term Conversations”; its [linked PDF](https://aclanthology.org/2025.coling-main.51.pdf) starts with “Beyond Retrieval: Embracing Compressive Memory in Real-World Long-Term Conversations.” [arXiv 2402.11975v2](https://arxiv.org/abs/2402.11975v2), 2024-07-01, has five authors versus six in COLING. Preserve these version differences.

**Resources:** [Official code](https://github.com/nuochenpku/COMEDY) is accessible, but full training/test release remains unverified: the train link targets an author profile; test is an unlinked placeholder. No root project-license file was visible. The [DPO data card](https://huggingface.co/datasets/Nuo97/Dolphin-DPO) is empty and its viewer unavailable. [7B](https://huggingface.co/Nuo97/COMEDY_7B), [13B-DPO](https://huggingface.co/Nuo97/COMEDY_13B_DPO) and DPO cards declare Apache-2.0; this is not project-wide or base-model license clearance.

**Actual reading:** COLING PDF §§2–3, limitations/ethics, Appendices B–F; Anthology/arXiv metadata; official README, dataset/model cards. Full corpus and weights were not downloaded or audited.

<a id="method-malp"></a>
### M105. MaLP / DPeM: medical personalization memory

[LLM-based Medical Assistant Personalization with Short- and Long-Term Memory Coordination](https://arxiv.org/html/2309.11696v3) — inspected arXiv v3, 2024-04-04; published at [NAACL 2024](https://aclanthology.org/2024.naacl-long.132/). The [v1 title](https://arxiv.org/abs/2309.11696v1), *Memory-Augmented LLM Personalization with Short- and Long-Term Memory Coordination*, belongs to the same paper; count once.

**Inspected:** Abstract, §§2–4, Appendices A/B, version history and official README/root listing.

- **Method:** Coordinated working/short-/long-term memory, frequency-based promotion, domain adaptation and user LoRA.
- **Evidence:** Profiles derive from Medical-Dialogue-System, followed by model self-chat; medical adaptation uses HealthCareMagic-100k/iCliniq. Sixty simulated users and 10,920 self-chat dialogues; QA, preference classification and response judging. Two master's-student raters with medical backgrounds screened 100 dataset samples, reporting 94% without identified safety issues. Separately, two master's students rated 100 response pairs to check agreement with automated scoring.
- **Limits:** The 94% is a small dataset-sample safety screen—not clinical safety, patient outcomes or efficacy. No longitudinal patient trial; persistent-memory deletion/correction/consent controls are not established.
- **Resources/rights:** The [official repository](https://github.com/MatthewKKai/MaLP) exposes data and generation/memory/training code and has an MIT LICENSE, while its README License section describes research purposes. These differing signals do not justify unrestricted commercial use and do not establish upstream medical-data/model rights, patient consent or commercial authorization.

<a id="agent-methods"></a>
<a id="methods-b-planning-tools-reflection-proactivity-and-coordination"></a>
<a id="planning-action-methods"></a>
## Methods: Planning, tools, and action

How do preferences and experience shape plans, tool calls, skills, or coordination? Planning and generated calls are not necessarily completed real-world actions. External experience is not parameter-level continual learning, and multiple agents are not automatically more reliable.

<a id="method-generative-agents"></a>
### M7. Generative Agents · Memory, reflection, and planning

[Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) — 2023.

**Checked / reading scope:** 2026-10-31; Paper abstract; official README simulation environment, code scope, and model-call notes.

- **Idea:** Record experiences, retrieve memories, form higher-level reflections, and plan behavior; studied in a town with 25 simulated characters.
- **Relevance and limits:** Offers patterns for persistent state and plans. Its goal is believable human-behavior simulation, not completing authorized tasks for real users.
- **Resources:** [Official simulator, environment, and replay instructions](https://github.com/joonspk-research/generative_agents). Uses external model calls; not a standalone model-weight release.

<a id="method-react"></a>
### M8. ReAct · Interleaving reasoning and action

[ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) — 2022 preprint; ICLR 2023.

**Checked / reading scope:** 2026-10-31; Paper abstract and arXiv version notes; official README and code/prompt directory listing.

- **Idea:** Interleave task reasoning and tool actions, using returned observations to revise subsequent steps.
- **Relevance and limits:** A foundation for general tool-use loops. Original experiments cover QA, fact verification, and interactive environments, not persistent memory, permissions, or continuous scheduling.
- **Resources:** [Official code, prompts, and experimental notebooks](https://github.com/ysymyth/ReAct). Primarily a prompting implementation, not a complete personal assistant.

<a id="method-reflexion"></a>
### M9. Reflexion · Carrying feedback into another attempt

[Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) — NeurIPS 2023.

**Checked / reading scope:** 2026-10-31; Paper abstract; official README experiment, log, and execution notes.

- **Idea:** Turn task feedback into verbal reflection stored in episodic memory for later attempts, without directly updating model weights.
- **Relevance and limits:** Useful for retries and experience memory. Gains depend on feedback quality and retry budget; reflection does not guarantee correction or continual improvement.
- **Resources:** [Official code, logs, and demos](https://github.com/noahshinn/reflexion). Original evaluations cover decision-making, reasoning, and coding, not long-term personal assistance.

<a id="method-toolformer"></a>
### M10. Toolformer · Learning when to call tools

[Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) — 2023 preprint.

**Checked / reading scope:** 2026-10-31; Paper abstract and §7 limitations; Meta publication page and its available resource links.

- **Idea:** Use a few API demonstrations to generate candidate calls, filter by their benefit to subsequent language prediction, and train on the augmented corpus.
- **Relevance and limits:** Shows how tool use can be learned. The original method lacks chained and interactive tool use; it is not a complete multi-step agent.
- **Resources:** [Official research page](https://ai.meta.com/research/publications/toolformer-language-models-can-teach-themselves-to-use-tools/). The checked paper / official page did not provide corresponding full code, training-data, and weight releases. Third-party reproductions are not official artifacts.

<a id="method-voyager"></a>
### M13. Voyager · Reusable executable skills

[Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/html/2305.16291v2) — inspected 2023 preprint v2, 2023-10-19.

**Checked / reading scope:** 2026-10-31; Abstract, iterative-code description, §3.1 and evaluation-task overview, official README and license.

- **Idea:** Minecraft state, curriculum goals, and previous skills → executable code, refined using environment feedback, errors, and self-verification. Successful skills enter a library for later reuse.
- **Relevance and limits:** A general embodied / game method with reusable skill-learning patterns. Evaluation covers items, milestones, traversal, and new-task transfer. Lifelong learning primarily accumulates external skills rather than updating base-model weights; Minecraft results do not establish email, calendar, or real-computer competence.
- **Resources:** [Official code, prompts, and skill library](https://github.com/MineDojo/Voyager), MIT. Minecraft and model / API terms are separate. Experiments used historical GPT-4 / GPT-3.5 APIs; replacement models change the setup.

<a id="method-expel"></a>
### M14. ExpeL · Distilling experience across tasks

[ExpeL: LLM Agents Are Experiential Learners](https://arxiv.org/html/2308.10144v3) — AAAI 2024; inspected v3, 2024-12-20.

**Checked / reading scope:** 2026-10-31; Abstract, §5.1 tasks / metrics / four-fold setup, official README and license.

- **Idea:** Distill natural-language insights from successful and failed training episodes, then retrieve insights and examples for new tasks without updating base-model weights. The emphasis is cross-task reuse, not only reflection on one failed attempt.
- **Relevance and limits:** Offers patterns for assistant experience memory. Wikipedia QA / fact verification, ALFWorld household tasks, and WebShop use exact match, success, and shopping rewards. Four-fold experience learning is not longitudinal human use; stale insights and privacy need separate tests.
- **Resources:** [Official code, data directories, and prompts](https://github.com/LeapLabTHU/ExpeL), Apache-2.0; check environment and dataset terms separately. No weight fine-tuning does not mean no cost: collecting episodes and extracting insights still require model calls.

<a id="method-autogen"></a>
### M15. AutoGen · Multi-agent conversation and human participation (historical)

[AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/html/2308.08155v2) — inspected 2023 preprint v2, 2023-10-03.

**Checked / reading scope:** 2026-10-31; Abstract, §3 A1–A4 applications / evaluation and human-in-the-loop discussion, current official README and legal notices.

- **Idea:** Encapsulate LLMs, tool execution, and human input as conversable agents; a math request, for example, leads to code, execution-result, and feedback exchanges before an answer.
- **Relevance and limits:** General multi-agent orchestration research, not a personalization benchmark. MATH, retrieval QA, ALFWorld, and OptiGuide use application-specific metrics. More agents or human involvement do not automatically provide permission isolation, reliable authorization, or lower cost; single-agent controls and safety tests remain necessary.
- **Resources:** [Official repository](https://github.com/microsoft/autogen): MIT code; CC BY 4.0 documentation / other content. The current README reports archival and no Microsoft maintenance. Retain as historical research, not a maintained production recommendation. Current packages differ from the 2023 API; a paper-era commit was not identified.

<a id="method-petoolllama"></a>
### M22. PEToolLLaMA · Training preference-aware tool calls

[PEToolLLM: Towards Personalized Tool Learning in Large Language Models](https://aclanthology.org/2025.findings-acl.1107/) — Findings of ACL 2025; same paper as B33. PEToolLLM is the paper title, PEToolBench the benchmark and PEToolLLaMA the method.

**Verified / reading scope:** 2026-11-01; [v1](https://arxiv.org/html/2502.18980v1) §3 metrics and §4 method overview; official README/LICENSE and dataset file listing. Not a full-paper read.

- **Mechanism:** personalized SFT conditions on history, instructions and candidate tools; DPO then improves preference-consistent call selection.
- **Evidence:** tool and parameter accuracies under PEToolBench's three synthetic-history settings.
- **Limits:** training is not persistent-memory management. Results do not establish real service completion, online preference shifts or safe side-effect control.
- **Resources:** [official training/test scripts](https://github.com/travis-xu/PEToolBench), [data](https://huggingface.co/datasets/travisxu/PEToolBench/tree/main). Repository: Apache-2.0; upstream terms still require checking. Complete weight release and executable reproduction were not confirmed.

<a id="method-me-agent"></a>
### M29. Me-Agent · Experience and hierarchical preference memory

[Me-Agent](https://arxiv.org/html/2601.20162v1) — same paper as B42; do not count twice.

**Verified / actual reading scope:** 2026-11-01; v1 §4.2–4.4 methodology, relevant §5.1–5.2 settings/results passages, and Limitations; repository root and README. Selected passages, not a line-by-line full-paper review; no installation, execution, or experimental reproduction.

- **Mechanism:** VLM-scored trajectories yield natural-language experiences for prompts; app-specific memory supplies workflows and content preferences. The method describes parameter-free adaptation, not personalized backbone fine-tuning.
- **Evidence/limits:** Evaluated on User FingerTip and general mobile tasks. UI changes can invalidate stored positions/workflows; situational factors such as current location remain limited. Inferring a habitual choice does not establish authorization for a new action.
- **Resources:** [Author implementation](https://github.com/Gianthaha/personal-mobile-agent); benchmark-count, packaging and licensing-scope caveats are shared with B42.

<a id="method-puma"></a>
### M31. PUMA · Learning tool parameters from behavioral histories

[Large Language Models Empowered Personalized Web Agents](https://arxiv.org/html/2410.17236v2) — WWW 2025; v2, 2025-03-24. PersonalWAB is cross-listed as B44, the same paper.

**Actual reading scope:** §§3, 5–6, Table 5, Appendices A.3/B; version record, project page, README, data directory and LICENSE. Targeted reading; no execution.

- **Mechanism:** Retrieves behavioral histories, retains task-specific fields, and learns function parameters through heuristic SFT and result-ranked DPO.
- **Evidence/boundary:** Table 5 overall function/result accuracy is .994/.406, versus .994/.373 without task-specific memory; recommendation result accuracy remains .054. These metrics are not real-world task-success rates. Shopping and simulator boundaries appear in B44.
- **Resources:** [Author repository](https://github.com/HongruCai/PersonalWAB) and data directory are readable. Root license is **CC BY-NC 4.0**, with separate MIT terms for inherited tau-bench portions. Released PUMA checkpoints and full-data integrity were not verified. Paper, code/data, Amazon and model terms must remain distinct.

<a id="method-coloragent"></a>
### M39. ColorAgent · Personalized mobile GUI execution and clarification

[ColorAgent](https://arxiv.org/html/2510.19386v2) — technical report; inspected v2, October 24, 2025.

**Checked / reading scope:** November 1, 2026; §§2–6; official README, LICENSE and ColorGUI-32B model card.

- **Mechanism:** step-wise RL, self-evolving training, retrieval, task orchestration and hierarchical reflection; user-history-derived SOPs/profile information personalize requests, with a separately trained clarification agent. Primarily **Android/mobile, not desktop**.
- **Evidence:** distinguish AndroidWorld/AndroidLab task success from MobileIAR intention-aligned action matching and VeriOS-Bench step-level matching.
- **Limits:** no established longitudinal user benefit. Benchmark realism, sandboxing and fine-grained permissions remain open; asking questions is not comprehensive security validation.
- **Resources:** [official repository](https://github.com/MadeAgents/mobile-use), verified [MIT code license](https://github.com/MadeAgents/mobile-use/blob/main/LICENSE). Later [ColorGUI-32B](https://huggingface.co/MadeAgents/ColorGUI-32B), released July 10, 2026 and marked Apache-2.0, uses Qwen3-VL; it is **not the paper’s GUI-Owl/Qwen2.5 checkpoint**. Pin code, model and evaluation revisions separately.

<a id="method-warpp"></a>
### M40. Agent WARPP · Attribute-conditioned runtime workflow pruning

[Agent WARPP](https://arxiv.org/html/2507.19543v1) — ICML 2025 Multi-Agent Systems Workshop, not the main conference; inspected v1, July 23, 2025.

**Checked / reading scope:** November 1, 2026; §§3–6, §§8–9; official README and LICENSE.

- **Mechanism:** a training-free Personalizer prunes workflows/tools using user attributes alongside simulated authentication, then hands off to fulfillment. Pruning retains success, failure and user-answer branches for retained tools. This is conditional execution, not persistent preference learning.
- **Evidence:** five intents, three domains, 50 examples each; synthetic customer records and GPT-4o client simulation. Separate trajectory matching, tool F1, argument fidelity, latency and judge-rated workflow quality.
- **Limits:** most calls and MFA are simulated; some complex workflows integrate APIs. This does not demonstrate production deployment or secure identity verification. Security, privacy, human-in-the-loop and conversation quality are explicitly outside scope. High-load behavior and evolving APIs remain untested.
- **Resources:** [official implementation/data](https://github.com/emiliamazzo/WARPP), verified [MIT LICENSE](https://github.com/emiliamazzo/WARPP/blob/main/LICENSE).

<a id="method-ptool"></a>
### M46. PTool · Synthetic training for personalized tool invocation

Same [paper](https://arxiv.org/html/2505.04072v1) and reading scope as B51.

- **Mechanism:** structured API/profile synthesis, role-play query/solution generation, rule/model validation, then LoRA SFT.
- **Evidence/boundary:** Qwen2.5-7B overall accuracy 7.38%→26.78%; generated-call evaluation, not live tool execution.

<a id="method-iotgpt"></a>
### M52. IoTGPT

**Method: personalized device execution with reusable task memory**

[Leveraging LLMs for Efficient and Personalized Smart Home Automation](https://arxiv.org/abs/2601.04680) · **arXiv v1, January 8, 2026**; archival venue unconfirmed.

Combines a Decompose–Derive–Refine pipeline, hierarchical task memory and environmental-property preferences for SmartThings control. Evaluation uses **97 tasks and 26 simulated devices**; warm-start testing paraphrases already learned tasks. Fifteen real participants join short studies, but preferences originate from **100 GPT-4o-generated logs**, not their personal histories. This is not evidence of longitudinal household personalization. Conflicting preferences and device side effects remain limitations; **users must screen unsafe or hallucinated commands**, with automated safeguards left to future work. No official implementation/license verified. **Read:** system, implementation, comparative evaluation, both user studies and limitations; no reproduction.

<a id="method-aipom"></a>
### M58. AIPOM — inspectable, editable multi-agent plans
- **Paper:** *AIPOM: Agent-aware Interactive Planning for Multi-Agent Systems*, EMNLP 2025 System Demonstrations, 85–96.
- **Evidence:** Chat plus editable task/agent/dependency/output graphs. Experiments use 50 GSM8K and 50 BBH arithmetic tasks with corrupted plans; pilot: nine LLM-experienced industry research-organization participants (interns, engineers and research scientists), 12 math tasks. Feedback was postprocessed, without asking users to accept/reject actual refinements.
- **Limits:** Plan inspection/refinement, not permission enforcement, sensitive-action authorization or security guarantees; not general-user longitudinal trust evidence. Centrally orchestrated modules are not autonomous proactive agents.
- **Resources/read scope:** [Paper](https://aclanthology.org/2025.emnlp-demos.7.pdf), §§2–4,6, Appendix C; [official code/demo](https://github.com/megagonlabs/aipom). Root LICENSE: BSD-3-Clause. Data/dependencies retain separate terms; README adds third-party-material restrictions. Web search is disabled by default. Not reproduced.

<a id="method-opencha"></a>
### M63. openCHA — health-scoped orchestration of personal data and analytical tools
- **Paper:** *Conversational health agents: a personalized large language model-powered agent framework*, JAMIA Open 8(4), ooaf067, published 2025-07-06; [DOI](https://doi.org/10.1093/jamiaopen/ooaf067). Earlier arXiv v5 (2024-09-25) has two demos/four use cases; the journal version has two demos/five use cases. Keep versions separate.
- **Method and evidence:** Planner/executor, data pipe and external analytical tools combine personal health records, knowledge retrieval and multistep operations. Journal examples include 100 diabetes questions, 500 emotion-question tests and PPG heart-rate estimation on existing home-monitoring data from 45 people. These are distinct use cases, not one pooled participant trial.
- **Limits:** A health research framework, not evidence of treatment improvement, diagnostic safety or longitudinal clinical deployment. Longitudinal source data are not longitudinal agent intervention. Performance depends on configured sources; HIPAA/GDPR compliance is implementation-dependent, and the framework does not manage deployment/scalability.
- **Resources and reading:** [Journal paper](https://academic.oup.com/jamiaopen/article/8/4/ooaf067/8186991), methods, demonstrations/use cases, Table 4 and discussion; compared with [v5](https://arxiv.org/html/2310.02374v5), §§3–5. [Official code](https://github.com/Institute4FutureHealth/CHA) is MIT and includes documentation/examples/tests—not clinical certification or permission to reuse health data.

<a id="method-llm-personalize"></a>
### M67. LLM-Personalize · Preference-aligned embodied planning

[LLM-Personalize: Aligning LLM Planners with Human Preferences via Reinforced Self-Training for Housekeeping Robots](https://aclanthology.org/2025.coling-main.98/) — COLING 2025; arXiv `2404.14285v3` is the same work.

**Checked / reading scope:** 2026-11-01; method §3, experimental setup and Table 1 in §4, limitations §6, and author repository documentation and license label.

- **Input → output:** Local observations, instructions and preference feedback → scene-graph-based plans and low-level actions; imitation learning followed by preference-filtered self-training.
- **Evidence / measurement:** Four simulated Housekeep scenes with human-annotated placement preferences; five test tasks per scene and five runs per task. The reported success metric measures net correction of misplaced objects and can be negative; it is not episode completion.
- **Boundary / counterexample:** On the Scene 4 test split, ST2 scores 20.4 versus 25.7 for imitation learning alone (IL). However, ST2 improves over ST1 in all four test scenes; these baselines must not be conflated. No physical-robot or real-household deployment is validated.
- **Resources:** The [author repository](https://github.com/gdg94/codellmpersonalize) is MIT-labelled and includes planning, simulation and training code; legacy OpenAI SDK, GPT-3.5 and Habitat dependencies limit claims of immediate reproducibility.

<a id="method-personal-travel-solver"></a>
### M68. Personal Travel Solver · Implicit preferences and constraint solving

[Personal Travel Solver: A Preference-Driven LLM-Solver System for Travel Planning](https://aclanthology.org/2025.acl-long.1339/) — ACL 2025 Main. RealTravel is this paper's dataset, not a separate paper.

**Checked / reading scope:** 2026-11-01; dataset and methods §§3.1–3.8, results §4, evaluation Appendix B, and repository README/file listing.

- **Input → output:** Travel requests, review histories and a closed database → itineraries produced through LLM-based processing and SCIP optimization.
- **Data / measurement:** Real Google Local reviews and POI metadata support requests constructed through constraint sampling, feasibility checks and LLM verbalization. The 1,000-example test set yields 96.60% final constraint pass rate; personalization is separately judged by DeepSeek-V3.
- **Boundary / counterexample:** Constraint feasibility is not traveler satisfaction, booking execution or real-world deployment. Real reviews do not make constructed requests real commissions.
- **Resources:** The [official linked repository](https://github.com/cliftclift/PTS) exposes RealTravel data/processing resources. A complete PTS solver release and an explicit top-level license were not verified; do not label it a fully open-source system.

<a id="method-vaiage"></a>
### M92. Vaiage

**Vaiage: A Multi-Agent Solution to Personalized Travel Planning** | 2025, arXiv 2505.10922v1 (2025-05-16; formal venue unverified). **Scope: a multi-agent travel-planning prototype grounded in stated user constraints and external map/weather data.** It generates attractions, routes and budgets with interactive adjustment. Quantitative results primarily use **GPT-4/GPT-3.5 proxy judges**; 8.5/10 is not observed user satisfaction. Human-in-the-loop and qualitative claims do not establish a clearly specified participant sample and human-study protocol. The abstract and main text describe the no-API variant’s 6.8 differently, so avoid treating it as an unambiguous overall score. Booking integration and long-term personalization are future work: **real booking completion and authorization safety are not established.** Public application/evaluation artifacts exist, but no root license was found and GitHub license metadata is null. Multiple API credentials are required; reuse permission and complete reproducibility remain unverified.

Sources:
- [Exact version and metadata](https://arxiv.org/abs/2505.10922v1)
- [Original architecture and interface, §§3–4; evaluation §5; future booking integration §6](https://arxiv.org/html/2505.10922v1)
- [Author repository and dependency/setup documentation](https://github.com/Binwen6/Vaiage)
- [Inspected evaluation sample: four-day request, two itinerary day objects, score 9](https://github.com/Binwen6/Vaiage/blob/main/evaluation%20score.txt)
- [Evaluation directory; existence verified](https://github.com/Binwen6/Vaiage/tree/main/evaluation)

Actual inspection: version page; original architecture, user-flow, evaluation and conclusion passages; repository directory, README, license metadata and evaluation score.txt. That sample requests four days but contains only two itinerary day objects and still receives 9/10: a concrete warning about judge reliability, not an estimated population error rate. evaluation/eval.json could not be retrieved: connector HTTP 400 (too large or unsupported), followed by a web cache miss. Complete human-evaluation data inspection is not claimed. The system was not installed, executed or independently reproduced.

<a id="method-valuepilot"></a>
### M94.  Method

**ValuePilot: A Two-Phase Framework for Value-Driven Decision-Making** | Two distinct IDs, one method family:
- [2503.04569v1](https://arxiv.org/html/2503.04569v1), 2025-03-06, five authors.
- [2512.13716v1](https://arxiv.org/html/2512.13716v1), 2025-12-09, seven authors. [Metadata](https://arxiv.org/abs/2512.13716) reports acceptance at the LAW Workshop at NeurIPS 2025, not the main conference.

Generated value-annotated scenarios, T5 value assessment, contextual/feasibility scoring and PROMETHEE rank actions using supplied six-dimensional personal value weights. The dataset contains 11,938 scenarios and 100,255 actions. Human questionnaire rankings are not deployment trials.

**Sample-reporting discrepancy:** March §4.3 reports 40 people, but Appendix D explicitly says ten remained after screening. December reports 40 and omits the screening sentence while retaining DMM scores of 73.16% OS-Sim and 46.14% First-Acc. The 10-versus-40 discrepancy remains unresolved. The strongest comparison changes from GPT-4o-mini to GPT-5; do not mix versions’ baselines. Score differences are percentage points, despite misleading relative-percentage wording in the papers.

Synthetic scenarios, directly supplied ratings and simplified value representations do not demonstrate longitudinal preference learning, actual execution or authorization. **Resources/license:** March paper uses arXiv’s nonexclusive license; December paper CC BY 4.0. Official code/data release and associated licenses unverified. **Inspected:** both versions’ methods, experiments/results, Appendix D questionnaires/sample descriptions, limitations and metadata; no raw questionnaires or reproduction run.

<a id="proactive-clarification-methods"></a>
## Methods: Proactivity and clarification

When should an agent initiate help, ask a question, or avoid interruption? Target-oriented dialogue and adjacent enterprise clarification are distinguished from longitudinal personal assistance within each entry.

<a id="method-proactive-agent"></a>
### M11. Proactive Agent · Predicting acceptable assistance

[Proactive Agent: Shifting LLM Agents from Reactive Responses to Active Assistance](https://arxiv.org/abs/2410.12361) — 2024 preprint; ICLR 2025; same paper as B6.

**Checked / reading scope:** 2026-10-31; Same check as B6: paper abstract, official README pipeline/release notes, and the weight-file listing.

- **Idea:** Train a reward model using activity traces and human acceptance / rejection labels, generate environment data, and train an agent to offer help proactively.
- **Relevance and limits:** Directly studies proactive assistance. Anticipated needs are not authorization; deployment must address activity-capture privacy and unwanted interruptions.
- **Resources:** [Code / data / evaluation](https://github.com/thunlp/ProactiveAgent), [officially linked Agent and Reward Model weights](https://huggingface.co/YancyLee/ProactiveAgent/tree/main). Check weight, base-model, and code licenses separately.

<a id="method-memoproagent"></a>
### M12. MemoProAgent · Using memory to decide whether to interrupt

[MemoProAgent: Toward Memory-Driven Proactive Assistance](https://arxiv.org/html/2610.22671v2) — 2026 preprint v2, 2026-10-21; same paper as B11.

**Checked / reading scope:** 2026-10-31; Same check as B11: v2 abstract, §3.3 metrics, method overview, official README and LICENSE.

- **Idea:** Organize personal history as graph memory, retrieve experiences relevant to current video activity, and gate delivery to the generator by interruption value. The paper also includes an RL post-training stage.
- **Relevance and limits:** Directly studies proactive assistance without explicit queries. MemoProBench evaluates reminder content, timing, and repetition. Constructed histories are not longitudinal human deployment, and inferred needs are not execution permission.
- **Resources:** [Official inference harness](https://github.com/facebookresearch/Memo-Pro-Agent): CC BY-NC 4.0. The official [README data notes](https://github.com/facebookresearch/Memo-Pro-Agent#data-and-reproducibility) identify the [history data (restricted)](https://huggingface.co/datasets/facebook/MemProBench) as currently private, requiring authorized Hugging Face access. Download access was not obtained in this review; independent dataset licensing remains unconfirmed. [Ego4D videos](https://ego4d-data.org/) require separate access and terms. Public inference code is not a complete RL training-code or weight reproduction package.

<a id="method-cep"></a>
### M18. CEP · Separate clarification, execution and planning

[Ask-before-Plan](https://aclanthology.org/2024.findings-emnlp.636/) — Same paper as B30; count once.

**Checked / reading scope:** 2026-11-01; abstract, evaluation setup, Appendix B.3 and official README training / inference entries.

- **Mechanism:** Three specialized roles; trajectory tuning for clarification and static execution, memory recollection for dynamic execution.
- **Limits:** Role separation is not persistent profiling or authorization. Integrated final planning still uses ground-truth conversation (Appendix B.3); do not label it fully free-running. Resources and licenses: [B30](#benchmark-ask-before-plan).

<a id="method-ppp"></a>
### M30. PPP · Learning proactive clarification and personalized interaction

[Training Proactive and Personalized LLM Agents](https://arxiv.org/html/2511.02208v2) — COLM 2026; v2, 2026-08-23. UserVille is cross-listed as B43, the same paper.

**Actual reading scope:** v2 §§4–8, Table 1, Appendix A; version record, conference listings, author README/tree/LICENSE. Targeted reading, not a complete line-by-line review; no execution.

- **Mechanism:** GRPO jointly optimizes task outcomes, clarification burden and preference adherence with preference-conditioned simulated users. This is not persistent individual memory or lifelong profiling.
- **Evidence/boundary:** Separate automated evaluation from the human study described in B43. Additional questions can increase human effort; simulator-based burden does not directly establish human experience.
- **Resources:** [Author code](https://github.com/sunnweiwei/PPP-Agent) is Apache-2.0. Linked weights/data pages were inaccessible through the inspection tool; download availability and asset licenses remain unverified, not proven absent. README additionally requires a vLLM bias patch. Repository licensing does not automatically cover models, data or upstream benchmarks.

<a id="method-curio"></a>
### M50. CURIO · Rewarding improvements in the user model

- **Paper/version:** [Enhancing Personalized Multi-Turn Dialogue with Curiosity Reward](https://arxiv.org/html/2504.03206v3), [NeurIPS 2025](https://proceedings.nips.cc/paper_files/paper/2025/hash/e48d5af30c95be08762489c5141f7fbc-Abstract-Conference.html); arXiv v3, 2025-10-02.
- **Mechanism:** Add turn-level intrinsic rewards for better user-type beliefs to multi-turn RLHF, comparing accuracy, entropy and potential-difference rewards.
- **Evidence:** Exercise attributes map deterministically to eight strategies. Over 200 simulated conversations, best DiffAcc reaches 87.5%, versus 68.5% MTRLHF and 54% SFT. Education uses two prescribed preferences. Ten student judges evaluate generated dialogues, not live tutoring experiences.
- **Limits:** Static predefined types and LLM simulators constrain generalization; some entropy rewards favor one type. Human personalization preference for DiffLogAcc over MTRLHF is approximately 76%, with a discrepancy between appendix 152/200 and table 75.75%. Quality preference is 90/200, p=.179—not evidence of equivalence. No demonstrated learning or health outcomes.
- **Resources/read scope:** [Author project page](https://sites.google.com/cs.washington.edu/curio) verified; official code, weights, dataset release and artifact licenses not verified. Read methods, §§4–5, limitations, Appendix B.1–B.3 and proceedings metadata. No reproduction.

<a id="method-topdial"></a>
### M60. TopDial · Role-playing generation for personalized target-oriented dialogue

[Target-oriented Proactive Dialogue Systems with Personalization: Problem Formulation and Dataset Curation](https://arxiv.org/html/2310.07397v2) — EMNLP 2023; arXiv v1 2023-10-11, read v2 2023-10-13.

Three gpt-3.5-turbo roles—user, system and moderator—use repurposed DuRecDial 2.0, sampled profile slots and Big Five descriptions to generate 18,009 dialogues with system-side act/topic targets. Model/human comparison covers 100 targets; equal-sized DialoGPT/Alpaca-7B training and mixed-source testing assess training utility through BLEU, knowledge F1, persona F1 and target success.

**Limits:** Synthetic roles and offline metrics do not establish real-user acceptance of proactive help. Hallucination and mistaken moderator termination remain. Refusal-based termination triggers on the second explicit rejection of the target act, not the first; this is not a deployment safety guarantee. Authors emphasize target constraints, privacy and bot-identity transparency.

**Read:** v2 §§3–4, Limitations and Ethical Considerations; paper-provided code/data link, no reproduction. Listed once as a method, without a second benchmark entry.

<a id="method-eclair"></a>
### M86. ECLAIR: Enterprise clarification [Adjacent capability]

[ECLAIR: Enhanced Clarification for Interactive Responses](https://arxiv.org/html/2503.15739v1) — IAAI-25 Emerging Applications, AAAI proceedings 39(28):28864–28870; read arXiv v1, 2025-03-19. [Official publication record](https://ojs.aaai.org/index.php/AAAI/article/view/35152). This is the full paper, not demonstration `2503.20791`.

**Type / capability:** An adjacent enterprise clarification method, not demonstrated long-term personalization. It combines sentence-, product- and entity-ambiguity agent outputs and domain grounding to decide whether to clarify and generate a question.

**Evidence / boundaries:** Evaluation uses 100 filtered hard cases from natural AEP customer queries—not random production traffic. Clarification-needed precision improves .732→.904, while recall falls .833→.635 and F1 .779→.746; macro F1 improves .520→.657. User-profile retrieval is future work. The 98% precision figure is a deployment target, not an achieved result. No longitudinal personalization benefit is established.

**Resources / actual reading:** No official code or customer-data release was found in this check; the arXiv distribution license does not license such artifacts. Read: architecture, experiments, lessons, deployment sections and official publication record; searched author resources. No reproduction run.

<a id="privacy-safety-methods"></a>
## Methods: Privacy, authorization, and safety

What information may be accessed or disclosed, and which actions are safe or authorized? Privacy judgments, prompt defenses, and permission mechanisms have different guarantees; the entries retain their individual threat models and limits.

<a id="method-airgapagent"></a>
### M26. AirGapAgent · Separate third-party context from personal-data selection

[AirGapAgent: Protecting Privacy-Conscious Conversational Agents](https://arxiv.org/abs/2405.05175) — CCS 2024; v1 (2024-05-08) used *Air Gap*, while v2 (2024-09-18) uses *AirGapAgent*. Same paper.

**Verification / reading scope**: 2026-11-01; relevant [v1](https://arxiv.org/html/2405.05175v1) §2–6 threat, design, and experiment passages; v2 metadata/abstract. No exhaustive cross-version experimental comparison.

- **Mechanism**: A separate minimizer selects necessary data using trusted user tasks and records; the conversational agent subsequently interacts with the untrusted third party, reducing context-hijacking leakage.
- **Evidence/limits**: Synthetic privacy/utility tests use 20 users, 26 fields, and eight tasks. Trusted tasks/records are assumptions; this is not physical isolation, universal injection defense, or system-wide non-leakage. The abstract's 97% protection is setup-specific, not an overall safety rate.
- **Resources**: Original official code/data and licensing were not verified. The later AirGapAgent-R is a third-party reconstructed evaluation, not a verified original release.

<a id="method-collaborative-memory"></a>
### M27. Collaborative Memory · Cross-user memory permissions

[Collaborative Memory: Multi-User Memory Sharing in LLM Agents with Dynamic Access Control](https://arxiv.org/abs/2505.18279) — 2025 preprint; v1, 2025-05-23.

**Verification / reading scope**: 2026-11-01; relevant [v1](https://arxiv.org/html/2505.18279v1) §3–5 method/evaluation passages and Appendix D synthetic-task setup.

- **Mechanism**: Private/shared memory tiers preserve provenance and filter access against current user–agent–resource permissions, including permission changes.
- **Evidence**: MultiHop-RAG, 200 synthetic business tasks, and a SciQAG dynamic-permission setting. Business tasks lack gold answers and primarily report resource usage, not verified answer accuracy.
- **Relevance/limits**: Useful for personal-agent multi-user boundaries, but primarily collaborative permission management rather than individual preference learning. Formal policy properties and controlled tests are not implementation audits or protection against all inferential leakage.
- **Resources**: Official code/data releases and licenses were not verified. Duplicate survey citations do not create another paper.

<a id="method-privacychecker"></a>
### M41. PrivacyChecker · Decision-time information-flow privacy judgments

[Privacy in Action](https://aclanthology.org/2025.findings-emnlp.925/) — Findings of EMNLP 2025; inspected [arXiv v1](https://arxiv.org/html/2509.17488v1). Benchmark: B48; count the paper once.

**Checked / reading scope:** November 1, 2026; §§3–4.5 and Limitations; ACL metadata and author resource link.

- **Mechanism:** prompts explicit contextual-integrity flow extraction and per-flow sharing judgments before action. Optional guidelines are excluded from main results; deployment uses system prompts, tool descriptions or a standalone MCP checker.
- **Evidence:** assess leakage together with helpfulness; keep static, live MCP, MCP+A2A and more complex workflows separate.
- **Limits:** flow extraction, judgment errors and judgment–action mismatch leave residual leakage. Adversarial memory poisoning is not the principal evaluation. Prompt-based mitigation is not mandatory access control, cryptographic protection or regulatory certification; a checker tool name does not establish non-bypassability.
- **Resources:** [author shortlink](https://aka.ms/privacy_in_action) was blocked by robots.txt; package availability and licenses are unverified. Public paper access does not establish an open implementation license.

<a id="method-agentraft"></a>
### M42. AgentRaft · Execution-time data over-exposure detection

[AgentRaft](https://arxiv.org/html/2603.07557v1) — 2026 preprint; inspected v1, March 8, 2026.

**Checked / reading scope:** November 1, 2026; §§3–6, including setup, component evaluation and limitations; paper links and targeted resource search.

- **Mechanism:** type compatibility and semantic validation construct a cross-tool dependency graph; targeted prompt synthesis, runtime taint tracking and multi-LLM judgments identify unnecessary transmitted fields.
- **Evidence:** 6,675 describes crawled ecosystem tools. Experiments use selected toolsets in four AgentDojo scenarios, generated PII/business assets and GPT-5.1 agents. The 57.07% figure denotes 347/608 tested potential call chains—not commercial-agent prevalence.
- **Limits:** requires internal traces; closed commercial agents and actual end-user deployments were not directly audited. Separate graph quality, prompt validity, detection and cost metrics. LLM errors and changing tools remain limitations; regulation-informed voting is not compliance certification, and proposed injection/runtime defenses are not validated guarantees.
- **Resources:** no author implementation/data release established from the paper or targeted search; **release status and implementation license unverified**. AgentDojo’s license does not license AgentRaft itself.

<a id="method-raise"></a>
### M48. RAISE · Selective acquisition of personal safety context

Same [paper](https://arxiv.org/html/2505.18882v5) and reading scope as B55; count once.

- **Mechanism:** offline LLM-guided MCTS caches acquisition paths; online retrieval guides questions and sufficiency/abstention decisions.
- **Boundary:** evaluated with benchmark contexts; not evidence of safe real-world counseling or validated permission to collect sensitive attributes.

<a id="method-gaap"></a>
### M53. GAAP

**Method: runtime information-flow and disclosure permissions**

[An AI Agent Execution Environment to Safeguard User Data](https://arxiv.org/abs/2604.19657) · **arXiv v3, September 24, 2026**; archival venue unconfirmed.

A restricted-plan interpreter and IFC combine persistent private-data, permission and disclosure stores. Confidentiality applies against malicious models/providers and services, subject to correct enforcement, user permissions and verified annotations. **Secrets placed directly in prompts, prompt timing metadata and integrity are excluded.** The custom 20-task/seven-attack suite reports no successful disclosures; AgentDojo/AgentDyn runs approve every disclosure and therefore assess utility, not privacy. These are not human usability studies; cost and latency overheads are substantial. [Public repository](https://github.com/rssta/gaap), but no LICENSE found and GitHub reports no license. **Read:** v3 threat model/design/evaluation/discussion and repository documentation/metadata; no security audit.

<a id="method-psg-agent"></a>
### M55. PSG-Agent · Staged guardrails for user-dependent risks

[PSG-Agent: Personality-Aware Safety Guardrail for LLM-based Agents](https://arxiv.org/html/2509.23614v1) — arXiv v1, 2025-09-28; venue unverified.

Mines profiles and compiles contextual safety criteria for plan, tool, response and memory-write checks. Its approximately 2,900 cases and histories are largely GPT-4o-generated from 132 manual seeds. Four experts checked 200 cases, each rating 50 distinct examples—not all four rating every case. ALLOW/REFUSE classification uses accuracy, precision, recall and F1; a separate three-model majority vote scores safety/helpfulness, with a 100-case human comparison. Evidence concerns synthetic profile-sensitive judgments, not real clinical/financial outcomes or proven long-term protection. Runtime gates offer no formal safety/privacy guarantee. The [anonymous repository linked by the paper](https://anonymous.4open.science/r/psg-agent-code-7724/) returned no readable content; completeness and licensing remain unverified.

**Reading scope:** §3–5, threat model, components, human review and LLM-judge setup; anonymous repository entry point. Targeted benchmark, framework and evaluation reading; repository landing-page check, no code audit.

<a id="method-privacy-risk-search"></a>
### M59. Searching for Privacy Risks — alternating attack/defense instruction search
- **Paper/cross-reference:** *Searching for Privacy Risks in LLM Agents via Simulation*, ICLR 2026; arXiv v3, 2026-05-08. Evaluation: **B62**; count once.
- **Method:** LLM trajectory analysis, parallel search and cross-thread propagation alternately optimize attacker/defender instructions, discovering impersonation/forged consent and prompt-level identity-verification state machines.
- **Limits:** Model instructions, not formal permission enforcement or cryptographic authentication; no guaranteed leakage prevention. Legitimate consent-sharing and deployment reliability remain separate questions.
- **Resources/read scope:** [v3](https://arxiv.org/html/2508.10880v3), §§3–4, ethics, Appendix G; [official code](https://github.com/SALT-NLP/search_privacy_risk), [trajectories](https://huggingface.co/datasets/SALT-NLP/search_privacy_risk). Dataset MIT-tagged; no root code license observed. Do not transfer dataset licensing to code. Viewer errors do not prove source files unavailable. Not reproduced.

<a id="tmp-b-ci"></a>

<a id="method-contextual-integrity-supervisor"></a>
### M70. Information-flow-card supervisor

**方法；唯一论文键 / Method; unique paper key: `CI`**

[Same paper](https://arxiv.org/html/2408.02373v2) · v2, 2024-09-13

An information-flow card structures context, actors, receiver, and disclosed information before a reasoning supervisor controls filling. Compared with self-censoring, binary, and ordinary reasoning supervisors. Prompt/few-shot controls are not hard authorization mechanisms; adversarial robustness and live interaction remain unverified.

Evaluation, sources, licensing, reading scope, and reproduction limits: [B74](#benchmark-operationalizing-ci). Not an H deployment study.

<a id="human-studies"></a>
## Human studies: real use and interaction

These studies document human experience; they are not benchmark scores or proof of long-term outcomes.

<a id="human-agent-memory-expectations"></a>
### H1. Users’ Expectations and Practices with Agent Memory

- **Paper/version:** [Author paper](https://younghokim.net/files/papers/jones-agent-memory-chi25lbw.pdf), CHI EA 2025 late-breaking work, eight pages; [DOI](https://doi.org/10.1145/3706599.3720158). Not a main-track full paper, benchmark or agent algorithm.
- **Design:** Six real users aged 24–35 completed 30–45-minute interviews; all self-rated tool proficiency 4/5. An additional 54 Reddit discussion threads underwent inductive thematic analysis.
- **Findings:** Incomplete memory mental models and demand for task/project/domain organization and separation; five interviewees wanted unrelated task memories kept disjoint. Workarounds included separate chats, personas/instructions and accounts.
- **Limits:** Small exploratory qualitative study; 54 threads are not 54 experimental participants. No population prevalence estimate, causal demonstration of hierarchical-memory benefits or implemented access-control guarantee.
- **Resources/read scope:** Read methods, findings and interview/survey/subreddit appendices. Raw study data/code release not verified. The author PDF retains copyright with specified personal/classroom copying permission, not a blanket open-data or open-source license.

<a id="human-memoro"></a>
### H2. Memoro · A concise interface for real-time memory assistance

- **Paper/version:** [Memoro: Using Large Language Models to Realize a Concise Interface for Real-Time Memory Augmentation](https://arxiv.org/html/2403.02135), CHI 2024; arXiv v1, 2024-03-04; [DOI](https://doi.org/10.1145/3613904.3642450). System plus human experiment, not a benchmark.
- **Mechanism/design:** Audio transcription and vector retrieval supply concise bone-conduction feedback through explicit Query or user-triggered Queryless interaction. Twenty participants aged 18–32 completed an approximately one-hour counterbalanced four-condition laboratory study, discussing fictional-person information with a researcher. External memories stayed fixed during conversation.
- **Evidence:** Average response length drops from 115.4 characters for Baseline to 16.6 for Query; correctness is 84% Query versus 70.7% Queryless. Recall confidence/difficulty are self-reported, not objective long-term memory gains. Several conversation measures show no significant differences, but naturalness is significantly below no-system: do not claim disruption-free interaction.
- **Limits/resources:** Queryless is not autonomous intervention. Consent is assumed and bystander controls remain unresolved. The [official MIT-licensed reference implementation](https://github.com/wazeerzulfikar/memoro/) is not a maintained product. Its later V2 older-adult field study is separate and V2 code is excluded. Read system, §§4–5, §7 and repository version/license descriptions. No reproduction.

<a id="human-loom"></a>
### H3. LOOM

**Human–AI study: proactive learning from daily conversations—not a benchmark**

[LOOM: Personalized Learning Informed by Daily LLM Conversations Toward Long-Term Mastery via a Dynamic Learner Memory Graph](https://arxiv.org/abs/2511.21037) · **AAAI 2026 PerFM Workshop**, not the AAAI main conference; arXiv v1, November 26, 2025.

A chat-to-course pipeline maintains a dynamic learner graph using inferred needs, completions and self-reported knowledge. The formative study includes **10 convenience-sampled participants over roughly two days**, each producing 10–15 realistic-workflow chats. Findings concern perceived relevance, coherence and gap discovery. Without controls, pre/post assessments or delayed recall, **durable learning gains are unestablished**. Content inconsistency, repetition and premature mastery inference remain concerns. The [PDF](https://arxiv.org/pdf/2511.21037)’s [anonymous code/demo link](https://anonymous.4open.science/r/LoomDemo) returned **HTTP 403**; artifact contents/license unverified. **Read:** system, study methods/results/limitations and PDF venue/resource notes; no execution.

<a id="human-compeer"></a>
### H4. ComPeer — Proactive peer support
- **Paper:** *ComPeer: A Generative Conversational Agent for Proactive Peer Support*, UIST 2024, DOI `10.1145/3654777.3676430`; reviewed arXiv v2 (2024-08-06).
- **Method/evidence:** Event detection, reflection and scheduling personalize proactive messages. Twenty-four Chinese university students were randomized to ComPeer or a reactive baseline sharing its memory/generation modules for one week; everyone used ComPeer in week two.
- **Boundary:** Self-reported stress declined in both groups without a significant between-group difference—not evidence of superior stress reduction or clinical efficacy. Short duration, sample composition and novelty limit generalization; interruption, misinformation, peer pressure and dependence remain concerns.
- **Resources/reading scope:** [Paper](https://arxiv.org/html/2407.18064v2) §§4–7 and [author repository](https://github.com/liutj9/ComPeer) reviewed. Code license unconfirmed; arXiv distribution permission is not a software license.

<a id="human-planfitting"></a>
### H5. PlanFitting — Constraint-aware exercise planning
- **Paper:** *PlanFitting: Personalized Exercise Planning with Large Language Model-driven Conversational Agent*, published CUI 2025 version, 19 pages; DOI `10.1145/3719160.3736607`.
- **Method/evidence:** Dynamic prompting and retrieval elicit goals, availability and obstacles to create revisable IF–THEN weekly plans. Eighteen people completed an approximately one-hour study; revision used imagined next-week scenarios. Two researchers checked guideline adherence; three physical therapists each assessed six initial plans. This was not a randomized health intervention.
- **Boundary:** Evidence concerns plan quality and perceptions, not sustained adherence, exercise benefits or clinical safety. Rest-day and exercise-combination problems remained.
- **Resources/reading scope:** [Published PDF](https://faculty.washington.edu/garyhs/docs/shin-cui2025-planfitting-paper.pdf) §§4–6 and §7.5 reviewed. Paper: CC BY 4.0; implementation/data licenses unconfirmed.

<a id="human-teachtune"></a>
### H6. TeachTune — Teacher review through student simulation
- **Paper:** *TeachTune: Reviewing Pedagogical Agents Against Diverse Student Profiles with Simulated Students*, CHI 2025; DOI `10.1145/3706598.3714054`.
- **Method/evidence:** Teachers author agent state diagrams and student profiles, then inspect simulated conversations. Thirty science teachers compared direct-chat/single-turn testing, full Autochat and knowledge-only simulation; six additional observational participants were excluded from comparative statistics. Autochat participants submitted more distinct student profiles; self-rated perceived coverage did not differ significantly. Expert-rated agent quality also did not differ significantly.
- **Boundary:** Teachers were real; students were simulated. No student learning gains were tested. One phase-transition topic, limited static traits and uncertain simulation fidelity constrain generalization.
- **Resources/reading scope:** [Paper](https://jeongeonpark.com/assets/pdf/papers/chi25-teachtune.pdf) §4, §§5.3–5.4, Table 5 and §7; [project page](https://teachtune.kixlab.org/) reviewed. Paper: CC BY-NC-SA 4.0; trial requires contacting authors, code license unconfirmed.

<a id="human-memolet"></a>
### H7. Memolet — Manipulable conversational memories
- **Paper:** *Memolet: Reifying the Reuse of User-AI Conversational Memories*, UIST 2024; DOI `10.1145/3654777.3676388`.
- **Method/evidence:** Interactive memory objects support extraction, organization, inclusion/exclusion, weighting and combination through prompts and RAG. Twelve people completed a within-subject comparison, reusing writing, programming or trip-planning conversations one day later; conditions shared underlying generation/retrieval capabilities.
- **Boundary:** Findings concern interaction control and user experience, not longitudinal memory accuracy or autonomous memory management. Convenience sampling, controlled tasks and a one-day gap limit deployment claims.
- **Resources/reading scope:** [Author PDF](https://www.jeffjianzhao.com/papers/memolet.pdf#page=1) §4.6, §§5–6 and §8 reviewed. The author copy specifies personal use and no redistribution; open code/data licenses unconfirmed.

<a id="human-chatlab"></a>
### H8. ChatLab — customizable personas, avatars and voice output
- **Paper:** *Customizing Emotional Support: How Do Individuals Construct and Interact With LLM-Powered Chatbots*, CHI 2025; arXiv v2, 2025-04-18.
- **Evidence:** Approximately week-long field study (protocol: 7–10 days): 26 completed fieldwork; data from 22 participants were analyzed, combining diaries, interviews and design activities. Supports persona/avatar customization and TTS output, **not voice input**.
- **Limits:** A design probe, not an efficacy trial. Short duration and Asian-cultural sample do not establish lasting mental-health benefit. Adjustable memory is a requested design opportunity, not an implemented capability. Research-team access restrictions/cloud storage do not establish security guarantees.
- **Resources/read scope:** [Paper](https://arxiv.org/html/2504.12943v2), §§3–4,6–8; [author prototype page](https://xizhengxi.com/prototypes.html). No official code/data release or software license confirmed; arXiv distribution permission is not an open-source license.

<a id="human-financial-advisors"></a>
### H9. Personalized Financial Advisors — elicitation, advice quality and perceived trust
- **Paper:** *Are Generative AI Agents Effective Personalized Financial Advisors?*, SIGIR 2025; arXiv v2 (2025-04-15).
- **Method and evidence:** Llama-3.1-8B elicits preferences and discusses four stocks, comparing non-personalized/personalized advice and extroverted/conscientious personas. Of 64 recruits, 60 remained in analysis: 29 personalization and 31 persona participants. Humans role-played three expert-designed investor profiles rather than expressing their own investment needs. The expert elicitation comparison used three participants per profile.
- **Limits:** Measures elicitation accuracy, agreement with expert asset rankings and subjective trust/satisfaction—not investment returns or long-term financial outcomes. Elicitation errors can lead to unsuitable advice; greater liking for an extroverted advisor does not imply better advice. Single-university role-play does not establish replacement of professional advisors.
- **Resources and reading:** [Paper](https://arxiv.org/html/2504.05862v2), §§3–5, conclusion and metadata; [official supplement](https://github.com/TTsamurai/LLMAdvisor_supplementary), describing profiles, prompts and analysis scripts. README declares MIT; the inspected arXiv v2 is CC BY 4.0 (not a statement of the SIGIR publication license). Complete raw participant-data release not verified.

<a id="reproducibility"></a>
## Comparison and reproducibility

Do not assemble a leaderboard from unrelated papers' highest scores. Record at least:

1. **Tasks and versions:** Paper version, code commit, dataset revision / file hashes, splits, counts, and excluded failures. Separate original, cleaned, verified, and successor versions.
2. **Visible information:** Full history, retrieval top-k, oracle evidence, schemas, screenshots / UI trees. Do not put answers or future sessions into memory.
3. **Models and systems:** Exact base-model, memory, embedding, reranker, and judge versions; prompts, tools, and code commit. Distinguish model improvements from system improvements.
4. **Budgets and metrics:** Time, tokens, cost, steps, and retries. Report single-run success, repeated reliability, retrieval recall, and answer correctness separately. `pass@k` and `pass^k` are not interchangeable.
5. **Safety and utility:** Report normal / attacked-task utility alongside leakage / violations, clarification frequency, restraint after rejection, interruption costs, and latency. Refusing every task is not a useful safety score.
6. **Memory lifecycle:** PersonaMem-v2 non-use, MemoryAgentBench conflict resolution, Zep edge invalidation, and MemOS governance design do not independently prove erasure from storage, backups, or parameters.
7. **Real-assistant gaps:** Months-long human utility, cross-user / multi-agent isolation, irreversible-action authorization, auditable revocation, idempotent recovery after restarts / disconnection, and actual storage erasure still require dedicated testing.

These are this guide's evaluation recommendations, not claims that every listed paper covers all dimensions. Use synthetic or authorized, de-identified data. Never publish real personal histories, secrets, or cookies in issues, logs, or benchmark repositories.

<a id="sources-and-rights"></a>
## Sources and rights

- Paper titles link to original papers / publication pages; resource links point to author-maintained entry points. They support task definitions, metrics, and dates. Suggested applications and capability gaps are this guide's synthesis, not author endorsements of product reliability.
- Summaries are original and brief. No paper figures, long passages, complete question sets, or hidden answers are copied. Cite the original paper using its BibTeX, rather than citing only this list.
- **Public access is not unrestricted reuse.** Entries flag noncommercial terms for LaMP, LoCoMo, PersonaBench, PrefEval, and MemoPro code; GAIA gating / contamination controls; and additional AppWorld / Ego4D resource rules. An omitted license does not imply unrestricted use; code, data, weights, and third-party assets may have different terms.
- This check did not include asset-by-asset legal review, downloading and validating full weights, or reproducing all dependencies. A GitHub link does not resolve missing licenses, inaccessible files, or changing external services.
- Prioritize correcting versions, scope, and broken resources before adding papers. Contributions should provide specific primary evidence; rankings, citation counts, and stars are not reliability findings.
