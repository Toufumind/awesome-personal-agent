# 个人 Agent 论文与评测 · Papers & benchmarks

[English](PAPERS.en.md) · [返回主清单](../README.md)

**先分清测了什么，再看分数。** 这里把 eval / benchmark 与 agent 方法 / 系统分开，并区分“直接研究个人上下文”“可迁移的通用记忆 / 执行能力”及“特定隐私 / 安全风险”。

文献与资源核验：**2026-10-31**。共 **68 篇不同论文**：44 个评测条目、34 个方法条目；Proactive Agent、MemoProAgent、PbP/InTU、Ask-before-Plan/CEP、PersonalAlign/HIM-Agent、PEToolLLM/PEToolLLaMA、MemGuide/MS-TOD、Me-Agent/User FingerTip、PPP/UserVille 与 PUMA/PersonalWAB 各同时贡献 benchmark 和方法，分别只计一次论文。来源为论文摘要与下列明示的原文段落、作者项目页、官方代码库和数据卡；**没有安装复现、独立跑分、模型训练或安全审计**。这是精选阅读入口，不是完整综述、最新论文榜或产品排名。

**条目核验**：B25–B44、M16–M34 核验于 2026-11-01；旧条目保留原核验日期。

**阅读范围**：每条记录实际读取的摘要、相关章节片段及资源页；未声称逐篇通读全文。翻译不构成额外核验。

年份与版本标识对应所列论文，而不是当前项目版本。原论文任务数不代表当前代码；`main`、数据卡和资源状态只是核验日观察，并非锁定的复现快照。“公开”仅表示找到官方入口，不保证商业许可、依赖可安装、权重齐全或结果可复现。

## 目录

