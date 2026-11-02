# Research surveys for personal agents

[简体中文](SURVEYS.md) · [Main list](../README.en.md) · [Papers and benchmarks](PAPERS.en.md) · [Task landscape](LANDSCAPE.en.md)

**Build a field map before comparing methods or scores.** These seven complementary surveys are separate from the methods and evaluation catalog; they are not additional benchmarks or agent systems.

**Original-source check: 2026-11-01 (UTC).** Versions and reading scopes below describe the original sections actually inspected, not complete cover-to-cover reading, reproduction, or independent verification of every cited result. This is an editorial selection, not an exhaustive review or latest-paper leaderboard. Years do not denote product versions or peer-review status. Translation adds no verification.

## Where to start

### S1 · Personalization across the agent

[Toward Personalized LLM-Powered Agents: Foundations, Evaluation, and Future Directions](https://arxiv.org/html/2602.22680v2) — 2026; v2, 2026-03-16.

- **Reading scope:** relevant planning, execution and evaluation passages in [v1](https://arxiv.org/html/2602.22680v1); evaluation (§7) and open problems (§9) in v2.
- **Useful for:** profile modeling, memory, planning and action execution; evaluation across effectiveness, adaptivity, generalization, robustness and risk. Start here rather than treating memory as the whole personal agent.

### S2 · From personalized retrieval to agents

[A Survey of Personalization: From RAG to Agent](https://arxiv.org/html/2504.10147v1) — 2025; v1, 2025-04-14.

- **Reading scope:** contents and relevant generation (§4.3), agent methods and discussion (§4.4) passages.
- **Useful for:** personalization before retrieval, during retrieval and in generation, and its connection to user understanding and tool execution. Role-playing and recommendation are also covered; their evidence does not substitute for real personal-assistant studies.

### S3 · Where personalization is implemented

[A Survey of Personalized Large Language Models: Progress and Future Directions](https://arxiv.org/html/2502.11528v2) — 2025; v2, 2025-09-20.

- **Reading scope:** methods table of contents, §§3.4–4.2 and §7.
- **Useful for:** prompting, parameter adaptation and preference alignment; shared versus per-user adapters; performance, privacy and deployment trade-offs. Personalized models do not automatically execute reliably, and per-user adapters alone do not establish formal privacy guarantees.

### S4 · Memory is more than a vector store

[Memory in the Age of AI Agents: A Survey—Forms, Functions and Dynamics](https://arxiv.org/html/2512.13564v1) — 2025; v1, 2025-12-15.

- **Reading scope:** full table of contents and consolidation/update passages in §5.2.
- **Useful for:** distinguishing memory substrates, functions and lifecycle operations; consolidation and factual correction are different operations. This broader agent-memory survey should not be relabeled entirely as personalization research.

### S5 · The lifecycle of personal memory graphs

[Graph-Based Personalized Memory for LLM Agents: Representation, Evolution, Retrieval, and Evaluation](https://arxiv.org/html/2609.08599v1) — 2026; v1, 2026-09-08.

- **Reading scope:** contents, evaluation (§VI) and challenges (§VII).
- **Useful for:** representation, evolution, retrieval and evaluation; correct answers do not establish correct memory organization. Newly encountered benchmarks still require checking their original papers, not merely their inclusion here.

### S6 · Privacy throughout execution

[Agents That Know Too Much: A Data-Centric Survey of Privacy in LLM Agents](https://arxiv.org/html/2606.26627v1) — 2026; v1, 2026-06-25; labeled a working draft by its authors.

- **Reading scope:** governance (§5), evaluation (§6) and personal-assistant passages in §7.
- **Useful for:** exposure through queries, tool arguments, memory and inter-agent messages. The authors identify an end-to-end, cross-surface evaluation gap under one policy; this is their assessment, not proof by this list that no such research exists anywhere.

### S7 · Personal devices, architecture, efficiency and security

[Personal LLM Agents: Insights and Survey about the Capability, Efficiency and Security](https://arxiv.org/html/2401.05459v2) — 2024; v2, 2024-05-08.

- **Reading scope / date:** 2026-11-02; abstract, relevant architecture and expert-discussion passages, conclusion.
- **Useful for:** Understanding agent architecture, capability, efficiency and security through personal data and devices; adds a foundational systems perspective. Literature synthesis and expert views are not end-user deployment studies or reliability benchmarks.

## A compact field map

This table synthesizes the surveys and the existing catalog. It is not a reproduced figure, and the linked benchmarks do not fully test each capability.

| Layer | Question | Read next |
| --- | --- | --- |
| Profile modeling | How are traits, temporary constraints and durable preferences distinguished? | S1, S3; [PersonaMem](PAPERS.en.md#benchmark-personamem-v1), [PrefEval](PAPERS.en.md#benchmark-prefeval) |
| Memory | When should information be stored, updated, retrieved or deleted? Is provenance and time preserved? | S4, S5; [memory methods](PAPERS.en.md#memory-methods) |
| Planning | How do preferences become constraints? When should the agent clarify or stay quiet? | S1, S2; [personal-context and proactivity evaluation](PAPERS.en.md#personal-evaluation) |
| Action | Are tools, arguments, outcomes and failure recovery correct? | S1; [Mem2ActBench](PAPERS.en.md#benchmark-mem2actbench), [execution evaluation](PAPERS.en.md#execution-evaluation) |
| Cross-cutting: evaluation | What improves over a non-personalized baseline? How are drift, cost and human utility measured? | S1, S5; [comparison and reproduction](PAPERS.en.md#reproducibility) |
| Cross-cutting: permissions | Does technical capability imply authorization? Where are approval, revocation and trust boundaries? | S6; [capability, permission and disclosure](LANDSCAPE.en.md#boundaries) |
| Cross-cutting: privacy | May information flow to this tool or recipient? Does deletion propagate? | S6; [privacy and security evaluation](PAPERS.en.md#safety-evaluation) |
| Cross-cutting: perception | Are screenshots, UI trees, speech or activity signals sufficient, reliable and authorized? | S5's multimodal directions; [mobile](LANDSCAPE.en.md#mobile) and [desktop](LANDSCAPE.en.md#execution) tasks |

**Limits.** This selection does not provide a dedicated comprehensive survey of perception or permission engineering. Those remain explicit reading and design questions, not completed evidence coverage. Profile modeling, memory, planning and action are not a strictly one-way pipeline: observations and user feedback update earlier decisions.

## How to use this page

Locate the question with S1, then choose a memory, implementation or privacy survey. Return to [PAPERS](PAPERS.en.md) for task definitions, versions and evaluation limits, and to [LANDSCAPE](LANDSCAPE.en.md) for practical needs. Thematic connections do not establish product adoption or performance.

Check original papers before adding entries; record real/synthetic users, static/longitudinal settings, visible information and judging methods. This page provides original short descriptions and links, not copied figures, long passages or test sets. Cite the original research when using its findings.
