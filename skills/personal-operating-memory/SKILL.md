---
name: personal-operating-memory
description: Operate a private Personal Operating Memory system using Codex plus a markdown vault. Use when asked to initialize, capture, remember, query, review, summarize, or hand off durable personal memory across emotion, relationships, work, finance, health, and life admin; ingest, summarize, classify, fact-check, and discuss articles, videos, reports, papers, books, links, transcripts, and reading notes as an OKF-style knowledge catalog with source digests, claims, ideas, topics, citations, and searchable indexes; provide warm user-prioritized relationship support; use Perplexity when current external evidence is needed; keep private facts in the vault, not the skill; and avoid replacing therapy, emergency, investment, tax, legal, or other professional advice.
---

# Personal Operating Memory

Use Codex as the frontend and a markdown vault as the source of truth. The vault
holds private facts; this skill holds the operating workflow. Do not store
private personal facts inside the skill.

## Start Here

When asked to initialize, template, clone, or set up a clean personal memory
repo from zero, read `references/setup-new-repo.md` first. If inputs are
missing, run its setup wizard by asking concise questions instead of requiring a
long prompt. Never copy private facts, raw inputs, populated indexes, or logs
from an existing personal vault into the new repo.

When working in a personal memory repo:

1. Read `AGENTS.md` if present.
2. Find the vault, usually `personal-memory/` in the current workspace.
3. Read `personal-memory/CHATBOT.md` and `personal-memory/SCHEMA.md` if present.
4. Read `personal-memory/index.md` and `personal-memory/indexes/concepts.json`
   if present.
5. If `personal-memory/knowledge-catalog/` or
   `personal-memory/indexes/sources.json` exists, read the catalog root index
   or generated source index before answering reading/research questions.
6. Search relevant concept and source pages before answering or writing.

If the user asks to initialize or repair the system, create or update the
standard `personal-memory/` structure described in
`references/schema.md`. Keep the vault empty of inferred private facts unless
the user explicitly supplies them.

When a task needs current external evidence, public profile research, market
research, finance context, travel/life-admin lookup, or source-backed claims,
read `references/perplexity-search.md`. Use Perplexity only with an explicit
API key in the environment, and keep external search results separate from
durable personal memory until the user asks to save them.

When the user shares articles, videos, reports, papers, books, links,
transcripts, highlights, or asks for 文摘, 摘要, digest, reading notes, source
capture, fact-checking, knowledge cataloging, topic maps, or cross-source
synthesis, read `references/source-digest.md`. Treat the reading layer as an
OKF-style knowledge bundle: markdown files with YAML frontmatter, stable
paths, `resource` URLs, structured bodies, cross-links, `# Citations`, `index.md`,
`log.md`, and generated indexes.

When the user discusses romance, attachment, jealousy, guilt, ambiguous
relationships, breakups, reconciliation, family pressure, disappearance
concerns, or emotionally loaded messages, read
`references/emotional-relationship-support.md`. Use it to respond warmly while
prioritizing the user's feelings, dignity, stability, agency, and long-term
interests. Keep private relationship facts in the vault, not in this skill.

## Core Workflow

For capture/update requests:

1. Decide whether the input deserves durable memory or should stay in chat.
2. Preserve raw source material under `personal-memory/raw-inputs/` when the
   user provides or points to a durable file, attachment, transcript, dataset,
   HTML page, document, spreadsheet, code artifact, or other source that may be
   queried, edited, verified, or reused later. Do not rely only on an external
   filesystem path, link, or summary when future work depends on the underlying
   content.
3. Update existing concepts before creating new ones.
4. Use concept types: `Question`, `Insight`, `Evidence`, `Signal`,
   `Snapshot`, `Decision`, `Experiment`, `ActionItem`.
5. Use `area` to distinguish `emotion`, `finance`, `work`, `relationship`,
   `health`, `life-admin`, or `unknown`.
6. Link related concepts by stable IDs in `links`.
7. Append a concise entry to `personal-memory/log.md`.
8. Regenerate or update `personal-memory/indexes/concepts.json` when possible.
9. Summarize what changed and name the files touched.

For source digest and knowledge-catalog requests:

1. Decide whether the item is a source to catalog, a claim/idea to extract, a
   personal-memory update, or only a chat summary.
