# Personal agent papers & benchmarks

[中文](PAPERS.md) · [Main list](../README.en.md)

**Understand what was measured before comparing scores.** This guide separates evaluations / benchmarks from agent methods / systems, and distinguishes research directly concerned with personal context from general capabilities transferable to personal assistants.

Initial source check: **2026-10-31**. **21 distinct papers**: 13 evaluation entries and 9 method entries. Proactive Agent contributes both a benchmark and a method, so its paper is counted once. Sources are paper abstracts and the explicitly identified passages below, author project pages, official repositories, and dataset cards. This is a literature and resource check: **no installation, independent benchmark run, or security audit was performed**. It is a selective reading guide, not a comprehensive survey, latest-paper feed, or product ranking.

**Reading scope:** Each entry records the abstract, relevant passages, and resource pages actually consulted. No claim is made that every paper was read end to end. Translation is not an additional verification.

Years identify the publication or preprint version listed. Original task counts do not necessarily describe current code. “Public” means an official resource entry point was found, not that commercial reuse is permitted, dependencies still install, or results are immediately reproducible.

## Contents

- [Start with a research question](#reading-paths)
- [Evaluation: personal context, memory, and proactivity](#personal-evaluation)
- [Evaluation: task execution and interaction](#execution-evaluation)
- [Methods: memory and persistent state](#memory-methods)
- [Methods: planning, tools, reflection, and proactivity](#agent-methods)
- [Comparison and reproducibility](#reproducibility)
- [Sources and rights](#sources-and-rights)

<a id="reading-paths"></a>
## Start with a research question

| Research question | Start here | Still needs separate testing |
| --- | --- | --- |
| Does it remember what the user said, including updates? | LongMemEval, LoCoMo | Deletion, correction, user isolation, real longitudinal use |
| Does the answer fit this person's preferences? | LaMP, PersonaMem | Open-ended response quality and actual user satisfaction |
| Does memory actually change tool arguments? | Mem2ActBench | Execution, side effects, and authorization |
| When should it help proactively or stay quiet? | ProactiveBench / Proactive Agent | Human acceptance, interruption cost, undo, and permission |
| Can it complete multi-app tasks? | AppWorld, WebArena, OSWorld, AndroidWorld | Real accounts, environment changes, irreversible actions |
| Does it reliably follow a workflow across repeated runs? | τ-bench | Simulated versus real users and process-level safety |
| How can a persistent assistant be structured? | MemGPT, MemoryBank, A-MEM, Mem0; then ReAct / Reflexion | Permissions, scheduling, observability, maintenance cost |

<a id="personal-evaluation"></a>
## Evaluation A: personal context, memory, and proactivity

These benchmarks directly involve user history, preferences, or proactive help. **None alone evaluates an entire personal agent.**

### B1. LaMP · Personalized language tasks

[LaMP: When Large Language Models Meet Personalization](https://aclanthology.org/2024.acl-long.399/) — ACL 2024.

**Checked / reading scope:** 2026-10-31; Paper abstract and §2.3 metric passages; official README licensing notes and data-download page.

- **Input → output:** Task input and the user's historical items → a personalized label or text. The paper covers three classification and four generation tasks.
- **Measures:** Accuracy / F1, rating MAE / RMSE, and generation ROUGE; user-based and time-based splits distinguish generalization settings.
- **Limits:** Tests personalized retrieval and generation, not multi-step tool execution or longitudinal use with real users.
- **Resources:** [Official code](https://github.com/LaMP-Benchmark/LaMP), [data](https://lamp-benchmark.github.io/download). Code and construction methods use CC BY-NC-SA 4.0; underlying datasets retain their own licenses.

### B2. LoCoMo · Long-term conversational memory

[Evaluating Very Long-Term Conversational Memory of LLM Agents](https://aclanthology.org/2024.acl-long.747/) — ACL 2024.

**Checked / reading scope:** 2026-10-31; Paper abstract, §4 QA metrics, relevant §6 summary-evaluation and §8 limitations passages; official README data notes and LICENSE.

- **Input → output:** Timestamped, multi-session conversations → QA, event summaries, or multimodal dialogue continuation. Model-generated dialogues are human-checked and edited.
- **Measures:** Category-level QA F1; ROUGE and atomic-fact measures for summaries; separate multimodal relevance measures. These are not one interchangeable “memory score.”
- **Limits:** The current official release contains **10 long conversations**, not the earlier 50-conversation release. Offline history is not months of real assistant use.
- **Resources:** [Code / data](https://github.com/snap-research/locomo). Original images are not distributed; URLs and related information are provided. [License](https://github.com/snap-research/locomo/blob/main/LICENSE.txt): CC BY-NC 4.0.

### B3. LongMemEval · Cross-session recall, updates, and abstention

[LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://arxiv.org/abs/2410.10813) — 2024 preprint; ICLR 2025.

**Checked / reading scope:** 2026-10-31; Paper abstract and §3.3 evaluation passages; official README data-format/evaluation notes and cleaned dataset card.

- **Input → output:** Timestamped user–assistant history and a question → an answer or abstention. Its 500 questions cover extraction, cross-session / temporal reasoning, updates, and abstention.
- **Measures:** LLM-judged answers, with optional retrieval Recall@k / NDCG@k. S, M, and oracle expose different history lengths and evidence.
- **Limits:** Retrieval recall is not answer accuracy; constructed-history QA does not establish task execution, deletion, or continuous availability.
- **Resources:** [Evaluation code](https://github.com/xiaowu0162/LongMemEval), [official cleaned data](https://huggingface.co/datasets/xiaowu0162/longmemeval-cleaned). Pin the data revision and judge version.

### B4. PersonaMem · Evolving user profiles

[Know Me, Respond to Me: Benchmarking LLMs for Dynamic User Profiling and Personalized Responses at Scale](https://arxiv.org/abs/2504.14225) — COLM 2025; this entry covers the original benchmark / v1 data.

**Checked / reading scope:** 2026-10-31; Original-paper revision: §2 task definition and relevant §4 results passages; official README data format and v1 dataset card.

- **Input → output:** Synthetic multi-session history with changing preferences and a new-scenario question → one of four candidate responses.
- **Measures:** Selection accuracy across seven query types, context lengths, and distances from preference mentions; separates recall, updates, and preference transfer.
- **Limits:** Four-choice accuracy is not open-ended personalized response quality. Synthetic personas are not longitudinal human participants. Do not mix with PersonaMem-v2 data.
- **Resources:** [Official code](https://github.com/bowen-upenn/PersonaMem), [v1 data](https://huggingface.co/datasets/bowen-upenn/PersonaMem-v1), including 32k, 128k, and 1M context settings.

### B5. Mem2ActBench · From memory to tool arguments

[Mem2ActBench: A Benchmark for Evaluating Long-Term Memory Utilization in Task-Oriented Autonomous Agents](https://aclanthology.org/2026.acl-long.370/) — ACL 2026.

**Checked / reading scope:** 2026-10-31; Paper abstract, relevant §4.1 experimental-setup and §5.4 tool-selection passages; official README, root listing, and data-directory entry points.

- **Input → output:** Historical memory, an implicitly constrained request, and tool schemas → tool selection and arguments. The paper constructs 400 memory-dependent tasks.
- **Measures:** Argument matching / F1, tool selection, and whole-call matching. Main experiments supply the correct tool; separate experiments add distractor tools.
- **Limits:** Correct arguments are not a completed real transaction. Main results should not be presented as open-ended tool-selection performance.
- **Resources:** [Official construction code / data directories](https://github.com/Cantaloupe-M/Mem2ActBench). No explicit root LICENSE was found. Check upstream ToolACE, BFCL, OASST1, and repository permissions before reuse.

### B6. ProactiveBench (Lu et al.) · When to offer help

[Proactive Agent: Shifting LLM Agents from Reactive Responses to Active Assistance](https://arxiv.org/abs/2410.12361) — 2024 preprint; ICLR 2025.

**Checked / reading scope:** 2026-10-31; Paper abstract and evaluation-metric passages; official README system overview, data statistics, and evaluation entry points.

- **Input → output:** User activity and environment events → a proposed assistance task, or no proposal. The paper includes 6,790 events across coding, writing, and daily-life settings.
- **Measures:** Precision, recall, F1, and false alarms under acceptance / rejection judgments; automated evaluation uses a learned reward model.
- **Limits:** Appropriate offers are not long-term human satisfaction or task completion. A proactive suggestion does not authorize execution.
- **Resources:** [Code, data, evaluation](https://github.com/thunlp/ProactiveAgent). Other papers use the same benchmark name; this entry specifically means Lu et al. See M9 for the method.

<a id="execution-evaluation"></a>
## Evaluation B: task execution and interaction

These can test a personal assistant's ability to act, but most are **general-agent, web / GUI, or service-domain benchmarks**, not personal-specific evaluations. AppWorld includes simulated personal apps and people, but not longitudinal personalization with real users.

### B7. AssistantBench · Realistic web information tasks

[AssistantBench: Can Web Agents Solve Realistic and Time-Consuming Tasks?](https://aclanthology.org/2024.emnlp-main.505/) — EMNLP 2024.

**Checked / reading scope:** 2026-10-31; Paper abstract and relevant §3.4 automatic-evaluation passages; official project page, code entry point, and dataset card.

- **Input → output:** A task requiring web search and synthesis → a string, number, or structured answer. The original benchmark has 214 tasks.
- **Measures:** Answer accuracy, answer rate, precision, and exact match, rather than an agent's own completion claim.
- **Limits:** Primarily information gathering, not writes to real accounts. Web changes and answer freshness affect reproducibility; persistent preferences are not tested.
- **Resources:** [Project](https://assistantbench.github.io/), [code](https://github.com/oriyor/assistantbench), [data](https://huggingface.co/datasets/AssistantBench/AssistantBench).

### B8. GAIA · General-assistant problem solving

[GAIA: a benchmark for General AI Assistants](https://arxiv.org/abs/2311.12983) — 2023 preprint.

**Checked / reading scope:** 2026-10-31; Paper abstract and relevant §3.2 evaluation passages; official dataset-card task, split, gating, and redistribution notes.

- **Input → output:** A natural-language question, sometimes with files / multimodal material → a short, verifiable answer. The paper contains 466 questions at three difficulty levels.
- **Measures:** Type-aware normalized, near-exact answer matching; tasks involve browsing, tools, multimodality, and reasoning.
- **Limits:** Single-question correctness is not personalization, background proactivity, or long-horizon reliability. Development and hidden-answer test sets differ.
- **Resources:** [Official dataset card and leaderboard entry point](https://huggingface.co/datasets/gaia-benchmark/GAIA). Access is gated; the authors prohibit resharing the dataset in crawlable form.

### B9. AppWorld · A sandbox for cross-app personal tasks

[AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents](https://arxiv.org/abs/2407.18901) — ACL 2024.

**Checked / reading scope:** 2026-10-31; Paper task overview and relevant §3.2 evaluation / §7 limitations passages; official project page, README, and licensing notes.

- **Input → output:** User instruction, simulated initial app state, and API documentation → interactive code / calls changing state. The paper has 750 tasks across nine apps.
- **Measures:** Database-state tests; TGC requires all tests for a task, while SGC requires success on every task variant in a scenario.
- **Limits:** Simulated APIs are not live services or GUIs. The original benchmark differs from later AppWorld-UL user-in-the-loop tasks.
- **Resources:** [Project](https://appworld.dev/appworld/), [code / data download workflow](https://github.com/StonyBrookNLP/appworld). Protected content has additional encrypted-redistribution requirements: [license notes](https://github.com/StonyBrookNLP/appworld#-license).

### B10. τ-bench · Tools, users, and domain rules

[τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](https://arxiv.org/abs/2406.12045) — 2024 preprint.

**Checked / reading scope:** 2026-10-31; Paper abstract, §3 reward/pass^k definitions, and relevant §6 discussion passages; official README outdated-task and migration warnings.

- **Input → output:** Simulated user dialogue, domain policies, and APIs → conversation and tool actions. Original domains are airline and retail services.
- **Measures:** Final database versus target state, plus required information in replies. **pass^k measures success on all k repeated trials, unlike pass@k's at-least-one-success criterion.**
- **Limits:** Service-agent workflows are not persistent personal assistance. Correct final state does not establish process-level compliance; user simulation affects results.
- **Resources:** [Original code / data](https://github.com/sierra-research/tau-bench). The official README now labels these tasks outdated and directs readers to τ³-bench. Distinguish historical reproduction from newer versions.

### B11. WebArena · Reproducible web interaction

[WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854) — 2023 preprint, revised 2024.

**Checked / reading scope:** 2026-10-31; Paper abstract and relevant §3 task/evaluation passages; official README version, environment, and implementation notes.

- **Input → output:** High-level intent and web observations → browser actions, final page state, or an answer. The paper contains 812 tasks.
- **Measures:** Functional outcomes: answers, navigation destinations, or page state, rather than a fixed click sequence.
- **Limits:** Self-hosted sites support reproducibility but do not cover every live website, login obstacle, or ongoing personalization. Results are not universal browser success rates.
- **Resources:** [Official code, environments, evaluation](https://github.com/web-arena-x/webarena). Pin task revisions and site images before comparing runs.

### B12. OSWorld · Desktop and cross-app workflows

[OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://arxiv.org/abs/2404.07972) — 2024.

**Checked / reading scope:** 2026-10-31; Paper abstract and introduction task/state-evaluation overview; official project-page version and resource notes.

- **Input → output:** A task, initial desktop / file state, and screenshots or accessibility trees → computer actions and final artifacts. The paper has 369 tasks.
- **Measures:** Task-specific execution-based evaluators; observation modes, action spaces, and step budgets affect comparability.
- **Limits:** Not a long-term user-relationship test; depends on VM / software versions. Original OSWorld, OSWorld-Verified, and OSWorld 2.0 differ; some cloud-document tasks require extra setup.
- **Resources:** [Official project and version links](https://os-world.github.io/), [code / tasks](https://github.com/xlang-ai/OSWorld).

### B13. AndroidWorld · Parameterized mobile tasks

[AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents](https://arxiv.org/abs/2405.14573) — 2024 preprint, revised 2025.

**Checked / reading scope:** 2026-10-31; Paper abstract, §3.4 state-based rewards, and Appendix A limitations passages; official project page and README.

- **Input → output:** Natural-language task, emulator state, and screen / UI tree → Android actions. There are 116 base tasks across 20 apps with randomized parameters.
- **Measures:** Initialization, success checks, and teardown inspect device state; parameter variation supports robustness testing.
- **Limits:** 116 is not the total number of randomized instances. Primarily open-source / system apps; generalization to commercial apps, other devices, or Chinese interfaces is unproven.
- **Resources:** [Project](https://google-research.github.io/android_world/), [environment / task code](https://github.com/google-research/android_world).

<a id="memory-methods"></a>
## Methods A: memory and persistent state

These entries describe reusable mechanisms, not research prototypes certified as reliable personal-assistant products.

### M1. MemoryBank · Updating, reinforcement, and forgetting

[MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://arxiv.org/abs/2305.10250) — 2023 preprint.

**Checked / reading scope:** 2026-10-31; Paper abstract; official README mechanism, evaluation-data, and model notes, plus the LoRA release page.

- **Idea:** Store / retrieve conversations, summarize user information, and strengthen or fade memories using a forgetting-curve-inspired mechanism.
- **Relevance and limits:** Directly targets long-term conversational companionship. SiliconFriend is not a tool-execution system, and its experiments are not clinical evidence for psychological services.
- **Resources:** [Code and Chinese / English evaluation data](https://github.com/zhongwanjun/MemoryBank-SiliconFriend), [ChatGLM / BELLE LoRA checkpoint release](https://github.com/zhongwanjun/MemoryBank-SiliconFriend/releases/tag/LoRA_checkpoint). Adapters and base models are different artifacts with separate permissions.

### M2. MemGPT · Hierarchical memory and context management

[MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) — 2023 preprint, revised 2024.

**Checked / reading scope:** 2026-10-31; Paper abstract; research project page, data entry point, Letta README current-source/historical-version notes, and the letta-code entry point.

- **Idea:** Borrow OS-style memory hierarchies to move information between limited context and external memory, with control flow for continued execution.
- **Relevance and limits:** Includes multi-session chat and long-document experiments. Virtual context does not mean infinite, lossless, or cost-free memory.
- **Resources:** [Research page / experimental data entry point](https://research.memgpt.ai/), [historical MemGPT / Letta entry point](https://github.com/letta-ai/letta), [current Letta Code source](https://github.com/letta-ai/letta-code). The legacy entry point directs readers to letta-code and keeps the retired V1 server on its archive branch. Reproduction requires locating the original version; neither the current product nor retired V1 automatically matches the paper implementation.

### M3. A-MEM · Linked notes and evolving memory

[A-MEM: Agentic Memory for LLM Agents](https://arxiv.org/abs/2502.12110) — NeurIPS 2025.

**Checked / reading scope:** 2026-10-31; Paper abstract and relevant §4.2 dataset/metric passages; purpose statements in the two official repositories.

- **Idea:** Organize memory as Zettelkasten-inspired notes, generate attributes and links, and revise existing memory representations as information arrives.
- **Relevance and limits:** A structure for associative assistant memory. Long-dialogue QA does not establish real task completion or consistently correct memory edits.
- **Resources:** [Paper evaluation code](https://github.com/WujiangXu/A-mem), [integrable system](https://github.com/WujiangXu/A-mem-sys). These repositories have different purposes; this is an external-memory method, not a new foundation model.

### M4. Mem0 · Extraction, consolidation, and retrieval

[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://arxiv.org/abs/2504.19413) — 2025 arXiv paper version.

**Checked / reading scope:** 2026-10-31; 2025 paper abstract; current official README and research page, used to distinguish the paper from later project changes.

- **Idea:** Extract important conversational information, consolidate updates, and retrieve it; the paper also explores graph memory.
- **Relevance and limits:** Supports cross-session personal context. LoCoMo accuracy, latency, and token measurements cannot be generalized to every task or deployment.
- **Resources:** [Official project code](https://github.com/mem0ai/mem0). Code, hosted services, and algorithms continue evolving. This entry covers the 2025 approach, not current marketing scores presented as independent reproduction.

<a id="agent-methods"></a>
## Methods B: planning, tools, reflection, and proactivity

### M5. Generative Agents · Memory, reflection, and planning

[Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) — 2023.

**Checked / reading scope:** 2026-10-31; Paper abstract; official README simulation environment, code scope, and model-call notes.

- **Idea:** Record experiences, retrieve memories, form higher-level reflections, and plan behavior; studied in a town with 25 simulated characters.
- **Relevance and limits:** Offers patterns for persistent state and plans. Its goal is believable human-behavior simulation, not completing authorized tasks for real users.
- **Resources:** [Official simulator, environment, and replay instructions](https://github.com/joonspk-research/generative_agents). Uses external model calls; not a standalone model-weight release.

### M6. ReAct · Interleaving reasoning and action

[ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) — 2022 preprint; ICLR 2023.

**Checked / reading scope:** 2026-10-31; Paper abstract and arXiv version notes; official README and code/prompt directory listing.

- **Idea:** Interleave task reasoning and tool actions, using returned observations to revise subsequent steps.
- **Relevance and limits:** A foundation for general tool-use loops. Original experiments cover QA, fact verification, and interactive environments, not persistent memory, permissions, or continuous scheduling.
- **Resources:** [Official code, prompts, and experimental notebooks](https://github.com/ysymyth/ReAct). Primarily a prompting implementation, not a complete personal assistant.

### M7. Reflexion · Carrying feedback into another attempt

[Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) — NeurIPS 2023.

**Checked / reading scope:** 2026-10-31; Paper abstract; official README experiment, log, and execution notes.

- **Idea:** Turn task feedback into verbal reflection stored in episodic memory for later attempts, without directly updating model weights.
- **Relevance and limits:** Useful for retries and experience memory. Gains depend on feedback quality and retry budget; reflection does not guarantee correction or continual improvement.
- **Resources:** [Official code, logs, and demos](https://github.com/noahshinn/reflexion). Original evaluations cover decision-making, reasoning, and coding, not long-term personal assistance.

### M8. Toolformer · Learning when to call tools

[Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) — 2023 preprint.

**Checked / reading scope:** 2026-10-31; Paper abstract and §7 limitations; Meta publication page and its available resource links.

- **Idea:** Use a few API demonstrations to generate candidate calls, filter by their benefit to subsequent language prediction, and train on the augmented corpus.
- **Relevance and limits:** Shows how tool use can be learned. The original method lacks chained and interactive tool use; it is not a complete multi-step agent.
- **Resources:** [Official research page](https://ai.meta.com/research/publications/toolformer-language-models-can-teach-themselves-to-use-tools/). The checked paper / official page did not provide corresponding full code, training-data, and weight releases. Third-party reproductions are not official artifacts.

### M9. Proactive Agent · Predicting acceptable assistance

[Proactive Agent: Shifting LLM Agents from Reactive Responses to Active Assistance](https://arxiv.org/abs/2410.12361) — 2024 preprint; ICLR 2025; same paper as B6.

**Checked / reading scope:** 2026-10-31; Same check as B6: paper abstract, official README pipeline/release notes, and the weight-file listing.

- **Idea:** Train a reward model using activity traces and human acceptance / rejection labels, generate environment data, and train an agent to offer help proactively.
- **Relevance and limits:** Directly studies proactive assistance. Anticipated needs are not authorization; deployment must address activity-capture privacy and unwanted interruptions.
- **Resources:** [Code / data / evaluation](https://github.com/thunlp/ProactiveAgent), [officially linked Agent and Reward Model weights](https://huggingface.co/YancyLee/ProactiveAgent/tree/main). Check weight, base-model, and code licenses separately.

<a id="reproducibility"></a>
## Comparison and reproducibility

Do not assemble a leaderboard from unrelated papers' highest scores. Record at least:

1. **Tasks and versions:** Dataset revision / file hashes, splits, counts, and excluded failures. Separate original, cleaned, verified, and successor versions.
2. **Visible information:** Full history, retrieval top-k, oracle evidence, schemas, screenshots / UI trees. Do not put answers or future sessions into memory.
3. **Models and systems:** Exact base-model, memory, embedding, reranker, and judge versions; prompts, tools, and code commit. Distinguish model improvements from system improvements.
4. **Budgets and metrics:** Time, tokens, cost, steps, and retries. Report single-run success, repeated reliability, retrieval recall, and answer correctness separately. `pass@k` and `pass^k` are not interchangeable.
5. **Real-assistant gaps:** Test memory correction / deletion, user isolation, prompt injection, authorization / undo, interruption costs, cross-day unfinished tasks, and human utility separately.

These are this guide's evaluation recommendations, not claims that every listed paper covers all dimensions. Use synthetic or authorized, de-identified data. Never publish real personal histories, secrets, or cookies in issues, logs, or benchmark repositories.

<a id="sources-and-rights"></a>
## Sources and rights

- Paper titles link to original papers / publication pages; resource links point to author-maintained entry points. They support task definitions, metrics, and dates. Suggested applications and capability gaps are this guide's synthesis, not author endorsements of product reliability.
- Summaries are original and brief. No paper figures, long passages, complete question sets, or hidden answers are copied. Cite the original paper using its BibTeX, rather than citing only this list.
- **Public access is not unrestricted reuse.** Entries flag LaMP / LoCoMo noncommercial terms, GAIA gating / contamination controls, and AppWorld protected-content rules. An omitted license does not imply unrestricted use; code, data, weights, and third-party assets may have different terms.
- This check did not include asset-by-asset legal review, downloading and validating full weights, or reproducing all dependencies. A GitHub link does not resolve missing licenses, inaccessible files, or changing external services.
- Prioritize correcting versions, scope, and broken resources before adding papers. Contributions should provide specific primary evidence; rankings, citation counts, and stars are not reliability findings.