- [从研究问题开始](#reading-paths)
- [评测：个人上下文、记忆与主动性](#personal-evaluation)
- [评测：可迁移记忆与连续任务](#transferable-memory-evaluation)
- [评测：任务执行与交互能力](#execution-evaluation)
- [评测：隐私规范与对抗安全](#safety-evaluation)
- [方法：记忆与长期状态](#memory-methods)
- [方法：规划、工具、反思、主动性与协作](#agent-methods)
- [方法：个性化与偏好学习](#personalization-methods)
- [怎样比较与复现](#reproducibility)
- [来源与许可边界](#sources-and-rights)

<a id="reading-paths"></a>
## 从研究问题开始

| 你想研究什么 | 阅读入口 | 仍需另外验证 |
| --- | --- | --- |
| 计划修订后是否仍符合偏好 | [PDEU-Bench](#benchmark-pdeu-bench) | 真实服务、完整执行与授权 |
| 是否为未来主动获取偏好 | [ATRBench](#benchmark-atrbench) | 真实变化的偏好、提问成本 |
| 不可靠主张是否写入并影响以后 | [PASB](#benchmark-pasb) | 产品总体风险、真实长期使用 |
| 记得用户说过什么、是否更新过 | [LongMemEval](#benchmark-longmemeval)、[LoCoMo](#benchmark-locomo)；[MemoryAgentBench](#benchmark-memoryagentbench) 测通用增量记忆 | 删除、纠错、跨用户隔离、真实长期使用 |
| 回答是否符合这个人的偏好 | [LaMP](#benchmark-lamp)、[PersonaMem](#benchmark-personamem-v1) / [PersonaMem-v2](#benchmark-personamem-v2)、[PersonaBench](#benchmark-personabench)、[PrefEval](#benchmark-prefeval) | 真人满意度、私人文档部署安全；不同 QA / 生成 / MCQ 协议分别比较 |
| 记忆是否影响工具参数与后续行动 | [Mem2ActBench](#benchmark-mem2actbench)、[MemoryArena](#benchmark-memoryarena) | 真实执行、副作用授权、任务中断后的恢复 |
| 何时主动帮忙、何时澄清或不打扰 | [ProactiveBench](#benchmark-proactivebench-lu) / [Proactive Agent](#method-proactive-agent)、[KnowU-Bench](#benchmark-knowu-bench)、[MemoProBench](#benchmark-memoprobench) / [MemoProAgent](#method-memoproagent)、[π-Bench](#benchmark-pi-bench) | 真人接受率、打扰成本、拒绝后克制、撤销与授权 |
| 多应用任务能否真的完成 | [AppWorld](#benchmark-appworld)、[WebArena](#benchmark-webarena)、[OSWorld](#benchmark-osworld)、[AndroidWorld](#benchmark-androidworld) | 真实账号、环境变化、不可逆操作 |
| 多次尝试是否稳定遵守流程 | [τ-bench](#benchmark-tau-bench) | 模拟用户与真人差异、完整过程安全 |
| 读到的信息是否应该向外分享 | [PrivacyLens](#benchmark-privacylens)、[AgentCIBench](#benchmark-agentcibench)；[AgentDojo](#benchmark-agentdojo) 另测间接提示注入 | 完整隐私合规、跨用户 / 多代理隔离、所有攻击面 |
| 怎样从个人反馈学习偏好 | [P-RLHF](#method-p-rlhf) | 冷启动、偏好变化、真人长期效用；不等同于记忆存储 |
| 怎样管理长期记忆与生命周期 | [MemGPT](#method-memgpt)、[MemoryBank](#method-memorybank)、[A-MEM](#method-a-mem)、[Mem0](#method-mem0)、[Zep](#method-zep)、[MemOS](#method-memos) | 失效或不再使用不等于物理删除；还需权限、调度与可观测性 |
| 怎样复用经验、技能与多代理协作 | [ReAct](#method-react)、[Reflexion](#method-reflexion)、[Voyager](#method-voyager)、[ExpeL](#method-expel)、[AutoGen](#method-autogen)（历史） | 长期真人效用、单代理对照、经验过时与运行成本 |


**个人规划阅读路线**：先看 [TravelPlanner+](#benchmark-travelplanner-plus)：怎样把画像与个人概念变成计划条件；再看 [PbP](#benchmark-pbp) / [InTU](#method-intu)：怎样从行为提炼未明说的偏好；信息不足时读 [Ask-before-Plan](#benchmark-ask-before-plan) / [CEP](#method-cep)；执行反馈后的偏好保持读 [PDEU-Bench](#benchmark-pdeu-bench)；最后用 [AuthorizationBench](#benchmark-authorizationbench) 区分“完成了”与“有权这样做”。这是按问题组织的阅读顺序，不是单一系统的完整能力证明；跨会话状态、真实长期效用及授权变更仍须另测。

<a id="user-profile-reading-path"></a>
### 用户画像：按四个问题读

这是跨条目的阅读路线，**不替代“评测 / 方法”分类，同一论文可出现在多行**。这里的“画像”包括用户历史、偏好摘要和学到的用户表示，不一定是一张固定资料卡；下表是本清单的归纳，不是论文自带的分类。

| 问题 | 先读什么、看什么 | 不能据此认定什么 |
| --- | --- | --- |
| **1. 怎么理解用户？** | [MemoryBank](#method-memorybank)：从历史互动汇总用户信息；[P-RLHF](#method-p-rlhf)：从显式偏好文本和个人比较反馈学习用户表示；[PrefEval](#benchmark-prefeval)：检验显式 / 隐含偏好能否被识别并遵循。 | 用户表示不等于完整、准确的人格；PrefEval 是能力测试，不是画像构建系统。 |
| **2. 怎么存、怎么更新？** | [MemoryBank](#method-memorybank)：存储、检索、强化与淡化记忆；[Zep](#method-zep)：用时间关系处理冲突并保留历史。再用 [LongMemEval](#benchmark-longmemeval) 检验更新后能否答对。 | 记忆淡化或关系失效不等于物理删除；P-RLHF 的训练也不是持续记忆更新机制。 |
| **3. 怎么把画像用起来？** | [LaMP](#benchmark-lamp)：将用户历史用于个性化分类 / 生成；[P-RLHF](#method-p-rlhf)：让生成随学到的用户偏好变化。若关心行动，接着读 [Mem2ActBench](#benchmark-mem2actbench) 的记忆到工具参数。 | 检索历史与学习用户表示是不同路线；回答更合偏好、工具参数正确，都不等于真实任务已完成。 |
| **4. 怎么评估？** | [LaMP](#benchmark-lamp)：个性化任务质量；[PrefEval](#benchmark-prefeval)：是否遵循已知偏好；[PersonaMem（v1）](#benchmark-personamem-v1)：能否识别偏好变化并迁移到新场景。 | 三者不是同一指标；PersonaMem 的合成历史与四选一不能代替开放式回答质量或长期真人满意度。 |

<a id="personal-evaluation"></a>
## 评测 A：个人上下文、记忆与主动性

这一组更直接涉及用户历史、偏好或主动帮助；**也没有哪一个单独测完了“个人 Agent”**。

<a id="benchmark-lamp"></a>
### B1. LaMP · 个性化语言任务

[LaMP: When Large Language Models Meet Personalization](https://aclanthology.org/2024.acl-long.399/) — ACL 2024。

**核验日期 / 阅读范围**：2026-10-31；论文摘要、§2.3 指标段落；官方 README 的许可说明与数据下载页。

- **输入 → 输出**：任务输入与该用户的历史条目 → 个性化分类标签或文本；原论文涵盖 3 类分类、4 类生成任务。
- **测量**：分类准确率 / F1、评分误差 MAE / RMSE、生成 ROUGE；使用用户划分和时间划分区分泛化设置。
- **边界**：适合测个性化检索与生成，不是多步工具执行，也不是持续真实用户实验。
- **资源**：[官方代码](https://github.com/LaMP-Benchmark/LaMP)、[数据入口](https://lamp-benchmark.github.io/download)。代码与构建方法标为 CC BY-NC-SA 4.0；底层数据另按各自许可。

<a id="benchmark-locomo"></a>
### B2. LoCoMo · 长期对话记忆

[Evaluating Very Long-Term Conversational Memory of LLM Agents](https://aclanthology.org/2024.acl-long.747/) — ACL 2024。

**核验日期 / 阅读范围**：2026-10-31；论文摘要、§4 QA 指标、§6 摘要评测与 §8 局限相关段落；官方 README 的数据说明及 LICENSE。

- **输入 → 输出**：跨会话、带时间的长对话 → 事实问答、事件摘要或多模态续话；数据由模型生成并经人工核验编辑。
- **测量**：QA 分类型 F1；事件摘要用 ROUGE 与基于原子事实的指标；多模态任务另测相关性。不要把它们合成同一“记忆分数”。
- **边界**：官方当前公开集为 **10 段长对话**，不是早期 50 段版本；离线长对话不等于助理陪伴真人数月。
- **资源**：[官方代码 / 数据](https://github.com/snap-research/locomo)。不发布原始图片，只提供 URL 等信息；[许可](https://github.com/snap-research/locomo/blob/main/LICENSE.txt)为 CC BY-NC 4.0。

<a id="benchmark-longmemeval"></a>
### B3. LongMemEval · 跨会话记忆、更新与拒答

[LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://arxiv.org/abs/2410.10813) — 2024 预印本；ICLR 2025。

**核验日期 / 阅读范围**：2026-10-31；论文摘要与 §3.3 评测段落；官方 README 的数据格式/评测说明及 cleaned 数据卡。

- **输入 → 输出**：带时间的用户—助理历史及问题 → 回答或在证据不足时拒答。500 个问题覆盖信息提取、跨会话 / 时间推理、知识更新和 abstention。
- **测量**：LLM judge 判断答案；可另测检索 Recall@k / NDCG@k。S、M、oracle 的历史长度和可见证据不同，不能混报。
- **边界**：检索召回不等于最终答对；构造历史上的 QA 不证明任务执行、隐私删除或持续在线能力。
- **资源**：[官方评测代码](https://github.com/xiaowu0162/LongMemEval)、[官方 cleaned 数据](https://huggingface.co/datasets/xiaowu0162/longmemeval-cleaned)。固定数据修订版和 judge 版本。

<a id="benchmark-personamem-v1"></a>
### B4. PersonaMem · 动态用户画像

[Know Me, Respond to Me: Benchmarking LLMs for Dynamic User Profiling and Personalized Responses at Scale](https://arxiv.org/abs/2504.14225) — COLM 2025；此处指原始 benchmark / v1 数据。

**核验日期 / 阅读范围**：2026-10-31；原论文修订版的 §2 任务定义及 §4 结果相关段落；官方 README 数据格式与 v1 数据卡。

- **输入 → 输出**：包含偏好变化的合成多会话历史及新场景问题 → 从四个候选回答中选择一个。
- **测量**：按七类问题、上下文长度和偏好距离报告选择准确率，区分记住事实、识别变化与迁移偏好。
- **边界**：四选一表现不等于开放式个性化回答质量；合成人物也不等于真实长期用户。不要与 PersonaMem-v2 数据混用。
- **资源**：[官方代码](https://github.com/bowen-upenn/PersonaMem)、[v1 数据](https://huggingface.co/datasets/bowen-upenn/PersonaMem-v1)，含 32k、128k、1M 上下文设置。

<a id="benchmark-mem2actbench"></a>
### B5. Mem2ActBench · 从记忆到工具参数

[Mem2ActBench: A Benchmark for Evaluating Long-Term Memory Utilization in Task-Oriented Autonomous Agents](https://aclanthology.org/2026.acl-long.370/) — ACL 2026。

**核验日期 / 阅读范围**：2026-10-31；论文摘要、§4.1 实验设置与 §5.4 工具选择评测相关段落；官方 README（含 License 声明）、根目录与数据目录入口。

- **输入 → 输出**：历史记忆、隐含约束的请求与工具 schema → 工具选择及参数；论文构建 400 个记忆依赖任务。
- **测量**：参数匹配 / F1、工具选择及调用整体匹配；主实验给定正确工具，另有干扰工具测试。
- **边界**：重点是把记忆用于参数，不应把生成正确调用写成已完成真实交易；主实验也不能当作开放工具选择成绩。
- **资源**：[官方构建代码 / 数据目录](https://github.com/Cantaloupe-M/Mem2ActBench)。[README 的 License 节](https://github.com/Cantaloupe-M/Mem2ActBench#license)声明 MIT License，但所查根目录未见独立 LICENSE 文件；复用前确认完整许可文本及适用范围。ToolACE、BFCL、OASST1 等上游数据仍须分别核对条款，不能由该声明推定全部数据都获 MIT 授权。

<a id="benchmark-proactivebench-lu"></a>
### B6. ProactiveBench（Lu et al.）· 主动帮助时机

[Proactive Agent: Shifting LLM Agents from Reactive Responses to Active Assistance](https://arxiv.org/abs/2410.12361) — 2024 预印本；ICLR 2025。

**核验日期 / 阅读范围**：2026-10-31；论文摘要与评测指标相关段落；官方 README 的系统概述、数据统计及评测入口。

- **输入 → 输出**：用户活动与环境事件 → 提议帮助任务，或不提议；包含编码、写作、日常场景，论文数据为 6,790 个事件。
- **测量**：接受 / 拒绝判断下的 precision、recall、F1 与 false alarm；自动评估使用学习到的 reward model。
- **边界**：主要测帮助是否合时宜，不能等同真人长期满意度或任务完成率；主动提议也不等于获准执行。
- **资源**：[官方代码、数据、评测](https://github.com/thunlp/ProactiveAgent)。同名 ProactiveBench 有其他论文，此处只指 Lu et al. 的版本；方法见 M11。

<a id="benchmark-personabench"></a>
### B7. PersonaBench · 从私人文档理解用户

[PersonaBench: Evaluating AI Models on Understanding Personal Information through Accessing (Synthetic) Private User Data](https://aclanthology.org/2025.findings-acl.49/) — Findings of ACL 2025；查阅原文为 [arXiv v2，2025-08-20](https://arxiv.org/html/2502.20616v2)。

**核验日期 / 阅读范围**：2026-10-31；论文摘要、§5.3 指标；官方 README 的数据示例及许可。

- **输入 → 输出**：合成的带时间私人文档（人际聊天、与 AI 对话、购买记录等）及个人问题 → 事实答案，例如从聊天记录找到音乐偏好。
- **测量**：检索 Recall / NDCG；端到端答案 Recall / F1。两类结果分开报告。
- **边界**：直接研究个人上下文 QA，不是自主执行或隐私保护评测。合成社交关系不能证明真人个性化效果；官方 v1.0 公开示例为两个社区、每社区三人，不代表论文全部数据。
- **资源**：[官方代码、公开评测数据及 README](https://github.com/SalesforceAIResearch/personabench)。CC BY-NC-SA 4.0；README 另有使用限制，复用前一并检查。

<a id="benchmark-prefeval"></a>
### B8. PrefEval · 记住偏好不等于遵循偏好

[Do LLMs Recognize Your Preferences? Evaluating Personalized Preference Following in LLMs](https://arxiv.org/html/2502.09597v1) — ICLR 2025；查阅 v1，2025-02-13。

**核验日期 / 阅读范围**：2026-10-31；论文摘要、§2.2、§2.5、§3.4；官方 README 及 LICENSE。

- **输入 → 输出**：显式或隐含偏好、无关对话及后续请求 → 开放式回答或四选一；例如先表露饮食偏好，再请求旅行餐厅建议。1,000 个基础偏好—问题对各有三种表达，不是 3,000 个独立用户。
- **测量**：生成评测用四个二元 judge 检查并归入错误类型；分类用准确率，不能混报。
- **边界**：直接研究偏好遵循；这里的 personalization proactiveness 是无需提醒便沿用已知偏好，不是后台监控或自主发起任务，也不等于真人满意度。
- **资源**：[官方代码及完整格式](https://github.com/amazon-science/PrefEval)、[显式偏好数据](https://huggingface.co/datasets/siyanzhao/prefeval_explicit)。[仓库许可](https://github.com/amazon-science/PrefEval/blob/main/LICENSE)为 CC BY-NC 4.0；所链 HF 数据仅为 explicit 子集，不是三种表达的全集。

<a id="benchmark-personamem-v2"></a>
### B9. PersonaMem-v2 · 隐含偏好、归属与不再使用

[PersonaMem-v2: Towards Personalized Intelligence via Learning Implicit User Personas and Agentic Memory](https://arxiv.org/html/2512.06688v1) — 2025 预印本；查阅 v1，2025-12-07。不同于 B4 的原始 PersonaMem 论文。

**核验日期 / 阅读范围**：2026-10-31；论文摘要、§2.3–2.4、§4.1；官方数据卡与系列 README。

- **输入 → 输出**：合成多会话历史及当前问题 → 开放式回答或四选一；包含隐含、变化、他人偏好，以及敏感或用户要求忘记的信息。
- **测量**：MCQ 正确选项匹配；开放回答汇总三个 judge 的判断。两种协议分开。
- **边界**：要求忘记后不再使用信息，不证明存储、备份或模型参数中已删除。论文另训练可读记忆系统；其结果不是现成 Agent 的普遍能力。本条限定 text 设置。
- **资源**：[官方数据](https://huggingface.co/datasets/bowen-upenn/PersonaMem-v2)标 CC BY 4.0；[系列仓库](https://github.com/bowen-upenn/PersonaMem)标 MIT。当前数据卡含后续 multimodal 资源，须固定 text revision、split、32k / 128k 与评测模式；未确认系列入口提供完整 v2 RL 训练复现包。

<a id="benchmark-knowu-bench"></a>
### B10. KnowU-Bench · 澄清、主动同意与拒绝后克制

[KnowU-Bench: Towards Interactive, Proactive, and Personalized Mobile Agent Evaluation](https://arxiv.org/html/2604.08455v1) — 2026 预印本；查阅 v1，2026-04-09。

**核验日期 / 阅读范围**：2026-10-31；论文摘要、§3.4 及实验讨论相关段落；官方仓库。

- **输入 → 输出**：行为日志、模糊请求或主动触发条件及 Android 状态 → GUI 操作、澄清提问、请求同意或不行动；用户画像对 Agent 隐藏，但可向基于画像的模拟用户提问。
- **测量**：42 个通用、86 个个性化、64 个主动任务。规则检查收件人、订单 / 日程 / 设置状态及拒绝后违规；judge 评价语义偏好。
- **边界**：直接研究个性化与主动移动 Agent；模拟器、rubric 与 judge 影响成绩，不能等同真人接受率。未下载环境或验证全部任务可运行。
- **资源**：[官方项目](https://zju-real.github.io/KnowU-Bench/)、[环境、任务及代码](https://github.com/ZJU-REAL/KnowU-Bench)。仓库 Apache-2.0；第三方 Android 应用、镜像与模型分别适用各自条款。

<a id="benchmark-memoprobench"></a>
### B11. MemoProBench · 何时开口、说什么、何时不说

[MemoProAgent: Toward Memory-Driven Proactive Assistance](https://arxiv.org/html/2610.22671v2) — 2026 预印本；查阅 v2，2026-10-21。早期索引可能仍用 ProPerAgent / ProPerMem；此处按 v2 命名，方法见 M12。

**核验日期 / 阅读范围**：2026-10-31；v2 摘要、§3.3 指标、方法概述；官方 README 及 LICENSE。

- **输入 → 输出**：第一人称视频流及长个人历史，无显式提问 → 有记忆依据的适时提醒，或保持安静。
- **测量**：Perfect 要求允许时间窗内恰好一次正确提醒；另报 Hit、过早、过晚、重复提醒及负例误触发，不能只报“曾命中”。
- **边界**：直接研究个人记忆驱动主动性，但长历史是受控构造，不是真人一年跟踪；不测真实授权交易完成，也不证明全天候体验。
- **资源**：[官方推理代码](https://github.com/facebookresearch/Memo-Pro-Agent)为 CC BY-NC 4.0；[历史数据入口（受限）](https://huggingface.co/datasets/facebook/MemProBench)。官方 [README 数据说明](https://github.com/facebookresearch/Memo-Pro-Agent#data-and-reproducibility)明确：`facebook/MemProBench` 历史数据当前为 private，须有获授权的 Hugging Face 访问权限；本次未取得下载访问，独立数据许可仍未确认，不能套用代码许可。视频须按 [Ego4D](https://ego4d-data.org/) 条款另行取得；公开推理 harness 不等于完整 RL 训练复现包。

<a id="benchmark-pi-bench"></a>
### B23. π-Bench · 跨会话隐含意图与主动澄清

[π-Bench: Evaluating Proactive Personal Assistant Agents in Long-Horizon Workflows](https://arxiv.org/html/2605.14678v1) — 2026 预印本；本条初读 v1，2026-05-14；官方 README 宣布获 NeurIPS 2026 接收，不将其等同已核验正式会议论文集。

**核验日期 / 阅读范围**：2026-10-31；v1 摘要、评测讨论与 §4 相关段落；官方项目页的指标定义、README 的资源与接收说明。文献初读，不是安装或实测。

- **输入 → 输出**：未充分说明的请求、先前会话与持久工作区 → 定向澄清、工具操作及文件产物；5 个用户角色各有 20 会话，共 100 个任务。
- **测量**：Proc 计入 Agent 主动满足、或通过定向提问澄清的隐含意图；Comp 评估完整轨迹、工具记录和产物的清单要求。最终完成不等于主动发现需求，两个指标分开报告。
- **边界**：这里的主动性是在交互中减少用户补充需求的负担，不是后台自主发起任务，也不授予执行权限。模拟用户与模型评分不证明长期真人满意度。
- **资源**：[官方代码 / 数据](https://github.com/Simplified-Reasoning/Pi-Bench)、[项目与指标说明](https://simplified-reasoning.github.io/Pi-Bench/)。仓库 Apache-2.0；AppWorld、NanoBot 及其他依赖另按各自条款。固定论文版本、代码、模型与 judge 配置后再比较。

<a id="benchmark-pdeu-bench"></a>
### B25. PDEU-Bench · 偏好能否贯穿计划修订

[PDEU-Bench: Benchmarking the Personalized Planning Lifecycle of Tool-Calling LLM Agents](https://arxiv.org/html/2609.34930v1) — 2026 预印本；v1，2026-09-28。

**核验日期 / 阅读范围**：2026-11-01；摘要、Environment Construction、Preference and Task Construction、Task Evaluation、Error Analysis 相关段落。

- **输入 → 输出**：合成用户历史与任务 → 初始计划、工具调用及每次尝试后的计划更新；214 个任务、12 个领域、94 个工具。
- **测量**：固定 judge 按二元 rubric 分别评偏好与计划质量；严格成功要求各相关阶段全部通过。执行阶段只评工具参数中的偏好落实。
- **边界**：离线沙箱与合成偏好，不证明真实交易成功或长期真人效用。
- **资源**：摘要称附录提供代码和数据，但本次所读 HTML 与检索未定位可核验官方入口；许可及可运行性未确认。

<a id="benchmark-atrbench"></a>
### B26. ATRBench · 现在问，留待以后用

[Ask Now, Use Later: Benchmarking the Proactivity Gap in Long-Lived LLM Agents](https://arxiv.org/html/2605.28108v3) — v3，2026-09-15；作者元数据标 EMNLP 2026 Main。

**核验日期 / 阅读范围**：2026-11-01；摘要、§3.1–3.2、Limitations、Ethical Considerations；官方 README 与 NOTICE。

- **输入 → 输出**：日常任务中的模拟用户互动 → 主动获取当前不需要、未来会用的偏好；学习后冻结历史，测试时用户离线。
- **测量**：TSAcc 确定性检查首个相关工具决策，按用户宏平均；另报提问、获取与应用指标。
- **边界**：20 个合成人物、固定规则与模型路由，不代表真实偏好变化或打扰成本；多问不等于更好。
- **资源**：[官方代码 / 数据](https://github.com/BUPT-GAMMA/ATRBench)。代码 Apache-2.0；NOTICE 单列源人物数据 CC BY 4.0，勿推定全部资产同一许可。未运行。

<a id="benchmark-travelplanner-plus"></a>
### B28. TravelPlanner+ · 用户画像怎样改变计划

[Personal Large Language Model Agents: A Case Study on Tailored Travel Planning](https://aclanthology.org/2024.emnlp-industry.37/) — EMNLP 2024 Industry Track。标题按 ACL 元数据；PDF 标题末词为 Tailored Travel Planners。

**核验日期 / 阅读范围**：2026-11-01；摘要、§1、§4.2 及结果表；待审，未复现。

- **输入 → 输出**：用户模型、含个人概念的请求及旅行参考信息 → 个性化行程。
- **测量**：计划交付、常识 / 硬约束与最终通过率；另用 LLM judge 比较个性化与通用计划的偏好率。
- **边界**：judge 偏好率不是真人满意度，也不等于约束通过率；部分个性化设置的约束指标下降。不是长期在线规划。
- **资源**：[论文全文](https://aclanthology.org/2024.emnlp-industry.37.pdf)；本次未定位可核验的 TravelPlanner+ 官方代码 / 数据入口，不以原始 TravelPlanner 仓库冒充。

<a id="benchmark-pbp"></a>
### B29. PbP · 从示范推断规划偏好

[Inferring the Unspoken: Aligning Embodied Agents with Implicit Preferences](https://arxiv.org/abs/2502.00858v4) — 2025 首发；此处为 2026-09-08 v4，arXiv 标注 EMNLP 2026。旧题为 Learning to Plan with Personalized Preferences；方法见 M17。

**核验日期 / 阅读范围**：2026-11-01；仅 v4 摘要与版本记录，待审初读。

- **输入 → 输出**：少量行为演示与新情境 → 符合隐含偏好的具身动作计划；摘要报告 5,000 个评测组、290 种偏好。
- **测量**：比较给定真实偏好与从行为推断偏好后的规划表现；具体指标和评分协议尚待全文核验，不录入分数。
- **边界**：具身场景，不代表办公工具规划或长期真人使用。PDF 抓取超出工具大小限制，HTML 不可用。
- **资源**：本次未定位可核验官方代码 / 数据入口；不推定公开或可复现。

<a id="benchmark-androidintent"></a>
### B32. AndroidIntent · 从长期记录理解 GUI 隐含意图

[PersonalAlign: Hierarchical Implicit Intent Alignment for Personalized GUI Agent with Long-Term User-Centric Records](https://aclanthology.org/2026.acl-long.1669/) — ACL 2026；查阅 [arXiv v2](https://arxiv.org/html/2601.09636v2)，2026-05-13。方法见 M21。

**核验日期 / 阅读范围**：2026-11-01；任务与数据构建相关段落、§6.1 指标、附录 A.3；官方 README 和根目录，非全文通读。

- **输入 → 输出**：长期手机操作记录、模糊指令或当前状态 → GUI 动作或主动建议；标注 775 个偏好案例与 215 个例行行为案例。
- **测量**：离线动作类型准确率、逐步成功率及加权 CSR；主动建议另测语义 / judge 对齐、precision、recall、false alarm 和 F1。
- **边界**：主评测是离线轨迹对照；CSR 不等于真实手机任务完成率。建议合适也不等于获准执行。
- **资源**：[官方代码与数据目录](https://github.com/iLearn-Lab/ACL26-PersonalAlign)。需另取 FingerTip-20k；README 说明曾因磁盘故障恢复资源，未验证完整性。所查根目录未见独立许可文件，上游数据条款另核对。

<a id="benchmark-petoolbench"></a>
### B33. PEToolBench · 从历史调用推断工具偏好

[PEToolLLM: Towards Personalized Tool Learning in Large Language Models](https://aclanthology.org/2025.findings-acl.1107/) — Findings of ACL 2025；查阅 [arXiv v1](https://arxiv.org/html/2502.18980v1)，2025-02-26。方法见 M22。

**核验日期 / 阅读范围**：2026-11-01；§3 任务、构建与指标、§4 方法概述；官方 README、LICENSE 与数据文件列表，非全文通读。

- **输入 → 输出**：指令、候选工具与用户历史调用 → 工具及参数；合成历史包括仅偏好、带评分、按时间变化三种设置。论文有 12,000 条样本，9,000 训练、3,000 测试。
- **测量**：分别报告工具选择准确率与参数准确率。
- **边界**：生成正确调用不等于服务已执行；合成偏好不能代替真实长期用户行为。
- **资源**：[官方代码](https://github.com/travis-xu/PEToolBench)、[数据文件](https://huggingface.co/datasets/travisxu/PEToolBench/tree/main)。[仓库许可](https://github.com/travis-xu/PEToolBench/blob/main/LICENSE)为 Apache-2.0；不能据此推定所有上游工具资料适用同一许可。

<a id="benchmark-etapp"></a>
### B34. ETAPP · 个性化工具交互与额外帮助

[Evaluating Personalized Tool-Augmented LLMs from the Perspectives of Personalization and Proactivity](https://aclanthology.org/2025.acl-long.1064/) — ACL 2025；查阅 [arXiv v1](https://arxiv.org/html/2503.00771v1)，2025-03-02。

**核验日期 / 阅读范围**：2026-11-01；§2 环境、记忆与样本构建、§3 评测；官方 README 与根目录，非全文通读。

- **输入 → 输出**：画像、工具偏好、当前状态、历史及请求 → 沙箱工具交互与回答；800 个案例由 50 条指令与 16 个合成人物组合，不是 800 位用户。
- **测量**：人工关键点辅助 LLM judge，分别按 0–5 分评价流程、个性化与主动性；区分给定工具和检索工具两种设置。
- **边界**：这里的主动性是请求之后提供额外有用帮助，不等于后台自主发起任务；judge 分数不证明真实世界的服务执行、安全或授权。
- **资源**：[官方代码、数据与工具](https://github.com/hypasd-art/ETAPP)，含推理和评测说明；所查根目录未见独立许可文件，未验证依赖或 API 可用性。

<a id="benchmark-toolspectrum"></a>
### B35. ToolSpectrum · 同时考虑画像与环境的工具选择

[ToolSpectrum: Towards Personalized Tool Utilization for Large Language Models](https://aclanthology.org/2025.findings-acl.1063/) — Findings of ACL 2025；查阅 [arXiv v1](https://arxiv.org/html/2505.13176v1)，2025-05-19。

**核验日期 / 阅读范围**：2026-11-01；§3 任务、构建与统计、§4.1 指标；官方 README 与根目录，非全文通读。

- **输入 → 输出**：请求、显式画像、环境与功能重叠的工具集 → 应用、API、必需及个性化可选参数，或按应用规则返回 `None`。
- **测量**：四个层级分别算 F1。共 1,000 个案例：画像 450、环境 220、二者结合 330。
- **边界**：测给定画像后的选择与参数，不测从历史学习画像或真实交易；仅环境子集也不等于个体偏好学习。
- **资源**：[官方仓库](https://github.com/BUAA-IRIP-LLM/ToolSpectrum)含 `api`、`data`、`prompts`。README 未给出完整评测运行流程；所查根目录未见独立许可文件。

<a id="benchmark-memsim"></a>
### B36. MemSim / MemDaily · 合成个人记忆评测

[MemSim: A Bayesian Simulator for Evaluating Memory of LLM-based Personal Assistants](https://arxiv.org/abs/2409.20163) — 2024 预印本；v1，2024-09-30。

**核验日期 / 阅读范围**：2026-11-01；[v1](https://arxiv.org/html/2409.20163v1) §3 方法、§4 数据质量与 §5 benchmark 相关段落；官方 README 与根目录。

- **输入 → 输出**：合成用户消息流及个人问题 → 文本答案或单选答案；另提供所需消息的检索标注。
- **测量**：区分回答与检索能力，涵盖单跳、多跳、比较、聚合、后处理及噪声；比较全文、近期、检索、无记忆与 oracle 等设置，主 backbone 为 GLM-4-9B。无关帖子比例不同的 MemDaily 设置不可混报。
- **边界**：贝叶斯关系网络与结构化 hints 提高生成一致性，但人工抽查不是全量无误保证。合成事实 QA 不证明真人长期偏好理解或工具执行。
- **资源**：[官方代码 / 数据](https://github.com/nuster1128/MemSim)包含生成器、benchmark 与 `data_generation/final_dataset/memdaily.json`；README 记录 2,954 条轨迹 / 问题、26,003 条消息。代码 / 数据许可未核实；论文 CC BY 4.0 不自动覆盖它们。

<a id="benchmark-ms-tod"></a>
### B37. MS-TOD · 跨会话任务意图与槽位

[MemGuide: Intent-Driven Memory Selection for Goal-Oriented Multi-Session LLM Agents](https://ojs.aaai.org/index.php/AAAI/article/view/40313) — AAAI 2026；2026-03-14 出版。与 M25 同一论文。

**核验日期 / 阅读范围**：2026-11-01；[arXiv v2](https://arxiv.org/html/2505.20231v2) Dataset、MemGuide、Experiments 相关段落，正式出版记录 / PDF 的资源链接；官方 README 与根目录。

- **输入 → 输出**：用户历史会话、当前对话与 QA 记忆 → 推进或确认当前任务的回复。
- **测量**：GPT-4 judge、Joint Goal Accuracy、完成轮数、成功率与人工质量评分。论文报告 132 personas、956 task goals；官方 README 记录 2,860 sessions。
- **边界**：基于 SGD 种子与 GPT-4 生成，每任务构造三个时间有序会话，人工验证；每 session 简化为单 service / intent。槽位与确认式对话的成功不等于真实预订、支付或长周期真人效用。
- **版本 / 资源**：2505.20231v1（2025-05-26）题为 *Bridging the Long-Term Gap: A Memory-Active Policy for Multi-Session Task-Oriented Dialogue*，v2（2025-08-13）改为 MemGuide，不能重复计数。[官方代码 / 数据](https://github.com/Elvin-Yiming-Du/MS_TOD_Memory)；未见根目录许可，代码与数据的再利用条款未核实。

<a id="benchmark-prefdisco"></a>
### B38. PrefDisco · 主动发现沟通偏好

[PrefDisco: Benchmarking Proactive Personalized Reasoning](https://arxiv.org/html/2510.00177v2) — [ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/82d50077a0e140b524a18f380c95d55a-Abstract-Conference.html)；查阅 arXiv v2，2026-03-04。v1 题名为 *Personalized Reasoning: Just-in-time Personalization and Why LLMs Fail at It*。

**核验日期／实际阅读范围**：2026-11-01；v2 §2 偏好建模与指标、§3 基准构造、§4 实验设置相关段落及 Limitations；arXiv 版本记录与作者 README。 非全文逐项通读；未安装、运行或复现实验。

- **评什么**：将静态推理题转换为冷启动多轮任务，以生成画像和被动用户模拟器考察询问、偏好发现与回答适配；PrefAlign 与题目正确率分别报告。
- **边界**：主要测沟通偏好，不是内容偏好、长期偏好变化或真人效用；不覆盖过度个性化与迎合行为。
- **资源**：[作者代码](https://github.com/stellalisy/PrefDisco)提供构造、下载与评测入口；未确认仓库复用许可。当前 README 的 PEP 扩展不能直接视为所读 v2 的实验；先前 workshop 版本关系未核实。

<a id="benchmark-latent-information"></a>
### B39. Latent Information Discovery · 通过对话揭示隐藏偏好

[Do LLMs Recognize Your Latent Preferences?](https://arxiv.org/html/2510.17132v1) — arXiv v1，2025-10-20。

**核验日期／实际阅读范围**：2026-11-01；v1 §3 任务与评测协议、附录 A 的 judge／用户比较相关说明、附录 D 数据来源；arXiv 版本记录。 非全文逐项通读；未安装、运行或复现实验。

- **评什么**：20 Questions、个性化问答与摘要；用户、助理、judge 三角色，报告满足全部隐藏偏好的成功率及平均停止轮数；失败样本按轮次上限计入后者。
- **边界**：用户与 judge 均由 GPT-4o 模拟；偏好固定且用户如实回应。猜物游戏是信息发现诊断，不等于个性化应用；模型判分不证明真人满意度。
- **资源**：论文附录给出数据构造与来源；问答生成沿用的 PrefEval 代码有 CC-BY-NC-4.0 限制，摘要文档来源条款各异。未核实作者完整代码／数据发布，不能据此断言没有资源。

<a id="benchmark-pdr-bench"></a>
### B40. PDR-Bench · 研究报告是否适合这个用户

[Towards Personalized Deep Research: Benchmarks and Evaluations](https://arxiv.org/html/2509.25106v3) — ICLR 2026；查阅 v3，2026-03-04。

**核验日期／实际阅读范围**：2026-11-01；v3 §3 数据构造、§4 PQR 评测相关段落、附录 A 限制及 B.1–B.2 设置／子集选择；作者 README、根目录与 LICENSE。 非全文逐项通读；未安装、运行或复现实验。

- **评什么**：50 个研究任务、25 个志愿者画像，构成 250 个任务—用户配对；PQR 分别评价个性化、内容质量和事实／引用可靠性。
- **边界**：结构化画像来自真人，但动态交互由专业标注员模拟。中文采集后提供英文版本；附录描述 250→150→50 的筛选，不能把总规模当成全部实测覆盖。报告适配不等于安全执行或长期真人效用。
- **资源**：[作者代码与数据](https://github.com/OPPO-PersonalAI/PersonalizedDeepResearchBench)，根许可 Apache-2.0；需模型与检索 API，第三方资产另查条款。

<a id="benchmark-personalens"></a>
### B41. PersonaLens · 多领域个性化对话

[PersonaLens: A Benchmark for Personalization Evaluation in Conversational AI Assistants](https://aclanthology.org/2025.findings-acl.927/) — Findings ACL 2025；查阅 [arXiv v1](https://arxiv.org/html/2506.09902v1)，2025-06-11。

**核验日期／实际阅读范围**：2026-11-01；v1 §2 画像／任务／模拟协议、§3 实验设置、§4 评测相关段落及 Limitations；ACL 出版记录、作者 README 与 LICENSE.md。 非全文逐项通读；未安装、运行或复现实验。

- **评什么**：111 项任务、20 个领域；模拟用户与 judge 评价个性化、任务完成、自然度与连贯性。
- **边界**：1,500 个画像采用 PRISM 真人统计属性，但偏好、历史摘要和情境由 LLM 生成；不是 1,500 位真人的助理使用实验。§3 明确全部实验仅随机抽样 50 个画像，包含 3,283 单域及 813 多域对话；构建规模不能当作实测规模。预订、购买仅为对话模拟，没有真实系统执行；人口属性条件化还可能引入刻板印象。
- **资源**：[作者代码与数据](https://github.com/amazon-science/PersonaLens)，已核验 `LICENSE.md` 为 **CC-BY-NC-4.0**；运行依赖 Amazon Bedrock 权限。

<a id="benchmark-user-fingertip"></a>
### B42. User FingerTip · 从模糊指令恢复应用与内容偏好

[Me-Agent: A Personalized Mobile Agent with Two-Level User Habit Learning for Enhanced Interaction](https://arxiv.org/html/2601.20162v1) — arXiv v1，2026-01-28；与 M29 为同一论文。

**核验日期／实际阅读范围**：2026-11-01；v1 §3 User FingerTip 构造与统计、§5.1–5.2 指标与结果及表 3、Limitations；arXiv 版本记录、作者仓库根目录与 README。 非全文逐项通读；未安装、运行或复现实验。

- **评什么**：在 FingerTip 基础上删除应用名或模糊化内容；报告 60 用户、33 应用、300 条 Type I 与 267 条 Type II 指令，分别测应用选择、内容偏好与执行表现。
- **边界**：总条数与“每用户 15 条训练、5 条测试”的表述需进一步澄清，不能称未见用户测试。表 3 应用选择率 100% 不等于任务全成功，其 TSR 为 80%／50%；未建立长期真人部署证据。
- **资源**：[作者仓库](https://github.com/Gianthaha/personal-mobile-agent)标 MIT，已有代码目录，但 README 仍预告更新；完整基准发布与可复现性未确认。

<a id="benchmark-userville"></a>
### B43. UserVille · 隐含任务与交互偏好

与 M30 同篇，不另计。[原文](https://arxiv.org/html/2511.02208v2)阅读范围及资源限制同 M30。

- **自动部分**：修改任务描述并用偏好条件化 LLM 模拟用户；20种交互偏好含8种留出。代码定位用 F1，BrowseComp-Plus 用 EM；个性化指标只统计提问会话。
- **真人部分**：v2 有33名程序员、300次任务评估；任务来自 SWE-Bench，参与者可见题目与标准补丁，不是自然长期个人部署。满意度 PPP 3.75、GPT-5 3.79；报告解决率71%、85%，不能只宣传满意度接近。
- **解释**：表1综合均值62.04对 Seed-OSS-36B 45.32；+16.72 指这个比较，不是相对 GPT-5 的提升，更不是任务成功率百分点。

<a id="benchmark-personalwab"></a>
### B44. PersonalWAB · 购物历史条件化函数任务

与 M31 同篇，不另计。[原文](https://arxiv.org/html/2410.17236v2)阅读范围及资源限制同 M31。

- **数据与环境**：抽样1,000名 Amazon 用户的真实历史/评论；画像、请求和交互用户由模型合成。任务为搜索、推荐、评论生成，环境是简化函数，不是浏览器 GUI 或真实交易；成功调用后即假定评论已发布。
- **解释**：function accuracy 检查工具与参数格式，result accuracy 对商品使用排名、对评论使用嵌入相似度，不能合成通用成功率。
- **边界**：作者称历史按80/10/10划分，又写画像使用全部历史；复现需审计预处理，当前不能断言已证实泄漏。模拟器、推断画像与未验证隐私保护均限制真实助理结论。

<a id="transferable-memory-evaluation"></a>
## 评测 B：可迁移记忆与连续任务

以下研究增量记忆或跨会话任务依赖，属于**可迁移的通用能力评测**；不能因此称为完整的个人助理或长期真人实验。

<a id="benchmark-memoryagentbench"></a>
### B12. MemoryAgentBench · 增量记忆与冲突更新

[Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions](https://arxiv.org/html/2507.05257v1) — 2025 预印本；官方仓库标 ICLR 2026。本条固定 v1，2025-07-07。

**核验日期 / 阅读范围**：2026-10-31；论文摘要、增量构建描述、附录 A / 表 5 的任务与指标；官方 README 和数据卡。

- **输入 → 输出**：逐块摄入长材料，再提出查询 → 事实答案、意图标签、推荐或摘要；例如用后来冲突的事实更新记忆，或从例子学银行意图分类。
- **测量**：v1 分 accurate retrieval、test-time learning、long-range understanding、conflict resolution；子任务分别用 SubEM、Recall、accuracy、ROUGE 或模型评审。
- **边界**：通用记忆组件评测，不是完整个人助理。分块摄入不等于持续真人互动，冲突更新不等于隐私删除；后续版本的 selective forgetting 命名不能静默替换 v1 设置或成绩。
- **资源**：[官方代码](https://github.com/HUST-AI-HYZ/MemoryAgentBench)、[数据卡](https://huggingface.co/datasets/ai-hyz/MemoryAgentBench)均标 MIT；重组数据的上游条款仍须逐一核对。

<a id="benchmark-memoryarena"></a>
### B13. MemoryArena · 跨会话依赖的行动闭环

[Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks](https://arxiv.org/html/2602.16313v2) — 查阅 v2，2026-09-17；项目名 MemoryArena。

**核验日期 / 阅读范围**：2026-10-31；论文摘要、§3.1 任务构造、§4.2 指标；项目页、代码根目录和数据卡。

- **输入 → 输出**：分会话的依赖子任务、环境观察及先前经历 → 后续行动与答案；例如后买商品须兼容先前商品，或多人旅行积累约束。v2 有 701 个任务组，覆盖购物、旅行、渐进搜索、数学和物理。
- **测量**：整体成功率 SR、完成子任务比例 PS、约束级 soft progress（sPS）；局部高分不等于全链成功。
- **边界**：通用连续任务，部分贴近个人助理；考察记忆如何影响行动，而非仅历史 QA，但不证明数月真人使用可靠性。
- **资源**：[项目页](https://memoryarena.github.io/)、[官方代码](https://github.com/ZexueHe/MemoryArena)、[数据](https://huggingface.co/datasets/ZexueHe/memoryarena)。数据 CC BY 4.0；代码 README 标 preview，所查根目录未见明确 LICENSE。数据许可不能代替代码许可；未验证 preview 与论文 v2 完全一致。

<a id="execution-evaluation"></a>
## 评测 C：任务执行与交互能力

以下可帮助测个人助理的“动手能力”，但多数属于**通用 Agent、网页 / GUI 或服务场景评测**，不能统称 personal-specific benchmark。AppWorld 有模拟个人应用与人物数据，仍不是长期真人个性化测试。

<a id="benchmark-assistantbench"></a>
### B14. AssistantBench · 现实网页信息任务

[AssistantBench: Can Web Agents Solve Realistic and Time-Consuming Tasks?](https://aclanthology.org/2024.emnlp-main.505/) — EMNLP 2024。

**核验日期 / 阅读范围**：2026-10-31；论文摘要与 §3.4 自动评测相关段落；官方项目页、代码入口与数据卡。

- **输入 → 输出**：需要网页查找、整合的任务 → 字符串、数值或结构化答案；原始集 214 个任务。
- **测量**：答案 accuracy、回答率、precision、exact match；不是只看 Agent 是否宣称完成。
- **边界**：侧重找信息而非真实账号写操作；网页变化和答案时效影响复现，不测长期偏好维护。
- **资源**：[官方项目页](https://assistantbench.github.io/)、[代码](https://github.com/oriyor/assistantbench)、[数据](https://huggingface.co/datasets/AssistantBench/AssistantBench)。

<a id="benchmark-gaia"></a>
### B15. GAIA · 通用助理综合解题

[GAIA: a benchmark for General AI Assistants](https://arxiv.org/abs/2311.12983) — 2023 预印本。

**核验日期 / 阅读范围**：2026-10-31；论文摘要与 §3.2 评测相关段落；官方数据卡的任务、分组及门控/再分发说明。

- **输入 → 输出**：自然语言问题，部分带文件 / 多模态材料 → 简短、可核验答案；原论文 466 题、三档难度。
- **测量**：按答案类型规范化后的近似 exact match，涉及浏览、工具、多模态与推理。
- **边界**：单次问题的正确性不是个性化、后台主动性或长期任务可靠性；公开开发集与隐藏答案测试集分开。
- **资源**：[官方数据卡与榜单入口](https://huggingface.co/datasets/gaia-benchmark/GAIA)。下载有门控条件，官方要求不要把题目集再分发成可爬取内容。

<a id="benchmark-appworld"></a>
### B16. AppWorld · 跨应用个人数字任务沙箱

[AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents](https://arxiv.org/abs/2407.18901) — ACL 2024。

**核验日期 / 阅读范围**：2026-10-31；论文任务概述、§3.2 评测与 §7 局限相关段落；官方项目页、README 及许可说明。

- **输入 → 输出**：用户指令、模拟应用初始状态及 API 文档 → 交互式代码 / 调用改变应用状态；原论文 750 任务、9 类应用。
- **测量**：数据库状态测试；TGC 要求单任务所有测试通过，SGC 要求同场景的所有任务变体通过。
- **边界**：模拟 API 不是实网服务或 GUI；原始 benchmark 不等于后来的 AppWorld-UL 用户在环任务。
- **资源**：[项目页](https://appworld.dev/appworld/)、[官方代码 / 数据下载流程](https://github.com/StonyBrookNLP/appworld)。保护内容有额外加密再分发要求，见[许可说明](https://github.com/StonyBrookNLP/appworld#-license)。

<a id="benchmark-tau-bench"></a>
### B17. τ-bench · 工具、用户与规则交互

[τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](https://arxiv.org/abs/2406.12045) — 2024 预印本。

**核验日期 / 阅读范围**：2026-10-31；论文摘要、§3 reward/pass^k 定义与 §6 讨论相关段落；官方 README 的过时任务和迁移警示。

- **输入 → 输出**：模拟用户对话、领域规则与 API → 对话和工具操作；原始任务围绕航空 / 零售服务。
- **测量**：终态数据库与目标状态比较，并检查要求告知用户的信息；**pass^k 是重复 k 次都成功的可靠性指标，不是 pass@k 的“至少成功一次”**。
- **边界**：客服侧领域流程不是长期私人助理；终态正确不保证每一步都合规，模拟用户会影响结果。
- **资源**：[原论文代码 / 数据](https://github.com/sierra-research/tau-bench)。官方已明确标注该仓库任务过时，并从 README 导向 τ³-bench；复现实验与运行新版必须分别标版本。

<a id="benchmark-webarena"></a>
### B18. WebArena · 可复现网页操作

[WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854) — 2023 预印本，2024 修订版。

**核验日期 / 阅读范围**：2026-10-31；论文摘要与 §3 任务/评测相关段落；官方 README 的版本、环境与实现说明。

- **输入 → 输出**：高层自然语言意图与网页观察 → 浏览器操作、页面终态或文字答案；原论文 812 个任务。
- **测量**：以功能结果为核心，检查答案、导航结果或页面状态，而非固定点击序列。
- **边界**：自托管站点利于复现，但不覆盖所有真实网站、登录障碍与持续个性化；不可直接代表任意浏览器任务成功率。
- **资源**：[官方代码、环境与评测](https://github.com/web-arena-x/webarena)。固定任务修订版和网站镜像，避免混合不同环境结果。

<a id="benchmark-osworld"></a>
### B19. OSWorld · 电脑操作与跨应用工作流

[OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://arxiv.org/abs/2404.07972) — 2024。

**核验日期 / 阅读范围**：2026-10-31；论文摘要及引言中的任务/状态评测概述；官方项目页的版本与资源说明。

- **输入 → 输出**：任务、初始桌面 / 文件状态、截图或 accessibility tree → 电脑操作与最终产物；原论文 369 个任务。
- **测量**：任务特定的 execution-based evaluator 检查结果；观察方式、动作空间、步数预算都影响可比性。
- **边界**：不测长期用户关系；依赖 VM / 软件版本。原版、OSWorld-Verified 和 OSWorld 2.0 不能混报；部分云文档任务另需配置。
- **资源**：[官方项目页及版本入口](https://os-world.github.io/)、[代码 / 任务](https://github.com/xlang-ai/OSWorld)。

<a id="benchmark-androidworld"></a>
### B20. AndroidWorld · 动态手机任务

[AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents](https://arxiv.org/abs/2405.14573) — 2024 预印本，2025 修订版。

**核验日期 / 阅读范围**：2026-10-31；论文摘要、§3.4 状态奖励与附录 A 局限相关段落；官方项目页及 README。

- **输入 → 输出**：自然语言任务、模拟器状态与屏幕 / 界面树 → Android 操作；116 个任务模板覆盖 20 个应用并随机化参数。
- **测量**：初始化、成功检测与清理逻辑直接检查设备状态；参数变化可测试稳健性。
- **边界**：116 是基础任务数，不是随机实例总数；以开源 / 系统应用为主，不保证对商业 App、不同手机或中文界面泛化。
- **资源**：[官方论文项目页](https://google-research.github.io/android_world/)、[环境 / 任务代码](https://github.com/google-research/android_world)。

<a id="benchmark-ask-before-plan"></a>
### B30. Ask-before-Plan · 缺信息或不可行时先澄清

[Ask-before-Plan: Proactive Language Agents for Real-World Planning](https://aclanthology.org/2024.findings-emnlp.636/) — Findings of EMNLP 2024；方法见 M18。

**核验日期 / 阅读范围**：2026-11-01；摘要、§5.1–5.2 评测及附录 B.2–B.3；官方 README；待审。

- **输入 → 输出**：对话与环境反馈 → 澄清问题、工具调用及旅行计划。
- **测量**：澄清判断 / 问题质量、调用正确性、约束与最终通过率分别报告。
- **边界**：子任务评测给后续模块正确的前序结果；整体框架的最终规划也使用 ground-truth conversation（附录 B.3），不能当作完全自由运行的端到端成绩。这是交互规划，不是长期画像学习。
- **资源**：[官方代码 / 评测](https://github.com/magicgh/Ask-before-Plan)、[数据](https://huggingface.co/datasets/magicgh/Ask-before-Plan)。README 声明代码 MIT、数据与环境 CC BY 4.0；环境需另下载，未安装验证。

<a id="safety-evaluation"></a>
## 评测 D：隐私规范与对抗安全

分别看“本来就不该分享的信息”和“外部内容诱导的越权行为”。这些评测提供特定风险证据，**不构成完整隐私、安全或合规认证**；低违规率必须与任务效用一起看。

<a id="benchmark-privacylens"></a>
### B21. PrivacyLens · 没有攻击者也会泄漏

[PrivacyLens: Evaluating Privacy Norm Awareness of Language Models in Action](https://arxiv.org/html/2409.00138v3) — NeurIPS 2024 Datasets and Benchmarks；查阅 v3，2025-03-14。

**核验日期 / 阅读范围**：2026-10-31；论文摘要、§1 风险例子、§3.3；官方多层评测 README 与数据卡。

- **输入 → 输出**：通信指令及含敏感信息的模拟工具轨迹 → 最后发送 / 发帖动作；例如可读取私人求职安排，不代表应把它写进给主管的邮件。
- **测量**：隐私规范问答准确率、最终动作泄漏率与 helpfulness 分开报告；不能通过拒绝一切换取低泄漏率。
- **边界**：关注个人通信的上下文隐私，不需要攻击者。主要补全预构建轨迹，不是完整自主执行；美国规范、合成场景与模型 judge 限制泛化，也不等于完整隐私合规。
- **资源**：[官方代码与构建流程](https://github.com/SALT-NLP/PrivacyLens)为 MIT；[官方数据](https://huggingface.co/datasets/SALT-NLP/PrivacyLens)为 CC BY 4.0，代码与数据许可不能混用。

<a id="benchmark-agentdojo"></a>
### B22. AgentDojo · 工具结果中的不可信指令

[AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://arxiv.org/html/2406.13352v3) — NeurIPS 2024；查阅 v3，2024-11-24。

**核验日期 / 阅读范围**：2026-10-31；论文摘要、§3.4 指标；官方 README 和许可标记。

- **输入 → 输出**：合法任务、工具及可被攻击者修改的工具返回内容 → 邮件、银行或旅行沙箱中的操作与终态。原论文有 97 个用户任务、629 个安全测试用例。
- **测量**：正常任务效用、受攻击时任务效用与 targeted ASR 同时报；既未执行攻击又未完成用户任务，不能算好助理。
- **边界**：通用工具 Agent 间接注入环境，不是个人化评测；不覆盖全部隐私、权限、长期记忆投毒或多代理风险。本次没有生成或运行攻击。
- **资源**：[官方环境、任务和评测](https://github.com/ethz-spylab/agentdojo)，MIT。项目可扩展且 API 仍演进；固定 suite、攻击集合、工具 schema、模型与预算再比较。

<a id="benchmark-agentcibench"></a>
### B24. AgentCIBench · 跨应用分享与收件人边界

[Capable but Careless: Do Computer-Use Agents Follow Contextual Integrity?](https://arxiv.org/html/2606.23189v2) — 初读 v2，2026-09-10；[作者提交的 arXiv 元数据](https://arxiv.org/abs/2606.23189)标 EMNLP 2026 Main。

**核验日期 / 阅读范围**：2026-10-31；v2 摘要、§3 指标与失败分类相关段落；官方 README 和数据卡的资源 / 许可说明。文献初读，不是安装或实测。

- **输入 → 输出**：个人应用状态、未充分说明的任务与指定收件人 → 对外可见的消息、日程或帖子；关注界面相邻信息混入、模糊任务下过度分享与收件人不匹配。
- **测量**：效用 U、泄漏 L、拒绝 R 及参与条件下泄漏 L/(1−R)。§3 明确使用确定性匹配与 LLM 改写检测的混合评分，不能因摘要称“deterministically scored”就把全流程写成纯确定性。
- **边界**：没有攻击者也可能发生上下文隐私违规；这是精选披露压力测试，不代表总体真实发生率或全面法律合规。最终披露与端到端 UI 执行设置须分开，不能靠拒绝全部任务换取低泄漏。
- **资源**：[官方代码](https://github.com/UKPLab/emnlp2026-agentcibench)、[官方数据](https://huggingface.co/datasets/UKPLab/agentcibench)。代码 Apache-2.0；数据 / 场景池 CC BY 4.0。旧 arxiv2026-agentcibench 路径与现行仓库名称不同，复现应固定版本；未运行环境或生成攻击。

<a id="benchmark-pasb"></a>
### B27. PASB · 迎合如何写入长期状态

[Agents Don't Just Agree, They Remember: Benchmarking Persistent Sycophancy in Self-Improving Personal Agents](https://arxiv.org/html/2607.10526v5) — 2026 预印本；v5，2026-10-10。

**核验日期 / 阅读范围**：2026-11-01；摘要、§3.3、§4、§5.1 及附录 A.8、A.10；官方 README、LICENSE。

- **输入 → 输出**：含用户主张的五轮对话 → 清除会话后，仅凭留下的状态回答三个新问题；1,600 个任务，Hermes-Agent / OpenClaw 两套框架。
- **测量**：Commit% 记录目标论断是否写入可供后续读取的持久状态；judge 另评后续迎合等风险。Max-FR@3 指三答中任一达到失败阈值；downstream failure 是四个逐回答维度的 Max-FR@3 均值，不是六项总平均。
- **边界**：受控压力测试，不是产品总体风险率；低失败可能来自不会调用记忆工具。人工校验的 88% 是 ±1 Likert 一致，不是精确匹配。
- **资源**：[官方代码 / 数据入口](https://github.com/henrymao2004/agent-sycophancy)。代码 MIT；论文称 PASB 为 CC BY 4.0，README 要求保留 PersistBench / ELEPHANT 上游条款，数据许可链仍需确认。未运行。

<a id="benchmark-authorizationbench"></a>
### B31. AuthorizationBench · 完成任务不等于有权执行

[Act on Your Behalf, Beyond Your Authorization: Benchmarking LLM Agent Authorization Alignment](https://arxiv.org/html/2610.27548v2) — 2026 预印本；v2，2026-10-21。

**核验日期 / 阅读范围**：2026-11-01；摘要、§4.1 指标、官方 README 的资源与许可说明；待审。

- **输入 → 输出**：带授权边界的委托及沙箱状态 → 工具行动轨迹；286 个任务。
- **测量**：结合完整轨迹与状态证据，分别判断任务完成和越权。
- **边界**：通用委托边界评测，不是个性化规划方法；模拟服务与 judge 不代表真实部署风险率。
- **资源**：[官方代码 / 任务](https://github.com/PEACH-Research-Lab/AuthorizationBench)。README 声明原创软件 / 基准制品 MIT，第三方材料另计；公开 6,864 份判定但仅保留 4,981 份原始轨迹，不能视为完整轨迹全集。未运行。

<a id="memory-methods"></a>
## 方法 A：记忆与长期状态

这些条目解释可借鉴的系统机制，不把研究原型写成已验证的个人助理产品。

<a id="method-memorybank"></a>
### M1. MemoryBank · 更新、强化与遗忘

[MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://arxiv.org/abs/2305.10250) — 2023 预印本。

**核验日期 / 阅读范围**：2026-10-31；论文摘要；官方 README 的机制、评测数据与模型说明，以及 LoRA 发布页。

- **核心**：存储 / 检索对话记忆、汇总用户信息，并用受遗忘曲线启发的机制强化或淡化记忆。
- **关联与边界**：直接面向长期对话伙伴；SiliconFriend 实验不是工具执行系统，也不是心理服务有效性的临床证据。
- **资源**：[代码与中英文评测数据](https://github.com/zhongwanjun/MemoryBank-SiliconFriend)、[ChatGLM / BELLE LoRA checkpoint 发布页](https://github.com/zhongwanjun/MemoryBank-SiliconFriend/releases/tag/LoRA_checkpoint)。适配器不等于底座模型，许可分别核对。

<a id="method-memgpt"></a>
### M2. MemGPT · 分层记忆与上下文管理

[MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) — 2023 预印本，2024 修订版。

**核验日期 / 阅读范围**：2026-10-31；论文摘要；研究项目页、数据入口，以及 Letta README 的现行源码/历史版本说明和 letta-code 入口。

- **核心**：借鉴操作系统内存分层，在有限上下文与外部记忆间调度信息，用控制流管理多轮执行。
- **关联与边界**：论文含多会话聊天与长文档实验；“虚拟上下文”不意味着无限、无损、无需成本的记忆。
- **资源**：[论文项目页 / 实验数据入口](https://research.memgpt.ai/)、[历史 MemGPT / Letta 入口](https://github.com/letta-ai/letta)、[现行 Letta Code 源码](https://github.com/letta-ai/letta-code)。旧入口的 README 指向 letta-code，并将 V1 服务端保留于 archive 分支；复现论文须另定位当时版本，不能把现行产品或退休 V1 自动等同论文实现。

<a id="method-a-mem"></a>
### M3. A-MEM · 关联笔记与记忆演化

[A-MEM: Agentic Memory for LLM Agents](https://arxiv.org/abs/2502.12110) — NeurIPS 2025。

**核验日期 / 阅读范围**：2026-10-31；论文摘要与 §4.2 数据/指标相关段落；官方两仓库的用途说明。

- **核心**：以 Zettelkasten 式笔记组织记忆，为新信息生成属性与关联，并按新信息更新已有记忆表示。
- **关联与边界**：可用于助理的可关联记忆；长对话 QA 实验不证明真实任务完成或记忆修改始终正确。
- **资源**：[论文评测代码](https://github.com/WujiangXu/A-mem)、[可集成系统代码](https://github.com/WujiangXu/A-mem-sys)。两仓库用途不同；是外接记忆方法，不是一个新底座模型。

<a id="method-mem0"></a>
### M4. Mem0 · 提取、整合与检索

[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://arxiv.org/abs/2504.19413) — 2025 arXiv 论文版。

**核验日期 / 阅读范围**：2026-10-31；2025 论文摘要；当前官方 README 与研究页，仅用于区分论文和后续项目状态。

- **核心**：从对话提取重要信息，整合更新并检索；论文另有图记忆变体。
- **关联与边界**：适用于跨会话个人上下文；论文基于 LoCoMo 的正确性、延迟与 token 评估，不能外推所有任务或所有部署。
- **资源**：[官方项目代码](https://github.com/mem0ai/mem0)。项目、托管服务与算法已持续演进；本文链接的是 2025 方案，不将当前宣传数字作为该论文的独立复现结果。

<a id="method-zep"></a>
### M5. Zep / Graphiti · 时间有效性与历史保留

[Zep: A Temporal Knowledge Graph Architecture for Agent Memory](https://arxiv.org/html/2501.13956v1) — 2025 预印本；查阅 v1，2025-01-20。

**核验日期 / 阅读范围**：2026-10-31；论文摘要、§2.2.3、§3 检索接口、§4 评测概述；官方代码 README 与许可。

- **核心**：将对话或业务事件转成带时间的实体和关系；新冲突关系使旧边失效，但保留历史。查询返回有时间有效范围的上下文，再交给回答模型。
- **关联与边界**：可借鉴个人事实 / 偏好版本管理；论文在 DMR、LongMemEval 测 QA 正确性与延迟。模型可能误判冲突；失效不是物理删除，QA 提升不证明工具任务成功。
- **资源**：[Graphiti 官方代码](https://github.com/getzep/graphiti)，Apache-2.0；[官方 Zep / Graphiti 区分](https://help.getzep.com/zep-vs-graphiti)。公开引擎、完整托管服务及 2025 论文配置不能互相等同，也不是新底座模型发布。

<a id="method-memos"></a>
### M6. MemOS · 把记忆当作可治理资源

[MemOS: A Memory OS for AI System](https://arxiv.org/html/2507.03724v1) — 本条固定 2025 预印本 v1，2025-07-04。

**核验日期 / 阅读范围**：2026-10-31；v1 摘要、§4.2 元数据、§5.5 治理接口相关片段、§6 评测概述；当前官方 README 与许可。

- **核心**：MemCube 将记忆内容与来源、版本、访问策略及生命周期元数据封装，提出统一调度明文、激活态和参数记忆。历史、查询及记忆操作产生更新后的记忆资源和推理上下文。
- **关联与边界**：为长期助理的记忆治理提供架构；v1 有 LoCoMo QA、检索与 KV 加速实验。治理设计不等于经验证的删除、权限或跨租户隔离保证，不能把愿景全部当成已实现功能。
- **资源**：[官方仓库](https://github.com/MemTensor/MemOS)，Apache-2.0。当前 README 为 MemOS 2.0 Stardust，不是论文冻结代码；复现应另定位 MemOS-0630 配置，不沿用当前宣传分数。LoCoMo 等数据各有上游条款。

<a id="agent-methods"></a>
## 方法 B：规划、工具、反思、主动性与协作

其中既有直接研究主动助理的工作，也有可借鉴的通用技能学习与编排方法。外部经验积累不等于已解决参数级持续学习，多代理也不自动更可靠。

<a id="method-generative-agents"></a>
### M7. Generative Agents · 记忆—反思—规划

[Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) — 2023。

**核验日期 / 阅读范围**：2026-10-31；论文摘要；官方 README 的模拟环境、代码范围与模型调用说明。

- **核心**：记录经历、检索相关记忆，形成高层反思并据此规划行为；在 25 个虚拟角色的小镇中研究互动。
- **关联与边界**：为长期状态与计划提供结构思路；目标是可信的人类行为模拟，不是替真实用户办事或履行授权的证据。
- **资源**：[官方模拟器、环境与回放说明](https://github.com/joonspk-research/generative_agents)。依赖外部模型调用，不应当作独立模型权重发布。

<a id="method-react"></a>
### M8. ReAct · 交替推理与行动

[ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) — 2022 预印本；ICLR 2023。

**核验日期 / 阅读范围**：2026-10-31；论文摘要及 arXiv 版本说明；官方 README 与代码/提示目录。

- **核心**：交替生成任务推理、工具动作，并使用返回观察修正后续步骤。
- **关联与边界**：通用工具执行循环的基础；原实验为问答、事实核验与交互环境，不自带长期记忆、权限治理或全天候调度。
- **资源**：[官方代码、提示样例与实验 notebook](https://github.com/ysymyth/ReAct)。主要为 prompting 实现，不是完整个人助理。

<a id="method-reflexion"></a>
### M9. Reflexion · 把失败反馈留给下一次

[Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) — NeurIPS 2023。

**核验日期 / 阅读范围**：2026-10-31；论文摘要；官方 README 的实验、日志与运行说明。

- **核心**：把任务反馈变为语言反思，保存在 episodic memory 中供后续尝试使用，而非直接更新模型权重。
- **关联与边界**：可借鉴任务重试与经验记忆；效果依赖反馈质量与重试预算，不保证“想一想”就能纠错或持续自我提升。
- **资源**：[官方代码、实验日志与示例](https://github.com/noahshinn/reflexion)。原评测含决策、推理与编码，不是长期私人助理研究。

<a id="method-toolformer"></a>
### M10. Toolformer · 学会何时调用工具

[Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) — 2023 预印本。

**核验日期 / 阅读范围**：2026-10-31；论文摘要与 §7 局限；Meta 官方论文页及其提供的资源入口。

- **核心**：少量 API 示范引导模型生成候选调用，按对后续语言预测的帮助筛选，再用增强语料训练。
- **关联与边界**：说明工具调用可被学习；原方法不支持链式或交互式工具使用，不能当成完整多步 Agent。
- **资源**：[官方研究页](https://ai.meta.com/research/publications/toolformer-language-models-can-teach-themselves-to-use-tools/)。所查论文 / 官方页未给出对应完整代码、训练数据和模型权重入口；不将第三方复现标作官方发布。

<a id="method-proactive-agent"></a>
### M11. Proactive Agent · 从活动预测可接受的帮助

[Proactive Agent: Shifting LLM Agents from Reactive Responses to Active Assistance](https://arxiv.org/abs/2410.12361) — 2024 预印本；ICLR 2025，与 B6 同一论文。

**核验日期 / 阅读范围**：2026-10-31；与 B6 同次核验：论文摘要、官方 README 的流程/发布说明及权重文件列表。

- **核心**：以活动轨迹和人类接受 / 拒绝标注训练 reward model，结合环境生成数据，再训练主动提出帮助的 Agent。
- **关联与边界**：直接研究主动助理；预测用户需要不等于被授权替用户行动，部署还需处理活动采集隐私与误打扰。
- **资源**：[代码 / 数据 / 评测](https://github.com/thunlp/ProactiveAgent)、[官方链接的 Agent 与 Reward Model 权重](https://huggingface.co/YancyLee/ProactiveAgent/tree/main)。权重、底座与代码许可分别确认。

<a id="method-memoproagent"></a>
### M12. MemoProAgent · 用记忆决定是否值得打扰

[MemoProAgent: Toward Memory-Driven Proactive Assistance](https://arxiv.org/html/2610.22671v2) — 2026 预印本 v2，2026-10-21；与 B11 同一论文。

**核验日期 / 阅读范围**：2026-10-31；与 B11 同次核验：v2 摘要、§3.3 指标、方法概述；官方 README 及 LICENSE。

- **核心**：用图记忆组织个人历史，结合当前视频活动检索相关经历，再以打扰价值门控决定何时向生成器提供记忆、何时提醒；论文另有 RL 后训练阶段。
- **关联与边界**：直接研究无需显式提问的主动助理。MemoProBench 测提醒内容、时机和重复干扰；论文构造历史不是长期真人部署，推断需要也不是执行授权。
- **资源**：[官方推理 harness](https://github.com/facebookresearch/Memo-Pro-Agent)为 CC BY-NC 4.0；[历史数据（受限）](https://huggingface.co/datasets/facebook/MemProBench)据官方 [README 数据说明](https://github.com/facebookresearch/Memo-Pro-Agent#data-and-reproducibility)当前为 private，须有获授权的 Hugging Face 访问权限。本次未取得下载访问，独立数据许可仍未确认；[Ego4D 视频](https://ego4d-data.org/)须另行申请并遵循其条款。公开推理代码不等于完整 RL 训练代码或权重复现包。

<a id="method-voyager"></a>
### M13. Voyager · 可复用的可执行技能

[Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/html/2305.16291v2) — 查阅 2023 预印本 v2，2023-10-19。

**核验日期 / 阅读范围**：2026-10-31；论文摘要、代码迭代描述、§3.1 与实验任务概述；官方 README 及许可。

- **核心**：Minecraft 世界状态、自动课程目标及已有技能 → 可执行代码；借环境反馈、错误和自验证迭代，成功技能存入库供后续任务复用。
- **关联与边界**：通用具身 / 游戏方法，可借鉴技能积累；评测探索物品、里程碑、移动范围和新任务迁移。lifelong learning 主要累积外部技能，不是持续更新底座权重；不能从 Minecraft 外推邮件、日历或真实电脑效果。
- **资源**：[官方代码、prompt 与技能库](https://github.com/MineDojo/Voyager)，MIT；Minecraft 与模型 / API 分别授权。原实验使用当时的 GPT-4 / GPT-3.5 API，更换模型不属于严格复现。

<a id="method-expel"></a>
### M14. ExpeL · 从多任务经历提炼经验

[ExpeL: LLM Agents Are Experiential Learners](https://arxiv.org/html/2308.10144v3) — AAAI 2024；查阅 v3，2024-12-20。

**核验日期 / 阅读范围**：2026-10-31；论文摘要、§5.1 任务 / 指标 / 四折设置；官方 README 与许可。

- **核心**：从训练任务中的成功 / 失败经历提炼自然语言经验，新任务检索经验和示例来行动，不更新底座权重；重点是跨任务汇总与复用，而非只反思一次失败。
- **关联与边界**：可借鉴助理的经验记忆；评测含 Wikipedia QA / 事实核验、ALFWorld 家务和 WebShop 购物，分别用 EM、成功率、购物奖励等。四折经验增长不是长期真人持续学习，过时经验与隐私需另测。
- **资源**：[官方代码、数据目录和 prompt](https://github.com/LeapLabTHU/ExpeL)，Apache-2.0；各环境和数据集许可分别检查。无参数微调不代表无成本，轨迹采集与经验提取仍需模型调用。

<a id="method-autogen"></a>
### M15. AutoGen · 多代理对话与人类介入（历史）

[AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/html/2308.08155v2) — 查阅 2023 预印本 v2，2023-10-03。

**核验日期 / 阅读范围**：2026-10-31；论文摘要、§3 的 A1–A4 应用 / 评测及 human-in-the-loop 讨论；当前官方 README 与 legal notices。

- **核心**：将 LLM、工具执行和人类输入封装成可对话 Agent；例如数学请求经过代码、执行结果与反馈交换后产生答案。
- **关联与边界**：通用多代理编排研究，不是个人化 benchmark。MATH、检索 QA、ALFWorld、OptiGuide 使用各自指标；多 Agent 或人类在环不自动带来权限隔离、可靠授权或更低成本，仍需单代理基线与安全测试。
- **资源**：[官方仓库](https://github.com/microsoft/autogen)：代码 MIT，文档 / 其他内容 CC BY 4.0。当前 README 明确标“已归档、不再由 Microsoft 维护”；保留为研究沿革，不推荐为仍维护的生产选型。现行包结构不同于 2023 论文 API，未定位论文对应提交。

<a id="method-intu"></a>
### M17. InTU · 先说清偏好，再生成计划

[Inferring the Unspoken](https://arxiv.org/abs/2502.00858v4) — 与 B29 同一篇，勿重复计数。

**核验日期 / 阅读范围**：2026-11-01；仅 v4 摘要，待审初读。

- **机制**：先将多模态演示中的隐含偏好表述为语言，再以其为条件生成动作计划。
- **边界**：显式中间表示有助于解释与迁移，不意味着偏好推断已可靠；评测、资源和全文核验限制见 [B29](#benchmark-pbp)。

<a id="method-cep"></a>
### M18. CEP · 澄清、执行与规划分工

[Ask-before-Plan](https://aclanthology.org/2024.findings-emnlp.636/) — 与 B30 同一篇，勿重复计数。

**核验日期 / 阅读范围**：2026-11-01；摘要、评测设置及附录 B.3、官方 README 的训练和推理入口；待审。

- **机制**：澄清、执行、规划三个角色；对澄清和静态执行做轨迹微调，动态执行使用记忆回想。
- **边界**：角色分工不等于长期用户建模或执行授权；模块与整体成绩均须按各自协议解读，整体最终规划仍使用真实标注对话（附录 B.3）。资源及许可见 [B30](#benchmark-ask-before-plan)。

<a id="personalization-methods"></a>
## 方法 C：个性化与偏好学习

<a id="method-p-rlhf"></a>
### M16. P-RLHF · 从个人反馈学习偏好

[Personalized Language Modeling from Personalized Human Feedback](https://arxiv.org/html/2402.05133v3) — 2024 预印本；首发 2024-02-06，查阅 v3，2024-12-09。

**核验日期 / 阅读范围**：2026-11-01；摘要、§4.1–4.4 用户模型与 P-DPO、§5 实验相关段落；官方 README 的数据、训练与评测说明。未安装或训练。

- **核心**：联合学习轻量用户模型与 LLM；把用户文本中的显式偏好、个人比较反馈中的隐式偏好编码为用户嵌入。用户嵌入通过软提示参与生成，P-DPO 将偏好优化条件化到用户。
- **关联与边界**：个性化方法，不是 benchmark 或长期记忆系统。实验包含合成、半合成及 PRISM 真人反馈；回答比较依赖模型 judge，不证明长期真人满意度、动态偏好更新或工具执行。没有用户文本且用户 ID 未知时退回非个性化回答。
- **资源**：[官方实现](https://github.com/HumainLab/Personalized_RLHF)提供用户模型、数据处理、训练与评测入口；代码公开不代表训练已复现，上游数据和底座模型须另查条款。

<a id="method-personaagent"></a>
### M19. PersonaAgent · 用可更新的个人提示词连接记忆与行动

[PersonaAgent: Bridging Memory and Action for Personalized LLM Agents](https://aclanthology.org/2026.findings-acl.1315/) — Findings of ACL 2026；[arXiv v2](https://arxiv.org/html/2506.06254v2)，2026-05-27。早期标题 *When Large Language Model Agents Meet Personalization at Test Time* 是同一论文，不另计。

**核验日期 / 阅读范围**：2026-11-01；v1 方法相关段落、v2 §3.1 与附录 E–G、出版记录，非全文通读。

- **机制**：检索个人经历、概括稳定偏好；用用户专属系统提示词引导动作，再依据近期历史例子的文本反馈在测试时优化提示词。
- **证据**：LaMP 分类、评分与生成任务；对应 accuracy / F1、MAE / RMSE 和 ROUGE，不合成单一行动分数。
- **边界**：实际工具限于 Wikipedia 搜索和个人记忆检索；主要评测选择 100 位活跃用户，单次运行。不能推广为多应用交易或长期真人部署验证。
- **资源**：已核验论文；本次未确认作者发布的实现入口，勿用同名非作者仓库代替。

<a id="method-rlpa"></a>
### M20. RLPA · 在多轮对话中学习推断与使用画像

[Teaching Language Models to Evolve with Users: Dynamic Profile Modeling for Personalized Alignment](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2fbc1ea60e215275e823c86338417162-Abstract-Conference.html) — NeurIPS 2025；查阅 [arXiv v2](https://arxiv.org/html/2505.15456v2)，2025-12-11。

**核验日期 / 阅读范围**：2026-11-01；§2–3 方法相关段落、§4.1 与表 1；官方 README、根目录与 LICENSE，非全文通读。

- **机制**：Qwen2.5-3B 与模拟用户交互，以画像匹配和回答个性化两类奖励进行 PPO 训练；训练模型称 Qwen-RLPA。
- **证据**：ALOE 同画像格式与跨格式设置，报告平均对齐分数、归一化改进与归一化决定系数。
- **边界**：是对话方法，不是工具执行或部署后的持续在线学习。表 1 的 Extended 原始对齐分数 GPT-4o 仍高于 RLPA，不能笼统写“超过 GPT-4o”。
- **资源**：[官方训练代码](https://github.com/XingYuSSS/RLPA)，[Apache-2.0](https://github.com/XingYuSSS/RLPA/blob/main/LICENSE)。未确认完整检查点、数据及评测复现包。

<a id="method-him-agent"></a>
### M21. HIM-Agent · 分开记住个人偏好与例行行为

[PersonalAlign](https://aclanthology.org/2026.acl-long.1669/) — ACL 2026；与 B32 为同一论文。

**核验日期 / 阅读范围**：2026-11-01；[v2](https://arxiv.org/html/2601.09636v2) 方法概述、§6.1 及附录 A.3；官方 README 和根目录，非全文通读。

- **机制**：流式聚合记录，再通过基于执行的偏好过滤和基于状态的例行行为过滤，形成两类意图记忆。
- **证据**：AndroidIntent 上的离线 GUI 指标及主动建议对齐；评测范围见 B32。
- **边界**：记住日常规律不等于应当自动执行；未证明真实设备端到端完成、安全授权或长期真人效用。
- **资源**：[官方 HIM-Agent 与脚本](https://github.com/iLearn-Lab/ACL26-PersonalAlign)。数据依赖、恢复完整性与未见根许可的限制同 B32；README 的后续 skills-beta 不等于论文已验证的跨平台能力。

<a id="method-petoolllama"></a>
### M22. PEToolLLaMA · 训练偏好感知的工具调用

[PEToolLLM: Towards Personalized Tool Learning in Large Language Models](https://aclanthology.org/2025.findings-acl.1107/) — Findings of ACL 2025；与 B33 为同一论文。PEToolLLM 是论文名，PEToolBench 是评测集，PEToolLLaMA 是方法。

**核验日期 / 阅读范围**：2026-11-01；[v1](https://arxiv.org/html/2502.18980v1) §3 指标与 §4 方法概述；官方 README、LICENSE 与数据文件列表，非全文通读。

- **机制**：先用历史、指令与候选工具做个性化 SFT，再用 DPO 改善偏好一致的调用选择。
- **证据**：PEToolBench 三类合成历史设置下的工具与参数准确率。
- **边界**：模型训练与持久记忆管理不是一回事；没有证明真实服务完成、偏好在线变化或安全副作用控制。
- **资源**：[官方训练 / 测试脚本](https://github.com/travis-xu/PEToolBench)、[数据](https://huggingface.co/datasets/travisxu/PEToolBench/tree/main)。仓库 Apache-2.0，上游条款仍需核对；未确认完整权重发布或运行复现。

<a id="method-secom"></a>
### M23. SeCom · 主题分段与压缩去噪

[On Memory Construction and Retrieval for Personalized Conversational Agents](https://arxiv.org/abs/2502.05589) — ICLR 2025；会议题名添加 SeCom 前缀，与 arXiv 为同一论文。首发 2025-02-08，当前 v3 为 2025-03-03。

**核验日期 / 阅读范围**：2026-11-01；[v1](https://arxiv.org/html/2502.05589v1) §2–3 方法 / 实验相关段落、附录评测说明；官方项目页、README 与 LICENSE。未逐项比较 v1–v3。

- **机制**：将历史对话切成主题一致的片段，用 LLMLingua-2 压缩去噪后检索，改善记忆粒度与相关性。
- **证据 / 边界**：LOCOMO、Long-MT-Bench+ 的离线回答评测及独立分段实验；主 LOCOMO 表使用作者生成 QA，官方 QA 另列附录，不能直接混作其他论文的标准分数。不证明真实用户长期效用或工具执行。
- **资源**：[官方实现](https://github.com/microsoft/SeCom)，[MIT LICENSE](https://github.com/microsoft/SeCom/blob/main/LICENSE)已核实；上游模型与数据另查条款。

<a id="method-rmm"></a>
### M24. RMM · 前瞻整理与回顾式检索适配

[In Prospect and Retrospect: Reflective Memory Management for Long-term Personalized Dialogue Agents](https://aclanthology.org/2025.acl-long.413/) — ACL 2025；2503.08026 首发 2025-03-11，v2 为 2025-07-28。

**核验日期 / 阅读范围**：2026-11-01；[v1](https://arxiv.org/html/2503.08026v1) §4–8 方法、设置与结果相关段落；arXiv 版本和 ACL 出版记录。方法描述依据 v1，未逐项比较 v2。

- **机制**：会话结束后抽取 / 合并主题记忆；生成时依据 LLM 对记忆的引用反馈，以在线强化学习适配轻量 reranker。
- **证据**：MSC 的回复相似度与 LongMemEval 检索 / 答案指标；主生成器 Gemini-1.5-Flash。v1 表1中 GTE 设置的答案准确率 RAG 63.6%、RMM 70.4%，即 +6.8 个百分点，不是无条件“+10 个百分点”。
- **边界 / 资源**：模型引用奖励不是人工反馈，也非忠实归因保证；未证明真实长期部署或权限安全。本次未核实官方实现及许可，不据此断言“没有代码”。

<a id="method-memguide"></a>
### M25. MemGuide · 按当前意图与缺失槽位选记忆

[MemGuide](https://arxiv.org/html/2505.20231v2) — AAAI 2026；与 B37 同一篇，勿重复计数。

**核验日期 / 阅读范围**：2026-11-01；v2 的 MemGuide、Experiments 相关段落及表3；版本、数据和资源核验见 B37。

- **机制**：先按任务意图检索 QA 记忆，再用缺失槽位推理与微调的 LLaMA-8B filter 重排，引导回复减少重复询问。
- **证据 / 边界**：MS-TOD 上 GPT-4o-mini 相对 full-context 的成功率 88%→99%（+11 个百分点）、轮数 6.03→3.19；仅指这一设置，非所有模型或实际交易提升。记忆提供历史候选值不代表已获新操作授权。
- **资源**：[作者代码 / 数据](https://github.com/Elvin-Yiming-Du/MS_TOD_Memory)。同名 embodied MemAdapter 的 MemGuide 数据集不是本论文资产；许可限制见 B37。

<a id="method-airgapagent"></a>
### M26. AirGapAgent · 隔离第三方语境与个人数据筛选

[AirGapAgent: Protecting Privacy-Conscious Conversational Agents](https://arxiv.org/abs/2405.05175) — CCS 2024；v1（2024-05-08）题名为 *Air Gap*，v2（2024-09-18）为 *AirGapAgent*，同一论文。

**核验日期 / 阅读范围**：2026-11-01；[v1](https://arxiv.org/html/2405.05175v1) §2–6 威胁、设计与实验相关段落；v2 元数据 / 摘要。未逐项比较两版实验。

- **机制**：独立 minimizer 仅依据可信用户任务和资料选出必要数据，交互代理再与不可信第三方对话，降低 context hijacking 泄漏。
- **证据 / 边界**：合成 20 用户、26 字段、8 任务的隐私 / 效用测试；依赖任务与资料可信假设，非物理隔离、通用防注入或全系统无泄漏证明。摘要的97%保护率是特定设置，不能当总体安全率。
- **资源**：本次未核实原始官方代码 / 数据发布及许可。后续 AirGapAgent-R 是他人重建评测，不是已验证的原始资产。

<a id="method-collaborative-memory"></a>
### M27. Collaborative Memory · 跨用户记忆权限

[Collaborative Memory: Multi-User Memory Sharing in LLM Agents with Dynamic Access Control](https://arxiv.org/abs/2505.18279) — 2025 预印本；v1，2025-05-23。

**核验日期 / 阅读范围**：2026-11-01；[v1](https://arxiv.org/html/2505.18279v1) §3–5 方法与实验相关段落、附录 D 合成任务设置。

- **机制**：私有 / 共享双层记忆保留来源记录，按当前 user–agent–resource 权限过滤，支持授权变化。
- **证据**：MultiHop-RAG、200 条合成企业任务及 SciQAG 动态权限场景。企业任务没有 gold answers，主要报告资源调用，不能宣传为准确率验证。
- **关联与边界**：适用于个人代理的多用户数据边界，但主要是协作权限管理，不是个人偏好学习。形式化策略与受控实验不等于实现安全审计或防所有推断泄漏。
- **资源**：本次未核实官方代码 / 数据发布与许可；survey 中重复引文不另算论文。

<a id="method-rgmem"></a>
### M28. RGMem · 分层演化用户画像

[RGMem: Renormalization Group-inspired Memory Evolution for Language Agents](https://arxiv.org/html/2510.16392v3) — arXiv 标注 ICML 2026 接收；查阅 v3，2026-06-02。早期 “…Group-based…User Profile” 是同一论文。

**核验日期／实际阅读范围**：2026-11-01；v3 §3 方法相关段落、附录 B.1 评测协议；arXiv 版本／接收记录、作者 README 与仓库根目录。 非全文逐项通读；未安装、运行或复现实验。

- **机制**：将对话事实与用户推断逐层聚合进知识图谱，以阈值更新区分快变证据与较稳定特征，再结合多尺度检索回答；是外部记忆演化，不是底座持续训练。
- **证据／边界**：LOCOMO 使用 LLM judge，PersonaMem-128k 使用选择题准确率，三次运行取均值；不能混成通用分数，也不证明长期真人效用、画像真实性或隐私安全。
- **资源**：[作者实现](https://github.com/fenhg297/RGMem)标 MIT；依赖 Elasticsearch、Neo4j、Redis 等组件，未运行验证。

<a id="method-me-agent"></a>
### M29. Me-Agent · 用经验与分层记忆解释模糊指令

[Me-Agent](https://arxiv.org/html/2601.20162v1) — 与 B42 同一论文，不另计。

**核验日期／实际阅读范围**：2026-11-01；v1 §4.2–4.4 方法、§5.1–5.2 设置与结果相关段落及 Limitations；作者仓库根目录与 README。 非全文逐项通读；未安装、运行或复现实验。

- **机制**：VLM 评价执行轨迹，提炼自然语言经验用于提示词；分层记忆按应用检索流程和内容偏好。方法称无参数更新，不应写成对基础模型进行个性化微调。
- **证据／边界**：User FingerTip 与通用移动任务评测；UI 更新会使位置与流程经验失效，当前地点等情境因素未充分纳入。推断“常用选择”不等于获得新操作授权。
- **资源**：[作者实现](https://github.com/Gianthaha/personal-mobile-agent)；数据规模、资源完整性与许可范围的限制同 B42。

<a id="method-ppp"></a>
### M30. PPP · 学习主动澄清与个性化交互

[Training Proactive and Personalized LLM Agents](https://arxiv.org/html/2511.02208v2) — COLM 2026；v2，2026-08-23。评测环境 UserVille 见 B43，同一篇论文。

**实际阅读范围**：v2 §4–8、表1、附录A；版本记录、会议目录及作者 README / 目录 / LICENSE；非全文逐项通读，未运行。

- **机制**：在偏好条件化模拟用户环境中，以 GRPO 联合优化任务表现、澄清负担和偏好遵循；不等于持久个人记忆或终身用户建模。
- **证据与边界**：自动评测与真人研究须分开，见 B43。提问增加可能提高交互负担，模拟器中的低负担不能直接代表真人体验。
- **资源**：[作者代码](https://github.com/sunnweiwei/PPP-Agent)为 Apache-2.0；README 链接权重及数据，但本次相应网页不可访问，下载与资产许可未确认，不能推断未发布。运行说明另要求 vLLM bias patch；仓库许可不自动覆盖模型、数据或上游 benchmark。

<a id="method-puma"></a>
### M31. PUMA · 从行为历史学习工具参数

[Large Language Models Empowered Personalized Web Agents](https://arxiv.org/html/2410.17236v2) — WWW 2025；v2，2025-03-24。PersonalWAB 见 B44，同一篇论文。

**实际阅读范围**：§3、§5–6、表5、附录A.3 / B；版本记录、项目页、README、数据目录及 LICENSE；非全文逐项通读，未运行。

- **机制**：检索行为历史并保留任务相关字段，结合启发式 SFT 与结果排序 DPO 学习函数参数。
- **证据与边界**：表5整体 function/result accuracy 为 .994/.406；去除任务特定记忆为 .994/.373，但推荐 result accuracy 仍仅 .054。不同指标不能统称真实任务成功率；购物领域与模拟用户限制见 B44。
- **资源**：[作者仓库](https://github.com/HongruCai/PersonalWAB)及数据目录可读；根许可 **CC BY-NC 4.0**，tau-bench 继承部分另保留 MIT。未确认发布的 PUMA 检查点，未验证完整数据；论文许可、代码/数据许可及 Amazon/模型条款不可互相替代。

<a id="method-premem"></a>
### M32. PREMem · 存储前推理跨会话关系

[Pre-Storage Reasoning for Episodic Memory](https://aclanthology.org/2025.findings-emnlp.1204/) — Findings EMNLP 2025；[arXiv v1](https://arxiv.org/html/2509.10852v1)，2025-09-13。

**实际阅读范围**：v1 §3–5、表1/5、Limitations；出版记录、作者 README 与根目录；未逐项比较出版版本，未运行。

- **机制**：提取事实、经历与主观信息，再聚类、关联时序并生成跨会话推断，供回答时检索。
- **证据**：离线 LoCoMo 1,986 题与 LongMemEval-S 500题；LoCoMo 对话经模型生成及人工编辑，LongMemEval 会话为模拟及人工编辑，不是真人纵向使用记录。使用文本相似度、LLM judge 和不可回答题拒答准确率。
- **边界**：作者承认单跳较弱、原始语言细节损失及缺乏遗忘机制。推断内容不等于用户确认事实，也不代表操作授权。
- **资源**：[代码及运行说明](https://github.com/sangyeop-kim/PREMem)公开；根目录未见 LICENSE，代码复用许可未确认。README 标上游 LoCoMo 为 CC BY-NC 4.0、LongMemEval 为 MIT；不能据此推定 PREMem 代码许可。链接的数据压缩包未验证访问或完整性。

<a id="method-nemori"></a>
### M33. NEMORI · 依据预测误差蒸馏记忆

[What Deserves Memory: Adaptive Memory Distillation for LLM Agents](https://arxiv.org/html/2508.03341v4) — v4，2026-04-16；本次未确认会议归属。早期 *Nemori: Self-Organizing Agent Memory Inspired by Cognitive Science* 为同一 arXiv ID，不另计。

**实际阅读范围**：v4 §3–4.7、表2/7/8、Limitations；版本、作者 README、评测说明与 MIT LICENSE；未逐项比较历史版本，未运行。

- **机制**：将对话组织为叙事片段，再从实际内容与已有知识预测的差异蒸馏语义信息；不更新底座参数。
- **证据**：离线 LoCoMo 1,540题与 LongMemEval-S 500题；LoCoMo 对话经模型生成及人工编辑，LongMemEval 会话为模拟及人工编辑，不是真人纵向使用记录。LoCoMo 以 GPT-4.1-mini 为方法底座及回答模型、GPT-4o-mini 为 judge 时，平均分80.8，对全上下文80.6；以 GPT-4o-mini 为底座时，LongMemEval 知识更新子集反而61.5，对全上下文78.2。不能写成全面领先。
- **边界**：作者限制包括简单管理/检索、集成接口需逐项实现；不证明安全删除或真实长期用户效用。与 PREMem 的 LoCoMo 子集不同，不能横排分数。
- **资源**：[实现](https://github.com/nemori-ai/nemori)为 MIT；当前重写版不兼容旧 MVP，依赖 PostgreSQL、Qdrant 与模型 API。评测数据需另取并遵守原条款；README 的 V5 成绩不是 v4 论文成绩。

<a id="method-dpl"></a>
### M34. DPL · 用用户之间的差异构造个人表示

[Measuring What Makes You Unique](https://aclanthology.org/2025.findings-acl.1095/) — Findings ACL 2025；[arXiv v3](https://arxiv.org/html/2503.02450v3)，2025-06-11。

**实际阅读范围**：v3 §2–4、表1、附录A–F相关内容；出版 PDF 限制/伦理与附录A、作者预处理脚本、README、根目录及数据卡；非逐行通读，未运行。

- **机制**：比较目标用户与其他用户的评论风格、情感和语义差异，再与个人历史汇总形成生成条件；属于用户表示方法。
- **证据与边界**：Amazon/Yelp 真实评论记录上的离线生成，输入还包括目标评分和标题；不是多轮对话、无条件偏好预测或工具执行。主表跨五个温度取均值，不是相同配置的五个随机种子。跨用户信息使用还需隐私/同意约束。
- **一致性问题**：论文附录说测试用倒数第三条评论，当前代码用最后一条；不能把文字冲突直接断言为已证实泄漏，复现前应核对数据。
- **资源**：[作者代码](https://github.com/SnowCharmQ/DPL)根目录未见许可；[DPL-main](https://huggingface.co/datasets/SnowCharmQ/DPL-main)与[DPL-meta](https://huggingface.co/datasets/SnowCharmQ/DPL-meta)标 **CC BY-NC 4.0**，不能沿用论文伦理段的宽泛 MIT 说法。上游条款另查。

<a id="reproducibility"></a>
## 怎样比较与复现

不要把不同论文中的最高分拼成排行榜。至少记录：

1. **任务与版本**：论文版本、代码 commit、数据集 revision / 文件哈希、分组、题数、是否删除失败题；原版与 cleaned / verified / 后续版本分开。
2. **可见信息**：全历史、检索 top-k、oracle 证据、工具 schema、截图 / 界面树；禁止把答案或未来会话写入记忆。
3. **模型与系统**：底座精确版本、记忆 / embedding / reranker / judge、提示、工具、代码 commit；区分底座提升和系统提升。
4. **预算与指标**：时间、token、费用、步数、重试数；单次成功、重复稳定成功、检索召回、答案正确分别报告。`pass@k` 与 `pass^k` 不可互换。
5. **安全与有用性**：正常 / 受攻击任务效用、泄漏 / 违规率一起报告；同时记录澄清频率、被拒后克制、打扰成本与延迟。不靠拒绝所有任务制造“安全高分”。
6. **记忆生命周期**：PersonaMem-v2 的不再使用、MemoryAgentBench 的冲突更新、Zep 的边失效和 MemOS 的治理设计，均不能单独证明存储、备份或参数已彻底删除。
7. **真实助理缺口**：月级真人效用、跨用户 / 多代理隔离、不可逆操作授权、可审计撤销、重启 / 失联后的幂等恢复与真正存储删除，仍需专门测试。

以上是本清单的评测建议，不是声称这些论文已经覆盖了所有维度。使用合成或获授权的脱敏数据；不要向公开 Issue、日志或评测仓库上传真实个人历史、密钥、Cookie。

<a id="sources-and-rights"></a>
## 来源与许可边界

- 每条论文标题链接到原文 / 正式论文页，资源链接到作者维护入口；任务定义、指标、发布日期以这些来源为依据。方法用途与未覆盖能力由本清单归纳，不是作者对产品可靠性的背书。
- 摘要均为原创短述，不复制论文图表、长段正文、完整题库或隐藏答案。引用某项研究时应从原论文导出 BibTeX，而不是只引用这个清单。
- **公开可读不等于任意再利用**：LaMP、LoCoMo、PersonaBench、PrefEval 与 MemoPro 代码的非商业条款，GAIA 的门控 / 防污染要求，以及 AppWorld / Ego4D 的额外资源规则已在对应条目提示。未列许可不代表没有限制；代码、数据、模型和第三方素材可能适用不同条款。
- 本次未进行逐资产法律审查、下载完整权重验证或全依赖复现。根目录缺许可、文件访问失败或外部服务变化均不能被“有 GitHub 链接”消除。
- 维护时先修正文献版本、任务范围与失效资源，再补新论文；欢迎提供具体一手证据，不以榜单名次、引用量或 Star 作为可靠性结论。



