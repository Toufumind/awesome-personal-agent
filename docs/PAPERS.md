# 个人 Agent 论文与评测 · Papers & benchmarks

[English](PAPERS.en.md) · [返回主清单](../README.md)

**先分清测了什么，再看分数。** 这里把 eval / benchmark 与 agent 方法 / 系统分开，并区分“直接研究个人上下文”与“可迁移到个人助理的通用能力”。

初版核验：**2026-10-31**。共 **21 篇不同论文**：13 个评测条目、9 个方法条目；Proactive Agent 同时贡献 benchmark 与方法，计一次论文。来源为论文摘要与下列明示的原文段落、作者项目页、官方代码库和数据卡；以下均为文献与资源核验，**没有安装复现、独立跑分或安全审计**。这是精选阅读入口，不是完整综述、最新论文榜或产品排名。

**阅读范围**：每条记录实际读取的摘要、相关章节片段及资源页；未声称逐篇通读全文。翻译不构成额外核验。

年份注明所列论文的发表或预印本版本；原论文的任务数不代表当前代码版本。资源“公开”仅表示能找到官方入口，不保证许可适合商业使用、依赖仍可安装或结果能直接复现。

## 目录

- [从研究问题开始](#reading-paths)
- [评测：个人上下文、记忆与主动性](#personal-evaluation)
- [评测：任务执行与交互能力](#execution-evaluation)
- [方法：记忆与长期状态](#memory-methods)
- [方法：规划、工具、反思与主动性](#agent-methods)
- [怎样比较与复现](#reproducibility)
- [来源与许可边界](#sources-and-rights)

<a id="reading-paths"></a>
## 从研究问题开始

| 你想研究什么 | 阅读入口 | 仍需另外验证 |
| --- | --- | --- |
| 记得用户说过什么、是否更新过 | LongMemEval、LoCoMo | 删除、纠错、跨用户隔离、真实长期使用 |
| 回答是否符合这个人的偏好 | LaMP、PersonaMem | 开放式回答质量、用户实际满意度 |
| 记忆是否真正影响工具参数 | Mem2ActBench | 工具实际执行、副作用与授权 |
| 何时该主动帮忙、何时不打扰 | ProactiveBench / Proactive Agent | 真人接受率、打扰成本、撤销与授权 |
| 多应用任务能否真的完成 | AppWorld、WebArena、OSWorld、AndroidWorld | 真实账号、环境变化、不可逆操作 |
| 多次尝试是否稳定遵守流程 | τ-bench | 模拟用户与真人差异、完整过程安全 |
| 从结构上搭建长期助理 | MemGPT、MemoryBank、A-MEM、Mem0；再读 ReAct / Reflexion | 权限、调度、可观测性、维护成本 |

<a id="personal-evaluation"></a>
## 评测 A：个人上下文、记忆与主动性

这一组更直接涉及用户历史、偏好或主动帮助；**也没有哪一个单独测完了“个人 Agent”**。

### B1. LaMP · 个性化语言任务

[LaMP: When Large Language Models Meet Personalization](https://aclanthology.org/2024.acl-long.399/) — ACL 2024。

**核验日期 / 阅读范围**：2026-10-31；论文摘要、§2.3 指标段落；官方 README 的许可说明与数据下载页。

- **输入 → 输出**：任务输入与该用户的历史条目 → 个性化分类标签或文本；原论文涵盖 3 类分类、4 类生成任务。
- **测量**：分类准确率 / F1、评分误差 MAE / RMSE、生成 ROUGE；使用用户划分和时间划分区分泛化设置。
- **边界**：适合测个性化检索与生成，不是多步工具执行，也不是持续真实用户实验。
- **资源**：[官方代码](https://github.com/LaMP-Benchmark/LaMP)、[数据入口](https://lamp-benchmark.github.io/download)。代码与构建方法标为 CC BY-NC-SA 4.0；底层数据另按各自许可。

### B2. LoCoMo · 长期对话记忆

[Evaluating Very Long-Term Conversational Memory of LLM Agents](https://aclanthology.org/2024.acl-long.747/) — ACL 2024。

**核验日期 / 阅读范围**：2026-10-31；论文摘要、§4 QA 指标、§6 摘要评测与 §8 局限相关段落；官方 README 的数据说明及 LICENSE。

- **输入 → 输出**：跨会话、带时间的长对话 → 事实问答、事件摘要或多模态续话；数据由模型生成并经人工核验编辑。
- **测量**：QA 分类型 F1；事件摘要用 ROUGE 与基于原子事实的指标；多模态任务另测相关性。不要把它们合成同一“记忆分数”。
- **边界**：官方当前公开集为 **10 段长对话**，不是早期 50 段版本；离线长对话不等于助理陪伴真人数月。
- **资源**：[官方代码 / 数据](https://github.com/snap-research/locomo)。不发布原始图片，只提供 URL 等信息；[许可](https://github.com/snap-research/locomo/blob/main/LICENSE.txt)为 CC BY-NC 4.0。

### B3. LongMemEval · 跨会话记忆、更新与拒答

[LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://arxiv.org/abs/2410.10813) — 2024 预印本；ICLR 2025。

**核验日期 / 阅读范围**：2026-10-31；论文摘要与 §3.3 评测段落；官方 README 的数据格式/评测说明及 cleaned 数据卡。

- **输入 → 输出**：带时间的用户—助理历史及问题 → 回答或在证据不足时拒答。500 个问题覆盖信息提取、跨会话 / 时间推理、知识更新和 abstention。
- **测量**：LLM judge 判断答案；可另测检索 Recall@k / NDCG@k。S、M、oracle 的历史长度和可见证据不同，不能混报。
- **边界**：检索召回不等于最终答对；构造历史上的 QA 不证明任务执行、隐私删除或持续在线能力。
- **资源**：[官方评测代码](https://github.com/xiaowu0162/LongMemEval)、[官方 cleaned 数据](https://huggingface.co/datasets/xiaowu0162/longmemeval-cleaned)。固定数据修订版和 judge 版本。

### B4. PersonaMem · 动态用户画像

[Know Me, Respond to Me: Benchmarking LLMs for Dynamic User Profiling and Personalized Responses at Scale](https://arxiv.org/abs/2504.14225) — COLM 2025；此处指原始 benchmark / v1 数据。

**核验日期 / 阅读范围**：2026-10-31；原论文修订版的 §2 任务定义及 §4 结果相关段落；官方 README 数据格式与 v1 数据卡。

- **输入 → 输出**：包含偏好变化的合成多会话历史及新场景问题 → 从四个候选回答中选择一个。
- **测量**：按七类问题、上下文长度和偏好距离报告选择准确率，区分记住事实、识别变化与迁移偏好。
- **边界**：四选一表现不等于开放式个性化回答质量；合成人物也不等于真实长期用户。不要与 PersonaMem-v2 数据混用。
- **资源**：[官方代码](https://github.com/bowen-upenn/PersonaMem)、[v1 数据](https://huggingface.co/datasets/bowen-upenn/PersonaMem-v1)，含 32k、128k、1M 上下文设置。

### B5. Mem2ActBench · 从记忆到工具参数

[Mem2ActBench: A Benchmark for Evaluating Long-Term Memory Utilization in Task-Oriented Autonomous Agents](https://aclanthology.org/2026.acl-long.370/) — ACL 2026。

**核验日期 / 阅读范围**：2026-10-31；论文摘要、§4.1 实验设置与 §5.4 工具选择评测相关段落；官方 README、根目录与数据目录入口。

- **输入 → 输出**：历史记忆、隐含约束的请求与工具 schema → 工具选择及参数；论文构建 400 个记忆依赖任务。
- **测量**：参数匹配 / F1、工具选择及调用整体匹配；主实验给定正确工具，另有干扰工具测试。
- **边界**：重点是把记忆用于参数，不应把生成正确调用写成已完成真实交易；主实验也不能当作开放工具选择成绩。
- **资源**：[官方构建代码 / 数据目录](https://github.com/Cantaloupe-M/Mem2ActBench)。根目录未见明确 LICENSE，且使用 ToolACE、BFCL、OASST1 等来源；复用前分别确认许可。

### B6. ProactiveBench（Lu et al.）· 主动帮助时机

[Proactive Agent: Shifting LLM Agents from Reactive Responses to Active Assistance](https://arxiv.org/abs/2410.12361) — 2024 预印本；ICLR 2025。

**核验日期 / 阅读范围**：2026-10-31；论文摘要与评测指标相关段落；官方 README 的系统概述、数据统计及评测入口。

- **输入 → 输出**：用户活动与环境事件 → 提议帮助任务，或不提议；包含编码、写作、日常场景，论文数据为 6,790 个事件。
- **测量**：接受 / 拒绝判断下的 precision、recall、F1 与 false alarm；自动评估使用学习到的 reward model。
- **边界**：主要测帮助是否合时宜，不能等同真人长期满意度或任务完成率；主动提议也不等于获准执行。
- **资源**：[官方代码、数据、评测](https://github.com/thunlp/ProactiveAgent)。同名 ProactiveBench 有其他论文，此处只指 Lu et al. 的版本；方法见 M9。

<a id="execution-evaluation"></a>
## 评测 B：任务执行与交互能力

以下可帮助测个人助理的“动手能力”，但多数属于**通用 Agent、网页 / GUI 或服务场景评测**，不能统称 personal-specific benchmark。AppWorld 有模拟个人应用与人物数据，仍不是长期真人个性化测试。

### B7. AssistantBench · 现实网页信息任务

[AssistantBench: Can Web Agents Solve Realistic and Time-Consuming Tasks?](https://aclanthology.org/2024.emnlp-main.505/) — EMNLP 2024。

**核验日期 / 阅读范围**：2026-10-31；论文摘要与 §3.4 自动评测相关段落；官方项目页、代码入口与数据卡。

- **输入 → 输出**：需要网页查找、整合的任务 → 字符串、数值或结构化答案；原始集 214 个任务。
- **测量**：答案 accuracy、回答率、precision、exact match；不是只看 Agent 是否宣称完成。
- **边界**：侧重找信息而非真实账号写操作；网页变化和答案时效影响复现，不测长期偏好维护。
- **资源**：[官方项目页](https://assistantbench.github.io/)、[代码](https://github.com/oriyor/assistantbench)、[数据](https://huggingface.co/datasets/AssistantBench/AssistantBench)。

### B8. GAIA · 通用助理综合解题

[GAIA: a benchmark for General AI Assistants](https://arxiv.org/abs/2311.12983) — 2023 预印本。

**核验日期 / 阅读范围**：2026-10-31；论文摘要与 §3.2 评测相关段落；官方数据卡的任务、分组及门控/再分发说明。

- **输入 → 输出**：自然语言问题，部分带文件 / 多模态材料 → 简短、可核验答案；原论文 466 题、三档难度。
- **测量**：按答案类型规范化后的近似 exact match，涉及浏览、工具、多模态与推理。
- **边界**：单次问题的正确性不是个性化、后台主动性或长期任务可靠性；公开开发集与隐藏答案测试集分开。
- **资源**：[官方数据卡与榜单入口](https://huggingface.co/datasets/gaia-benchmark/GAIA)。下载有门控条件，官方要求不要把题目集再分发成可爬取内容。

### B9. AppWorld · 跨应用个人数字任务沙箱

[AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents](https://arxiv.org/abs/2407.18901) — ACL 2024。

**核验日期 / 阅读范围**：2026-10-31；论文任务概述、§3.2 评测与 §7 局限相关段落；官方项目页、README 及许可说明。

- **输入 → 输出**：用户指令、模拟应用初始状态及 API 文档 → 交互式代码 / 调用改变应用状态；原论文 750 任务、9 类应用。
- **测量**：数据库状态测试；TGC 要求单任务所有测试通过，SGC 要求同场景的所有任务变体通过。
- **边界**：模拟 API 不是实网服务或 GUI；原始 benchmark 不等于后来的 AppWorld-UL 用户在环任务。
- **资源**：[项目页](https://appworld.dev/appworld/)、[官方代码 / 数据下载流程](https://github.com/StonyBrookNLP/appworld)。保护内容有额外加密再分发要求，见[许可说明](https://github.com/StonyBrookNLP/appworld#-license)。

### B10. τ-bench · 工具、用户与规则交互

[τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](https://arxiv.org/abs/2406.12045) — 2024 预印本。

**核验日期 / 阅读范围**：2026-10-31；论文摘要、§3 reward/pass^k 定义与 §6 讨论相关段落；官方 README 的过时任务和迁移警示。

- **输入 → 输出**：模拟用户对话、领域规则与 API → 对话和工具操作；原始任务围绕航空 / 零售服务。
- **测量**：终态数据库与目标状态比较，并检查要求告知用户的信息；**pass^k 是重复 k 次都成功的可靠性指标，不是 pass@k 的“至少成功一次”**。
- **边界**：客服侧领域流程不是长期私人助理；终态正确不保证每一步都合规，模拟用户会影响结果。
- **资源**：[原论文代码 / 数据](https://github.com/sierra-research/tau-bench)。官方已明确标注该仓库任务过时，并从 README 导向 τ³-bench；复现实验与运行新版必须分别标版本。

### B11. WebArena · 可复现网页操作

[WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854) — 2023 预印本，2024 修订版。

**核验日期 / 阅读范围**：2026-10-31；论文摘要与 §3 任务/评测相关段落；官方 README 的版本、环境与实现说明。

- **输入 → 输出**：高层自然语言意图与网页观察 → 浏览器操作、页面终态或文字答案；原论文 812 个任务。
- **测量**：以功能结果为核心，检查答案、导航结果或页面状态，而非固定点击序列。
- **边界**：自托管站点利于复现，但不覆盖所有真实网站、登录障碍与持续个性化；不可直接代表任意浏览器任务成功率。
- **资源**：[官方代码、环境与评测](https://github.com/web-arena-x/webarena)。固定任务修订版和网站镜像，避免混合不同环境结果。

### B12. OSWorld · 电脑操作与跨应用工作流

[OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://arxiv.org/abs/2404.07972) — 2024。

**核验日期 / 阅读范围**：2026-10-31；论文摘要及引言中的任务/状态评测概述；官方项目页的版本与资源说明。

- **输入 → 输出**：任务、初始桌面 / 文件状态、截图或 accessibility tree → 电脑操作与最终产物；原论文 369 个任务。
- **测量**：任务特定的 execution-based evaluator 检查结果；观察方式、动作空间、步数预算都影响可比性。
- **边界**：不测长期用户关系；依赖 VM / 软件版本。原版、OSWorld-Verified 和 OSWorld 2.0 不能混报；部分云文档任务另需配置。
- **资源**：[官方项目页及版本入口](https://os-world.github.io/)、[代码 / 任务](https://github.com/xlang-ai/OSWorld)。

### B13. AndroidWorld · 动态手机任务

[AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents](https://arxiv.org/abs/2405.14573) — 2024 预印本，2025 修订版。

**核验日期 / 阅读范围**：2026-10-31；论文摘要、§3.4 状态奖励与附录 A 局限相关段落；官方项目页及 README。

- **输入 → 输出**：自然语言任务、模拟器状态与屏幕 / 界面树 → Android 操作；116 个任务模板覆盖 20 个应用并随机化参数。
- **测量**：初始化、成功检测与清理逻辑直接检查设备状态；参数变化可测试稳健性。
- **边界**：116 是基础任务数，不是随机实例总数；以开源 / 系统应用为主，不保证对商业 App、不同手机或中文界面泛化。
- **资源**：[官方论文项目页](https://google-research.github.io/android_world/)、[环境 / 任务代码](https://github.com/google-research/android_world)。

<a id="memory-methods"></a>
## 方法 A：记忆与长期状态

这些条目解释可借鉴的系统机制，不把研究原型写成已验证的个人助理产品。

### M1. MemoryBank · 更新、强化与遗忘

[MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://arxiv.org/abs/2305.10250) — 2023 预印本。

**核验日期 / 阅读范围**：2026-10-31；论文摘要；官方 README 的机制、评测数据与模型说明，以及 LoRA 发布页。

- **核心**：存储 / 检索对话记忆、汇总用户信息，并用受遗忘曲线启发的机制强化或淡化记忆。
- **关联与边界**：直接面向长期对话伙伴；SiliconFriend 实验不是工具执行系统，也不是心理服务有效性的临床证据。
- **资源**：[代码与中英文评测数据](https://github.com/zhongwanjun/MemoryBank-SiliconFriend)、[ChatGLM / BELLE LoRA checkpoint 发布页](https://github.com/zhongwanjun/MemoryBank-SiliconFriend/releases/tag/LoRA_checkpoint)。适配器不等于底座模型，许可分别核对。

### M2. MemGPT · 分层记忆与上下文管理

[MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) — 2023 预印本，2024 修订版。

**核验日期 / 阅读范围**：2026-10-31；论文摘要；研究项目页、数据入口，以及 Letta README 的现行源码/历史版本说明和 letta-code 入口。

- **核心**：借鉴操作系统内存分层，在有限上下文与外部记忆间调度信息，用控制流管理多轮执行。
- **关联与边界**：论文含多会话聊天与长文档实验；“虚拟上下文”不意味着无限、无损、无需成本的记忆。
- **资源**：[论文项目页 / 实验数据入口](https://research.memgpt.ai/)、[历史 MemGPT / Letta 入口](https://github.com/letta-ai/letta)、[现行 Letta Code 源码](https://github.com/letta-ai/letta-code)。旧入口的 README 指向 letta-code，并将 V1 服务端保留于 archive 分支；复现论文须另定位当时版本，不能把现行产品或退休 V1 自动等同论文实现。

### M3. A-MEM · 关联笔记与记忆演化

[A-MEM: Agentic Memory for LLM Agents](https://arxiv.org/abs/2502.12110) — NeurIPS 2025。

**核验日期 / 阅读范围**：2026-10-31；论文摘要与 §4.2 数据/指标相关段落；官方两仓库的用途说明。

- **核心**：以 Zettelkasten 式笔记组织记忆，为新信息生成属性与关联，并按新信息更新已有记忆表示。
- **关联与边界**：可用于助理的可关联记忆；长对话 QA 实验不证明真实任务完成或记忆修改始终正确。
- **资源**：[论文评测代码](https://github.com/WujiangXu/A-mem)、[可集成系统代码](https://github.com/WujiangXu/A-mem-sys)。两仓库用途不同；是外接记忆方法，不是一个新底座模型。

### M4. Mem0 · 提取、整合与检索

[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://arxiv.org/abs/2504.19413) — 2025 arXiv 论文版。

**核验日期 / 阅读范围**：2026-10-31；2025 论文摘要；当前官方 README 与研究页，仅用于区分论文和后续项目状态。

- **核心**：从对话提取重要信息，整合更新并检索；论文另有图记忆变体。
- **关联与边界**：适用于跨会话个人上下文；论文基于 LoCoMo 的正确性、延迟与 token 评估，不能外推所有任务或所有部署。
- **资源**：[官方项目代码](https://github.com/mem0ai/mem0)。项目、托管服务与算法已持续演进；本文链接的是 2025 方案，不将当前宣传数字作为该论文的独立复现结果。

<a id="agent-methods"></a>
## 方法 B：规划、工具、反思与主动性

### M5. Generative Agents · 记忆—反思—规划

[Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) — 2023。

**核验日期 / 阅读范围**：2026-10-31；论文摘要；官方 README 的模拟环境、代码范围与模型调用说明。

- **核心**：记录经历、检索相关记忆，形成高层反思并据此规划行为；在 25 个虚拟角色的小镇中研究互动。
- **关联与边界**：为长期状态与计划提供结构思路；目标是可信的人类行为模拟，不是替真实用户办事或履行授权的证据。
- **资源**：[官方模拟器、环境与回放说明](https://github.com/joonspk-research/generative_agents)。依赖外部模型调用，不应当作独立模型权重发布。

### M6. ReAct · 交替推理与行动

[ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) — 2022 预印本；ICLR 2023。

**核验日期 / 阅读范围**：2026-10-31；论文摘要及 arXiv 版本说明；官方 README 与代码/提示目录。

- **核心**：交替生成任务推理、工具动作，并使用返回观察修正后续步骤。
- **关联与边界**：通用工具执行循环的基础；原实验为问答、事实核验与交互环境，不自带长期记忆、权限治理或全天候调度。
- **资源**：[官方代码、提示样例与实验 notebook](https://github.com/ysymyth/ReAct)。主要为 prompting 实现，不是完整个人助理。

### M7. Reflexion · 把失败反馈留给下一次

[Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) — NeurIPS 2023。

**核验日期 / 阅读范围**：2026-10-31；论文摘要；官方 README 的实验、日志与运行说明。

- **核心**：把任务反馈变为语言反思，保存在 episodic memory 中供后续尝试使用，而非直接更新模型权重。
- **关联与边界**：可借鉴任务重试与经验记忆；效果依赖反馈质量与重试预算，不保证“想一想”就能纠错或持续自我提升。
- **资源**：[官方代码、实验日志与示例](https://github.com/noahshinn/reflexion)。原评测含决策、推理与编码，不是长期私人助理研究。

### M8. Toolformer · 学会何时调用工具

[Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) — 2023 预印本。

**核验日期 / 阅读范围**：2026-10-31；论文摘要与 §7 局限；Meta 官方论文页及其提供的资源入口。

- **核心**：少量 API 示范引导模型生成候选调用，按对后续语言预测的帮助筛选，再用增强语料训练。
- **关联与边界**：说明工具调用可被学习；原方法不支持链式或交互式工具使用，不能当成完整多步 Agent。
- **资源**：[官方研究页](https://ai.meta.com/research/publications/toolformer-language-models-can-teach-themselves-to-use-tools/)。所查论文 / 官方页未给出对应完整代码、训练数据和模型权重入口；不将第三方复现标作官方发布。

### M9. Proactive Agent · 从活动预测可接受的帮助

[Proactive Agent: Shifting LLM Agents from Reactive Responses to Active Assistance](https://arxiv.org/abs/2410.12361) — 2024 预印本；ICLR 2025，与 B6 同一论文。

**核验日期 / 阅读范围**：2026-10-31；与 B6 同次核验：论文摘要、官方 README 的流程/发布说明及权重文件列表。

- **核心**：以活动轨迹和人类接受 / 拒绝标注训练 reward model，结合环境生成数据，再训练主动提出帮助的 Agent。
- **关联与边界**：直接研究主动助理；预测用户需要不等于被授权替用户行动，部署还需处理活动采集隐私与误打扰。
- **资源**：[代码 / 数据 / 评测](https://github.com/thunlp/ProactiveAgent)、[官方链接的 Agent 与 Reward Model 权重](https://huggingface.co/YancyLee/ProactiveAgent/tree/main)。权重、底座与代码许可分别确认。

<a id="reproducibility"></a>
## 怎样比较与复现

不要把不同论文中的最高分拼成排行榜。至少记录：

1. **任务与版本**：数据集 revision / 文件哈希、分组、题数、是否删除失败题；原版与 cleaned / verified / 后续版本分开。
2. **可见信息**：全历史、检索 top-k、oracle 证据、工具 schema、截图 / 界面树；禁止把答案或未来会话写入记忆。
3. **模型与系统**：底座精确版本、记忆 / embedding / reranker / judge、提示、工具、代码 commit；区分底座提升和系统提升。
4. **预算与指标**：时间、token、费用、步数、重试数；单次成功、重复稳定成功、检索召回、答案正确分别报告。`pass@k` 与 `pass^k` 不可互换。
5. **真实助理缺口**：错误记忆纠正与删除、跨用户隔离、提示注入、授权与撤销、误打扰、跨天未完成任务、真人效用，需要补充专门测试。

以上是本清单的评测建议，不是声称这些论文已经覆盖了所有维度。使用合成或获授权的脱敏数据；不要向公开 Issue、日志或评测仓库上传真实个人历史、密钥、Cookie。

<a id="sources-and-rights"></a>
## 来源与许可边界

- 每条论文标题链接到原文 / 正式论文页，资源链接到作者维护入口；任务定义、指标、发布日期以这些来源为依据。方法用途与未覆盖能力由本清单归纳，不是作者对产品可靠性的背书。
- 摘要均为原创短述，不复制论文图表、长段正文、完整题库或隐藏答案。引用某项研究时应从原论文导出 BibTeX，而不是只引用这个清单。
- **公开可读不等于任意再利用**：LaMP、LoCoMo 的非商业条款，GAIA 的门控 / 防污染要求，AppWorld 的保护内容规则已在对应条目提示。未列许可不代表没有限制；代码、数据、模型和第三方素材可能适用不同条款。
- 本次未进行逐资产法律审查、下载完整权重验证或全依赖复现。根目录缺许可、文件访问失败或外部服务变化均不能被“有 GitHub 链接”消除。
- 维护时先修正文献版本、任务范围与失效资源，再补新论文；欢迎提供具体一手证据，不以榜单名次、引用量或 Star 作为可靠性结论。
