# 从个人任务出发：连接论文、项目与产品

[English](LANDSCAPE.en.md) · [主列表](../README.md) · [论文](PAPERS.md) · [产品](PRODUCTS.md) · [任务卡](TASKS.md)

**先选你不能接受的失败，再看功能列表。** 本页把实际需求、技术思路、相关评测与可进一步考察的实现放在一起，帮助阅读和选型；不是排行榜，也不表示某个产品采用了某篇论文。

**核对日期：2026-10-31（UTC）。** 依据是仓库中带日期的目录，以及下文链接的一手来源。未安装产品、连接账号或运行基准；六张本地任务卡仍全部为**未执行**。示例是有选择的；没有列出不等于没有能力，也不等于测试失败。

## 选择一条路线

| 你想做什么 | 最需要区分什么 | 路线 |
| --- | --- | --- |
| “下次记得我修改后的偏好。” | 记得、更新、真正遵循偏好不是一件事 | [1 · 记忆](#memory) |
| “结合你对我的了解，准备正确的操作。” | 记住事实、填对工具参数、获得授权并完成操作不同 | [2 · 从记忆到行动](#memory-action) |
| “持续做事、按时提醒，或在合适的时候帮忙。” | 持续执行已委托任务、定时触发、自主提出帮助不同 | [3 · 跨时间工作](#across-time) |
| “研究资料，并产出或整理文件。” | 看起来合理的回答不等于可核查的网页/文件状态 | [4 · 浏览器与桌面](#execution) |
| “替我操作手机里的 App。” | 手机聊天入口不等于手机 GUI 控制 | [5 · 手机](#mobile) |
| “发出去之前问我，不要听文档里的恶意指令。” | 工具权限、操作授权、信息是否适合外传不同 | [6 · 边界](#boundaries) |

**如何理解这里的关联**

- **直接关联：** 作者或维护者明确连接论文、代码或基准；[来源关系表](#direct-links)只记录证据支持的窄范围结论。
- **主题关联：** 本指南把机制、评测问题与示例放在一起，**不证明采用关系、架构等价、参加过该基准或性能可比。六条路线中，项目/产品与基准的搭配一律是主题关联，除非来源关系表另有说明。**
- 建议的本地检查不是所引用的科研基准；即使通过小测试，也不能据此验证整篇论文的主张。

<a id="memory"></a>
## 1 · 记住修改，而不只是旧事实

**技术阅读。** [MemGPT](https://arxiv.org/abs/2310.08560)研究上下文与外部记忆之间的信息调度；[2025 年 Mem0 论文](https://arxiv.org/abs/2504.19413)研究对话信息的提取、整合与检索。两者是不同机制，不能统称为“有记忆”就不再区分。见[记忆方法 M2/M4](PAPERS.md#memory-methods)。

**评测问题。** [LongMemEval](https://github.com/xiaowu0162/LongMemEval)区分知识更新、时间推理、回忆与拒答；[PrefEval B8](PAPERS.md#personal-evaluation)进一步问回答是否真正遵循偏好。能正确回忆，不能证明偏好使用、删除或用户隔离正确。

**考察实现。** [Letta Code](https://github.com/letta-ai/letta-code)记录了可编辑记忆与历史检索；[Mem0](https://github.com/mem0ai/mem0)是记忆组件，不是完整助手。托管产品可对照 [Lindy](PRODUCTS.md#lindy)所描述的[用户可编辑记忆文件](https://www.lindy.ai/)。这是相近的用户需求，**不是 Lindy 采用 MemGPT 或 Mem0 的证据**。

**先做什么检查。** [T05](TASKS.md#t05)：修改一条合成偏好，真正新建会话，并检查/移除该测试记忆。会话内纠正、跨会话连续性、可删除性分别记录。历史检索也可能解释连续性；此测试不能识别隐藏架构，或证明备份中的信息已被擦除。

<a id="memory-action"></a>
## 2 · 把个人上下文用于正确的行动

**技术阅读。** 在上面的记忆问题之外，加上工具循环：[ReAct](https://arxiv.org/abs/2210.03629)展示如何交替推理、行动并利用观察结果。把这两类机制结合起来是本指南的分析，不是对某个产品实现方式的断言。

**评测问题。** [Mem2ActBench](https://aclanthology.org/2026.acl-long.370/)考察依赖记忆的工具选择与参数；[MemoryArena B13](PAPERS.md#transferable-memory-evaluation)考察跨会话相互依赖的任务。参数正确不代表真实交易完成。Mem2ActBench 主实验提供正确工具，不能改写成不受限的工具选择成绩。

**考察实现。** [Hermes Agent](https://github.com/NousResearch/hermes-agent)记录了记忆、历史检索、工具与消息渠道；[Lindy](PRODUCTS.md#lindy)把个人工作上下文连接到邮件和排期。这些是观察“记忆到行动”边界的候选，**不是已通过上述基准的实现**。

**先做什么检查 / 缺口。** [T02](TASKS.md#t02)在不连接邮箱的条件下检查受约束的合成回复；[T05](TASKS.md#t05)单独检查连续性。**两者都不测试依赖记忆的工具执行，把分数相加也不能替代。** 后者需要另行定义模拟工具任务，保留可见参数、最终状态检查与授权规则。这里尚未执行此类测试。

<a id="across-time"></a>
## 3 · 区分持续工作、定时任务与主动帮助

这里其实有三个不同问题：

1. **持续执行已委托任务：** 已获授权的任务能否继续、汇报进展、停止和恢复，而不重复产生副作用？
2. **定时或事件触发：** 明确设定的规则是否按预期触发，能否取消？
3. **主动帮助：** 智能体此刻是否应该提出帮助，内容是什么，何时出现？

**技术思路 → 评测。** [Proactive Agent / ProactiveBench](https://github.com/thunlp/ProactiveAgent)把基于活动的任务建议与接受/拒绝评测连接起来；[MemoProAgent / MemoProBench](https://arxiv.org/html/2610.22671v2)把个人历史检索、干预门控与内容、时机、重复和保持安静的评测连接起来。这是直接的方法—评测关系，不是可靠调度或可恢复事务的证据。

**考察实现。** [Hermes Agent](https://github.com/NousResearch/hermes-agent)记录了 cron 调度器；[Gemini Tasks](PRODUCTS.md#gemini)记录了[时间/事件调度和暂停/删除控制](https://support.google.com/gemini/answer/17094710)，产品条目另有实验性状态与准入限制。定时简报不能自动等同于这些论文研究的主动需求推断。

**先做什么检查 / 缺口。** [T04](TASKS.md#t04)用正对照检查一次性执行与取消，**只适用于输出到本地/模拟接收器的隔离调度器**。服务无法提供该环境时，应记录 blocked/unsupported，而不是改用真实收件人。它不测打扰是否合适，也不测断连恢复；持续任务恢复需要自己的协议。

<a id="execution"></a>
## 4 · 验证浏览器与桌面的实际结果

**技术阅读。** ReAct 的行动—观察循环是起点；[Reflexion M9](PAPERS.md#agent-methods)加入跨尝试的反馈。两者都不意味着多重试必然更好，也不意味着重复一次写操作是安全的。

**评测问题。** [WebArena](https://github.com/web-arena-x/webarena)关注可复现的网页任务；[OSWorld](https://os-world.github.io/)关注桌面/跨应用结果；[AppWorld B16](PAPERS.md#execution-evaluation)则使用模拟应用 API。按真实执行接口选择环境，不要把原版 OSWorld、Verified 与 2.0 的结果混在一起。

**考察实现。** [Browser Use](https://github.com/browser-use/browser-use)区分 Python 库、CLI 与托管智能体/浏览器路径。[Claude Cowork](PRODUCTS.md#claude-cowork)与 [Manus](PRODUCTS.md#manus)是文件与任务产出的产品入口；Manus 文档描述了[沙箱计算机](https://manus.im/docs/introduction/welcome)。执行形态相近，不证明采用相同智能体架构或取得相同基准结果。

**先做什么检查。** [T01](TASKS.md#t01)核查公开资料的逐项引用；[T03](TASKS.md#t03)核查可丢弃副本上的文件操作。检查实际产物、原件未变、成本与人工介入。这些卡不测试登录恢复或真实跨应用交易。

<a id="mobile"></a>
## 5 · 手机 GUI 控制不等于手机访问入口

**技术思路。** 手机执行需要感知/行动接口，例如截图或 UI 树、点击与输入，还需要设备权限和人工接管。这与在手机上向智能体发消息不同。

**评测问题。** [AndroidWorld](https://github.com/google-research/android_world)提供参数化模拟器任务与状态检查；[KnowU-Bench](https://github.com/ZJU-REAL/KnowU-Bench)进一步研究隐藏偏好、澄清、征求同意以及被拒绝后的克制。模拟用户不是真实用户接受度的证据。

**考察实现。** [Mika](https://github.com/wangzan101/Mika)是提供后台屏幕控制的 Android 应用，目前为公开测试版；[Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM)是含确认与接管回调的模型/框架入口，不是与 Mika 等价的安装包。列在这里不表示本仓库已在 AndroidWorld 或 KnowU-Bench 上评测过它们。

**产品边界 / 缺口。** [产品目录](PRODUCTS.md)含手机入口，但本页不把其中任何一个认定为等价的任意 Android App 控制器。**T01–T06 中没有手机 GUI 任务卡。** 未来设备试验应先规定可丢弃的 App/模拟器状态、所需系统与权限、结果检查、接管与停止行为，不要用真实发消息或购买任务替代。

<a id="boundaries"></a>
## 6 · 把能力、权限与信息外传分开

**设计问题。** 系统可能技术上能读文档、知道隐私、点击“发送”，却未获授权披露该信息或发送消息。应检查工具策略、沙箱范围、收件人边界、审批与撤销，而不只看模型指令。

**评测问题。** [AgentDojo](https://github.com/ethz-spylab/agentdojo)研究工具返回内容中的间接提示注入；[PrivacyLens](https://github.com/SALT-NLP/PrivacyLens)研究涉及隐私的最终动作与帮助程度，不以存在攻击者为前提。两者测量不同风险，都不是完整的授权或安全审计。见 [B21/B22](PAPERS.md#safety-evaluation)。

**考察实现。** [OpenClaw 安全文档](https://docs.openclaw.ai/gateway/security)明确每个 gateway 是一个共同信任边界，不是对抗性多租户隔离；[Claude Cowork 安全文档](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)区分直接电脑操作与普通工具权限检查。这些是待检查的文档边界，不是独立安全认证。

**先做什么检查。** [T02](TASKS.md#t02)检查“仅起草”；[T06](TASKS.md#t06)使用合成恶意文字与仅拦截、不执行的工具。合法任务结果与安全分别报告；即使被拦截，提出禁止操作的请求仍是安全失败；缺少操作日志时，安全结论仍为 inconclusive。不要对真实账号进行注入测试。

<a id="direct-links"></a>
## 一手来源实际支持的直接关联

| 关系 | 证据支持什么 | 没有证明什么 |
| --- | --- | --- |
| MemGPT → Letta → 当前 Letta Code | [Letta 旧入口](https://github.com/letta-ai/letta)说明曾名为 MemGPT，并指向当前 Letta Code；[Letta Code](https://github.com/letta-ai/letta-code)说明开发者的 MemGPT 研究背景。 | 当前代码等于原论文实现，或继承原实验结果。 |
| Mem0 论文 → Mem0 项目；论文 → LoCoMo | [2025 年论文](https://arxiv.org/abs/2504.19413)报告 LoCoMo 实验；[官方项目](https://github.com/mem0ai/mem0)是实现入口。 | 当前算法等于 2025 年配置，或组件就是完整个人智能体。 |
| Proactive Agent → ProactiveBench | [作者仓库](https://github.com/thunlp/ProactiveAgent)连接方法、基准与评测。 | Hermes、Gemini 或其他商业助手采用该方法，或参加了该研究的评测。 |
| MemoProAgent → MemoProBench | [论文](https://arxiv.org/html/2610.22671v2)与[作者仓库](https://github.com/facebookresearch/Memo-Pro-Agent)连接方法与评测。 | 已部署的消费者产品或完整训练复现。核对时 README 说明历史数据需要获授权的私有 Hugging Face 访问；Ego4D 视频另有准入条件。 |

## 如何把这张地图变成选择

1. 先选**一个具体任务和一个不可接受的失败**。“个人智能体”太宽，不能直接拿来测试。
2. 明确选的是**应用、运行时、框架、组件还是托管产品**。组件需要集成；产品需要检查账号、地区和权限。
3. 阅读相关[论文条目](PAPERS.md)、[项目注意事项](../README.md#source-projects)和[产品条目](PRODUCTS.md)，不要只看本页名字；保留其版本、许可、数据流与准入条件。
4. 仅在满足隔离要求时采用匹配的[任务卡](TASKS.md)。不支持或被阻塞就如实记录，不要强行制造可比性。
5. 保存确切版本、输入、观察记录、任务/安全结果、人工介入和成本。**文档声称与未执行任务卡都不能变成测试成绩。**

更新时，先在原目录中补充证据，再修改本页。持续区分直接来源关系与编辑性搭配，不必强行填满每个“研究—项目—产品”格子。
