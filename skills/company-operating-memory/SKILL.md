---
name: company-operating-memory
description: Initialize and maintain company operating memory with Codex and a Markdown vault. Use to capture meetings, customer feedback, evidence, decisions, experiments, and action items; query past context with sources; review open work; and prepare team handoffs. Supports a clean setup for any company without copying another company's private data.
---

# Company Operating Memory

Use Codex as the frontend and a markdown vault as the source of truth. The repo
holds the facts; this skill holds the operating workflow. Do not store private
company facts inside the skill.

Use this for founders, managers, and teams at any company. A new vault can be
initialized using this skill alone; no source-company repository or service is
required. The conventional data folder remains `founder-memory/` so existing
vaults keep working; do not rename an existing vault as part of installing this
skill.

## Start Here

When asked to initialize, template, clone, or set up a clean memory repo for a
new company, read `references/setup-new-repo.md` first. If inputs are missing,
run its setup wizard by asking concise questions instead of requiring the user
to paste a long prompt. Keep the source repo's company facts isolated from the
target repo.

When working in a memory repo:

1. Read `AGENTS.md` if present.
2. Read the vault workflow docs, usually `founder-memory/CHATBOT.md` and
   `founder-memory/SCHEMA.md`.
3. Read `founder-memory/index.md` and `founder-memory/indexes/concepts.json`.
4. Search relevant concept pages before answering or writing.

If these files are missing, infer the closest equivalent from the repo, then ask
whether to initialize the standard structure.

## Core Workflow

For new repo setup requests:

1. Confirm the target company name and target repo path before writing files.
2. Copy or create only generic workflow, schema, app, test, template, and skill
   files.
3. Rewrite `AGENTS.md`, `README.md`, and any copied docs for the target company.
4. Never copy source `founder-memory/raw-inputs/`, source concept pages, source
   indexes, source logs, credentials, caches, or `.git/`.
5. Initialize an empty vault, regenerate the index, run available checks, and
   report that the new repo contains no source-company facts.

For capture/update requests:

1. Preserve the source as a raw input when it is durable evidence.
2. Update existing concepts before creating new ones.
3. Use supported concept types: `Question`, `Hypothesis`, `Evidence`,
   `Decision`, `Experiment`, `CustomerSignal`, `ActionItem`.
4. Keep concept frontmatter simple, OKF-compatible, and consistent.
5. Link related concepts by stable concept IDs in `links`.
6. Append a concise entry to `founder-memory/log.md`.
7. Regenerate `founder-memory/indexes/concepts.json`.
8. Run checks/tests and OKF validation if available.
9. Commit after material or batched memory changes; push only when asked.

For query/review requests:

1. Read the generated index first.
2. Open the most relevant concept pages.
3. Answer from memory with file references.
4. Offer to write back only when the answer changes durable company state.

## Write Discipline

Write durable memory:

- strategic decisions
- unresolved questions
- customer, partner, candidate, or market signals
- evidence
- experiments
- action items
- changed company context

Avoid writing:

- casual thoughts without durable conclusion
- duplicate concepts
- large binaries
- raw confidential data inside the skill
- full transcripts when a structured summary is enough
- ad hoc frontmatter fields not listed in `founder-memory/SCHEMA.md`

## References

Read only the reference needed for the task:

- `references/setup-new-repo.md`: initialize a clean memory repo for another
  company without copying private facts from the source repo.
- `references/standalone-vault.md`: schema, templates, and index requirements
  for a new vault when no template repository is available.
- `references/capture-query-review.md`: capture, query, update, weekly review,
  and schema conventions.
- `references/multimedia.md`: screenshots, images, audio, video, and asset
  handling.
- `references/git-rhythm.md`: commit and push discipline.
- `references/install-and-share.md`: how teammates install or invoke this skill.
