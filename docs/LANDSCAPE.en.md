# From a personal task to research, projects, and products

[中文](LANDSCAPE.md) · [Main list](../README.en.md) · [Papers](PAPERS.en.md) · [Products](PRODUCTS.en.md) · [Task protocols](TASKS.en.md)

**Start with the failure you need to avoid—not the longest feature list.** This map connects a practical question to a technical approach, a relevant evaluation, and implementations to inspect. It is a reading and selection aid, not a leaderboard or a claim that a product implements a paper.

**Reviewed: 2026-10-31 (UTC).** Evidence is the repository's dated directories plus the primary sources linked below. No products were installed, accounts connected, or benchmarks run. All six local task protocols remain **not run**. Examples are selective; omission means neither absence of a capability nor failure.

## Choose a route

| What you want | The distinction that matters | Route |
| --- | --- | --- |
| “Remember my corrected preference next time.” | Recall vs updating vs actually following a preference | [1 · Memory](#memory) |
| “Use what you know about me to prepare the right action.” | A remembered fact vs correct tool arguments vs an authorized result | [2 · Memory into action](#memory-action) |
| “Keep working, remind me, or help at the right moment.” | Ongoing delegated work vs scheduled triggers vs unsolicited intervention | [3 · Work across time](#across-time) |
| “Research this and produce or organize files.” | A plausible answer vs verified browser/file state | [4 · Browser and desktop](#execution) |
| “Operate apps on my phone.” | A mobile chat interface vs actual mobile GUI control | [5 · Mobile](#mobile) |
| “Ask before sending, and don't follow instructions hidden in documents.” | Tool access vs action authorization vs appropriate disclosure | [6 · Boundaries](#boundaries) |

**How to read relationships**

- **Direct:** an author or maintainer explicitly connects the paper, code, or benchmark. The [provenance table](#direct-links) records the narrow claim supported.
- **Thematic:** this guide pairs a mechanism, evaluation question, and example. It does **not** establish adoption, architectural equivalence, benchmark participation, or comparable performance. **All project/product-to-benchmark pairings in the six routes are thematic unless the provenance table says otherwise.**
- A proposed local check is not the cited research benchmark. A passing small check would not validate the full research claim.

<a id="memory"></a>
## 1 · Remember corrections, not just old facts

**Technical reading.** [MemGPT](https://arxiv.org/abs/2310.08560) studies movement between context and external memory; the [2025 Mem0 paper](https://arxiv.org/abs/2504.19413) studies extracting, consolidating, and retrieving conversational information. These are different mechanisms, not synonyms for “has memory.” See [memory methods M2/M4](PAPERS.en.md#memory-methods).

**Evaluation question.** [LongMemEval](https://github.com/xiaowu0162/LongMemEval) separates updates, temporal reasoning, recall, and abstention. [PrefEval B8](PAPERS.en.md#personal-evaluation) asks whether responses actually follow preferences. Correct recall does not establish correct preference use, deletion, or user isolation.

**Inspect implementations.** [Letta Code](https://github.com/letta-ai/letta-code) documents editable memory and history search; [Mem0](https://github.com/mem0ai/mem0) is a memory component rather than a complete assistant. For a hosted-product comparison, [Lindy](PRODUCTS.en.md#lindy) describes [user-editable memory files](https://www.lindy.ai/). This is a comparable user need, **not evidence that Lindy uses MemGPT or Mem0**.

**First check.** [T05](TASKS.en.md#t05): correct a synthetic preference, open a genuinely new session, and inspect/remove only that test memory. Record in-session correction, cross-session continuity, and removability separately. History retrieval can explain continuity; this test cannot identify the hidden architecture or prove erasure from backups.

<a id="memory-action"></a>
## 2 · Turn personal context into the right action

**Technical reading.** Combine the memory question above with a tool loop: [ReAct](https://arxiv.org/abs/2210.03629) illustrates alternating reasoning and actions using observations. That conceptual combination is this guide's synthesis, not a claim about any named product's implementation.

**Evaluation question.** [Mem2ActBench](https://aclanthology.org/2026.acl-long.370/) examines memory-dependent tool selection and arguments; [MemoryArena B13](PAPERS.en.md#transferable-memory-evaluation) examines dependent tasks across sessions. Correct call arguments are not proof that a real transaction completed. Main Mem2ActBench experiments supply the correct tool; do not reinterpret them as unrestricted tool selection.

**Inspect implementations.** [Hermes Agent](https://github.com/NousResearch/hermes-agent) documents memory, history search, tools, and messaging; [Lindy](PRODUCTS.en.md#lindy) connects personal-work context to email and scheduling. These are candidates for examining the memory-to-action boundary, **not verified passes on either benchmark**.

**First check / gap.** [T02](TASKS.en.md#t02) checks a constrained synthetic reply without connecting a mailbox; [T05](TASKS.en.md#t05) checks continuity separately. **Neither, nor combining their scores, tests memory-dependent tool execution.** That needs a separately specified mock-tool task with visible arguments, final-state checks, and approval rules. No such test has been run here.

<a id="across-time"></a>
## 3 · Distinguish ongoing work, schedules, and proactive help

There are three different questions:

1. **Ongoing delegated work:** can an already authorized task continue, report progress, stop, and resume without duplicate effects?
2. **Scheduled or event-triggered work:** does an explicit rule fire when intended, and can it be canceled?
3. **Proactive help:** should the agent offer assistance at all, with what content, and at what time?

**Technical reading → evaluation.** [Proactive Agent / ProactiveBench](https://github.com/thunlp/ProactiveAgent) links activity-conditioned task proposals to acceptance/rejection evaluation. [MemoProAgent / MemoProBench](https://arxiv.org/html/2610.22671v2) links personal-history retrieval and an intervention gate to content, timing, repetition, and silence. These are direct method–evaluation relationships, not evidence for reliable scheduling or resumable transactions.

**Inspect implementations.** [Hermes Agent](https://github.com/NousResearch/hermes-agent) documents a cron scheduler. [Gemini Tasks](PRODUCTS.en.md#gemini) documents [time/event schedules and pause/delete controls](https://support.google.com/gemini/answer/17094710); the product entry records its experimental status and access restrictions. A scheduled briefing is not automatically the kind of proactive inference studied in these papers.

**First check / gap.** [T04](TASKS.en.md#t04) covers one-shot execution and cancellation with a positive control, **only in an isolated scheduler with local/mock output**. If the service cannot provide that environment, record blocked/unsupported rather than substituting a real recipient. It does not measure interruption quality or recovery after disconnection. Ongoing-task recovery needs its own protocol.

<a id="execution"></a>
## 4 · Verify browser and desktop outcomes

**Technical reading.** ReAct's action–observation loop is a useful starting point; [Reflexion M9](PAPERS.en.md#agent-methods) adds feedback across attempts. Neither implies that additional retries always improve a task or that retrying a write is safe.

**Evaluation question.** [WebArena](https://github.com/web-arena-x/webarena) concerns reproducible web tasks; [OSWorld](https://os-world.github.io/) concerns desktop/cross-app outcomes. [AppWorld B16](PAPERS.en.md#execution-evaluation) instead uses simulated app APIs. Choose the environment that matches the execution interface. Keep original OSWorld, Verified, and 2.0 results separate.

**Inspect implementations.** [Browser Use](https://github.com/browser-use/browser-use) distinguishes its Python library, CLI, and hosted agent/browser paths. [Claude Cowork](PRODUCTS.en.md#claude-cowork) and [Manus](PRODUCTS.en.md#manus) are product entry points for files and task deliverables; Manus documents a [sandbox computer](https://manus.im/docs/introduction/welcome). Sharing an execution pattern does not establish a common agent architecture or benchmark result.

**First check.** [T01](TASKS.en.md#t01) verifies claim-level public citations; [T03](TASKS.en.md#t03) verifies file operations on disposable copies. Check actual outputs, unchanged originals, costs, and human interventions. These cards do not test login recovery or real cross-app transactions.

<a id="mobile"></a>
## 5 · Separate mobile GUI control from mobile access

**Technical approach.** Mobile execution needs a perception/action interface—such as screenshots or UI trees, taps, and typing—plus device permissions and takeover. This is distinct from messaging an agent from a phone.

**Evaluation question.** [AndroidWorld](https://github.com/google-research/android_world) supplies parameterized emulator tasks and state checks. [KnowU-Bench](https://github.com/ZJU-REAL/KnowU-Bench) additionally studies hidden preferences, clarification, consent, and restraint after rejection. Its simulated user is not evidence of real-user acceptance.

**Inspect implementations.** [Mika](https://github.com/wangzan101/Mika) is an Android application with background-screen control, currently public beta. [Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM) is a model/framework entry point with confirmation and takeover callbacks—not a packaged equivalent of Mika. Neither listing means this repository evaluated it on AndroidWorld or KnowU-Bench.

**Product boundary / gap.** The [product directory](PRODUCTS.en.md) includes mobile interfaces, but this map does not establish any as an equivalent arbitrary-Android-app controller. **No mobile-GUI task card exists among T01–T06.** Before a future device trial, specify a disposable app/emulator state, required OS/permissions, outcome checks, and takeover/stop behavior. Do not substitute a real messaging or purchase task.

<a id="boundaries"></a>
## 6 · Keep capability, permission, and disclosure separate

**Design question.** A system may technically read a document, know a private fact, or click Send without being authorized to disclose that fact or send that message. Examine tool policy, sandbox scope, recipient boundaries, approvals, and revocation—not just model instructions.

**Evaluation question.** [AgentDojo](https://github.com/ethz-spylab/agentdojo) studies indirect prompt injection through tool results. [PrivacyLens](https://github.com/SALT-NLP/PrivacyLens) examines privacy-sensitive final actions and helpfulness, even without an attacker. They measure different risks; neither is a complete authorization or security audit. See [B21/B22](PAPERS.en.md#safety-evaluation).

**Inspect implementations.** [OpenClaw's security guidance](https://docs.openclaw.ai/gateway/security) states one trusted boundary per gateway, not hostile multi-tenant isolation. [Claude Cowork's safety guidance](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely) distinguishes computer-use risks from ordinary tool permission checks. These are documented boundaries to examine, not independent safety certifications.

**First check.** [T02](TASKS.en.md#t02) checks draft-only behavior; [T06](TASKS.en.md#t06) uses synthetic malicious text and intercept-only tools. Report legitimate-task outcome and safety separately. A prohibited request is a safety failure even if intercepted; absent action logs, safety remains inconclusive. Do not run injection tests against real accounts.

<a id="direct-links"></a>
## Direct links that the sources actually support

| Relationship | Supported claim | Not established |
| --- | --- | --- |
| MemGPT → Letta → current Letta Code | [Letta's legacy entry point](https://github.com/letta-ai/letta) identifies the former MemGPT name and redirects current development to Letta Code; [Letta Code](https://github.com/letta-ai/letta-code) identifies its creators' MemGPT research. | Current code equals the original paper implementation, or inherits its experimental results. |
| Mem0 paper → Mem0 project; paper → LoCoMo | The [2025 paper](https://arxiv.org/abs/2504.19413) reports LoCoMo experiments; the [official project](https://github.com/mem0ai/mem0) is an implementation entry point. | Current algorithm equals the 2025 configuration, or the component is a complete personal agent. |
| Proactive Agent → ProactiveBench | The [author repository](https://github.com/thunlp/ProactiveAgent) connects the method, benchmark, and evaluation. | Hermes, Gemini, or other commercial assistants use this method or were evaluated in that work. |
| MemoProAgent → MemoProBench | The [paper](https://arxiv.org/html/2610.22671v2) and [author repository](https://github.com/facebookresearch/Memo-Pro-Agent) connect the method and evaluation. | A deployed consumer product or full training reproduction. The checked README says history data requires authorized private Hugging Face access; Ego4D videos have separate access terms. |

## Turn the map into a decision

1. Pick **one concrete task and one unacceptable failure**. “Personal agent” is too broad to test.
2. Select an **application, runtime, framework, component, or hosted product** deliberately. A component needs integration; a product needs account/region/permission checks.
3. Read the relevant [paper entry](PAPERS.en.md), [project caveat](../README.en.md#source-projects), and [product entry](PRODUCTS.en.md), not just names in this map. Follow their version, license, data-flow, and access notes.
4. Use a matching [task protocol](TASKS.en.md) only when its isolation requirements are met. Record unsupported/blocked capabilities instead of manufacturing comparability.
5. Preserve exact versions, inputs, observations, task/safety outcomes, interventions, and costs. **Do not turn documentation claims or an unrun card into a result.**

For updates, add evidence to the existing directories first, then change this map. Keep direct provenance distinct from editorial pairings; there is no requirement to fill every research–project–product cell.
