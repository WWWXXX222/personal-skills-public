# Personal Operating Memory Schema

The vault is an LLM-maintained personal operating memory. It follows plain
markdown, YAML frontmatter, stable links, and git-friendly diffs.

The goal is not to archive everything. The goal is to preserve durable personal
judgment so future sessions can recover patterns, evidence, decisions,
questions, experiments, and next actions without replaying old chats.

## Standard Layout

```text
personal-memory/
  life/
    questions/
    insights/
    signals/
    snapshots/
    decisions/
    experiments/
    evidence/
    action-items/
  raw-inputs/
    emotion/
    finance/
    work/
  knowledge-catalog/
    sources/
      articles/
      videos/
      reports/
      papers/
      books/
    claims/
    ideas/
    questions/
    topics/
  indexes/
  templates/
  CHATBOT.md
  SCHEMA.md
  index.md
  log.md
```

`raw-inputs/` stores source material. Do not rewrite raw inputs for style. Avoid
saving secrets or full credentials. When the user provides or points to an
important reusable file, attachment, transcript, HTML export, document,
spreadsheet, source artifact, or dataset, store a raw copy here before writing
only a summary concept. Use dated slug directories for multi-file or editable
artifacts, and link maintained `life/` concepts back to the raw copy.

`life/` stores maintained concept pages. These pages are the compiled memory
layer and may be updated as understanding changes.

`knowledge-catalog/` stores OKF-style source digests and derived source
knowledge. Use it for articles, videos, reports, papers, books, transcripts,
claims, reusable ideas, research questions, and topic maps. Each non-reserved
markdown file should have YAML frontmatter with a `type` field.

`indexes/concepts.json` is generated from life concept frontmatter.
`indexes/sources.json` and `indexes/topics.json` are generated from the
knowledge catalog. If no generator exists, maintain simple JSON arrays of
metadata.

## Frontmatter Contract

Each maintained concept page should start with:

```yaml
---
id: in_20260628_feedback-trigger
type: Insight
title: "被突然否定时容易进入防御状态"
domain: personal
area: emotion
status: active
priority: medium
tags: [emotion, feedback, trigger]
created: 2026-06-28
updated: 2026-06-28
confidence: medium
sensitivity: private
links: []
summary: "连续几次复盘显示，突然的负面反馈比具体问题本身更容易触发防御。"
---
```

Use simple YAML: scalar values and one-line arrays. Keep IDs stable.

## Concept Types

`Question` captures an unresolved question. Include current view, missing
evidence, stakes, and next action.

`Insight` captures stable self-understanding, work judgment, or financial
pattern. Include what repeated evidence supports it and what might change it.

`Evidence` captures sourced facts. Say what it proves, what it does not prove,
and which concepts it supports.

`Signal` captures one meaningful event: an emotion event, work feedback,
financial change, relationship signal, health signal, or life-admin signal.
Distinguish observation from interpretation.

`Snapshot` captures periodic state such as monthly finance, emotional baseline,
workload, energy, health routine, or relationship context.

`Decision` captures a committed rule, direction, boundary, or policy. Include
context, decision, rationale, review trigger, and consequences.

`Experiment` captures a habit, budget, communication pattern, career strategy,
or other test. Include goal, design, success criteria, date window, and results.

`ActionItem` captures a next step. Include owner when relevant, due date if
known, linked context, and done criteria.

## Knowledge Catalog Types

The knowledge catalog follows an OKF-style markdown bundle. Use these types for
reading and research material:

`Source` captures a whole article, video, report, paper, book, transcript,
thread, dataset, or note. Include `resource`, `source_type`, source metadata,
summary, key claims, credibility, personal relevance, and citations.

`Claim` captures a source-backed or falsifiable assertion. Include support,
counterevidence, uncertainty, and linked sources.

`Idea` captures a reusable framework, mental model, strategy, or principle.
Include when to use it, where it may fail, and linked sources.

`TopicMap` captures a navigable cluster of sources, claims, ideas, and open
questions around a theme.

Catalog source frontmatter should include at least:

```yaml
---
type: Source
title: "Readable title"
description: "One-sentence summary for search snippets."
resource: "https://example.com/source"
source_type: article
author: "Author or unknown"
publisher: "Publisher or platform"
published: 2026-06-29
captured: 2026-06-29
language: zh
tags: [topic, source-type]
timestamp: 2026-06-29T00:00:00-07:00
confidence: medium
sensitivity: low
links: []
summary: "Short durable summary."
---
```

Use `# Citations` at the bottom of source-backed catalog pages.

## Area Values

Use one of:

- `emotion`
- `finance`
- `work`
- `relationship`
- `health`
- `life-admin`
- `unknown`

Use tags for finer categories such as `budget`, `investing`, `feedback`,
`career`, `family`, `sleep`, or `tax`.

## Status Values

Recommended values:

- `active`
- `open`
- `decided`
- `done`
- `closed`
- `superseded`

## Sensitivity Values

Recommended values:

- `low`
- `private`
- `sensitive`
- `restricted`

Use `restricted` for especially sensitive personal, medical, legal, financial,
or relationship material. Never store credentials or full financial identifiers.

## ID Prefixes

Use these prefixes:

- `q_` for `Question`
- `in_` for `Insight`
- `ev_` for `Evidence`
- `sg_` for `Signal`
- `sn_` for `Snapshot`
- `de_` for `Decision`
- `ex_` for `Experiment`
- `ai_` for `ActionItem`

Suggested ID shape: `<prefix><YYYYMMDD>_<short-slug>`.

For knowledge catalog pages, the file path is the stable concept ID. When an
explicit ID is useful, use `src_` for `Source`, `cl_` for `Claim`, `idea_` for
`Idea`, and `tm_` for `TopicMap`.

## Empty Index Shape

When initializing an empty vault, create:

```json
[]
```

Each indexed concept should include at least `id`, `type`, `title`, `area`,
`status`, `priority`, `tags`, `updated`, `summary`, and `path`.

Create empty `sources.json` and `topics.json` as:

```json
[]
```
