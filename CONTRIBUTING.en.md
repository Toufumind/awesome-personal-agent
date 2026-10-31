# Contributing

[简体中文](CONTRIBUTING.md) | English

Thank you for making this list more useful. The goal is not to collect the most names, but to distinguish **products people can use, source projects people can install or build on, and papers that measure or construct agents**.

## Where contributions belong

| Content | Location | Primary evidence |
| --- | --- | --- |
| Source projects: applications, runtimes, frameworks, and components | Relevant [README](README.en.md) category; evidence in [SOURCES](docs/SOURCES.en.md) | Official repository and version-specific usage/deployment documentation |
| Publicly available products, including commercial services | [PRODUCTS](docs/PRODUCTS.en.md) | Official access point, help center, availability, and pricing documentation |
| Eval / Benchmark papers | Evaluation/benchmark group in [PAPERS](docs/PAPERS.en.md) | Original paper, publication page or preprint; official code and task specifications if available |
| Agent Methods / Systems papers | Methods/systems group in [PAPERS](docs/PAPERS.en.md) | Original paper, publication page or preprint; official implementation if available |

A brand may have both a source project and a commercial service; a system may have both a paper and code. Cross-links are welcome, but do not count them as independently verified results.

## Bilingual content and document format

This repository uses consistent **Markdown documents** in Chinese and English. It does not require a separate website or frontend.

| 简体中文 | English |
| --- | --- |
| [README.md](README.md) | [README.en.md](README.en.md) |
| [CONTRIBUTING.md](CONTRIBUTING.md) | [CONTRIBUTING.en.md](CONTRIBUTING.en.md) |
| [docs/PRODUCTS.md](docs/PRODUCTS.md) | [docs/PRODUCTS.en.md](docs/PRODUCTS.en.md) |
| [docs/PAPERS.md](docs/PAPERS.md) | [docs/PAPERS.en.md](docs/PAPERS.en.md) |
| [docs/SOURCES.md](docs/SOURCES.md) | [docs/SOURCES.en.md](docs/SOURCES.en.md) |

- Link each document to its counterpart at the top. Keep categories, entry order, table fields, and evidence conventions aligned.
- Update both languages for the same change. Names, canonical links, versions, review dates, availability, and limitations must not contradict each other.
- Natural translation is welcome; word-for-word matching is unnecessary. Do not imply extra capabilities, broader access, or testing conclusions in only one language.
- Cite the same underlying evidence. Translation is not a new review and must not refresh the review date.

## Before submitting

1. Search existing entries to avoid duplicates. Update an existing entry when its project is renamed or moved.
2. Provide the appropriate primary source: an official repository/document, product access point, or original paper. Aggregators, promotional pages, and third-party downloads are not substitutes.
3. Source projects need usage or research documentation. Commercial products need not be open source, and papers need not publish an implementation. Label demos, waitlists, and roadmaps rather than presenting them as open access or delivered capabilities.
4. Explain the connection to personal tasks. Chat-only, coding-only, and generic enterprise-automation projects generally do not belong in the main list.
5. There is no star threshold, and stars do not establish reliability. Disclose your relationship to the project. Paid placement and affiliate links are not accepted.

## Source-project entries

- **Name and canonical link**: use the currently maintained official repository; check redirects and migrations.
- **Category**: application, runtime, framework, component, or research; choose the README group that best matches actual use.
- **One-sentence purpose**: describe concrete tasks without unsupported “best,” “fully autonomous,” or “completely secure” claims.
- **Key prerequisite or limitation**: device/platform, external models, hosted services, preview status, permissions, or deployment dependencies.
- **Evidence and date**: add the official source, what was read, review date, and review scope to `docs/SOURCES.en.md` and its Chinese counterpart.

Entry format:

```text
| [Project name](official repository URL) | Type. Describe its purpose in your own words. | One important prerequisite or limitation. |
```

Sort names alphabetically within each group rather than implying a ranking. Keep both languages clear and use consistent product names and key terms.

## Product entries

