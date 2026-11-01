# Personal agent papers & benchmarks

[中文](PAPERS.md) · [Main list](../README.en.md)

**Understand what was measured before comparing scores.** This guide separates evaluations / benchmarks from methods / systems, and distinguishes direct personal-context research, transferable general memory / execution capabilities, and specific privacy / security risks.

Literature and resource check: **2026-10-31**. **108 distinct papers**: 61 evaluation entries, 55 method entries, and 7 human-study entries. Proactive Agent, MemoProAgent, PbP/InTU, Ask-before-Plan/CEP, PersonalAlign/HIM-Agent, PEToolLLM/PEToolLLaMA, MemGuide/MS-TOD, Me-Agent/User FingerTip, PPP/UserVille, PUMA/PersonalWAB, MPR/HybridMem, PrivacyLens-Live/PrivacyChecker, PTBench/PTool, PAL-Bench/H²Memory, and PENGUIN/RAISE each contribute a benchmark and a method; each paper is counted once. Sources are paper abstracts and the explicitly identified passages below, author project pages, official repositories, and dataset cards. **No installation, independent benchmark run, model training, or security audit was performed.** This is a selective reading guide, not a comprehensive survey, latest-paper feed, or product ranking.

**Entry checks:** B25–B61, M16–M55, and H1–H7 were checked on 2026-11-01; earlier entries retain their original check dates.

**Reading scope:** Each entry records the abstract, relevant passages, and resource pages actually consulted. No claim is made that every paper was read end to end. Translation is not an additional verification.

Years and versions identify the listed paper, not the current project. Original task counts may differ from current code. Branches, dataset cards, and resource status are observations on the check date, not pinned reproduction snapshots. “Public” means an official entry point was found, not that commercial reuse is permitted, dependencies install, weights are complete, or results reproduce.

## Contents