2. Store source digests under `personal-memory/knowledge-catalog/sources/` and
   derived claims, ideas, questions, or topic maps under matching catalog
   subdirectories.
3. Use OKF-style frontmatter with at least `type`, `title`, `description`,
   `resource` when available, `source_type`, `tags`, `captured`, `timestamp`,
   `confidence`, and `sensitivity`.
4. Put source-backed links under `# Citations`; keep verbatim quotes short and
   only when useful.
5. Link durable personal implications back into `life/` concepts only when the
   source changes the user's decisions, patterns, questions, experiments, or
   action items.
6. Update `personal-memory/knowledge-catalog/index.md`,
   `personal-memory/knowledge-catalog/log.md`, and generated source/topic
   indexes when possible.

For query/review requests:

1. Read the generated index first.
2. Open the most relevant concept pages.
3. For reading or research questions, search `sources.json`, `topics.json`, and
   catalog source pages before synthesizing.
4. Answer from memory with file references.
5. Distinguish sourced memory, source-backed external evidence, inference, and
   current uncertainty.
6. Offer to write back only when the answer creates or changes durable memory
   or catalog knowledge.

For external research requests:

1. Search local memory first when the question is about the user.
2. Use Perplexity Search API for ranked raw web results.
3. Use Perplexity Sonar for cited, web-grounded synthesis.
4. Cite sources and separate current web evidence from personal memory.
5. Save research to the vault only when the user asks or when it becomes a
   durable `Evidence`, `Question`, `Decision`, `Snapshot`, or `ActionItem`.

## Write Discipline

Do write durable personal judgment:

- recurring emotional patterns, triggers, boundaries, and effective coping moves
- finance snapshots, budget rules, decision policies, questions, and experiments
- work feedback, commitments, project state, operating principles, and reviews
- relationship or life-admin signals that change future decisions
- action items with clear next steps
- raw copies of important user-provided files when those files are evidence or
  are likely to be edited, queried, re-rendered, compared, or reused later

Do write durable source knowledge:

- source digests for articles, videos, reports, papers, books, and transcripts
- claims, ideas, topic maps, and open questions that recur across sources
- credibility notes, counterarguments, and evidence quality judgments
- personal relevance when a source changes future thinking or behavior

Avoid writing:

- every mood swing or casual thought
- every casual article skim or low-value link
- full account numbers, card numbers, tax IDs, passwords, seed phrases, or login
  details
- duplicate concepts or raw dumps when a structured summary is enough
- company operating facts that belong in a separate company/founder vault

## Safety Boundaries

Emotion: Be supportive and reflective, but do not diagnose or replace therapy.
If the user mentions self-harm, imminent danger, abuse, or inability to stay
safe, prioritize real human support and emergency resources before memory work.
For romantic or attachment-heavy situations, soothe the user's feeling first,
then redirect away from self-abandonment, coercion, stalking, or emotional
games. Safety confirmation is appropriate when concrete risk exists; anxious
pursuit for reassurance should be gently contained.

Finance: Track facts, hypotheses, decisions, and questions. Do not make
automatic personalized investment, tax, legal, lending, or insurance decisions.
Before trades, borrowing, tax filings, or legally binding actions, ask for
explicit user confirmation and suggest a qualified professional when appropriate.

Work: Keep personal operating memory separate from company memory. Personal
memory records how the user works, what they learn, and their career judgment;
company vaults record company facts and business decisions.

## References

Read only what the task needs:

- `references/setup-new-repo.md`: initialize a clean personal memory repo or
  vault without copying private facts from another vault.
- `references/schema.md`: vault layout, frontmatter, concept types, body
  conventions, and empty index shape.
- `references/capture-query-review.md`: detailed capture, query, update,
  periodic review, and response workflows.
- `references/source-digest.md`: OKF-style source digest, article/video/report
  summarization, claim extraction, topic mapping, citation, credibility, and
  searchable knowledge-catalog workflow.
- `references/emotional-relationship-support.md`: warm relationship support
  workflow that prioritizes the user's emotional reality, dignity, agency,
  boundaries, and safety without replacing therapy or encouraging manipulation.
- `references/perplexity-search.md`: Perplexity Search/Sonar API usage,
  routing, secret handling, citations, and research-to-memory rules.
