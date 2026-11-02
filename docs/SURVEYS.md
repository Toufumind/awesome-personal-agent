# 个人 Agent 研究综述入口

[English](SURVEYS.en.md) · [主清单](../README.md) · [论文与评测](PAPERS.md) · [任务导读](LANDSCAPE.md)

**先建立领域地图，再读单篇方法和分数。** 本页精选七篇互补综述，单列于方法与评测目录之外；不把综述计作新增 benchmark 或系统。

**原文核验：2026-11-01（UTC）。** 下列版本及阅读范围对应实际查阅的原文相关章节，不表示逐篇通读、复现或独立验证了综述引用的每项结果。这是编辑性整理，不是穷尽式综述或最新文献榜；年份不是产品版本，也不表示同行评审状态。译文不构成额外核验。

## 先读哪一篇

### S1 · 个人化贯穿整个 Agent

[Toward Personalized LLM-Powered Agents: Foundations, Evaluation, and Future Directions](https://arxiv.org/html/2602.22680v2) — 2026，v2，2026-03-16。

- **阅读范围：** [v1](https://arxiv.org/html/2602.22680v1) 规划、执行与评测相关段落；v2 §7 评测与 §9 开放问题。
- **帮助理解：** 画像、记忆、规划、执行四种能力，以及有效性、适应性、泛化、稳健性和风险的评测维度。适合作为总入口，而非用记忆代表整个个人 Agent。

### S2 · 从个性化检索到 Agent

[A Survey of Personalization: From RAG to Agent](https://arxiv.org/html/2504.10147v1) — 2025，v1，2025-04-14。

- **阅读范围：** 目录、§4.3 生成、§4.4 Agent 方法与讨论相关段落。
- **帮助理解：** 检索前、检索与生成的个人化，以及用户理解和工具执行之间的连接。它也覆盖角色扮演与推荐；这些证据不能直接替代真实个人助理实验。

### S3 · 个性化发生在哪一层

[A Survey of Personalized Large Language Models: Progress and Future Directions](https://arxiv.org/html/2502.11528v2) — 2025，v2，2025-09-20。

- **阅读范围：** 方法目录、§3.4–4.2、§7。
- **帮助理解：** 提示、参数适配与偏好对齐三类技术路线；共享和每用户适配器的差别，以及效果、隐私和部署成本的权衡。模型个人化不自动带来可靠执行；每用户适配器也不自动提供形式隐私保证。

### S4 · 记忆不只是一个向量库

[Memory in the Age of AI Agents: A Survey—Forms, Functions and Dynamics](https://arxiv.org/html/2512.13564v1) — 2025，v1，2025-12-15。

- **阅读范围：** 完整目录及 §5.2 记忆整合、更新相关段落。
- **帮助理解：** 按载体、用途与生命周期区分记忆；抽象整合与事实修正是不同操作。此篇覆盖通用 Agent，不能将全部研究都标作个人化方法。

### S5 · 个人记忆图的生命周期

[Graph-Based Personalized Memory for LLM Agents: Representation, Evolution, Retrieval, and Evaluation](https://arxiv.org/html/2609.08599v1) — 2026，v1，2026-09-08。

- **阅读范围：** 目录、§VI 评测与 §VII 挑战。
- **帮助理解：** 表示、演化、检索、评测的分工；回答正确不等于记忆结构正确。新增评测名称仍须回查原论文，不能因被综述收录就视为已核验。

### S6 · 隐私是整个执行过程的属性

[Agents That Know Too Much: A Data-Centric Survey of Privacy in LLM Agents](https://arxiv.org/html/2606.26627v1) — 2026，v1，2026-06-25；作者标注 working draft。

- **阅读范围：** §5 治理、§6 评测及 §7 个人助理应用相关段落。
- **帮助理解：** 查询、工具参数、记忆和代理间通信都是潜在泄漏通道。作者指出跨数据表面、同一政策下的端到端评测缺口；这是该综述的判断，不是本清单证明全领域不存在对应工作。

### S7 · 个人设备、架构、效率与安全

[Personal LLM Agents: Insights and Survey about the Capability, Efficiency and Security](https://arxiv.org/html/2401.05459v2) — 2024；v2，2024-05-08。

- **阅读范围 / 日期**：2026-11-02；摘要、架构与专家讨论相关段落、结论。
- **适合解决**：从个人数据与设备出发理解 Agent 架构、能力、效率和安全；补充基础系统视角。文献综述与专家观点不是终端用户部署实验，也不是可靠性基准。

## 紧凑领域地图

下表是本清单对综述与现有目录的综合整理，不是某篇论文的原图，也不表示所列基准完整覆盖该能力。

| 层面 | 要问的问题 | 继续阅读 |
| --- | --- | --- |
| 画像 | 用户特征、临时约束与稳定偏好如何区分？ | S1、S3；[PersonaMem](PAPERS.md#benchmark-personamem-v1)、[PrefEval](PAPERS.md#benchmark-prefeval) |
| 记忆 | 何时写入、更新、检索与删除？证据和时间是否保留？ | S4、S5；[记忆方法](PAPERS.md#memory-methods) |
| 规划 | 如何把偏好变成约束，何时澄清，何时保持安静？ | S1、S2；[主动帮助与交互评测](PAPERS.md#personal-evaluation) |
| 行动 | 工具、参数、实际结果与失败恢复是否正确？ | S1；[Mem2ActBench](PAPERS.md#benchmark-mem2actbench)、[执行评测](PAPERS.md#execution-evaluation) |
| 横切：评测 | 相比不使用个人信息有何收益？如何衡量漂移、成本与真人效用？ | S1、S5；[比较与复现](PAPERS.md#reproducibility) |
| 横切：权限 | 能执行是否等于获准执行？审批、撤销与信任边界在哪里？ | S6；[能力、权限与外传](LANDSCAPE.md#boundaries) |
| 横切：隐私 | 信息能否流向这个工具或收件人？删除是否传播？ | S6；[隐私与安全评测](PAPERS.md#safety-evaluation) |
| 横切：感知 | 截图、UI 树、语音或活动信号是否充分、可靠且获授权？ | S5 的多模态方向；[手机任务](LANDSCAPE.md#mobile)、[桌面任务](LANDSCAPE.md#execution) |

**边界。** 本页没有专门覆盖感知或权限工程的完整综述；两项被保留为阅读与系统设计问题，不冒充已经补齐的研究证据。画像、记忆、规划和行动也不是严格单向流水线，观察与用户反馈会反向更新它们。

## 怎样使用

先用 S1 定位问题，再选择记忆、实现技术或隐私综述；回到 [PAPERS](PAPERS.md) 查看具体任务、版本和评测限制，再用 [LANDSCAPE](LANDSCAPE.md) 连接实际需求。主题关联不证明产品采用关系或性能。

新增论文前回查一手原文；记录真实/合成用户、静态/纵向设置、可见信息与评审方式。这里只提供原创短述与链接，不复制论文图表、长段正文或题库；引用研究时应引用原论文。
