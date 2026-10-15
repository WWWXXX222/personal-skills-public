# Source Digest And Knowledge Catalog

Use this reference when the user shares or asks about articles, videos,
reports, papers, books, links, transcripts, highlights, fact checks, reading
notes, 文摘, 摘要, or cross-source synthesis.

## Operating Model

Treat the reading layer as an OKF-style knowledge bundle inside
`personal-memory/knowledge-catalog/`.

Use plain markdown files with YAML frontmatter, stable paths, source URLs in
`resource`, structural headings, markdown links, `# Citations`, `index.md`,
`log.md`, and generated JSON indexes. The goal is a durable library that both
humans and agents can read, diff, search, and maintain.

Keep the layers distinct:

- `knowledge-catalog/`: what a source says, what claims it supports, what ideas
  it contributes, and how topics connect.
- `life/`: what this changes about the user's personal decisions, patterns,
  questions, experiments, or action items.
- `raw-inputs/`: user-provided source files or transcripts worth preserving as
  evidence.

## Routing

Create a source digest when the item is useful future context, the user asks to
save it, or the item supports future search/discussion.

Do not catalog every low-value link. For quick reading, answer in chat and ask
or offer to save only if the output creates reusable knowledge.

For current external evidence, follow `perplexity-search.md` when the task
requires web-grounded lookup. Save external search results only when they become
durable source evidence or the user asks.

## Directory Layout

Recommended layout:

```text
personal-memory/knowledge-catalog/
  index.md
  log.md
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
```

Use bundle-root-relative markdown links when possible.

## Source Digest Frontmatter

Use simple YAML and preserve unknown fields.

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

Use `source_type` values such as `article`, `video`, `report`, `paper`, `book`,
`podcast`, `thread`, `dataset`, or `note`.

## Source Digest Body

Use these headings by default:

```markdown
# TLDR

# Core Thesis

# Key Claims

# Evidence

# Assumptions

# Counterpoints

# Credibility

# Personal Relevance

# Follow-up Questions

# Citations
```

For videos, add `# Timeline` when timestamps are available. For reports and
papers, add `# Methods` and `# Data` when relevant. For books, add `# Chapters`
or `# Reusable Ideas`.

## Derived Concept Types

Use source digests for whole sources. Create derived catalog concepts only when
the extracted unit will be useful across multiple sources.

`Claim` captures a falsifiable or source-backed assertion. Include what supports
it, what would weaken it, and linked source digests.

`Idea` captures a reusable mental model, framework, analogy, strategy, or
principle. Include when to use it and where it may fail.

`Question` captures an unresolved research question from one or more sources.
Include stakes, current view, missing evidence, and next source to check.

`TopicMap` captures a navigable cluster of sources, claims, ideas, and open
questions around a theme.

## Quality Bar

Good digests should:

- preserve the source's actual thesis before adding interpretation
- separate claim, evidence, inference, and personal relevance
- name uncertainty and credibility limits
- avoid long raw dumps and excessive quotation
- use short direct quotes only when phrasing matters
- include citations for source-backed claims
- link to related source digests and personal concepts when useful

## Capture Workflow

1. Identify source metadata: title, author, publisher/platform, URL or local
   path, date, language, and source type.
2. Decide whether to preserve raw input in `raw-inputs/`.
3. Search existing `sources.json`, `topics.json`, and catalog pages for
   duplicates or related material.
4. Write or update the source digest.
5. Extract `Claim`, `Idea`, `Question`, or `TopicMap` pages only when reusable.
6. Link related catalog pages and any personal-memory implications.
7. Update catalog `index.md`, catalog `log.md`, and generated indexes when
   possible.
8. Summarize what was saved, what remains uncertain, and what can be discussed
   next.

## Query Workflow

1. Read `personal-memory/indexes/sources.json` and
   `personal-memory/indexes/topics.json` if present.
2. Open the most relevant source and topic pages.
3. Answer with file references and citation links when claims depend on
   external sources.
4. Distinguish local catalog memory from current web evidence and inference.
5. Offer to save new synthesis only when it changes durable catalog knowledge or
   personal memory.

## Fact-Check Workflow

For a claim from an article/video/report:

1. Identify the exact claim and who is making it.
2. Search local catalog first.
3. Use current web evidence when the claim is time-sensitive or source-backed
   precision matters.
4. Classify the result as `supported`, `partially supported`, `unverified`,
   `misleading`, or `contradicted`.
5. Save a digest, claim, or credibility note only if the result is reusable.

## Indexing

When an index script exists, run it after catalog writes. The generated
`sources.json` should expose title, description, resource, source type, tags,
published/captured/timestamp, confidence, sensitivity, summary, and path.
`topics.json` should group catalog pages by tag and topic map.
