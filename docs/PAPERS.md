# 个人 Agent 论文与评测 · Papers & benchmarks

[English](PAPERS.en.md) · [返回主清单](../README.md)

**先分清测了什么，再看分数。** 这里把 eval / benchmark 与 agent 方法 / 系统分开，并区分“直接研究个人上下文”“可迁移的通用记忆 / 执行能力”及“特定隐私 / 安全风险”。

文献与资源核验：**2026-10-31**。共 **128 篇不同论文**：70 个评测条目、66 个方法条目及 9 个人机研究条目；Proactive Agent、MemoProAgent、PbP/InTU、Ask-before-Plan/CEP、PersonalAlign/HIM-Agent、PEToolLLM/PEToolLLaMA、MemGuide/MS-TOD、Me-Agent/User FingerTip、PPP/UserVille、PUMA/PersonalWAB、MPR/HybridMem、PrivacyLens-Live/PrivacyChecker、PTBench/PTool、PAL-Bench/H²Memory、PENGUIN/RAISE、Searching for Privacy Risks 与 THEANINE/TeaFarm 各同时贡献 benchmark 和方法，分别只计一次论文。来源为论文摘要与下列明示的原文段落、作者项目页、官方代码库和数据卡；**没有安装复现、独立跑分、模型训练或安全审计**。这是精选阅读入口，不是完整综述、最新论文榜或产品排名。

