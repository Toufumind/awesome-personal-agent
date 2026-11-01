# 个人 Agent 论文与评测 · Papers & benchmarks

[English](PAPERS.en.md) · [返回主清单](../README.md)

**先分清测了什么，再看分数。** 这里把 eval / benchmark 与 agent 方法 / 系统分开，并区分“直接研究个人上下文”“可迁移的通用记忆 / 执行能力”及“特定隐私 / 安全风险”。

文献与资源核验：**2026-10-31**。共 **40 篇不同论文**：27 个评测条目、15 个方法条目；Proactive Agent 与 MemoProAgent 各同时贡献 benchmark 和方法，分别只计一次论文。来源为论文摘要与下列明示的原文段落、作者项目页、官方代码库和数据卡；**没有安装复现、独立跑分、模型训练或安全审计**。这是精选阅读入口，不是完整综述、最新论文榜或产品排名。

**待审增量**：B25–B27 核验于 2026-11-01；旧条目保留原核验日期。尚未发布。

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
| 怎样管理长期记忆与生命周期 | [MemGPT](#method-memgpt)、[MemoryBank](#method-memorybank)、[A-MEM](#method-a-mem)、[Mem0](#method-mem0)、[Zep](#method-zep)、[MemOS](#method-memos) | 失效或不再使用不等于物理删除；还需权限、调度与可观测性 |
| 怎样复用经验、技能与多代理协作 | [ReAct](#method-react)、[Reflexion](#method-reflexion)、[Voyager](#method-voyager)、[ExpeL](#method-expel)、[AutoGen](#method-autogen)（历史） | 长期真人效用、单代理对照、经验过时与运行成本 |


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