- **Name, official access point, and purpose**: explain how it helps an individual complete tasks, rather than listing only a company or model.
- **Access and availability**: public signup/download/subscription, restricted preview, invitation, waitlist, or announcement. Note region, operating-system, account, and plan requirements. Mark uncertain details as unconfirmed.
- **Charging and deployment**: free, free allowance, subscription, usage-based billing, additional resource charges, and vendor-hosted/local options. Open source versus free, and paid versus closed source, are separate dimensions.
- **Evidence and date**: link official help, availability, and pricing pages. Support capabilities, availability, and pricing separately and record the reading date; avoid undated fixed prices.
- **Testing status**: label documentation-only review. A login button does not establish that your account has access, and a demo video is not a task test.

The main product list should cover publicly available services. If an invite-only, waitlisted, or announced-only product is worth retaining, separate or clearly label it; do not count it as publicly available. Do not register accounts, start trials, purchase services, or accept terms without authorization merely to verify an entry.

## Paper entries

- **Identity**: exact title, year, publication or preprint status, and original link. Do not list different versions of the same work as separate papers.
- **Category**: Eval / Benchmark or Agent Methods / Systems. For work spanning both, choose its main contribution and explain the overlap; do not confuse a measurement tool with the system being measured.
- **Contribution and relevance**: explain the research and its connection to personal agents in your own words. Do not add general language-model papers indiscriminately.
- **Eval / Benchmark**: describe tasks, environments, metrics, and known limitations. Preserve comparison conditions such as model, version, tool permissions, and budget.
- **Methods / Systems**: describe mechanisms, experiments or use cases, and availability of code, data, and models. Missing code is not an automatic exclusion; available code is not proof of successful reproduction.
- **Reading scope and evidence**: state whether you read the abstract, specified sections, or the full paper, with a review date. An abstract-only review cannot establish implementation, ablation, or limitations-section details.
- **Result attribution**: identify original numbers as author-reported. Call something this repository's reproduction or hands-on test only when accompanied by environment, version, task, and outcome records. Do not treat paper results as commercial-product performance.

Treat paper citations, code licenses, and data terms separately. Linking a paper does not grant permission to reproduce its figures or full text, or distribute restricted data.

## How to verify

- Open the appropriate official documentation or original paper, not just search snippets.
- Distinguish stable releases, main-branch features, previews, cloud services, and future plans.
- Do not infer security from Docker support or the absence of external data transfers from local execution.
- Do not copy another list's descriptions. Summarize in your own words and retain direct sources.
- If adding license information, check the official license for the specific version. Public source visibility does not automatically imply an open-source license.
- If you did not install it, say “documentation review.” If you tried it once, state the task and result rather than claiming comprehensive testing.
- Track product availability, paper-reading scope, and source-code execution tests separately. Updating one does not refresh the dates or status of the others.

Usage records may include date, project version/commit, operating system and device, model, task, success criteria, human interventions, cost, and failure reasons. Do not upload API keys, cookies, tokens, real private conversations, or personal information without consent.

## Updating or removing entries

- Broken links: look for an official migration announcement first. A temporary access failure alone is not a reason to remove a project.
- Inactive or archived projects: record verified status and date. Retain material with learning value or move it to a historical category.
- Inaccurate capability or privacy descriptions: prioritize corrections and explain the evidence.
- Product renaming, regional restrictions, charging, or availability changes: update official sources and dates. Do not keep a discontinued service labeled as available.
- Paper versions, publication status, or implementation URLs: preserve version correspondence. Do not apply old conclusions to a new version without reviewing it.
- Security issues: do not post usable credentials or private data in public issues. Follow the affected project's official security-reporting route. This repository is not a third-party product's support or incident-response team.

## Submission checklist

- [ ] Official links are accessible and canonical.
- [ ] Classification matches the content; an SDK, research prototype, or waitlisted product is not presented as a complete, available assistant.
- [ ] Capabilities, availability, or research contributions have appropriate primary evidence and important conditions are stated.
- [ ] Review date and reading/testing scope are clear; author reports and independent tests are distinguished.
- [ ] Evidence in the relevant directory is updated, along with the README and source index where needed.
- [ ] Corresponding Chinese and English documents are updated, with matching categories, entries, links, dates, and limitations.
- [ ] Local document links and contents anchors have been checked.
- [ ] No secrets, private data, affiliate links, or unauthorized copying of long passages are included.

## License status

No content license has yet been selected for this repository; keep that status in mind before contributing. Contributions do not relicense third-party projects. Do not add a repository license without the maintainer's decision.