- [Start with a research question](#reading-paths)
- [Evaluation: personal context, memory, and proactivity](#personal-evaluation)
- [Evaluation: transferable memory and sequential tasks](#transferable-memory-evaluation)
- [Evaluation: task execution and interaction](#execution-evaluation)
- [Evaluation: privacy norms and adversarial safety](#safety-evaluation)
- [Methods: memory and persistent state](#memory-methods)
- [Methods: planning, tools, reflection, proactivity, and coordination](#agent-methods)
- [Methods: personalization and preference learning](#personalization-methods)
- [Human studies](#human-studies)
- [Comparison and reproducibility](#reproducibility)
- [Sources and rights](#sources-and-rights)

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

<a id="personal-evaluation"></a>
## Evaluation A: personal context, memory, and proactivity

These benchmarks directly involve user history, preferences, or proactive help. **None alone evaluates an entire personal agent.**

<a id="benchmark-lamp"></a>
### B1. LaMP · Personalized language tasks

[LaMP: When Large Language Models Meet Personalization](https://aclanthology.org/2024.acl-long.399/) — ACL 2024.

**Checked / reading scope:** 2026-10-31; Paper abstract and §2.3 metric passages; official README licensing notes and data-download page.

- **Input → output:** Task input and the user's historical items → a personalized label or text. The paper covers three classification and four generation tasks.
- **Measures:** Accuracy / F1, rating MAE / RMSE, and generation ROUGE; user-based and time-based splits distinguish generalization settings.
- **Limits:** Tests personalized retrieval and generation, not multi-step tool execution or longitudinal use with real users.
- **Resources:** [Official code](https://github.com/LaMP-Benchmark/LaMP), [data](https://lamp-benchmark.github.io/download). Code and construction methods use CC BY-NC-SA 4.0; underlying datasets retain their own licenses.

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

<a id="benchmark-personamem-v1"></a>
### B4. PersonaMem · Evolving user profiles

[Know Me, Respond to Me: Benchmarking LLMs for Dynamic User Profiling and Personalized Responses at Scale](https://arxiv.org/abs/2504.14225) — COLM 2025; this entry covers the original benchmark / v1 data.

**Checked / reading scope:** 2026-10-31; Original-paper revision: §2 task definition and relevant §4 results passages; official README data format and v1 dataset card.

- **Input → output:** Synthetic multi-session history with changing preferences and a new-scenario question → one of four candidate responses.
- **Measures:** Selection accuracy across seven query types, context lengths, and distances from preference mentions; separates recall, updates, and preference transfer.
- **Limits:** Four-choice accuracy is not open-ended personalized response quality. Synthetic personas are not longitudinal human participants. Do not mix with PersonaMem-v2 data.
- **Resources:** [Official code](https://github.com/bowen-upenn/PersonaMem), [v1 data](https://huggingface.co/datasets/bowen-upenn/PersonaMem-v1), including 32k, 128k, and 1M context settings.

<a id="benchmark-mem2actbench"></a>
### B5. Mem2ActBench · From memory to tool arguments

[Mem2ActBench: A Benchmark for Evaluating Long-Term Memory Utilization in Task-Oriented Autonomous Agents](https://aclanthology.org/2026.acl-long.370/) — ACL 2026.

**Checked / reading scope:** 2026-10-31; Paper abstract, relevant §4.1 experimental-setup and §5.4 tool-selection passages; official README (including its License statement), root listing, and data-directory entry points.

- **Input → output:** Historical memory, an implicitly constrained request, and tool schemas → tool selection and arguments. The paper constructs 400 memory-dependent tasks.
- **Measures:** Argument matching / F1, tool selection, and whole-call matching. Main experiments supply the correct tool; separate experiments add distractor tools.
- **Limits:** Correct arguments are not a completed real transaction. Main results should not be presented as open-ended tool-selection performance.
- **Resources:** [Official construction code / data directories](https://github.com/Cantaloupe-M/Mem2ActBench). The [README License section](https://github.com/Cantaloupe-M/Mem2ActBench#license) declares MIT License, but no separate LICENSE file was observed in the root listing. Confirm the full license text and scope before reuse. Check upstream ToolACE, BFCL, and OASST1 terms separately; this declaration does not establish MIT licensing for all data.

<a id="benchmark-proactivebench-lu"></a>
### B6. ProactiveBench (Lu et al.) · When to offer help

[Proactive Agent: Shifting LLM Agents from Reactive Responses to Active Assistance](https://arxiv.org/abs/2410.12361) — 2024 preprint; ICLR 2025.

**Checked / reading scope:** 2026-10-31; Paper abstract and evaluation-metric passages; official README system overview, data statistics, and evaluation entry points.

- **Input → output:** User activity and environment events → a proposed assistance task, or no proposal. The paper includes 6,790 events across coding, writing, and daily-life settings.
- **Measures:** Precision, recall, F1, and false alarms under acceptance / rejection judgments; automated evaluation uses a learned reward model.
- **Limits:** Appropriate offers are not long-term human satisfaction or task completion. A proactive suggestion does not authorize execution.
- **Resources:** [Code, data, evaluation](https://github.com/thunlp/ProactiveAgent). Other papers use the same benchmark name; this entry specifically means Lu et al. See M11 for the method.

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

<a id="benchmark-pdeu-bench"></a>
### B25. PDEU-Bench · Preferences across plan revisions

[PDEU-Bench: Benchmarking the Personalized Planning Lifecycle of Tool-Calling LLM Agents](https://arxiv.org/html/2609.34930v1) — 2026 preprint; v1, 2026-09-28.

**Checked / reading scope:** 2026-11-01; abstract and relevant passages in Environment Construction, Preference and Task Construction, Task Evaluation, and Error Analysis.

- **Input → output:** Synthetic user histories and tasks → initial plans, tool calls, and updates after every attempt; 214 tasks, 12 domains, 94 tools.
- **Measures:** A fixed judge applies binary preference/quality rubrics; strict success requires all relevant stages to pass. Execution scores preference-sensitive arguments only.
- **Limits:** Synthetic preferences and an offline sandbox do not establish real transactions or longitudinal user benefit.
- **Resources:** The abstract points to code/data in an appendix, but no verifiable official release was located in the consulted HTML or search. Licensing and runnability remain unconfirmed.

<a id="benchmark-atrbench"></a>
### B26. ATRBench · Ask now, use later

[Ask Now, Use Later: Benchmarking the Proactivity Gap in Long-Lived LLM Agents](https://arxiv.org/html/2605.28108v3) — v3, 2026-09-15; author metadata lists EMNLP 2026 Main.

**Checked / reading scope:** 2026-11-01; abstract, §§3.1–3.2, Limitations, Ethical Considerations; official README and NOTICE.

- **Input → output:** Ordinary simulated-user tasks → eliciting preferences useful later, not needed now. History is then frozen; test users are offline.
- **Measures:** TSAcc deterministically checks the first relevant tool decision, macro-averaged by user; asking, acquisition, and application are reported separately.
- **Limits:** Twenty synthetic personas, fixed rules, and model routing do not establish changing real preferences or interruption costs. More questions need not help.
- **Resources:** [Official code/data](https://github.com/BUPT-GAMMA/ATRBench). Code: Apache-2.0; NOTICE separately attributes source personas under CC BY 4.0. Do not assume one license covers every asset. Not run.

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

<a id="benchmark-memsim"></a>
### B36. MemSim / MemDaily · Synthetic personal-memory evaluation

[MemSim: A Bayesian Simulator for Evaluating Memory of LLM-based Personal Assistants](https://arxiv.org/abs/2409.20163) — 2024 preprint; v1, 2024-09-30.

**Verification / reading scope**: 2026-11-01; relevant passages in [v1](https://arxiv.org/html/2409.20163v1) §3 methods, §4 data quality, and §5 benchmark; official README and root listing.

- **Input → output**: Synthetic user-message streams and personal questions → text or multiple-choice answers; supporting-message annotations also enable retrieval evaluation.
- **Measures**: Answering and retrieval are separate; question types cover single-/multi-hop, comparison, aggregation, post-processing, and noise. Full, recent, retrieved, absent, and oracle memory are compared, primarily with GLM-4-9B. Do not pool MemDaily settings with different irrelevant-post ratios.
- **Limits**: Bayesian profiles and structured hints improve consistency, but sampled human checks do not guarantee error-free data. Synthetic factual QA does not establish real-user preference understanding or tool execution.
- **Resources**: [Official code/data](https://github.com/nuster1128/MemSim) includes generation, benchmarking, and `data_generation/final_dataset/memdaily.json`; README reports 2,954 trajectories/questions and 26,003 messages. Code/data licensing was not verified; the paper's CC BY 4.0 does not automatically cover them.

<a id="benchmark-ms-tod"></a>
### B37. MS-TOD · Cross-session intent and slot tracking

[MemGuide: Intent-Driven Memory Selection for Goal-Oriented Multi-Session LLM Agents](https://ojs.aaai.org/index.php/AAAI/article/view/40313) — AAAI 2026; published 2026-03-14. Same paper as M25.

**Verification / reading scope**: 2026-11-01; relevant Dataset, MemGuide, and Experiments passages in [arXiv v2](https://arxiv.org/html/2505.20231v2); proceedings metadata/PDF resource link; official README and root listing.

- **Input → output**: User history, current dialogue, and QA memories → a response advancing or confirming the current task.
- **Measures**: GPT-4 judging, Joint Goal Accuracy, completion turns, success rate, and human quality ratings. The paper reports 132 personas and 956 task goals; the official README reports 2,860 sessions.
- **Limits**: SGD-seeded, GPT-4-generated dialogues use three temporally ordered sessions per task with human validation; each session is simplified to one service/intent. Slot-based confirmation success is not a completed real booking, payment, or longitudinal user benefit.
- **Versions/resources**: 2505.20231v1 (2025-05-26), *Bridging the Long-Term Gap: A Memory-Active Policy for Multi-Session Task-Oriented Dialogue*, was renamed MemGuide in v2 (2025-08-13); count once. [Official code/data](https://github.com/Elvin-Yiming-Du/MS_TOD_Memory); no root license observed, and reuse terms remain unverified.

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

<a id="benchmark-user-fingertip"></a>
### B42. User FingerTip · Resolving ambiguous app and content requests

[Me-Agent](https://arxiv.org/html/2601.20162v1) — arXiv v1, January 28, 2026; same paper as M29.

**Verified / actual reading scope:** 2026-11-01; v1 §3 User FingerTip construction/statistics, §5.1–5.2 metrics/results and Table 3, and Limitations; arXiv version history, repository root, and README. Selected passages, not a line-by-line full-paper review; no installation, execution, or experimental reproduction.

- **Evaluation:** Extends FingerTip by removing app names or obscuring requested content. Reports 60 users, 33 apps, 300 Type-I and 267 Type-II instructions.
- **Limits:** Counts versus “15 training/5 test instructions per user” need clarification; this is not established held-out-user evaluation. Table 3’s perfect app selection accompanies task-success rates of 80%/50%, not universal success. Long-term human deployment is unproven.
- **Resources:** [Author repository](https://github.com/Gianthaha/personal-mobile-agent) is MIT-labeled and contains implementation directories, but README still promises updates; complete benchmark packaging remains unverified.

<a id="benchmark-userville"></a>
### B43. UserVille · Hidden tasks and interaction preferences

Same paper as M30; do not count twice. [Original paper](https://arxiv.org/html/2511.02208v2); reading scope and resource limitations as above.

- **Automated component:** Obscures task descriptions and uses preference-conditioned LLM users; 20 interaction preferences include eight held out. Code localization uses F1, BrowseComp-Plus uses EM; personalization covers only sessions containing a question.
- **Human component:** v2 includes 33 programmers and 300 evaluations on SWE-Bench tasks. Participants could see descriptions and gold patches; this is not natural longitudinal deployment. Satisfaction is PPP 3.75 versus GPT-5 3.79, but reported resolution is 71% versus 85%. Do not report satisfaction alone.
- **Interpretation:** Table 1 composite means are 62.04 versus Seed-OSS-36B 45.32. The +16.72 comparison is against Seed, not GPT-5, and is not task-success percentage points.

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

<a id="benchmark-mpr"></a>
### B46. MPR · Multi-hop personalized factual reasoning

[Explicit v.s. Implicit Memory: Exploring Multi-hop Complex Reasoning Over Personalized Information](https://arxiv.org/html/2508.13250v1) — arXiv v1, 2025-08-18; method in M38. Count the paper once.

**Verification date / reading scope:** 2026-11-01; §3–6; official README, complete file tree and release metadata.

- **Input → output:** Synthetic user graphs, generated single-hop statements and questions → 2–10-hop personalized factual answers; not observed human histories.
- **Measurement:** Normalized answer exact match; experiments use a balanced 2,700-question subset. Report oracle and ordinary retrieval separately.
- **Boundary:** Not tool execution, online preference changes or longitudinal satisfaction. Table 2 says 108,000 QA but §3.3.3 says 10,800; retain the discrepancy rather than silently correcting it.
- **Resources:** [official repository](https://github.com/nuster1128/MPR), master, last pushed 2025-08-24; no releases or declared repository license. README links a Drive dataset, but its archive was inaccessible during verification. Paper CC BY 4.0 does not establish code/data reuse rights.

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

<a id="benchmark-pal-bench"></a>
### B52. PAL-Bench · Requirements and preferences from long-term personal histories

[Mem-PAL: Towards Memory-based Personalized Dialogue Assistants for Long-term User-Agent Interaction](https://arxiv.org/html/2511.13410v2) — v2, 2025-11-26; AAAI 2026 Oral. Same paper as M47.

**Actual reading scope:** PAL-Bench construction/tasks, H²Memory framework and Experiments, including external validation; repository README and file listing. Appendices were sampled, not comprehensively read.

- **Input → output:** behavioral logs plus dialogue history → restated requirements, proposed/selected solutions, multi-turn responses.
- **Measures:** BLEU, GPT-4 implicit-need judgments, solution-selection scores and pairwise dialogue judgments.
- **Boundary:** PAL-Set has 100 synthetic users, approximately 29 sessions and 9.4 simulated months each; human verification does not make this a longitudinal user study. Multi-turn users are simulated by an LLM. External validation covers only LongMemEval’s single-session-preference subset and uses the dialogue components (Topic Outline + Principle), not the complete four-component system.
- **Resources/language:** [official code/data](https://github.com/hzp3517/Mem-PAL). README identifies the English version as a DeepSeek-V3 translation without item-by-item human verification. Appendix B states an intended PAL-Set release under CC BY-NC 4.0; this author statement uses future-release wording and is separate from verifying the distributed dataset’s terms or the implementation’s license. Repository reuse-license verification remains incomplete.

<a id="benchmark-memento"></a>
### B53. MEMENTO · Applying personal memories to embodied tasks

[Embodied Agents Meet Personalization: Investigating Challenges and Solutions Through the Lens of Memory Utilization](https://arxiv.org/html/2505.16348v4) — v4, 2026-02-13; ICLR 2026.

**Actual reading scope:** §§3–4, overview of memory-design contribution, Appendix A.1–A.2; author project and repository README. Detailed §6 algorithm/ablations and extended Appendix E were not comprehensively read; method cross-index remains provisional.

- **Input → output:** personal object meanings/routines and episodic memories → object-rearrangement actions.
- **Measures:** matched acquisition/utilization goals, single/joint memories, percent complete, success rate and planning cost; 438 episodes across 12 Habitat scenes with generated personal knowledge.
- **Boundary:** main setting guarantees gold memories among retrieved candidates and oracle perception/motor skills. It isolates memory utilization, not unconstrained retrieval or real-world robot reliability. Synthetic users, no conversational clarification. GPT-4o joint-memory success drops 30.5 percentage points relative to its matched acquisition baseline.
- **Resources/identity:** [official repository](https://github.com/Connoriginal/MEMENTO), MIT repository with Habitat/PARTNR dependencies. README’s older subtitle “Exploring Memory Utilization for Personalized Assistance” denotes the same paper.

<a id="benchmark-realmem"></a>
### B56. RealMem

**Benchmark: long-term project state and cross-session memory**

[RealMem: Benchmarking LLMs in Real-World Memory-Driven Interaction](https://aclanthology.org/2026.findings-acl.703/) · **Findings of ACL 2026**, with arXiv:2601.06966v1 as the earlier version.

Evaluates evolving state, temporal reasoning and goal alignment using over 2,000 **synthetic** cross-session dialogues across 11 scenarios—not longitudinal deployment logs. Final Table 2 reports memory-only GPT-4o QA of 0.567 for MemoryOS versus 0.804 for the oracle. Human validation covers 30 instances and two NLP-background annotators, not user outcomes. Prefer the final paper, which adds LightMem, full-context baselines and evaluation details. Synthetic data and model-based judging limit generalization. [Official code/data](https://github.com/AvatarMemory/RealMemBench) are available; **LICENSE states Apache-2.0; README badge says MIT**. **Read:** arXiv methods/results, final PDF results/limitations/human protocol, repository README/LICENSE; no reproduction.

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

<a id="benchmark-personafeedback"></a>
### B59. PersonaFeedback · Response selection with explicit personas

[PersonaFeedback: A Large-scale Human-annotated Benchmark For Personalization](https://arxiv.org/html/2506.12915v1) — arXiv v1, 2025-06-15, work in progress.

**English review:** Evaluates binary response selection given explicit personas using selection accuracy against labels, with 8,298 human-labelled cases—not 8,298 real participants. Twenty real seed profiles underpin constructed personas; 200 are used for benchmarking. Model-generated material is human-filtered, with majority labels from nine evaluators. This is not a longitudinal user study or evidence that RAG generally fails. Subjective labels and persona simplification constrain conclusions. The public dataset declares Apache-2.0; its viewer currently reports incompatible schemas. No formal privacy guarantee was established.

**Reading scope:** §3 construction/annotation, §4 evaluation setup, limitations; official dataset card and viewer status. Targeted construction, evaluation and limitations; dataset card/viewer, not a full dataset audit.

<a id="benchmark-atm-bench"></a>
### B60. ATM-Bench · Multi-source personal referential memory QA

[According to Me: Long-Term Personalized Referential Memory QA](https://arxiv.org/html/2603.01990v1) — arXiv v1, 2026-03-02, preprint.

**English review:** Uses roughly four years of human-origin multimodal memories and 1,038 human-annotated QA/evidence pairs. Structured memory supports retrieval and grounded answering. QS selects its scorer by answer type: EM for numbers, Jaccard for list recall, and an LLM judge for open-ended answers. Retrieval separately reports Recall@k and Recall@k_GT (k equals the ground-truth evidence count); Joint@k = QS × Recall@k. Consent, visual redaction, email paraphrasing and synthetic identifier replacement are not formal anonymity guarantees. The paper’s below-20% Hard finding belongs to its original evaluation. Code and data are now released: MIT code and CC BY-NC 4.0 data. Later repository benchmarks can use different release sets and must not be merged with preprint results.

**Reading scope:** §3–5, Appendix A privacy/licensing and Appendix B annotation; official repository timeline, result-version notes and dataset card. Targeted methods/evaluation/ethics/annotation plus release records; no raw personal-data inspection.

<a id="transferable-memory-evaluation"></a>
## Evaluation B: transferable memory and sequential tasks

These study incremental memory or cross-session task dependencies: **transferable general capabilities**, not complete personal assistants or longitudinal human studies.

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

<a id="execution-evaluation"></a>
## Evaluation C: task execution and interaction

These can test a personal assistant's ability to act, but most are **general-agent, web / GUI, or service-domain benchmarks**, not personal-specific evaluations. AppWorld includes simulated personal apps and people, but not longitudinal personalization with real users.

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

<a id="benchmark-ask-before-plan"></a>
### B30. Ask-before-Plan · Clarification before commitment

[Ask-before-Plan: Proactive Language Agents for Real-World Planning](https://aclanthology.org/2024.findings-emnlp.636/) — Findings of EMNLP 2024; method: M18.

**Checked / reading scope:** 2026-11-01; abstract, evaluation in §5.1–5.2 and Appendix B.2–B.3; official README.

- **Input → output:** Dialogue and environment feedback → questions, calls and travel plans.
- **Measures:** Clarification, call correctness and plan constraint / final pass rates, separately.
- **Limits:** Component tests supply correct upstream outputs; integral-framework final planning also receives ground-truth conversation (Appendix B.3). Neither establishes fully free-running end-to-end performance or longitudinal profiling.
- **Resources:** [Code](https://github.com/magicgh/Ask-before-Plan), [data](https://huggingface.co/datasets/magicgh/Ask-before-Plan). README declares MIT code and CC BY 4.0 data / environment. Separate environment download; not installed.

<a id="safety-evaluation"></a>
## Evaluation D: privacy norms and adversarial safety

Distinguish inappropriate sharing from malicious instructions in external content. These evaluations provide evidence about specific risks, **not full privacy, security, or compliance certification**. Interpret low violation rates alongside task utility.

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

**English review:** Executes 246 tasks on self-hosted web replicas with synthetic user data derived from human seeds. Final-state checks measure utility; GPT-4o judges action-text disclosure. Leakage rate is the fraction of instances with leakage; privacy performance equals 1 minus leakage rate. The 98% human agreement validates only one GPT-4o/axtree run. Its threat model excludes malicious actors and external attacks: this is inadvertent data minimization, not prompt-injection defense. Prompting reduces leakage without guaranteeing privacy. Official resources combine CC BY-NC 4.0, MIT components and additional Llama 3.1-derived data terms.

**Reading scope:** v3 §3 threat model, data, metrics and mitigation; §4–5 evaluation/discussion; arXiv venue metadata and official README licensing section. Targeted methods, evaluation and discussion plus venue/resource records; environments not deployed.

<a id="memory-methods"></a>
## Methods A: memory and persistent state

These entries describe reusable mechanisms, not research prototypes certified as reliable personal-assistant products.

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

<a id="agent-methods"></a>
## Methods B: planning, tools, reflection, proactivity, and coordination

This group includes direct proactive-assistant research and transferable skill-learning or orchestration methods. Accumulating external experience does not solve parameter-level continual learning, and multiple agents are not automatically more reliable.

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

<a id="method-intu"></a>
### M17. InTU · Verbalize preferences before planning

[Inferring the Unspoken](https://arxiv.org/abs/2502.00858v4) — Same paper as B29; count once.

**Checked / reading scope:** 2026-11-01; v4 abstract only; preliminary review.

- **Mechanism:** Express preferences inferred from multimodal demonstrations in language, then condition action plans on them.
- **Limits:** An interpretable intermediate representation does not guarantee correct inference. Evaluation, resources and reading limitations: [B29](#benchmark-pbp).

<a id="method-cep"></a>
### M18. CEP · Separate clarification, execution and planning

[Ask-before-Plan](https://aclanthology.org/2024.findings-emnlp.636/) — Same paper as B30; count once.

**Checked / reading scope:** 2026-11-01; abstract, evaluation setup, Appendix B.3 and official README training / inference entries.

- **Mechanism:** Three specialized roles; trajectory tuning for clarification and static execution, memory recollection for dynamic execution.
- **Limits:** Role separation is not persistent profiling or authorization. Integrated final planning still uses ground-truth conversation (Appendix B.3); do not label it fully free-running. Resources and licenses: [B30](#benchmark-ask-before-plan).

<a id="personalization-methods"></a>
## Methods C: personalization and preference learning

<a id="method-p-rlhf"></a>
### M16. P-RLHF · Learning preferences from individual feedback

[Personalized Language Modeling from Personalized Human Feedback](https://arxiv.org/html/2402.05133v3) — 2024 preprint; first submitted 2024-02-06; consulted v3, 2024-12-09.

**Checked / reading scope:** 2026-11-01; abstract, §4.1–4.4 user models / P-DPO, relevant §5 experiment passages; official README data, training, and evaluation instructions. No installation or training.

- **Core:** Jointly learns a lightweight user model and LLM. User embeddings combine explicit textual preferences with implicit preferences learned from individual comparison feedback. User embeddings enter generation through soft prompting, and P-DPO conditions preference optimization on the user.
- **Relevance and limits:** A personalization method, not a benchmark or long-term memory system. Experiments include synthetic, semi-synthetic, and PRISM human feedback; model-judged response comparisons do not establish longitudinal human satisfaction, changing-preference tracking, or tool execution. An unknown user without textual information receives a non-personalized response.
- **Resources:** [Official implementation](https://github.com/HumainLab/Personalized_RLHF) includes user models and data-processing, training, and evaluation entry points. Public code does not establish reproduced training; upstream data and base-model terms require separate checks.

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

<a id="method-petoolllama"></a>
### M22. PEToolLLaMA · Training preference-aware tool calls

[PEToolLLM: Towards Personalized Tool Learning in Large Language Models](https://aclanthology.org/2025.findings-acl.1107/) — Findings of ACL 2025; same paper as B33. PEToolLLM is the paper title, PEToolBench the benchmark and PEToolLLaMA the method.

**Verified / reading scope:** 2026-11-01; [v1](https://arxiv.org/html/2502.18980v1) §3 metrics and §4 method overview; official README/LICENSE and dataset file listing. Not a full-paper read.

- **Mechanism:** personalized SFT conditions on history, instructions and candidate tools; DPO then improves preference-consistent call selection.
- **Evidence:** tool and parameter accuracies under PEToolBench's three synthetic-history settings.
- **Limits:** training is not persistent-memory management. Results do not establish real service completion, online preference shifts or safe side-effect control.
- **Resources:** [official training/test scripts](https://github.com/travis-xu/PEToolBench), [data](https://huggingface.co/datasets/travisxu/PEToolBench/tree/main). Repository: Apache-2.0; upstream terms still require checking. Complete weight release and executable reproduction were not confirmed.

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

<a id="method-rgmem"></a>
### M28. RGMem · Hierarchical user-profile evolution

[RGMem: Renormalization Group-inspired Memory Evolution for Language Agents](https://arxiv.org/html/2510.16392v3) — arXiv records ICML 2026 acceptance; inspected v3, June 2, 2026. The earlier “…Group-based…User Profile” title is the same paper.

**Verified / actual reading scope:** 2026-11-01; v3 relevant §3 methodology passages and Appendix B.1 evaluation protocol; arXiv version/acceptance record, author README, and repository root. Selected passages, not a line-by-line full-paper review; no installation, execution, or experimental reproduction.

- **Mechanism:** Aggregates episodic facts and user inferences into a hierarchical graph, separating rapidly changing evidence from slower traits through thresholded updates and multi-scale retrieval.
- **Evidence/limits:** LOCOMO uses model judging; PersonaMem-128k uses multiple-choice accuracy, averaged over three runs. External-memory evolution is not continual backbone training; neither benchmark proves profile truth, privacy or long-term human utility.
- **Resources:** [Author implementation](https://github.com/fenhg297/RGMem), MIT-labeled; requires components including Elasticsearch, Neo4j and Redis. Not executed.

<a id="method-me-agent"></a>
### M29. Me-Agent · Experience and hierarchical preference memory

[Me-Agent](https://arxiv.org/html/2601.20162v1) — same paper as B42; do not count twice.

**Verified / actual reading scope:** 2026-11-01; v1 §4.2–4.4 methodology, relevant §5.1–5.2 settings/results passages, and Limitations; repository root and README. Selected passages, not a line-by-line full-paper review; no installation, execution, or experimental reproduction.

- **Mechanism:** VLM-scored trajectories yield natural-language experiences for prompts; app-specific memory supplies workflows and content preferences. The method describes parameter-free adaptation, not personalized backbone fine-tuning.
- **Evidence/limits:** Evaluated on User FingerTip and general mobile tasks. UI changes can invalidate stored positions/workflows; situational factors such as current location remain limited. Inferring a habitual choice does not establish authorization for a new action.
- **Resources:** [Author implementation](https://github.com/Gianthaha/personal-mobile-agent); benchmark-count, packaging and licensing-scope caveats are shared with B42.

<a id="method-ppp"></a>
### M30. PPP · Learning proactive clarification and personalized interaction

[Training Proactive and Personalized LLM Agents](https://arxiv.org/html/2511.02208v2) — COLM 2026; v2, 2026-08-23. UserVille is cross-listed as B43, the same paper.

**Actual reading scope:** v2 §§4–8, Table 1, Appendix A; version record, conference listings, author README/tree/LICENSE. Targeted reading, not a complete line-by-line review; no execution.

- **Mechanism:** GRPO jointly optimizes task outcomes, clarification burden and preference adherence with preference-conditioned simulated users. This is not persistent individual memory or lifelong profiling.
- **Evidence/boundary:** Separate automated evaluation from the human study described in B43. Additional questions can increase human effort; simulator-based burden does not directly establish human experience.
- **Resources:** [Author code](https://github.com/sunnweiwei/PPP-Agent) is Apache-2.0. Linked weights/data pages were inaccessible through the inspection tool; download availability and asset licenses remain unverified, not proven absent. README additionally requires a vLLM bias patch. Repository licensing does not automatically cover models, data or upstream benchmarks.

<a id="method-puma"></a>
### M31. PUMA · Learning tool parameters from behavioral histories

[Large Language Models Empowered Personalized Web Agents](https://arxiv.org/html/2410.17236v2) — WWW 2025; v2, 2025-03-24. PersonalWAB is cross-listed as B44, the same paper.

**Actual reading scope:** §§3, 5–6, Table 5, Appendices A.3/B; version record, project page, README, data directory and LICENSE. Targeted reading; no execution.

- **Mechanism:** Retrieves behavioral histories, retains task-specific fields, and learns function parameters through heuristic SFT and result-ranked DPO.
- **Evidence/boundary:** Table 5 overall function/result accuracy is .994/.406, versus .994/.373 without task-specific memory; recommendation result accuracy remains .054. These metrics are not real-world task-success rates. Shopping and simulator boundaries appear in B44.
- **Resources:** [Author repository](https://github.com/HongruCai/PersonalWAB) and data directory are readable. Root license is **CC BY-NC 4.0**, with separate MIT terms for inherited tau-bench portions. Released PUMA checkpoints and full-data integrity were not verified. Paper, code/data, Amazon and model terms must remain distinct.

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

<a id="method-rlpf"></a>
### M43. Prediction-guided user-profile compression

[RLPF](https://arxiv.org/html/2409.04421v2) — AAAI 2025; inspected v2, January 17, 2025.

**Read:** §§2–5, Appendix I task definitions, version record and resource search; not executed.

- Trains a history summarizer using future-activity prediction and length rewards; prediction selects the actual next item against three randomly selected negative options, rather than searching an unrestricted catalog.
- Offline evaluation uses MovieLens 2015/2003, Amazon reviews and Google Local reviews; some transfer tasks regress. It does not establish continual profile updating, action execution or privacy protection.
- Official implementation/new-data release not verified; paper licensing does not license upstream assets.
- **Deduplication:** Conference and arXiv versions count once.

<a id="method-ld-agent"></a>
### M44. Event memory and personas for long-term dialogue

[Hello Again!](https://aclanthology.org/2025.naacl-long.272/) — NAACL 2025; publication PDF; arXiv alias `2406.05925`.

**Read:** §§3–4, limitations, Appendix A, official README and license; not executed.

- Combines event memory, topic retrieval and user/agent personas.
- MSC role-play and generated CC dialogues do not establish authentic longitudinal utility. Text-overlap metrics, persona-classification accuracy and human response-quality ratings are separate measures, not action-success rates.
- [Implementation](https://github.com/leolee99/LD-Agent) is MIT; linked Drive assets unverified; CC release remains a README TODO.
- **Deduplication:** One publication, including its arXiv version.

<a id="method-aloe"></a>
### M45. Interactive individual-preference alignment

[Aligning LLMs with Individual Preferences via Interaction](https://aclanthology.org/2025.coling-main.511/) — COLING 2025; method inspected in [v2](https://arxiv.org/html/2410.03642v2), December 15, 2024.

**Read:** §§2–5, publication metadata and repository; no full version comparison or execution.

- Uses generated preference conversations for SFT and DPO.
- Evaluation uses 100 personas and ten-turn interactions with GPT-4o as both simulated user and alignment judge. Human rating checks are not longitudinal user trials; this does not validate continual online training or tool execution.
- [Code/data directories](https://github.com/ShujinWu-0814/ALOE) are accessible; no root license found; checkpoints unverified.
- **Deduplication:** ALOE is the same paper’s benchmark. Cross-link if needed; do not count twice.

<a id="method-ptool"></a>
### M46. PTool · Synthetic training for personalized tool invocation

Same [paper](https://arxiv.org/html/2505.04072v1) and reading scope as B51.

- **Mechanism:** structured API/profile synthesis, role-play query/solution generation, rule/model validation, then LoRA SFT.
- **Evidence/boundary:** Qwen2.5-7B overall accuracy 7.38%→26.78%; generated-call evaluation, not live tool execution.

<a id="method-h2memory"></a>
### M47. H²Memory · Concrete and abstract personal memory

Same [paper](https://arxiv.org/html/2511.13410v2) and reading scope as B52; count once, including PAL-Set alias.

- **Mechanism:** four components—Log Graph, Background, Topic Outline and Principle—with updates and linked retrieval.
- **Evidence/boundary:** improves the listed PAL-Bench baselines; simulated/judge-rated performance is not demonstrated real-user satisfaction or autonomous action success.

<a id="method-raise"></a>
### M48. RAISE · Selective acquisition of personal safety context

Same [paper](https://arxiv.org/html/2505.18882v5) and reading scope as B55; count once.

- **Mechanism:** offline LLM-guided MCTS caches acquisition paths; online retrieval guides questions and sufficiency/abstention decisions.
- **Boundary:** evaluated with benchmark contexts; not evidence of safe real-world counseling or validated permission to collect sensitive attributes.

<a id="method-prelude"></a>
### M49. PRELUDE / CIPHER · Learning context-dependent preferences from edits

- **Paper/version:** [Aligning LLM Agents by Learning Latent Preference from User Edits](https://arxiv.org/html/2404.15269v3), NeurIPS 2024; arXiv v3, 2024-11-23. PRELUDE is the framework and CIPHER its algorithm: one paper.
- **Mechanism:** Infer textual preferences from output edits, retrieve and aggregate preferences associated with similar contexts, and condition future generation without fine-tuning.
- **Evidence:** Summarization and email tasks use 200 rounds with GPT-4 simulated editing users and three seeds. Best configurations reduce cumulative token edit distance by approximately 31%/73% against no learning. On summarization only, seven human judges assess 15 pairs per comparison; three human editors follow assigned preferences.
- **Limits:** These human assessments are not natural longitudinal online personalization. Preferences are prescribed by source category; edit distance is not measured time saved or satisfaction. An oracle gap remains.
- **Resources/read scope:** [Official repository](https://github.com/gao-g/prelude), MIT; underlying dataset rights remain separate. Read v3 §§4.1–4.4, mechanism/metric passages, proceedings metadata and repository resource page. No reproduction.

<a id="method-curio"></a>
### M50. CURIO · Rewarding improvements in the user model

- **Paper/version:** [Enhancing Personalized Multi-Turn Dialogue with Curiosity Reward](https://arxiv.org/html/2504.03206v3), [NeurIPS 2025](https://proceedings.nips.cc/paper_files/paper/2025/hash/e48d5af30c95be08762489c5141f7fbc-Abstract-Conference.html); arXiv v3, 2025-10-02.
- **Mechanism:** Add turn-level intrinsic rewards for better user-type beliefs to multi-turn RLHF, comparing accuracy, entropy and potential-difference rewards.
- **Evidence:** Exercise attributes map deterministically to eight strategies. Over 200 simulated conversations, best DiffAcc reaches 87.5%, versus 68.5% MTRLHF and 54% SFT. Education uses two prescribed preferences. Ten student judges evaluate generated dialogues, not live tutoring experiences.
- **Limits:** Static predefined types and LLM simulators constrain generalization; some entropy rewards favor one type. Human personalization preference for DiffLogAcc over MTRLHF is approximately 76%, with a discrepancy between appendix 152/200 and table 75.75%. Quality preference is 90/200, p=.179—not evidence of equivalence. No demonstrated learning or health outcomes.
- **Resources/read scope:** [Author project page](https://sites.google.com/cs.washington.edu/curio) verified; official code, weights, dataset release and artifact licenses not verified. Read methods, §§4–5, limitations, Appendix B.1–B.3 and proceedings metadata. No reproduction.

<a id="method-grounded-memory"></a>
### M51. A Grounded Memory System · Visual observations into entity memory

- **Paper/version:** [A Grounded Memory System For Smart Personal Assistants](https://arxiv.org/html/2505.06328v1), arXiv v1, 2025-05-09; ESWC 2025 TEXT2KG workshop, not the ESWC main conference.
- **Mechanism:** GPT-4o captions overlapping video windows and labels entities; Neo4j stores embedded memory notes and temporal/entity relationships. A retrieval agent selects semantic search, PageRank expansion or text-to-Cypher.
- **Evidence:** An iPhone home-video prototype with illustrative question/answer outputs—not a controlled comparison, participant study or benchmark. Author-labeled correct examples do not establish 100% evaluated accuracy.
- **Limits:** Does not demonstrate superiority over standard RAG, reliable long-term entity consistency or validated dementia care. Scaling, long-term disambiguation and additional modalities remain future work.
- **Resources/read scope:** Official code/data release and artifact licenses not verified. Read §§3–5 and arXiv version/workshop metadata. No reproduction.

## New group: Human studies, not benchmarks

<a id="method-iotgpt"></a>
### M52. IoTGPT

**Method: personalized device execution with reusable task memory**

[Leveraging LLMs for Efficient and Personalized Smart Home Automation](https://arxiv.org/abs/2601.04680) · **arXiv v1, January 8, 2026**; archival venue unconfirmed.

Combines a Decompose–Derive–Refine pipeline, hierarchical task memory and environmental-property preferences for SmartThings control. Evaluation uses **97 tasks and 26 simulated devices**; warm-start testing paraphrases already learned tasks. Fifteen real participants join short studies, but preferences originate from **100 GPT-4o-generated logs**, not their personal histories. This is not evidence of longitudinal household personalization. Conflicting preferences and device side effects remain limitations; **users must screen unsafe or hallucinated commands**, with automated safeguards left to future work. No official implementation/license verified. **Read:** system, implementation, comparative evaluation, both user studies and limitations; no reproduction.

<a id="method-gaap"></a>
### M53. GAAP

**Method: runtime information-flow and disclosure permissions**

[An AI Agent Execution Environment to Safeguard User Data](https://arxiv.org/abs/2604.19657) · **arXiv v3, September 24, 2026**; archival venue unconfirmed.

A restricted-plan interpreter and IFC combine persistent private-data, permission and disclosure stores. Confidentiality applies against malicious models/providers and services, subject to correct enforcement, user permissions and verified annotations. **Secrets placed directly in prompts, prompt timing metadata and integrity are excluded.** The custom 20-task/seven-attack suite reports no successful disclosures; AgentDojo/AgentDyn runs approve every disclosure and therefore assess utility, not privacy. These are not human usability studies; cost and latency overheads are substantial. [Public repository](https://github.com/rssta/gaap), but no LICENSE found and GitHub reports no license. **Read:** v3 threat model/design/evaluation/discussion and repository documentation/metadata; no security audit.

<a id="method-alignxplore"></a>
### M54. AlignXplore · Updating explicit preferences from behavioral signals

[Extended Inductive Reasoning for Personalized Preference Inference from Behavioral Signals](https://arxiv.org/html/2505.18071v2) — arXiv v2, 2025-07-07; venue unverified.

**English review:** Converts behavioral examples into explicit preferences using synthetic cold-start training and GRPO; streaming inference reuses the previous summary. AlignX/P-Soups tests mainly use preference pairs. Metrics distinguish Acc_jud (preference judging), Acc_gen (preference-guided generation), and GPT-4 win rate; “online evaluation” uses GPT-4 judgments, not live users. The main setting uses two four-example rounds; §4.4 also tests simulated reversals among eight pairs, and §4.5 extends efficiency testing to round four, totaling 16 signals. These do not establish lifelong adaptation; real-user validation is missing. Privacy statements provide no formal guarantee. Official code is accessible, but a project root license was not confirmed; the paper’s CC BY-NC-ND license does not establish code licensing.

**Reading scope:** v2 §3, §4 evaluation setup and streaming experiments, Appendices C–D; official README and root listing. Targeted methods, evaluation and limitations reading; official README/root, not an exhaustive full-paper review.

<a id="method-psg-agent"></a>
### M55. PSG-Agent · Staged guardrails for user-dependent risks

[PSG-Agent: Personality-Aware Safety Guardrail for LLM-based Agents](https://arxiv.org/html/2509.23614v1) — arXiv v1, 2025-09-28; venue unverified.

**English review:** Mines profiles and compiles contextual safety criteria for plan, tool, response and memory-write checks. Its approximately 2,900 cases and histories are largely GPT-4o-generated from 132 manual seeds. Four experts checked 200 cases, each rating 50 distinct examples—not all four rating every case. ALLOW/REFUSE classification uses accuracy, precision, recall and F1; a separate three-model majority vote scores safety/helpfulness, with a 100-case human comparison. Evidence concerns synthetic profile-sensitive judgments, not real clinical/financial outcomes or proven long-term protection. Runtime gates offer no formal safety/privacy guarantee. The linked anonymous repository returned no readable content; completeness and licensing remain unverified.

**Reading scope:** §3–5, threat model, components, human review and LLM-judge setup; anonymous repository entry point. Targeted benchmark, framework and evaluation reading; repository landing-page check, no code audit.

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



