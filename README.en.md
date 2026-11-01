<div align="center">

# Awesome Personal Agent

</div>

![Awesome Personal Agent banner](assets/banner.png)

<div align="center">

Research, evaluation, and practice for personal agents.

[简体中文](README.md) · **English**

**[31 projects](#source-projects) · [Products](docs/PRODUCTS.en.md) · [Papers](docs/PAPERS.en.md) · [Timeline](docs/PRODUCTS.en.md#release-timeline)**

</div>

<a id="start-here"></a>
## Contents

- [Persistent assistants](#personal-assistants)
- [Mobile agents](#mobile-agents)
- [Desktop knowledge & work](#desktop-assistants)
- [Computer & browser use](#computer-and-browser)
- [Building blocks](#building-blocks)
- [Developer previews](#previews)

<a id="open-source--source-available-projects"></a>
<a id="source-projects"></a>
## Projects

Open-source and source-available projects, grouped by use—not ranked.

Stars are displayed via Shields.io and may be cached; they indicate interest, not quality.

<a id="persistent-personal-assistants"></a>
<a id="personal-assistants"></a>
### Persistent assistants

- [AstrBot](https://github.com/AstrBotDevs/AstrBot) [![AstrBot GitHub stars](https://img.shields.io/github/stars/AstrBotDevs/AstrBot?style=flat&label=Stars)](https://github.com/AstrBotDevs/AstrBot) — Chat interfaces, knowledge bases, and tool integrations.
- [Hermes Agent](https://github.com/NousResearch/hermes-agent) [![Hermes Agent GitHub stars](https://img.shields.io/github/stars/NousResearch/hermes-agent?style=flat&label=Stars)](https://github.com/NousResearch/hermes-agent) — Persistent memory, reusable skills, and scheduled tasks.
- [IronClaw](https://github.com/nearai/ironclaw) [![IronClaw GitHub stars](https://img.shields.io/github/stars/nearai/ironclaw?style=flat&label=Stars)](https://github.com/nearai/ironclaw) — Rust assistant runtime with WASM / MCP extensions.
- [Khoj](https://github.com/khoj-ai/khoj) [![Khoj GitHub stars](https://img.shields.io/github/stars/khoj-ai/khoj?style=flat&label=Stars)](https://github.com/khoj-ai/khoj) — Research assistant for personal documents and the web.
- [Letta Code](https://github.com/letta-ai/letta-code) [![Letta Code GitHub stars](https://img.shields.io/github/stars/letta-ai/letta-code?style=flat&label=Stars)](https://github.com/letta-ai/letta-code) — Persistent identity, editable memory, and tool execution.
- [Moltis](https://github.com/moltis-org/moltis) [![Moltis GitHub stars](https://img.shields.io/github/stars/moltis-org/moltis?style=flat&label=Stars)](https://github.com/moltis-org/moltis) — Assistant server with voice, chat, and scheduled tasks.
- [nanobot](https://github.com/HKUDS/nanobot) [![nanobot GitHub stars](https://img.shields.io/github/stars/HKUDS/nanobot?style=flat&label=Stars)](https://github.com/HKUDS/nanobot) — Lightweight Python agent with memory, tools, and messaging channels.
- [NanoClaw](https://github.com/nanocoai/nanoclaw) [![NanoClaw GitHub stars](https://img.shields.io/github/stars/nanocoai/nanoclaw?style=flat&label=Stars)](https://github.com/nanocoai/nanoclaw) — Customizable messaging assistant with container-based execution.
- [OpenClaw](https://github.com/openclaw/openclaw) [![OpenClaw GitHub stars](https://img.shields.io/github/stars/openclaw/openclaw?style=flat&label=Stars)](https://github.com/openclaw/openclaw) — Local Gateway connecting messaging channels, sessions, and tools.
- [PicoClaw](https://github.com/sipeed/picoclaw) [![PicoClaw GitHub stars](https://img.shields.io/github/stars/sipeed/picoclaw?style=flat&label=Stars)](https://github.com/sipeed/picoclaw) — Lightweight assistant with tools and reminders. **Pre-1.0; not for production.**
- [QwenPaw](https://github.com/agentscope-ai/QwenPaw) [![QwenPaw GitHub stars](https://img.shields.io/github/stars/agentscope-ai/QwenPaw?style=flat&label=Stars)](https://github.com/agentscope-ai/QwenPaw) — Formerly CoPaw; chat, office files, and browser tasks. **Desktop: Beta.**
- [ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw) [![ZeroClaw GitHub stars](https://img.shields.io/github/stars/zeroclaw-labs/zeroclaw?style=flat&label=Stars)](https://github.com/zeroclaw-labs/zeroclaw) — Rust runtime for messaging, webhooks, and hardware events.

[ Setup & caveats → ](docs/GUIDE.en.md#personal-assistants)

<a id="mobile-agents"></a>
### Mobile agents

- [Mika](https://github.com/wangzan101/Mika) [![Mika GitHub stars](https://img.shields.io/github/stars/wangzan101/Mika?style=flat&label=Stars)](https://github.com/wangzan101/Mika) — Android app control, browser, and scheduled tasks. **Early beta.**
- [Mobile-Agent](https://github.com/X-PLUG/MobileAgent) [![Mobile-Agent GitHub stars](https://img.shields.io/github/stars/X-PLUG/MobileAgent?style=flat&label=Stars)](https://github.com/X-PLUG/MobileAgent) — Research framework for mobile and cross-platform GUI agents.
- [Mobilerun](https://github.com/droidrun/mobilerun) [![Mobilerun GitHub stars](https://img.shields.io/github/stars/droidrun/mobilerun?style=flat&label=Stars)](https://github.com/droidrun/mobilerun) — Formerly DroidRun; CLI / Python mobile automation, not a standalone APK.
- [Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM) [![Open-AutoGLM GitHub stars](https://img.shields.io/github/stars/zai-org/Open-AutoGLM?style=flat&label=Stars)](https://github.com/zai-org/Open-AutoGLM) — Screenshot-driven phone research framework; requires a model endpoint.
- [Operit](https://github.com/AAswordman/Operit) [![Operit GitHub stars](https://img.shields.io/github/stars/AAswordman/Operit?style=flat&label=Stars)](https://github.com/AAswordman/Operit) — Android assistant for UI, files, terminal, and workflows. **ARM64 only.**

[ Setup & caveats → ](docs/GUIDE.en.md#mobile-agents)

<a id="desktop-knowledge--work-assistants"></a>
<a id="desktop-assistants"></a>
### Desktop knowledge & work

- [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) [![AnythingLLM GitHub stars](https://img.shields.io/github/stars/Mintplex-Labs/anything-llm?style=flat&label=Stars)](https://github.com/Mintplex-Labs/anything-llm) — Document knowledge bases, web research, and tool-driven file outputs.
- [Eigent](https://github.com/eigent-ai/eigent) [![Eigent GitHub stars](https://img.shields.io/github/stars/eigent-ai/eigent?style=flat&label=Stars)](https://github.com/eigent-ai/eigent) — Single- and multi-agent research, writing, and file organization.
- [LobsterAI](https://github.com/netease-youdao/LobsterAI) [![LobsterAI GitHub stars](https://img.shields.io/github/stars/netease-youdao/LobsterAI?style=flat&label=Stars)](https://github.com/netease-youdao/LobsterAI) — Desktop work assistant using the OpenClaw runtime.
- [OpenWorker](https://github.com/andrewyng/openworker) [![OpenWorker GitHub stars](https://img.shields.io/github/stars/andrewyng/openworker?style=flat&label=Stars)](https://github.com/andrewyng/openworker) — Meeting preparation, reports, and reviewable actions. **Open beta; Windows unsigned.**
- [Rowboat](https://github.com/rowboatlabs/rowboat) [![Rowboat GitHub stars](https://img.shields.io/github/stars/rowboatlabs/rowboat?style=flat&label=Stars)](https://github.com/rowboatlabs/rowboat) — Connects email, meetings, and conversations to a knowledge graph and background work.

[ Setup & caveats → ](docs/GUIDE.en.md#desktop-assistants)

<a id="computer-and-browser"></a>
### Computer & browser use

- [Agent Zero](https://github.com/agent0ai/agent-zero) [![Agent Zero GitHub stars](https://img.shields.io/github/stars/agent0ai/agent-zero?style=flat&label=Stars)](https://github.com/agent0ai/agent-zero) — Dockerized desktop, browser, memory, and multi-step tasks.
- [Browser Use](https://github.com/browser-use/browser-use) [![Browser Use GitHub stars](https://img.shields.io/github/stars/browser-use/browser-use?style=flat&label=Stars)](https://github.com/browser-use/browser-use) — Model-driven browser automation library and CLI.
- [goose](https://github.com/aaif-goose/goose) [![goose GitHub stars](https://img.shields.io/github/stars/aaif-goose/goose?style=flat&label=Stars)](https://github.com/aaif-goose/goose) — Runtime for research, writing, and file tasks through extensions and MCP.
- [UI-TARS Desktop / Agent TARS](https://github.com/bytedance/UI-TARS-desktop) [![UI-TARS Desktop / Agent TARS GitHub stars](https://img.shields.io/github/stars/bytedance/UI-TARS-desktop?style=flat&label=Stars)](https://github.com/bytedance/UI-TARS-desktop) — GUI desktop application and vision / tool agent stack.

[ Setup & caveats → ](docs/GUIDE.en.md#computer-and-browser)

<a id="building-blocks"></a>
### Building blocks

- [LangGraph](https://github.com/langchain-ai/langgraph) [![LangGraph GitHub stars](https://img.shields.io/github/stars/langchain-ai/langgraph?style=flat&label=Stars)](https://github.com/langchain-ai/langgraph) — Stateful agent orchestration, durable execution, and human intervention.
- [Mem0](https://github.com/mem0ai/mem0) [![Mem0 GitHub stars](https://img.shields.io/github/stars/mem0ai/mem0?style=flat&label=Stars)](https://github.com/mem0ai/mem0) — User, session, and agent memory layer—not a complete assistant.

[ Setup & caveats → ](docs/GUIDE.en.md#building-blocks)

<a id="developer-previews--alpha-projects"></a>
<a id="previews"></a>
### Developer previews

- [Leon](https://github.com/leon-ai/leon) [![Leon GitHub stars](https://img.shields.io/github/stars/leon-ai/leon?style=flat&label=Stars)](https://github.com/leon-ai/leon) — **2.0 Developer Preview**: memory, skills, and proactive polling; source setup required.
- [OpenMuse](https://github.com/CopilotKit/openmuse) [![OpenMuse GitHub stars](https://img.shields.io/github/stars/CopilotKit/openmuse?style=flat&label=Stars)](https://github.com/CopilotKit/openmuse) — **Alpha template**: mobile / web tasks and human takeover; payments and bookings remain roadmap items.
- [Operit2](https://github.com/AAswordman/Operit2) [![Operit2 GitHub stars](https://img.shields.io/github/stars/AAswordman/Operit2?style=flat&label=Stars)](https://github.com/AAswordman/Operit2) — **Cross-device preview**: resumes at persisted tool results, not live sessions.

[ Setup & caveats → ](docs/GUIDE.en.md#previews)

<a id="experimental-related"></a>
## Experimental related projects

This coding research prototype is included as an architecture reference, outside the 31 personal-agent source projects above.

- [dsh-superagent](https://github.com/deepseek-ai/dsh-superagent-prototype) [![dsh-superagent GitHub stars](https://img.shields.io/github/stars/deepseek-ai/dsh-superagent-prototype?style=flat&label=Stars)](https://github.com/deepseek-ai/dsh-superagent-prototype) — A DeepSeek-team proactive coding agent for one GitHub repository, built on DeepSeek Harness with optional Feishu integration. **Research prototype, not an official product; not tested here.** [Evidence](docs/SOURCES.en.md#deepseek-superagent)

<a id="publicly-available-products"></a>
<a id="products"></a>
## Products

- [ Publicly available products, including commercial services → ](docs/PRODUCTS.en.md) — Access, pricing, and region / account restrictions.

<a id="papers"></a>
## Papers

- [ Paper directory → ](docs/PAPERS.en.md) — Eval / Benchmark · Agent Methods / Systems.

<a id="scope"></a>
<a id="evaluation-guide"></a>
<a id="comparison"></a>
<a id="safety-checklist"></a>
<a id="safety"></a>
## Before you start

For tool-using AI systems working toward personal goals; frameworks and previews are not ready-made assistants.

Use test data and minimal permissions; require approval for sensitive actions. Local deployment or containers do not guarantee safety or offline inference.

[Scope](docs/GUIDE.en.md#scope) · [Evaluation guide](docs/GUIDE.en.md#comparison) · [Safety checklist](docs/GUIDE.en.md#safety) · [Task guide](docs/LANDSCAPE.en.md) · [Trial protocols](docs/TASKS.en.md)

Documentation review: **2026-10-31**. Not hands-on tests, reproductions, or security audits; trial protocols remain unexecuted. [Evidence & dates](docs/SOURCES.en.md) (products and papers have separate review dates).

<a id="related-lists"></a>
## Related lists

- [ahmadyan/awesome-personal-agents](https://github.com/ahmadyan/awesome-personal-agents)
- [upgundecha/awesome-personal-agents](https://github.com/upgundecha/awesome-personal-agents)
- [cubxxw/awesome-personal-agent-practices](https://github.com/cubxxw/awesome-personal-agent-practices)

<a id="contributing--licensing"></a>
<a id="contributing"></a>
## Contributing & license

[Contributing](CONTRIBUTING.en.md) · [Source notes](docs/SOURCES.en.md)

Original prose and curation: **CC BY 4.0**. Designated original scripts/tests: **MIT**. Third-party terms remain separate; see [license scope](docs/LICENSE.md#en).
