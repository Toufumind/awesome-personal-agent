# Personal agent papers & benchmarks

[中文](PAPERS.md) · [Main list](../README.en.md)

**Understand what was measured before comparing scores.** This guide separates evaluations / benchmarks from methods / systems, and distinguishes direct personal-context research, transferable general memory / execution capabilities, and specific privacy / security risks.

Literature and resource check: **2026-10-31**. **63 distinct papers**: 42 evaluation entries and 29 method entries. Proactive Agent, MemoProAgent, PbP/InTU, Ask-before-Plan/CEP, PersonalAlign/HIM-Agent, PEToolLLM/PEToolLLaMA, MemGuide/MS-TOD, and Me-Agent/User FingerTip each contribute a benchmark and a method; each paper is counted once. Sources are paper abstracts and the explicitly identified passages below, author project pages, official repositories, and dataset cards. **No installation, independent benchmark run, model training, or security audit was performed.** This is a selective reading guide, not a comprehensive survey, latest-paper feed, or product ranking.

**Entry checks:** B25–B42 and M16–M29 were checked on 2026-11-01; earlier entries retain their original check dates.

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

**Checked / reading scope:** 2026-11-01; abstract, §1, §4.2 and result tables; draft, not reproduced.

- **Input → output:** User models, personal queries and travel information → personalized itineraries.
- **Measures:** Delivery, constraint and final pass rates; separately, judge preference between personal and generic plans.
- **Limits:** Judge preference is neither human satisfaction nor constraint satisfaction; some personalized settings reduce constraint scores. Not longitudinal planning.
- **Resources:** [Paper](https://aclanthology.org/2024.emnlp-industry.37.pdf). No verified official TravelPlanner+ release located; the original TravelPlanner repository is not a substitute.

<a id="benchmark-pbp"></a>
### B29. PbP · Inferring planning preferences from demonstrations

[Inferring the Unspoken: Aligning Embodied Agents with Implicit Preferences](https://arxiv.org/abs/2502.00858v4) — First submitted 2025; v4, 2026-09-08, marked EMNLP 2026 on arXiv. Earlier title: Learning to Plan with Personalized Preferences. Method: M17.

**Checked / reading scope:** 2026-11-01; v4 abstract and version history only; preliminary draft.

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

**Checked / reading scope:** 2026-11-01; abstract, evaluation in §5.1–5.2 and Appendix B.2–B.3; official README; draft.

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

**Checked / reading scope:** 2026-11-01; abstract, §4.1 metrics and official README; draft.

- **Input → output:** Scoped delegation and sandbox state → action trajectories; 286 tasks.
- **Measures:** Completion and authorization violations, using trajectories and state evidence.
- **Limits:** Delegation benchmark, not a personalized planning method; simulated services and judges do not establish deployment risk.
- **Resources:** [Official repository](https://github.com/PEACH-Research-Lab/AuthorizationBench). README declares MIT for original artifacts, excluding third-party sources. Released verdicts cover 6,864 runs, but only 4,981 original trajectories remain. Not run.

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

**Checked / reading scope:** 2026-11-01; v4 abstract only; preliminary draft.

- **Mechanism:** Express preferences inferred from multimodal demonstrations in language, then condition action plans on them.
- **Limits:** An interpretable intermediate representation does not guarantee correct inference. Evaluation, resources and reading limitations: [B29](#benchmark-pbp).

<a id="method-cep"></a>
### M18. CEP · Separate clarification, execution and planning

[Ask-before-Plan](https://aclanthology.org/2024.findings-emnlp.636/) — Same paper as B30; count once.

**Checked / reading scope:** 2026-11-01; abstract, evaluation setup, Appendix B.3 and official README training / inference entries; draft.

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