**条目核验**：B25–B70、M16–M66、H1–H9 核验于 2026-11-01；旧条目保留原核验日期。

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
- [人机研究](#human-studies)
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

**核验日期 / 阅读范围**：2026-11-01；摘要、§1、§4.2 及结果表；未复现。

- **输入 → 输出**：用户模型、含个人概念的请求及旅行参考信息 → 个性化行程。
- **测量**：计划交付、常识 / 硬约束与最终通过率；另用 LLM judge 比较个性化与通用计划的偏好率。
- **边界**：judge 偏好率不是真人满意度，也不等于约束通过率；部分个性化设置的约束指标下降。不是长期在线规划。
- **资源**：[论文全文](https://aclanthology.org/2024.emnlp-industry.37.pdf)；本次未定位可核验的 TravelPlanner+ 官方代码 / 数据入口，不以原始 TravelPlanner 仓库冒充。

<a id="benchmark-pbp"></a>
### B29. PbP · 从示范推断规划偏好

[Inferring the Unspoken: Aligning Embodied Agents with Implicit Preferences](https://arxiv.org/abs/2502.00858v4) — 2025 首发；此处为 2026-09-08 v4，arXiv 标注 EMNLP 2026。旧题为 Learning to Plan with Personalized Preferences；方法见 M17。

**核验日期 / 阅读范围**：2026-11-01；仅 v4 摘要与版本记录，初读。

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

<a id="benchmark-triptailor"></a>
### B45. TripTailor · 个性化旅行计划评测

[TripTailor: A Real-World Benchmark for Personalized Travel Planning](https://aclanthology.org/2025.findings-acl.503/) — Findings of ACL 2025，July。

**核验日期 / 阅读范围：**2026-11-01；论文 §3、§4、Appendix B.1、Limitation；官方仓库 README、完整文件树和 release 元数据。

- **输入→输出：**单轮旅行请求/偏好与中国旅行沙箱→行程。多数实验预先提供搜索信息（含参考行程所需 POI），不能直接当作开放式搜索和规划的端到端成绩。
- **数据/测量：**真实 POI、旅行平台行程经补全和 LLM 改写，查询由模型构造；先由 LLM 从自然语言计划抽取关键实体与活动，再由脚本对照沙箱检查可行性/合理性；不是直接对原始计划进行纯确定性评估。模型裁判与奖励模型另对照参考行程评价个性化。
- **边界：**不是数千真人请求；中国场景、单轮交互和模型查询/裁判偏差限制泛化，不验证预订或实际旅行。
- **资源：**公开代码、data.7z；main，最后推送 2025-10-22，无 GitHub release。README 无许可声明、完整树无 LICENSE/COPYING、GitHub license=null；复用许可未确立。

<a id="benchmark-mpr"></a>
### B46. MPR · 多跳个人事实推理

[Explicit v.s. Implicit Memory: Exploring Multi-hop Complex Reasoning Over Personalized Information](https://arxiv.org/html/2508.13250v1) — arXiv v1，2025-08-18；方法见 M38，同一论文只计一次。

**核验日期 / 阅读范围：**2026-11-01；§3–6；官方 README、完整文件树和 release 元数据。

- **输入 → 输出：**合成用户图及模型生成的单跳事实陈述与问题 → 2–10 跳个人事实答案；不是观察到的真人历史。
- **测量：**规范化答案精确匹配；实验使用均衡的 2,700 题子集。Oracle 与普通检索设置须分别报告。
- **边界：**不是工具执行、在线偏好变化或长期满意度评测。表 2 写 108,000 QA，§3.3.3 写 10,800；保留数量矛盾，不静默修正。
- **资源：**[官方仓库](https://github.com/nuster1128/MPR)，master，最后推送 2025-08-24，无 release、无声明的仓库许可；README 链接 Drive 数据，但本次无法读取归档。论文 CC BY 4.0 不自动覆盖代码/数据复用。

<a id="benchmark-familytool"></a>
### B47. FamilyTool · 多跳个人知识到工具参数

[FamilyTool: A Multi-hop Personalized Tool Use Benchmark](https://arxiv.org/html/2504.06766v2) — 2025 预印本；查阅 v2，2025-05-26。

**核验日期 / 阅读范围**：2026-11-01；§§4–6、§9、附录 C.2；官方 README、仓库许可元数据及根目录 LICENSE 查询。

- **输入 → 输出**：合成家庭关系 / 偏好 KG、带说话人身份的请求及候选工具 → 工具调用及参数；KGETool 先抽取相关子图，再生成调用。
- **测量**：483 个基础、455 个扩展样例，均使用 102 个工具；分别覆盖 1–4、2–6 个关系跳数。子图抽取的 EM / F1 / coverage 等与调用 EM、工具选择准确率、参数值准确率分开；golden sub-KG 与实际抽取子图不能混报。
- **边界**：家庭、偏好和请求由合成与人工检查构建，主要测试静态调用生成，不是实际完成预订、长期家庭部署或开放多轮执行。最长跳数样例较少；正确参数不等于已获授权或执行成功。
- **资源**：[官方代码 / 数据](https://github.com/yxzwang/FamilyTool)含基础 / 扩展 JSONL、KG 与流水线。根目录 `LICENSE` 查询返回 404，仓库许可字段为空；**复用许可未确认**，不能由公开可读推定为 MIT 等开放许可。MTU-Bench / UnifiedToolHub 上游资源另核对条款。

<a id="benchmark-compass"></a>
### B49. 区分可行规划与偏好最优规划

[COMPASS: Benchmarking Constrained Optimization in LLM Agents](https://arxiv.org/html/2510.07043v2) — 查阅 v2，2026-04-16；会议归属未确认。

**阅读范围：**§§3–6、附录 H；版本记录、仓库 README、目录与 LICENSE；未运行。

- **评测：**281 个旅行任务、工具化检索及模拟用户交互；分别以 FR 检查硬约束可行性，以 OR-A% 检查方案是否位于可行解效用排名前 A%。
- **边界：**真实来源商品数据不等于真人使用；人工研究主要核对模拟器。最优率采用前 A% 排名口径，不必然是精确最优解，也不证明完成真实预订。
- **资源：**[仓库](https://github.com/sunnytqin/compass)根许可 MIT；数据库完整性及第三方数据权利未审计。
- **去重：**仓库长名称与论文标题属于同一研究；无需新增独立方法条目。

<a id="benchmark-aware-us"></a>
### B50. 偏好约束冲突与查询修复

[AWARE-US: Preference-Aware Infeasibility Resolution in Tool-Calling Agents](https://arxiv.org/html/2601.02643v2) — 查阅 v2，2026-03-01；会议录用未确认。

**阅读范围：**§§3–7、表1–5；版本记录、官方 README、目录及数据卡；未运行。

- **评测：**122 个合成画像汽车查询，测试澄清、恢复可行性及与 oracle 偏好的匹配。
- **边界：**表5中，SFT+DPO 后的 Qwen3-8B 局部权重方法取得 48% Car match；该指标以正确放松约束为门控，不应据此断言以正确放松样本数为分母，更不是满意度。表1与结果表/讨论的 S2/S3 标签不一致，分组成绩暂不转录；仅测试结构化汽车领域和静态偏好，不覆盖偏好漂移。推断偏好不等于获得放松真实硬约束的授权。
- **资源：**[代码](https://github.com/mhtkrmz/Infeasible-task)及[数据入口](https://huggingface.co/datasets/MehmetKurmaz/AWARE-US)可读；代码根目录无 LICENSE，数据复用许可未确认。
- **去重：**局部/全局权重及成对排序方法可交叉引用本条，不另计论文。


<a id="benchmark-ptbench"></a>
### B51. PTBench · 工具选择与参数填充中的个人偏好

[Advancing and Benchmarking Personalized Tool Invocation for LLMs](https://arxiv.org/html/2505.04072v1) — 预印本；v1，2025-05-07。与 M46 为同一论文，仅计一次。

**实际阅读范围：** §3–4、§5.1–5.3，重点为表1–2；官方仓库目录与 README。其余附录未全面精读。

- **输入 → 输出：** 用户画像/行为、请求及候选 API → 偏好平台与带参数的工具调用。
- **评测证据：** 1,083 条经人工核验的合成测试样本，80 个画像、360 个 API、五类场景；其中六个画像未进入训练。分别测量平台选择、请求/画像相关参数及完整输出准确率。
- **边界：** 人工核验不等于真实用户交互。静态生成调用不能证明交易完成、调用获授权或长期偏好适应。表1内部亦有算术冲突：训练7,096加测试1,083应为8,179，而印刷总数为8,197；数据总量正文也不一致。应保留明确标注的划分计数并提示总数未调和，不能把整张表当作无矛盾真值。
- **资源：** [官方代码与测试数据](https://github.com/hyfshadow/PTBench)；训练数据/模型发布情况和再利用许可未核实。

<a id="benchmark-pal-bench"></a>
### B52. PAL-Bench · 从长期个人历史理解需求与偏好

[Mem-PAL: Towards Memory-based Personalized Dialogue Assistants for Long-term User-Agent Interaction](https://arxiv.org/html/2511.13410v2) — v2，2025-11-26；AAAI 2026 Oral。与 M47 为同一论文。

**实际阅读范围：** PAL-Bench 构建/任务、H²Memory 框架与实验（包括外部验证）；官方仓库 README 与目录。附录仅抽查，未全面精读。

- **输入 → 输出：** 行为日志与对话历史 → 需求重述、方案生成/选择及多轮回答。
- **指标：** BLEU、GPT-4 隐含需求评分、方案选择分数及对话成对比较。
- **边界：** PAL-Set 包含100名合成用户，每人约29次会话、9.4个月模拟历史；人工检查不会使其变成长期真人研究。多轮用户由 LLM 模拟。外部验证仅覆盖 LongMemEval 的 single-session-preference 子集，且仅使用对话组件（Topic Outline + Principle），并非完整四组件系统。
- **资源/语言：** [官方代码/数据](https://github.com/hzp3517/Mem-PAL)。README 明确英文版本由 DeepSeek-V3 翻译，未逐项人工核验。附录B以未来发布措辞声明 PAL-Set 将采用 CC BY-NC 4.0；这是作者的许可声明，应与实际分发数据条款及实现许可的核验分开。仓库再利用许可核验仍未完成。

<a id="benchmark-memento"></a>
### B53. MEMENTO · 将个人记忆用于具身任务

[Embodied Agents Meet Personalization: Investigating Challenges and Solutions Through the Lens of Memory Utilization](https://arxiv.org/html/2505.16348v4) — v4，2026-02-13；ICLR 2026。

**实际阅读范围：** §3–4、记忆设计贡献概述、附录 A.1–A.2；作者项目页及仓库 README。§6 的详细算法/消融与扩展附录 E 未全面精读，因此方法交叉索引暂定。

- **输入 → 输出：** 物品的个人含义/行为惯例与情景记忆 → 物品重排动作。
- **评测：** 获得记忆/使用记忆阶段保持目标相同；区分单记忆/联合记忆，统计目标完成比例、成功率和规划成本。438个回合、12个 Habitat 场景，个人知识由模型生成。
- **边界：** 主设置确保检索候选含正确记忆，并采用理想感知与运动技能，隔离的是记忆利用，而非无约束检索或现实机器人可靠性。使用合成个人信息，缺少对话澄清。GPT-4o 联合记忆任务相对对应获得记忆阶段成功率下降30.5个百分点。
- **资源/身份：** [官方仓库](https://github.com/Connoriginal/MEMENTO)，MIT 仓库，依赖 Habitat/PARTNR。README 旧副标题 “Exploring Memory Utilization for Personalized Assistance” 指同一论文。

<a id="benchmark-realmem"></a>
### B56. RealMem

**Benchmark：长期项目状态与跨会话记忆**

[RealMem: Benchmarking LLMs in Real-World Memory-Driven Interaction](https://aclanthology.org/2026.findings-acl.703/) · **Findings of ACL 2026**；arXiv:2601.06966v1。

- **测什么：** 11 类项目场景、2,000 余段合成跨会话对话中的状态更新、时间推理和个人目标对齐；不是自然用户长期部署数据。
- **证据：** 正式版 Table 2 中，GPT-4o memory-only QA 为 MemoryOS 0.567、oracle 0.804；另有 30 个实例、两名 NLP 背景标注者的人类核验，不能等同用户效果实验。
- **边界：** 正式版较 arXiv v1 增补 LightMem、全文上下文基线和评估说明；应以正式版为准。合成数据及模型裁判仍限制外推。
- **资源：** [官方代码与数据](https://github.com/AvatarMemory/RealMemBench)；实际 LICENSE 为 **Apache-2.0**，README 的 MIT 徽章与之不一致。
- **实际阅读：** arXiv 方法与结果；ACL 正式 PDF 的结果表、局限及人工评估协议；官方 README/LICENSE。未复现。

<a id="benchmark-personal"></a>
### B57. PersONAL

**Benchmark：用户物品归属、导航与空间定位**

[PersONAL: Towards a Comprehensive Benchmark for Personalized Embodied Agents](https://arxiv.org/abs/2509.19843) · **ICRA 2026**（[帕多瓦大学机构记录](https://unifind.unipd.it/resource/item/894811?language=en-US)确认题名、作者与会议）；本次实读版本为 **arXiv v1，2025-09-24**，未将其结果自动视为会议最终版结果。

- **测什么：** 基于显式物品归属描述，在 HM3D/Habitat 场景中执行个性化主动导航或预探索后的物体定位；共 **2,020 个 episode**。
- **证据：** 导航人类基线包含五名真人；不是家庭用户部署。另有三房间办公室 LoCoBot 可行性实验，定位成功 **5/15**。
- **边界：** 静态归属不代表动态偏好学习或终身适应；人类定位使用可交互 GLB 场景，与模型地图输入不同。POG 正文的 25% 与 Table V 的总分 16.8% 不一致，勿直接引用前者为总体结果。
- **资源：** [官方仓库](https://github.com/ZiliottoFilippoDev/PersONAL)为 **CC-BY-4.0**；数据、生成程序及 [baselines 分支](https://github.com/ZiliottoFilippoDev/PersONAL/tree/baselines)代码已存在。HM3D 另需 Matterport 访问及上游许可。
- **实际阅读：** arXiv v1 §§III–VII、结果表、官方主分支及 baseline README/目录、帕多瓦大学发表元数据；未核对会议最终版全文，未运行机器人或基线。

<a id="benchmark-pin"></a>
### B58. PIN / PInNED — 用户特定物体导航
- **论文**：*Personalized Instance-based Navigation Toward User-Specific Objects in Realistic Environments*，NeurIPS 2024 Datasets and Benchmarks；读取 arXiv v2（2025-02-19）。PIN 是任务、PInNED 是数据集，按一篇计。
- **设置与证据**：在 Habitat 仿真中根据图片/人工描述寻找特定实例并区分同类干扰物；338 个物体、18 类，比较模块化及端到端导航基线。不是实际家庭用户或实体机器人试验。
- **边界**：反映受控仿真中的实例识别与导航；小物体、远距离细节和渲染退化是困难，不证明真实家庭个人助理可靠性。
- **许可与实读范围**：[论文](https://arxiv.org/html/2410.18195v2) §3–5、Appendix B/G/I；[项目](https://aimagelab.github.io/pin/)、[代码](https://github.com/aimagelab/pin)。代码 MIT；episodes/描述 CC BY；HM3D 非商业学术条件；物体混合多种 CC 许可，不能整体称可商用。

<a id="benchmark-personafeedback"></a>
### B59. PersonaFeedback · 显式画像下的响应偏好判断

[PersonaFeedback: A Large-scale Human-annotated Benchmark For Personalization](https://arxiv.org/html/2506.12915v1) — arXiv v1, 2025-06-15，work in progress.

给定画像、问题和候选回答，选择更个性化且有帮助的回答；8,298个人工标注二选一测试例，以selection accuracy衡量判断是否符合标签。20个真实种子画像扩展为构造画像，基准使用其中200个；问题/回答含模型生成，九位评者多数选择作为标签。不是8,298名真实用户、长期画像推断或部署满意度研究；主观标签及构造画像偏差限制结论，“RAG不足”仅限所测设置。[公开数据](https://huggingface.co/datasets/PersonalAILab/PersonaFeedback)标注Apache-2.0，区别于论文CC BY 4.0；当前在线预览有字段不一致报错，不代表文件不可获取。未发现形式隐私保证。

**实读范围：** §3构造和标注、§4评测设置、limitations；官方数据卡和预览状态。定向阅读，未复核全量样例

<a id="benchmark-atm-bench"></a>
### B60. ATM-Bench · 跨来源个人指代记忆问答

[According to Me: Long-Term Personalized Referential Memory QA](https://arxiv.org/html/2603.01990v1) — arXiv v1, 2026-03-02，preprint.

约四年的人类来源邮件、图像和视频，配1,038个人工问题—答案—证据标注；考察指代、多证据和更新记忆。Schema-Guided Memory统一结构；答案指标QS按答案类型选择：数值类用EM，列表召回类用Jaccard，开放回答用LLM裁判。检索另报Recall@k及Recall@k_GT（k取真实证据数）；Joint@k=QS×Recall@k。同意、视觉模糊/脱敏、邮件改写和合成标识替换不构成可证明匿名性。论文Hard低于20%的结论仅适用于原实验。[代码库](https://github.com/JingbiaoMei/ATM-Bench)已发布代码与后续代理评测，注明发布集可能不同于预印本；[数据](https://huggingface.co/datasets/Jingbiao/ATM-Bench)现已公开，CC BY-NC 4.0，代码MIT。勿沿用论文“待发布”脚注或混合新旧榜单。

**实读范围：** §3–5、Appendix A隐私/许可、B标注；官方仓库时间线、结果版本说明与数据卡。定向阅读，未检查原始个人数据

<a id="benchmark-triptide"></a>
### B65. TripTide · 扰动后的个性化行程修订

[TripTide: A Benchmark for Adaptive Travel Planning under Disruptions](https://arxiv.org/html/2510.21329v1) — arXiv 2510.21329v1, 2025-10-24; no verified conference publication.

扩展TripCraft的1,000个3/5/7天计划；模型生成候选扰动，人工选择并修订，包含step/day/plan严重度及两类容忍画像。比较GPT-4o、Qwen2.5-7B、Phi-4-mini的约束通过、语义/空间/顺序变化与扰动响应；Llama裁判仅评GPT-4o输出，另由三位专家评审100个修订计划。

**边界：** §4.2在整个数据集上评测，没有预定义训练/测试划分；结果用于诊断规划行为，不构成留出测试上的泛化证据。合成扰动和预设画像，不是真实旅行部署；响应率不是计时延迟，少改动不等于可执行。裁判感知质量与硬约束可不一致。未验证实时库存、交易授权或用户满意度。文中残留2018会场/DOI模板，不作发表证据。

**实读范围：** v1 §3–6及相关附录段落；匿名代码入口由论文提供，未复现。

<a id="benchmark-convomem"></a>
### B66. ConvoMem · 完整上下文作为记忆强基线

[ConvoMem Benchmark: Why Your First 150 Conversations Don't Need RAG](https://arxiv.org/html/2511.10523v1) — arXiv 2511.10523v1, 2025-11-13.

75,336个QA覆盖用户/助手事实、拒答、偏好、事实变化及隐含联系；企业角色合成人设经场景、证据、对话生成，证据与填充对话使用同一流程并由多模型校验。比较完整上下文、Mem0与两阶段提取的准确率、成本及延迟，历史长度实验延至300段对话。

**边界：** “150段无需RAG”是特定数据、模型及成本设置下的经验，非通用阈值；不是真实长期用户日志。缺失信息拒答不等于隐私/权限拒答；未验证同意、删除、访问隔离或泄露防护。

**实读范围：** v1 §2–3、§5及Appendix A；代码/数据入口由原文提供，未独立复现或确认再利用许可。

<a id="benchmark-perltqa"></a>
### B68. 个人记忆问答 / Personal-memory QA

[PerLTQA: A Personal Long-Term Memory Dataset for Memory Classification, Retrieval, and Synthesis in Question Answering](https://arxiv.org/html/2402.16288v1) — 查阅 / reviewed v1, 2024-02-26；[SIGHAN-10 2024 发表版](https://aclanthology.org/2024.sighan-1.18/)标题末段改为 / published title uses “Fusion”。


- **阅读范围**：§§3–5、生成及验证附录；官方 README / LICENSE。
- **输入 → 输出**：合成人物的画像、社会关系、事件、对话及问题 → 记忆类型、检索结果与答案。ChatGPT / Wikipedia 提供种子，GPT-3.5 生成并经人工检查；8,593 道 QA 覆盖 30 个人物，不是 30 名长期真人用户。
- **测量**：分类 P/R/F1/accuracy、Recall@K、记忆锚点 MAP、模型判断的正确性 / 连贯性。
- **边界**：合成 QA 不证明真人满意度、执行能力或隐私安全。
- **资源**：[代码 / 数据](https://github.com/Elvin-Yiming-Du/PerLTQA)、[数据许可 CC BY-NC 4.0](https://github.com/Elvin-Yiming-Du/PerLTQA/blob/main/LICENSE.txt)。README 记录 2025-12-22 一致性修复；固定 revision，勿混同原论文数据。

<a id="benchmark-personaconvbench"></a>
### B69. 多用户对话历史 / Multi-user conversational history

[A Personalized Conversational Benchmark: Towards Simulating Personalized Conversations](https://arxiv.org/html/2505.14106v2) — [NeurIPS 2025 MTI-LLM workshop（非主会 / not main conference）](https://research.adobe.com/publication/a-personalized-conversational-benchmark-towards-simulating-personalized-conversations/)；方法与实验查阅 / methods and experiments reviewed in arXiv v2, 2025-05-25。


- **阅读范围**：§§2–4、附录 C；官方 `Latest` README 与数据卡。
- **输入 → 输出**：十领域 Reddit 原始帖子构建的既往对话 / 用户轨迹 → 二分类标签、社区反馈分预测或下一条用户文本。
- **测量**：accuracy/F1/MCC、回归误差、生成相似度；各任务分开比较。论文规定按时间提供历史并遮蔽目标文本，未独立审计实现。
- **比较口径**：§C.3 的文本生成对除 Claude 外的模型生成 10 个候选，再按最高 SBERT 分选取 best-of-10；Claude 仅一个候选。因此跨模型生成分数不是相同采样预算下的单次生成比较。
- **边界**：“sentiment” 标签来自 Reddit 评分，不是经过验证的个人情绪；历史数据评测不等于真实部署或心理支持效果。
- **资源**：[代码](https://github.com/PERSONA-bench/PERSONA/tree/Latest)、[数据](https://huggingface.co/datasets/PERSONABench/PERSONA-Bench)。HF 标 MIT，仓库数据表却写 research-only / Reddit TOS；许可存在不一致，不能称为无限制 MIT 数据。

<a id="benchmark-teafarm"></a>
### B70. 反事实记忆压力测试 / Counterfactual memory stress test

[Towards Lifelong Dialogue Agents via Timeline-based Memory Management](https://arxiv.org/html/2406.10996v3) — NAACL 2025；查阅 / reviewed v3, 2025-01-29。方法见 / method: **M65**；同一论文 / same paper。


- **阅读范围**：§§3–5、附录 D/E/J；官方代码 / 数据入口。
- **输入 → 输出**：MSC / Conversation Chronicles 的五会话历史、合成续话与反事实问题 → 回答；TeaBag 含 100 个原始 episode、200 对 QA 与 200 段 GPT-4 合成第六会话。
- **测量**：正确回忆且不被错误前提误导的成功率；不与普通生成质量混为一项。
- **边界**：人物故事是人工构造内容，不是真人终身观察；反事实问答也不是全面对抗安全认证。
- **资源**：[代码](https://github.com/kimnamssya/Theanine)、[数据](https://huggingface.co/datasets/LangAGI-Lab/teafarm)（当前 200 行）。附录 J 指定学术 / 非商业用途；数据与上游条款仍应分别确认。

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

**核验日期 / 阅读范围**：2026-11-01；摘要、§5.1–5.2 评测及附录 B.2–B.3；官方 README。

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

**核验日期 / 阅读范围**：2026-11-01；摘要、§4.1 指标、官方 README 的资源与许可说明。

- **输入 → 输出**：带授权边界的委托及沙箱状态 → 工具行动轨迹；286 个任务。
- **测量**：结合完整轨迹与状态证据，分别判断任务完成和越权。
- **边界**：通用委托边界评测，不是个性化规划方法；模拟服务与 judge 不代表真实部署风险率。
- **资源**：[官方代码 / 任务](https://github.com/PEACH-Research-Lab/AuthorizationBench)。README 声明原创软件 / 基准制品 MIT，第三方材料另计；公开 6,864 份判定但仅保留 4,981 份原始轨迹，不能视为完整轨迹全集。未运行。

<a id="benchmark-privacylens-live"></a>
### B48. PrivacyLens-Live · 动态工具 / 多代理信息披露

[Privacy in Action: Towards Realistic Privacy Mitigation and Evaluation for LLM-Powered Agents](https://aclanthology.org/2025.findings-emnlp.925/) — Findings of EMNLP 2025；方法原文查阅 [arXiv v1，2025-09-22](https://arxiv.org/html/2509.17488v1)。方法见 M41；同一论文只计一次。

**核验日期 / 阅读范围**：2026-11-01；§§3–4.5、Limitations；ACL 论文元数据及作者资源链接。

- **输入 → 输出**：由 PrivacyLens 轨迹重建的私人内容与请求，经 MCP 工具 / 双代理交互 → 最终发送动作；不是直接观察自然发生的真人任务。
- **测量**：论文先用 493 个静态 PrivacyLens 样例评估缓解；Live 初始使用 150 个 Gmail / Notion 样例，另加 36 个三工具流程。泄露率、helpfulness 与按 helpfulness 调整的泄露率分开；静态与 live、模型及部署位置必须注明。
- **边界**：Gmail / Notion 测试账号有实际工具交互，但内容来自重建样例；A2A 是关键组件的复现，不能视为所有协议实现的互操作或安全测试。更复杂流程仍有残余泄露；不证明完整隐私合规或抵抗提示注入。
- **资源**：作者给出[代码 / 数据短链接](https://aka.ms/privacy_in_action)，但本次抓取被 robots.txt 拒绝，**发布内容及代码 / 数据许可未确认**；不要写成已验证可复现。它扩展已有 PrivacyLens，不是原始 PrivacyLens 的同名版本更新。

<a id="benchmark-privacybench"></a>
### B54. PrivacyBench · 个人对话中的泄露与过度保密

[PrivacyBench: A Conversational Benchmark for Evaluating Privacy in Personalized AI](https://arxiv.org/html/2512.24848v1) — 预印本；v1，2025-12-31。

**实际阅读范围：** §3–8、表2、附录 C.3；另核对 [PDF 第8页](https://arxiv.org/pdf/2512.24848) 表2；官方代码/数据仓库目录和 README。

- **输入 → 输出：** 合成社交画像、文档及秘密 → 在直接/间接探测下的多轮 RAG 回答。
- **指标与规模：** 泄露、过度保密、不当检索及人格一致性；48名合成用户、31,972份文档、五种助手，最多十轮。
- **数值警示：** 表中直接探测平均数16.31%→5.43%，与所列五模型行的简单平均17.064%→7.38%不一致。整体15.80%→5.12%仅为作者报告，聚合尚未调和。26.56%是最差模型的直接探测结果，并非整体基线。提示词并非一致有效：Kimi-K2 的直接探测泄露率反而由14.58%升至18.13%。
- **边界：** 严格的完整/明确秘密泄露定义不涵盖暗示及部分泄露；仅测试标准 RAG，不能推为所有智能体隐私/合规结论。人工评审校验不是真人部署。不同于 PrivacyLens、PrivacyLens-Live 与 PrivacyChecker。
- **资源：** [代码](https://github.com/sri-ja/privacy-bench)、[数据](https://github.com/sri-ja/privacy-bench-dataset)；再利用许可未核实。提示词缓解不另列为一篇方法论文。

<a id="benchmark-penguin"></a>
### B55. PENGUIN · 以个人背景为条件的安全评测

[Personalized Safety in LLMs: A Benchmark and A Planning-Based Agent Approach](https://arxiv.org/html/2505.18882v5) — v5，2026-01-13；[NeurIPS 2025](https://papers.nips.cc/paper_files/paper/2025/hash/8c2bb821410066459be64d03a4dc5719-Abstract-Conference.html)。与 M48 为同一论文。

**实际阅读范围：** §3–4、§5 方法概述/结果、Limitations 与 Ethical Statement；官方项目页/仓库 README。MCTS 数学附录及全部扩展实验未全面精读。

- **输入 → 输出：** 带/不带结构化个人背景的请求 → 考虑个人处境的回答。
- **指标：** 风险敏感性、情感共情与用户特定对齐。14,000个场景，Reddit 衍生与合成各半，覆盖七个领域；以350例、三位标注者校验 GPT-4o 评审。
- **边界：** 测量回答的代理评分，而非实际伤害下降。Reddit 富背景筛选、人工定义属性及等成本获取假设限制推广。
- **资源：** [官方实现](https://github.com/yuchenlwu/PersonalizedSafety)、[项目页](https://personalized-safety.github.io/)；README 含过时克隆地址/运行文件引用。已核验可访问，未尝试复现；README 的 MIT 声明未另以许可文件核对。

<a id="benchmark-agentdam"></a>
### B61. AgentDAM · Web执行中的非必要披露

[AgentDAM: Privacy Leakage Evaluation for Autonomous Web Agents](https://arxiv.org/html/2503.09780v3) — arXiv v3, 2025-10-01；[NeurIPS 2025 Datasets & Benchmarks](https://arxiv.org/abs/2503.09780).

246个任务在自托管Reddit、GitLab与购物站副本中实际运行代理；人工种子扩展合成用户资料。最终站点状态衡量效用，动作文本由GPT-4o判断不必要披露；泄漏率为发生泄漏的实例比例，隐私率为1−泄漏率。98%人工一致率仅验证GPT-4o/axtree的一次运行。威胁模型明确无恶意参与者/外部攻击；不能代表提示注入防御。隐私感知提示减少泄漏但不保证零泄漏。[官方资源](https://github.com/facebookresearch/ai-agent-privacy)主体CC BY-NC 4.0、VisualWebArena部分MIT，数据另受Llama 3.1相关条款约束；不能整体标为MIT。

**实读范围：** v3 §3威胁模型、数据、指标、缓解方法，§4–5评测/讨论；arXiv会场记录及官方README许可段。定向阅读，未部署Web环境

<a id="benchmark-privacy-risk-search"></a>
### B62. Searching for Privacy Risks — 多轮身份冒充与伪造同意
- **论文与交叉索引**：ICLR 2026 / arXiv v3；方法见 **M59**。
- **评测对象与证据**：Training-5 与 Testing-100 配置，测试默认每配置模拟 10 次；Gemini 泄漏判断在 200 条人工标注动作上取得 98.5% 一致率。主体是合成 Agent 交互，不是真人研究。v3 另含 Atlas/GPT-5.1 操作真实 Outlook 界面的微型案例：5 次试验中攻击成功 3 次。
- **边界**：不能把 3/5 当产品总体风险或人群发生率。模拟中数据主体不再授予同意，合法分享尚未覆盖；人工标注一致率不是部署安全证明。此版本主指标称 leak velocity，与 leak rate 区分，不沿用旧版名称或混合数值。
- **资源与实读范围**：与 **M59** 相同；同篇、同版本、同许可边界。论文声明没有真人被试或个人可识别数据，真实邮件界面案例不等于使用了真实受害者数据。

<a id="benchmark-personal-data-flows"></a>
### B63. 第三方 GPT 的数据流与政策可追溯性

[Personal Data Flows and Privacy Policy Traceability in Third-party LLM Apps in the GPT Ecosystem](https://petsymposium.org/popets/2026/popets-2026-0015.pdf) — PoPETs 2026(1), 273–295; DOI 10.56553/popets-2026-0015.

**生态测量，非传统任务 benchmark。** 以 GPTStore.ai（2024年4月抓取）和 BeeTrove 为来源，筛出5,286个可解析 Action schema 的 GPT、44,102个参数；结合个人信息分类与政策解析，检查参数所指的数据类别是否获政策披露。约35%参数被归为敏感/可识别类别；792个GPT约占总体15%，具完整可追溯性；其中753个的相关Action参数全部被分类为NON_PI，未发现经这些参数发送个人信息。因此15%不是采集个人数据的应用中的充分披露率（§4.4.5）。

**边界：** 大规模结果主要描述schema允许/声明的数据流，并非逐个监测生产调用；另有三个受控端点的主动审计。完整披露不等于合法授权或隐私安全。仅研究Action参数收集，未追踪后续处理；英语政策限制、分类误差与跨平台外推须保留。

**实读范围：** 正式PDF §3.1–3.5、§4.1/4.4、§5.3；定向阅读，未独立复现。

<a id="benchmark-privaci"></a>
### B64. PrivaCI-Bench · 上下文理解与合规分类

[PrivaCI-Bench: Evaluating Privacy with Contextual Integrity and Legal Compliance](https://aclanthology.org/2025.acl-long.518/) — ACL 2025 Long Papers, July 2025, 10544–10559.

6,351个合规性判定样本及147,840道选择题，来自法院/执法案例、OPP-115/APP-350政策，以及基于AI Act检查器的合成情境；LLM提取CI信息流；三位作者与两位法学院学生校正解析错误，三位作者进行抽样质检。评测许可/禁止/不适用三分类与上下文理解，比较直接提示、CoT、RAG及给定标注CI/法规的条件；分类报告准确率、精确率、召回率与F1，选择题报告准确率。

**边界：** 将政策作为许可样本是构造假设，非独立法律审计；法律规范未覆盖个人、文化、伦理期待。单次评测、固定提示，未检验提示敏感性；不是运行时权限执行或专业法律判断系统。

**实读范围：** ACL原文§3–5、Limitations、Ethical Considerations。代码入口来自原文；未安装或核实再利用许可。

<a id="benchmark-mextra"></a>
### B67. 记忆抽取风险 / Memory extraction risk

[Unveiling Privacy Risks in LLM Agent Memory](https://arxiv.org/html/2502.13172v2) — ACL 2025 main；查阅 / reviewed v2, 2025-06-03。


- **阅读范围**：§§2–6、限制讨论、附录 B–C；官方仓库 README / 根目录。
- **输入 → 输出**：黑盒查询访问及不同程度的系统知识 → 从检索到的历史查询—解答记忆中抽取查询；主实验为 EHRAgent 与 RAP/WebShop，静态 200 条记忆。
- **测量**：独立抽取数、抽取效率、检索数、完全 / 任意抽取率；每个提示最多尝试三次。记忆由数据集查询及代理生成解答构成，不是正在运行的多用户服务调查。
- **边界**：研究设置没有用户 / 会话级记忆隔离；不能外推为隔离良好的产品同样泄漏，亦非完整隐私合规评测。
- **资源**：[官方代码](https://github.com/wangbo9719/MEXTRA)。所查根目录 / README 未见明确总许可；上游代码与数据条款需分别确认。

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

**核验日期 / 阅读范围**：2026-11-01；仅 v4 摘要，初读。

- **机制**：先将多模态演示中的隐含偏好表述为语言，再以其为条件生成动作计划。
- **边界**：显式中间表示有助于解释与迁移，不意味着偏好推断已可靠；评测、资源和全文核验限制见 [B29](#benchmark-pbp)。

<a id="method-cep"></a>
### M18. CEP · 澄清、执行与规划分工

[Ask-before-Plan](https://aclanthology.org/2024.findings-emnlp.636/) — 与 B30 同一篇，勿重复计数。

**核验日期 / 阅读范围**：2026-11-01；摘要、评测设置及附录 B.3、官方 README 的训练和推理入口。

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

<a id="method-guided-profile-generation"></a>
### M35. Guided Profile Generation · 引导式画像生成

[Guided Profile Generation Improves Personalization with LLMs](https://arxiv.org/html/2409.13093v1) — arXiv v1，2024-09-19。

**核验日期 / 阅读范围：**2026-11-01；§3–6、任务定义、指标和结果表。

- **方法：**按任务提问帮助消化个人历史，再生成自然语言画像，供后续回答使用；主实验仍保留原始历史。
- **评测：**Amazon 历史构成四选一购买预测、LaMP-7 文风重写、PER-CHAT 回复生成；分别看准确率、词面指标、语义相似度，不是同一“画像质量分”。
- **边界：**真人来源历史上的离线构造任务，不是持续用户实验；单来源文本、主要一个 GPT-3.5 版本。不能证明画像准确性、持续更新或执行能力；购买预测收益部分来自减少拒答；PER-CHAT 回复生成收益弱且不一致。
- **资源：**未核实官方代码或新增数据发布。论文 CC BY 4.0 不覆盖上游数据。

<a id="method-knowledge-graph-tuning"></a>
### M36. Knowledge Graph Tuning · 反馈驱动事实更新

[Knowledge Graph Tuning: Real-time Large Language Model Personalization based on Human Feedback](https://arxiv.org/html/2405.19686v1) — arXiv v1，2024-05-30。

**核验日期 / 阅读范围：**2026-11-01；§4、§5.1–5.4、§6：方法、实验设置、指标、消融和局限。

- **方法：**从问题与答案反馈提取三元组，增删外部知识图谱，优化检索与回答概率；不更新 LLM 权重。
- **评测：**顺序输入 CounterFact 与 GPT-4 辅助构造的 CounterFactExtension；测原问及改写问的事实编辑效果、延迟和显存。
- **边界：**反事实 QA 是个性化事实更新代理，不是真人偏好变化实验；关系反馈消融由 GPT-4 模拟用户。效果依赖指令遵循及关系提取；概率比较不等于开放任务完成率。
- **资源：**未核实官方可用发布及代码/数据许可；论文 CC BY 4.0。先前通过 GitHub connector 直接 GET https://api.github.com/repos/W-R-Liu/KGT 返回明确 NOT_FOUND / HTTP 404；该链接来自二手页，不应写作已核实官方实现，也不能据此认定永不存在。

<a id="method-emg-rag"></a>
### M37. EMG-RAG · 可编辑个人记忆图

[Crafting Personalized Agents through Retrieval-Augmented Generation on Editable Memory Graphs](https://aclanthology.org/2024.emnlp-main.281/) — EMNLP 2024；方法核验版本为 [arXiv v1，2024-09-28](https://arxiv.org/html/2409.19401v1)。

**核验日期 / 阅读范围：**2026-11-01；arXiv §4–5.2、§7；ACL 出版元数据及 PDF 方法概述。

- **方法：**层级记忆图支持插入、删除和替换；RL 选择相关记忆交给冻结 LLM。
- **评测：**真实助理对话/截图，经 GPT-4 提取记忆、生成 QA 标签；QA 用 ROUGE/BLEU，填表、提醒和导航用关键实体精确匹配；另测四周连续编辑。
- **真人证据：**另报一个月线上 A/B 适配，收集真人问题及人工答案，不能称“纯离线/全合成”。但这些分数不是满意度或完整外部操作成功率。
- **边界/资源：**RL 训练需反复查询 LLM；图中删除不证明日志/备份删除。未核实公开业务数据或官方实现。arXiv 论文 CC0 不授权私人数据。

<a id="method-hybridmem"></a>
### M38. HybridMem · 检索与分簇参数记忆

[Explicit v.s. Implicit Memory: Exploring Multi-hop Complex Reasoning Over Personalized Information](https://arxiv.org/html/2508.13250v1) — arXiv v1，2025-08-18；基准见 B46，同一论文只计一次。

**核验日期 / 阅读范围：**2026-11-01；§3 实验设置、§4–5 对比及 §6 混合记忆；官方 README、完整文件树和 release 元数据。

- **方法：**聚类用户陈述，为不同簇分别训练 LoRA adapter；推理时检索陈述，再以投票选择相关 adapter。
- **评测：**MPR 合成个人事实的多跳 QA，以规范化精确匹配比较显式、隐式和混合记忆；结合不同推理结构分析，不能跨设置混报。
- **边界：**不证明真实用户持续受益、在线记忆更新、隐私删除或行动执行。基准规模存在正文/表格矛盾，见 B46。
- **资源：**[官方仓库](https://github.com/nuster1128/MPR)，master，最后推送 2025-08-24，无 release 或声明的仓库许可；Drive 数据归档本次未能读取。论文 CC BY 4.0 不自动授权代码/数据；未安装或复现。

<a id="method-coloragent"></a>
### M39. ColorAgent · 个性化移动 GUI 执行与澄清

[ColorAgent: Building A Robust, Personalized, and Interactive OS Agent](https://arxiv.org/html/2510.19386v2) — 2025 技术报告；查阅 v2，2025-10-24。

**核验日期 / 阅读范围**：2026-11-01；§§2–6，重点 §4 实验、§5 个性化 / 交互及 §6 后续工作；官方 README、LICENSE 与 ColorGUI-32B 模型卡。

- **机制**：step-wise RL、自演进训练及检索、任务编排、分层反思；从历史轨迹提炼 SOP 与用户画像，重写当前请求 / SOP；另训练 ask-agent 进行澄清。这里主要是 **Android 移动端，不是桌面执行**。
- **证据**：AndroidWorld / AndroidLab 测动态环境任务成功；MobileIAR 测与用户意图标注一致的动作，VeriOS-Bench 测逐步动作匹配。不能把整体任务成功率直接称为个性化分数，也不能把逐步正确率视为完整任务完成率。
- **边界**：未证明真人长期满意度；作者指出现有任务与真实复杂使用存在差距，沙箱及细粒度权限仍待完善。遇到不确定情境询问用户不是全面安全保障。
- **资源**：[官方 MobileUse 仓库](https://github.com/MadeAgents/mobile-use)支持该报告，代码 [MIT](https://github.com/MadeAgents/mobile-use/blob/main/LICENSE)。2026-07-10 后续发布的 [ColorGUI-32B](https://huggingface.co/MadeAgents/ColorGUI-32B)模型卡标 Apache-2.0，基于 Qwen3-VL；**不等同于论文中的 GUI-Owl / Qwen2.5 实验检查点**。固定所用代码、模型与评测版本。

<a id="method-warpp"></a>
### M40. Agent WARPP · 用户属性驱动的运行时流程裁剪

[Agent WARPP: Workflow Adherence via Runtime Parallel Personalization](https://arxiv.org/html/2507.19543v1) — 2025 预印本；ICML 2025 Multi-Agent Systems Workshop；查阅 v1，2025-07-23。

**核验日期 / 阅读范围**：2026-11-01；§§3–6、§§8–9；官方仓库 README 与 LICENSE。

- **机制**：无需额外训练；Personalizer 根据用户属性裁剪条件流程及工具集合，并与模拟身份验证并行，再交给 Fulfillment 执行。保留相关工具的成功、失败与用户回答分支；这是属性条件化执行，不是持续学习个人偏好。
- **证据**：银行、航班、医院付款共五种意图，各 50 个样例；使用合成客户数据与 GPT-4o 模拟用户。分别报告轨迹匹配 / LCS、工具 F1、参数匹配、延迟及 judge 评价的裁剪相关性 / 完整性。
- **边界**：多数工具调用与 MFA 为模拟，部分复杂流程连接真实 API；不能因此称为生产部署或已验证身份安全。作者明确将安全、隐私、人参与及会话质量排除在本研究范围外；高负载、变化 API 与更复杂流程仍待检验。
- **资源**：[官方代码 / 数据](https://github.com/emiliamazzo/WARPP)，[MIT LICENSE](https://github.com/emiliamazzo/WARPP/blob/main/LICENSE)已核对；工作坊论文不要标作 ICML 主会论文。

<a id="method-privacychecker"></a>
### M41. PrivacyChecker · 决策时的信息流隐私判断

[Privacy in Action](https://aclanthology.org/2025.findings-emnlp.925/) — Findings of EMNLP 2025；查阅 [arXiv v1](https://arxiv.org/html/2509.17488v1)。评测见 B48；同一论文只计一次。

**核验日期 / 阅读范围**：2026-11-01；§3 方法 / 实验、§4 MCP 部署与扩展实验、Limitations；ACL 元数据与作者资源链接。

- **机制**：在行动决策时用提示明确提取 contextual-integrity 信息流，逐流判断可否披露；可选择加入隐私指南，主实验未使用可选指南。可放入系统提示、特定工具说明或独立 MCP 工具。
- **证据**：同时检查隐私泄露与任务帮助程度；静态 PrivacyLens、live MCP、MCP + A2A 和更复杂流程分别报告，不能把一个设置的降幅泛化至全部部署。
- **边界**：仍会因流提取、判断和行动不一致而泄露；记忆投毒等对抗场景不是主要验证范围。它是提示驱动缓解，不是强制访问控制、密码学保证或法规合规证明；独立检查工具也不能仅凭名称推断不可绕过。
- **资源**：同上[作者短链接](https://aka.ms/privacy_in_action)；抓取被 robots.txt 拒绝，当前发布包与许可未确认。论文公开不代表实现已获开放许可。

<a id="method-agentraft"></a>
### M42. AgentRaft · 执行过程中数据过度暴露检测

[AgentRaft: Automated Detection of Data Over-Exposure in LLM Agents](https://arxiv.org/html/2603.07557v1) — 2026 预印本；查阅 v1，2026-03-08。

**核验日期 / 阅读范围**：2026-11-01；§§3–6，包括实验设置、组件评测与局限；原文资源链接与定向资源检索。

- **机制**：由类型兼容性与语义判断构建跨工具调用图，合成触发指定路径的请求，结合运行时污点轨迹与多模型投票判断非必要数据是否传至外部。
- **证据**：6,675 是爬取工具的生态调查规模；实际实验为四类场景选定工具集，在 AgentDojo 中实现功能，并使用生成的 PII / 业务资产与 GPT-5.1 Agent。57.07% 指所测 608 条潜在调用链中的 347 条，不是全部商业 Agent 的泄露率。
- **边界**：依赖内部执行轨迹，未直接审计封闭商业 Agent 或终端用户真实部署。图边准确性、请求有效性、泄露检测与成本指标不能混报；LLM 判断错误和动态工具变化仍有限制。法规文本参与投票不构成法律认证；提示注入检测与运行时防御的扩展讨论不等于已证实安全能力。
- **资源**：原文未找到作者实现 / 数据发布链接，定向检索亦未确认；**发布状态与实现许可未确认**。AgentDojo 是实验底座，其开放许可不能替代 AgentRaft 实现许可。

<a id="method-rlpf"></a>
### M43. 用预测反馈压缩用户画像

[RLPF: Reinforcement Learning from Prediction Feedback for User Summarization with LLMs](https://arxiv.org/html/2409.04421v2) — AAAI 2025；查阅 v2，2025-01-17。

**阅读范围：**§§2–5，重点训练奖励、数据构造、评测指标、迁移结果与部署讨论，及附录 I 任务定义；版本记录及定向资源检索；未运行。

- **方法：**以未来行为预测正确性及长度奖励训练摘要器，将个人历史压缩成后续模型可用的自然语言画像；预测在真实下一项与三个随机负选项中选择，不是开放目录搜索。
- **证据与边界：**MovieLens 2015/2003、Amazon 评论与 Google Local 评论历史上的离线预测，不是真人长期助理实验；部分迁移任务退步。不能推导持续更新、执行能力或隐私保证。
- **资源：**未核实官方实现或新增数据发布；论文许可不覆盖上游数据与模型。
- **去重：**AAAI 与 arXiv 为同一研究；归入画像压缩，不另列画像更新成果。

<a id="method-ld-agent"></a>
### M44. 长期对话的事件与双向画像管理

[Hello Again! LLM-powered Personalized Agent for Long-term Dialogue](https://aclanthology.org/2025.naacl-long.272/) — NAACL 2025；出版 PDF；arXiv 别名 `2406.05925`。

**阅读范围：**§§3–4、Limitations、附录 A；官方 README、根目录和 LICENSE；未运行。

- **方法：**结合长短期事件记忆、主题检索、用户及助理画像，生成后续回复。
- **证据与边界：**MSC 众包角色扮演及 CC 模型生成对话上的离线评测；文本指标、画像分类和人工回复质量评分不等于真实长期效用或执行成功。
- **资源：**[官方实现](https://github.com/leolee99/LD-Agent)为 MIT；Drive 数据/权重未验证，README 仍将 CC 代码与数据列为待办。
- **去重：**出版版与 arXiv 只计一次。

<a id="method-aloe"></a>
### M45. 通过交互学习个人偏好对齐

[Aligning LLMs with Individual Preferences via Interaction](https://aclanthology.org/2025.coling-main.511/) — COLING 2025；方法查阅 [arXiv v2，2024-12-15](https://arxiv.org/html/2410.03642v2)。

**阅读范围：**§§2–5，含数据构造、训练、基准及人工评分核对；出版元数据、官方 README 和根目录；未逐项比较出版版，未运行。

- **方法：**生成树状偏好对话，进行 SFT 与 DPO；ALOE 是同篇研究的评测名称。
- **证据与边界：**100 个画像、十轮模拟交互；GPT-4o 扮演用户并评分。人工核对不等于真人纵向试用；不是持续在线学习或工具执行验证。
- **资源：**[代码与数据目录](https://github.com/ShujinWu-0814/ALOE)可读，根目录未见 LICENSE；检查点及资产许可未确认。
- **去重：**可设基准交叉链接，但不另增论文数；已有 RLPA 条目中的 ALOE 提及不构成独立收录。

<a id="method-ptool"></a>
### M46. PTool · 个性化工具调用的合成训练数据

与 B51 为[同一论文](https://arxiv.org/html/2505.04072v1)，实读范围相同。

- **机制：** 结构化 API/画像合成、角色扮演式请求与答案生成、规则/模型核验，再进行 LoRA SFT。
- **证据与边界：** Qwen2.5-7B 完整准确率由 7.38% 升至 26.78%；测量生成调用，非真实工具执行。

<a id="method-h2memory"></a>
### M47. H²Memory · 具体与抽象两层个人记忆

与 B52 为[同一论文](https://arxiv.org/html/2511.13410v2)，实读范围相同；PAL-Set 别名亦不另计。

- **机制：** 四组件准确为 Log Graph（日志图）、Background（背景）、Topic Outline（话题提纲）、Principle（原则），配合更新和关联检索。
- **证据与边界：** 优于列出的 PAL-Bench 基线；模拟交互与模型评分不能证明真实用户满意度或自主行动成功。

<a id="method-raise"></a>
### M48. RAISE · 选择性获取个人安全背景

与 B55 为[同一论文](https://arxiv.org/html/2505.18882v5)，实读范围相同，仅计一次。

- **机制：** 离线 LLM 引导 MCTS 缓存属性获取路径；在线检索指导提问，并判断信息是否足够/是否暂缓回答。
- **边界：** 使用基准中的用户背景进行评估；不证明现实咨询安全，也不构成收集敏感属性的授权依据。

<a id="method-prelude"></a>
### M49. PRELUDE / CIPHER · 从用户修改推断上下文相关偏好

- **论文与版本：** [Aligning LLM Agents by Learning Latent Preference from User Edits](https://arxiv.org/html/2404.15269v3)，NeurIPS 2024；arXiv v3，2024-11-23。PRELUDE 是框架、CIPHER 是算法，同一篇论文只计一次。
- **机制：** 从输出及其修改推断文字化偏好，检索相近上下文的偏好并聚合进生成提示；不微调基础模型。
- **证据：** 摘要写作与邮件写作各进行 200 轮 GPT-4 模拟用户交互，报告三个随机种子；最佳配置相对不学习基线的累计 token 编辑距离分别下降约 31% / 73%。另在 summarization 任务上有七名人工评审，每组比较 15 对输出；三名人工编辑按指定偏好修改输出。
- **边界：** 人工评审不是自然长期用户在线学习；主实验偏好由文档来源预设，编辑距离不等于真实时间节省或满意度，仍与已知真实偏好的 oracle 有差距。
- **资源与实读：** [官方代码与数据入口](https://github.com/gao-g/prelude)，仓库 MIT 许可，不替代来源数据自身许可。实读 v3 §§4.1–4.4、机制与指标段落，以及 NeurIPS 元数据和仓库资源页；未复现。

<a id="method-curio"></a>
### M50. CURIO · 用用户模型的改进奖励主动发现偏好

- **论文与版本：** [Enhancing Personalized Multi-Turn Dialogue with Curiosity Reward](https://arxiv.org/html/2504.03206v3)，[NeurIPS 2025](https://proceedings.nips.cc/paper_files/paper/2025/hash/e48d5af30c95be08762489c5141f7fbc-Abstract-Conference.html)；arXiv v3，2025-10-02。
- **机制：** 在多轮 RLHF 中加入逐轮用户类型信念改进的内在奖励；比较准确率、熵和势函数差分等奖励设计。
- **证据：** 运动推荐任务将采样属性按规则映射到八类策略；200 段模拟对话中最佳 DiffAcc 成功率 87.5%，MTRLHF 为 68.5%，SFT 为 54%。教育对话采用两种预设学习偏好。十名学生评审生成对话，非作为实时学习者使用系统。
- **边界：** 静态预设类型与 LLM 用户模拟限制外推；某些熵奖励出现偏向单一类型的行为。人工评审中 DiffLogAcc 相对 MTRLHF 的个性化偏好胜率约 76%，但附录的 152/200 与表格的 75.75% 不完全一致。质量偏好 90/200、p=.179，不能解释为证明等效；也未测量真实学习或健康效果。
- **资源与实读：** [作者项目页](https://sites.google.com/cs.washington.edu/curio)已核验，未核实官方代码、权重、数据集或其许可证，不标为开源。实读 v3 方法、§§4–5、局限、附录 B.1–B.3 及官方会议信息；未复现。

<a id="method-grounded-memory"></a>
### M51. A Grounded Memory System · 从视觉观察构建实体记忆

- **论文与版本：** [A Grounded Memory System For Smart Personal Assistants](https://arxiv.org/html/2505.06328v1)，arXiv v1，2025-05-09；ESWC 2025 TEXT2KG workshop，非 ESWC 主会论文。
- **机制：** GPT-4o 对重叠视频窗口生成描述并标识实体；Neo4j 存储带向量的记忆笔记与时间/实体图。检索 agent 在语义检索、PageRank 图扩展和 text-to-Cypher 间选择。
- **证据：** iPhone 家庭场景视频原型与代表性问答；不是对照实验、用户研究或公开基准。展示问答被作者标为正确，不应改写成评测准确率 100%。
- **边界：** 不能据此断言优于标准 RAG、具备可靠长期实体一致性或已在失智症照护中验证；扩展规模、长期实体消歧及更多模态均属于后续工作。
- **资源与实读：** 未核实官方代码/数据发布及其许可。实读 §§3–5 与 arXiv 版本/工作坊元数据；未复现。

<a id="method-iotgpt"></a>
### M52. IoTGPT

**方法：个性化设备执行与子任务记忆复用**

[Leveraging LLMs for Efficient and Personalized Smart Home Automation](https://arxiv.org/abs/2601.04680) · **arXiv v1，2026-01-08**；未确认正式发表场所。

- **机制：** Decompose–Derive–Refine 流程、层级任务记忆和环境属性偏好表，将指令转换为 SmartThings 操作并复用子任务。
- **证据：** 97 个任务、26 个模拟设备；warm 条件重做已学习任务的改写版本。15 名真人参加短时研究，但偏好来自 **100 条 GPT-4o 合成日志**，不是参与者自身历史。
- **边界：** 不证明真实家庭长期个性化；偏好冲突和设备副作用尚未完整处理。**不安全或幻觉指令仍需用户审核**，自动安全防护属于未来工作。
- **资源：** 尚未找到并核实作者官方实现与许可证；不写成已开源。
- **实际阅读：** 系统、实现、比较实验、两项用户研究及局限章节；未安装或复现。

<a id="method-gaap"></a>
### M53. GAAP

**方法：运行时信息流控制与披露授权**

[An AI Agent Execution Environment to Safeguard User Data](https://arxiv.org/abs/2604.19657) · **arXiv v3，2026-09-24**；未确认正式发表场所。

- **机制：** 受限计划解释器与信息流控制，结合持久化私有数据、权限和披露日志，约束跨步骤、跨任务的数据披露。
- **保证范围：** 针对恶意模型/提供方及外部服务；依赖正确执行、用户授权和经核验的工具语义标注。**提示词中直接输入的秘密、提示时序元数据及数据/系统完整性不在保证内**。
- **证据：** 自建 20 任务、七类攻击测试未出现成功披露；AgentDojo/AgentDyn 在批准全部披露的条件下仅测效用。不是普遍安全证明或真人可用性研究；论文报告显著费用/延迟开销。
- **资源：** [源码公开](https://github.com/rssta/gaap)，但未发现 LICENSE，GitHub 许可字段为空；不声称具备开源使用授权。
- **实际阅读：** v3 威胁模型、设计、评估与讨论；官方 README、目录和许可元数据；未安全审计。

<a id="method-alignxplore"></a>
### M54. AlignXplore · 从行为信号推断可更新偏好

[Extended Inductive Reasoning for Personalized Preference Inference from Behavioral Signals](https://arxiv.org/html/2505.18071v2) — arXiv v2, 2025-07-07；未核实正式会场。

将行为样例转换为自然语言偏好，以合成冷启动数据和GRPO训练推断模型；流式设置复用已有偏好摘要。AlignX/P-Soups实验主要使用偏好比较对；指标区分Acc_jud（偏好判断）、Acc_gen（偏好引导生成）与GPT-4 win rate；所谓“online evaluation”是GPT-4裁判比较生成回答，不是真实用户在线实验。主设置为两轮、每轮四条信号；§4.4另有八对信号的模拟反转测试，§4.5效率实验延至第四轮、累计16条信号。论文明确缺少真实LLM—用户交互验证，不能据此宣称长期偏好漂移已解决。隐私/同意陈述不是形式保证。[官方代码](https://github.com/AntResearchNLP/AlignXplore)可访问，未确认项目根目录许可证；论文CC BY-NC-ND不等于代码许可。

**实读范围：** v2 §3、§4评测设置与流式实验、Appendices C–D；官方README与根目录。定向阅读，非全文逐页审读

<a id="method-psg-agent"></a>
### M55. PSG-Agent · 用户相关风险的分阶段护栏

[PSG-Agent: Personality-Aware Safety Guardrail for LLM-based Agents](https://arxiv.org/html/2509.23614v1) — arXiv v1, 2025-09-28；未核实正式会场。

从历史和当前请求构造用户安全条件，再以计划、工具、回答及记忆写入检查落实。132个人工种子经GPT-4o扩展，约2,900例且历史为模型生成；200例质量检查由四位专家各评50例。ALLOW/REFUSE分类以准确率、精确率、召回率和F1评价；另行采用三模型多数裁决评估安全/帮助性，配100例人工一致性检查。评测支持合成场景下的用户差异化安全判断，不证明真实医疗/金融安全或长期风险控制；运行时门控也不是形式安全/隐私保证。[论文所链匿名代码](https://anonymous.4open.science/r/psg-agent-code-7724/)本次无可读正文，完整性与许可未核实。

**实读范围：** §3–5、威胁建模、组件与人工/模型裁判设置；匿名仓库入口。定向阅读，未审代码

<a id="method-encode-store-retrieve"></a>
### M56. Encode–Store–Retrieve — 语言编码的第一人称记忆
- **论文**：*Encode-Store-Retrieve: Augmenting Human Memory through Language-Encoded Egocentric Perception*，ISMAR 2024；arXiv `2308.05822` v3（2024-10-18）；作者页面亦使用 “Enhancing Memory Augmentation” 标题变体。
- **方法与证据**：ego-LLaVA 将视频编码为文本，Chroma 检索后交给 GPT-4。QA-Ego4D 评测之外，12 人使用 HoloLens 2 完成受控居家任务，5–7 天后测试回忆；参与者评分为系统 4.1/5、人类回答 2.5/5。
- **边界**：逐帧编码难以保留动态动作与计数；缺少真实长期部署。设备无关不等于跨设备同步。视频上传服务器、文本化存储均不能证明隐私保护或安全隔离。
- **资源与实读范围**：[ISMAR 作者 PDF](https://pokristensson.com/pubs/ShenEtAlISMAR2024a.pdf) §§3–7；[版本记录](https://arxiv.org/abs/2308.05822)。未确认官方实现、权重或软件/数据再使用许可；不把既有 QA-Ego4D 当成本论文新发布数据。

<a id="method-livia"></a>
### M57. Livia — AR 情绪陪伴与压缩记忆
- **论文**：*Livia: An Emotion-Aware AR Companion Powered by Modular AI Agents and Progressive Memory Compression*，AIVR 2025 作者接收稿；arXiv v1（2025-08-12）。
- **方法与证据**：模块化情绪、对话、记忆和行为编排，TBC/DIMF 记忆压缩与 AR 呈现。§8 报告 50 名用户的 200 条片段、38 人四周使用、24 人访谈及 11,504 轮日志；这些样本口径不可相加或互换。
- **边界**：年轻、北美、英语样本；比较分组描述有限。摘要宣称孤独感显著下降，但评测未给出对应量表、前后测统计或显著性检验，**不据此宣称临床/心理健康疗效**。实时面部表情分析属未来方向；加密、同意与安全存储是部署要求，非验证过的保证。
- **资源与实读范围**：[作者稿](https://arxiv.org/pdf/2509.05298) §§3–10；[版本/会议信息](https://arxiv.org/abs/2509.05298)。稿件 CC BY-NC-ND 4.0；未确认官方代码/数据发布或软件许可。

<a id="method-aipom"></a>
### M58. AIPOM — 可检查、可修改的多 Agent 计划
- **论文**：*AIPOM: Agent-aware Interactive Planning for Multi-Agent Systems*，EMNLP 2025 System Demonstrations，85–96。
- **方法与证据**：聊天与可编辑图联合表达任务、Agent 分配、依赖和输出。实验使用 50 道 GSM8K、50 道 BBH 算术题及人工扰动的计划；真人先导研究为 9 名有 LLM 经验的研究机构成员、12 道数学题。参与者反馈离线后处理，未要求其确认/拒绝实际修订结果。
- **边界**：支持计划检查与修改，不是执行权限、敏感操作授权或安全保证；不能推广为一般用户的长期信任。系统是集中编排的功能模块，不是自主主动 Agent 群。
- **资源与实读范围**：[论文](https://aclanthology.org/2025.emnlp-demos.7.pdf) §§2–4、6、附录 C；[官方代码/演示](https://github.com/megagonlabs/aipom)。根 `LICENSE` 为 BSD-3-Clause；数据和依赖许可独立，README 另列第三方材料限制；web-search 默认禁用。未安装复现。

<a id="method-privacy-risk-search"></a>
### M59. Searching for Privacy Risks — 交替搜索攻击与防御提示
- **论文与交叉索引**：*Searching for Privacy Risks in LLM Agents via Simulation*，ICLR 2026；arXiv v3（2026-05-08）。同篇评测见 **B62**，只计一篇。
- **方法**：用 LLM 分析轨迹，平行搜索并跨线程传播，交替优化攻击者与防御者指令；从直接索取发展到身份冒充/伪造同意，对应防御发展为提示层身份核验状态机。
- **边界**：这些是模型遵循的指令，不是形式化权限系统或加密身份认证；不得写成可保证防泄漏的安全机制。合法同意分享与真实部署可靠性仍需独立验证。
- **资源与实读范围**：[v3](https://arxiv.org/html/2508.10880v3) §§3–4、伦理说明、附录 G；[官方代码](https://github.com/SALT-NLP/search_privacy_risk)与[轨迹数据](https://huggingface.co/datasets/SALT-NLP/search_privacy_risk)。数据卡标 MIT；代码根目录未观察到许可，不能用数据许可替代代码许可。数据 viewer 报错不等于源文件不可下载；未运行复现。

<a id="method-topdial"></a>
### M60. TopDial · 个性化目标对话的角色扮演数据生成

[Target-oriented Proactive Dialogue Systems with Personalization: Problem Formulation and Dataset Curation](https://arxiv.org/html/2310.07397v2) — EMNLP 2023; arXiv v1 2023-10-11, read v2 2023-10-13.

用户、系统和moderator三个gpt-3.5-turbo角色，以重构DuRecDial 2.0、随机画像slot和Big Five描述生成18,009个多轮对话；目标为系统侧〈对话行为、主题〉。100个目标的配对对话由模型/人工评价；等训练量微调DialoGPT/Alpaca-7B，以混合测试集的BLEU、知识F1、画像F1及target success检验训练资源效果。

**边界：** 合成角色与离线指标，不是真实用户主动帮助接受度；存在幻觉和moderator误判终止。用户第二次明确拒绝目标行为时才触发拒绝终止规则；这不构成部署安全保证。作者提醒目标约束、用户隐私与bot身份透明。

**实读范围：** v2 §3–4、Limitations、Ethical Considerations；代码/数据链接来自原文，未复现。不另列第二个benchmark条目。

<a id="method-plus"></a>
### M61. PLUS — 共训练用户文字摘要与个性化奖励模型
- **论文**：*Learning to summarize user information for personalized reinforcement learning from human feedback*，ICLR 2026；arXiv v4（2026-08-26）。
- **方法与证据**：PPO 优化用户摘要，交替训练摘要条件奖励模型；Pets/UltraFeedback 为构造偏好任务，PRISM 为既有真人对话数据。PRISM 使用1,000位用户训练，已知用户奖励预测准确率62.9%（BTL 59.8%），未见用户预测仍困难。
- **边界**：GPT-4o 的72%胜率由依据用户自述偏好训练的 oracle 奖励模型判定，非人类投票或部署满意度；正文“308用户×2提示”与附录“906提示”不一致，不合并样本口径。online co-adaptation 指训练循环，非真实用户持续在线学习；摘要编辑是未来方向。训练对超参敏感，文字摘要不自动提供隐私保护。
- **资源与实读范围**：[v4](https://arxiv.org/html/2507.13579v4) §§4–7、伦理/复现说明、附录F；[官方项目页](https://sites.google.com/stanford.edu/plus/home)及其[代码](https://github.com/nam630/pluralistic_user_summary_public)。代码 Apache-2.0；论文 CC BY-NC-SA 4.0。未核实完整训练权重/数据发布。

<a id="method-user-profile-ablation"></a>
### M62. Understanding the Role of User Profile — 历史响应与上下文顺序消融
- **论文**：*Understanding the Role of User Profile in the Personalization of Large Language Models*，arXiv v1（2024-06-22）；未确认正式发表场所。
- **方法与证据**：在LaMP六任务（排除LaMP-6）比较用户历史输入、响应、映射关系及顺序；主要使用微调 Flan-T5-base，另测冻结 Llama2-7B-chat。报告验证集结果，非不可用的隐藏测试集；没有新招募用户试验。历史响应通常贡献较大，仅保留历史响应的上下文可容纳更多记录，靠前画像在该设置影响较大。
- **边界**：这是现有画像条件化机制分析，不是新通用执行Agent。结果限定于所测模型、任务、提示及输入长度；不能推出所有模型都应丢弃历史输入、忽略映射，或普遍存在相同位置效应。自动任务指标不等于真实用户满意度或长期适配效果。
- **资源与实读范围**：[原文](https://arxiv.org/html/2406.17803v1) §§3–5、附录A/B；[官方代码](https://github.com/Bingo-W/Personalisation-in-LLM)。代码 MIT；论文 CC BY 4.0。既有LaMP资源不是该论文新发布的数据集。

<a id="method-opencha"></a>
### M63. openCHA — 健康范围内的个体数据与分析工具编排
- **论文**：*Conversational health agents: a personalized large language model-powered agent framework*，JAMIA Open 8(4), ooaf067，2025-07-06；[DOI](https://doi.org/10.1093/jamiaopen/ooaf067)。早期 arXiv v5（2024-09-25）为两个演示、四用例；正式版为两个演示、五用例，不混用版本。
- **方法与证据**：planner/executor、数据管道及外部分析工具组合个体健康记录、知识检索与多步操作。正式版总结100道糖尿病问题、500次情绪问题测试及45人既有居家监测数据的PPG心率估计；这些是不同用例，不能汇总为统一参与者试验。
- **边界**：健康研究框架，不是治疗改善、诊断安全或长期临床部署证据。真实纵向健康数据不等于Agent进行了纵向干预。表现取决于外部来源及配置；论文明确HIPAA/GDPR合规取决于实施，框架本身不管理部署与扩展性。
- **资源与实读范围**：[正式版](https://academic.oup.com/jamiaopen/article/8/4/ooaf067/8186991) 方法、演示/用例、Table 4与讨论；对照[v5](https://arxiv.org/html/2310.02374v5) §§3–5；[官方代码](https://github.com/Institute4FutureHealth/CHA) MIT，含文档/示例/测试。代码许可不是临床使用认证或数据再使用授权。

<a id="method-scrapmem"></a>
### M64. ScrapMem — 多模态视觉压缩与事件图记忆
- **论文**：*ScrapMem: A Bio-inspired Framework for On-device Personalized Agent Memory via Optical Forgetting*，arXiv v2（2026-05-25）；未确认正式发表场所。
- **方法与证据**：多模态资料汇为scrapbook pages，以事件图检索并随资料年龄降低JPEG质量/分辨率。在ATM-Bench既有四年个人资料上，No-Forget 的 Joint@10/Recall@10 为51.0/70.3；表1遗忘配置为46.9/66.1。93%节省对应 Timed-Gentle（4302.9→299.5 MiB，Joint@10 46.3），不是51.0配置。
- **边界**：四年资料不等于四年Agent部署。Qwen3-VL-2B处理记忆，GPT-5-mini API作评判；实读实验段未报告具体终端硬件、延迟、能耗或端到端离线实测。压缩会丢失日期、时刻、地址，可能诱发错误推断；不等于安全擦除或隐私保证。
- **资源与实读范围**：[v2](https://arxiv.org/html/2605.03804v2) §§4–5、附录B及版本信息。论文与定向搜索未确认官方代码/权重发布；arXiv永久非独占分发许可不是软件开源许可。

<a id="method-theanine"></a>
### M65. 时间线记忆 / Timeline-based memory

[Towards Lifelong Dialogue Agents via Timeline-based Memory Management](https://arxiv.org/html/2406.10996v3) — NAACL 2025；查阅 / reviewed v3, 2025-01-29。评测见 / evaluation: **B70**；同一论文 / same paper。


- **阅读范围**：§§2–6、附录 D/E/J；官方 README / 根目录。
- **机制**：保留旧记忆，以时间及关系连接图节点；检索完整时间线、按当前对话精炼后辅助生成。
- **证据**：MSC / Conversation Chronicles 上的自动、模型与人工评测及消融；TeaFarm 另测反事实问题下的记忆使用。
- **边界**：“lifelong” 是系统目标，不是终身真人研究；保留旧记忆不解决撤回同意、删除及权限隔离。
- **资源**：[官方代码](https://github.com/kimnamssya/Theanine)。所查根目录未见独立代码 LICENSE；论文附录的非商业数据条款不应自动解释为代码授权，项目网站模板许可也不等于研究资源许可。

<a id="method-ariel"></a>
### M66. 脑电辅助情绪适配 / EEG-assisted emotional adaptation

[ARIEL: Brain-Computer Interfaces meet Large Language Models for Emotional Support Conversation](https://iris.uniroma1.it/handle/11573/1727073) — UMAP **Adjunct** ’24, pp.601–609；DOI 10.1145/3631700.3665193。


- **阅读范围**：机构记录及所附出版 PDF §§3–5。
- **机制**：脑电分类得到的情绪标签与文本消息，经硬提示模板输入 LLaMA 2 Chat。
- **证据**：组件研究采集 30 人、每人 40 个音乐视频试次的 Muse 2 EEG；论文报告知情同意及匿名化。LOSO 与五折调参下，SVM 分情绪（per-emotion）准确率分别为 Happy .77、Angry .78、Sad .76、Relaxed .80；端到端对话仅提供受控真实会话示例。
- **边界**：分类准确率不是心理支持疗效；in-vivo 系统评估仍列为未来工作。不得将推断标签写成对真实心理状态的可靠读取或临床有效性。
- **资源**：上述机构 PDF 为 all rights reserved；所查来源未找到官方代码 / 数据发布。作者所述隐私处理不等于独立安全审计。

<a id="human-studies"></a>
## 人机研究：真实使用与互动

以下研究记录真实人的体验，不作为 benchmark 分数或长期效果证明。

<a id="human-agent-memory-expectations"></a>
### H1. Users’ Expectations and Practices with Agent Memory · 用户对记忆的理解和控制需求

- **论文与版本：** [作者原文](https://younghokim.net/files/papers/jones-agent-memory-chi25lbw.pdf)，CHI EA 2025 late-breaking work，8 页；[DOI](https://doi.org/10.1145/3706599.3720158)。不是主会完整研究论文、benchmark 或 agent 算法。
- **研究设计：** 六名 24–35 岁的真实用户接受 30–45 分钟访谈；均将工具使用熟练度自评为 4/5。另对 54 个 Reddit 讨论线程作归纳主题分析。
- **发现：** 用户对记忆机制存在不完整心理模型，希望按任务、项目和领域组织/隔离记忆；五名受访者提出不相关任务记忆应分离。既有做法包括分开聊天、定制角色/指令和不同账号。
- **边界：** 小型探索性质性研究；线程不是 54 名实验参与者。不能据此估计总体比例、证明层级记忆的因果收益或声称实现了访问控制。
- **资源与实读：** 实读方法、发现及附录访谈提纲/问卷/社区名单。未核实原始研究数据或代码公开；作者 PDF 为作者保留版权并允许指定个人/课堂复制，不等于开放数据或开源许可。

<a id="human-memoro"></a>
### H2. Memoro · 实时记忆辅助的简洁交互

- **论文与版本：** [Memoro: Using Large Language Models to Realize a Concise Interface for Real-Time Memory Augmentation](https://arxiv.org/html/2403.02135)，CHI 2024，arXiv v1，2024-03-04；[DOI](https://doi.org/10.1145/3613904.3642450)。按系统与真实人机实验收录，不作为 benchmark。
- **机制与设计：** 音频转录和向量检索，经骨传导耳机返回简短提示；显式 Query 和用户按键触发的 Queryless 模式。20 名 18–32 岁参与者进行约一小时、四条件平衡顺序的实验室研究，围绕虚构人物资料与研究者交谈；谈话期间不新增外部记忆。
- **证据：** 回答平均字符数由 Baseline 的 115.4 降至 Query 的 16.6；正确率 Query 84%、Queryless 70.7%。回忆信心和困难度是自报指标，不是客观长期记忆提升。多项对话指标无显著差异，但自然度显著低于无系统条件，不能笼统声称毫无干扰。
- **边界与资源：** Queryless 不是自主主动干预；隐私同意为前提，旁观者权限控制未解决。[官方参考实现](https://github.com/wazeerzulfikar/memoro/)为 MIT 许可、非维护中产品；其另述 V2 老年人实地研究不属于本篇，V2 代码不在该仓库。实读系统、§§4–5、§7 及仓库版本/许可说明；未复现。

<a id="human-loom"></a>
### H3. LOOM

**人机研究：由日常对话驱动的主动学习辅助（非 benchmark）**

[LOOM: Personalized Learning Informed by Daily LLM Conversations Toward Long-Term Mastery via a Dynamic Learner Memory Graph](https://arxiv.org/abs/2511.21037) · **AAAI 2026 PerFM Workshop**；arXiv v1，2025-11-26，非 AAAI 主会论文。

- **系统：** 对话摘要、主题与课程规划、内容生成及动态学习者记忆图，结合完成记录与自报掌握程度调整建议。
- **真人证据：** 便利抽样的 **10 人、约两天**形成性研究；要求各自产生 10–15 段反映日常问题的新对话。主要观察是自报相关性、连贯性和知识缺口发现。
- **边界：** 无对照、前后测或延迟保持测试；**不能声称提高长期掌握程度**。内容质量、重复及模型推断“已掌握”仍有问题。
- **资源：** PDF 提供[匿名代码/演示入口](https://anonymous.4open.science/r/LoomDemo)，本次访问返回 **HTTP 403**；内容及许可证未核实。
- **实际阅读：** 原文系统、研究方法、结果和局限；[PDF](https://arxiv.org/pdf/2511.21037) 的 workshop 标注及资源脚注；未运行系统。

<a id="human-compeer"></a>
### H4. ComPeer — 主动同伴支持
- **论文**：*ComPeer: A Generative Conversational Agent for Proactive Peer Support*，UIST 2024；DOI `10.1145/3654777.3676430`。读取 arXiv v2（2024-08-06）。
- **方法与证据**：根据对话记忆检测事件、反思并安排主动消息。24 名中国大学生随机分组，首周与共享记忆和生成模块、但不主动发起对话的基线比较；第二周全部使用 ComPeer。
- **边界**：两组自报压力均下降，组间无显著差异；不能宣称优于基线的压力改善或临床疗效。短期、学生样本和新奇效应限制推广；打扰、错误信息、同伴压力与依赖风险仍存在。
- **资源与实读范围**：[论文](https://arxiv.org/html/2407.18064v2) §4–7；[作者代码](https://github.com/liutj9/ComPeer)。未确认代码许可证；arXiv 发布许可不等于代码许可。

<a id="human-planfitting"></a>
### H5. PlanFitting — 个人约束驱动的运动规划
- **论文**：*PlanFitting: Personalized Exercise Planning with Large Language Model-driven Conversational Agent*，**CUI 2025 正式版**，19 页；DOI `10.1145/3719160.3736607`。
- **方法与证据**：通过动态提示与检索收集目标、时间和障碍，生成并修订 IF–THEN 周计划。18 名真实参与者完成约一小时实验；后续修订基于**想象的下一周情境**。两名研究者检查指南一致性；三名物理治疗师各评六份初始计划。不是随机对照健康干预。
- **边界**：测量计划质量和用户感知，未验证长期依从性、运动收益或临床安全；仍有休息日和运动组合问题。
- **资源与实读范围**：[正式版本 PDF](https://faculty.washington.edu/garyhs/docs/shin-cui2025-planfitting-paper.pdf) §4–6、§7.5。论文 CC BY 4.0；代码/数据许可未确认。

<a id="human-teachtune"></a>
### H6. TeachTune — 教师审查与学生模拟
- **论文**：*TeachTune: Reviewing Pedagogical Agents Against Diverse Student Profiles with Simulated Students*，CHI 2025；DOI `10.1145/3706598.3714054`。
- **方法与证据**：教师编辑代理状态图及学生知识/特征，观察模拟对话。30 名科学教师分为三组：直接聊天/单轮测试、完整 Autochat、仅模拟知识的 Knowledge；另六名观察参与者不计入组间统计。Autochat 参与者提交更多不同学生画像；自评覆盖感无显著差异。两位专家评估的代理质量也无显著组间差异。
- **边界**：真实参与者是教师，学生是模拟的；未测真实学生学习增益。单一相变主题、有限静态特征和模拟真实性限制推广。
- **资源与实读范围**：[论文](https://jeongeonpark.com/assets/pdf/papers/chi25-teachtune.pdf) §4、§5.3–5.4、Table 5、§7；[项目页](https://teachtune.kixlab.org/)需联系试用。论文 CC BY-NC-SA 4.0；代码许可未确认。

<a id="human-memolet"></a>
### H7. Memolet — 可操作的对话记忆
- **论文**：*Memolet: Reifying the Reuse of User-AI Conversational Memories*，UIST 2024；DOI `10.1145/3654777.3676388`。
- **方法与证据**：可视对象支持抽取、组织、添加/排除、加权与合并记忆，并通过提示/RAG影响生成。12 名真实参与者进行被试内比较，在一天后复用写作、编程或旅行规划对话；两条件共享基础生成/检索能力。
- **边界**：主要支持交互控制与用户体验结论，不证明长期记忆准确性或自主记忆管理。便利样本、受控任务和一天间隔限制真实部署推广。
- **资源与实读范围**：[作者 PDF](https://www.jeffjianzhao.com/papers/memolet.pdf#page=1) §4.6、§5–6、§8。作者版标注个人使用、不得再分发；未确认开放代码/数据许可。

<a id="human-chatlab"></a>
### H8. ChatLab — 用户定制角色、头像与语音输出
- **论文**：*Customizing Emotional Support: How Do Individuals Construct and Interact With LLM-Powered Chatbots*，CHI 2025；arXiv v2（2025-04-18）。
- **方法与证据**：约一周田野研究（流程允许 7–10 天），26 人完成田野阶段，分析 22 人的资料，结合日记、访谈与设计活动；研究用户如何定制情感支持角色、头像和 TTS 输出。**不支持语音输入**。
- **边界**：设计探针，不是心理健康疗效试验；短期、亚洲文化样本不能证明长期获益。可调记忆是受访者提出的设计机会，不应写成已实现功能。研究团队访问控制与云端存储描述不构成安全保证。
- **资源与实读范围**：[论文](https://arxiv.org/html/2504.12943v2) §§3–4、6–8；[作者原型页](https://xizhengxi.com/prototypes.html)。未确认官方代码/数据发布或软件许可；arXiv 分发许可不等于开源许可。

<a id="human-financial-advisors"></a>
### H9. Personalized Financial Advisors — 偏好获取、建议质量与主观信任
- **论文**：*Are Generative AI Agents Effective Personalized Financial Advisors?*，SIGIR 2025；arXiv v2（2025-04-15）。
- **方法与证据**：Llama-3.1-8B 先通过对话获取偏好，再讨论四只股票；比较非个性化/个性化及外向/尽责人格。招募64人，分析保留60人（个性化29人、人格31人）。参与者扮演三个专家设计的投资者画像，并非表达自己的真实投资需求。专家偏好获取对照每画像3名参与者。
- **边界**：测偏好获取准确率、与专家资产排序的相关性及信任/满意度，不测真实交易收益或长期理财效果。错误偏好获取可能导致不适配建议；外向人格较受喜欢不等于建议更好。单校受控角色扮演不能支持替代专业顾问的结论。
- **资源与实读范围**：[原文](https://arxiv.org/html/2504.05862v2) §§3–5、结论及版本信息；[官方补充仓库](https://github.com/TTsamurai/LLMAdvisor_supplementary) 的画像、提示词及分析脚本说明。仓库 README 声明 MIT；所读 arXiv v2 为 CC BY 4.0（不代表 SIGIR 出版版许可）。未核实完整原始参与者数据发布。

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
