# Capture, Query, Update, Review

## Capture

Use this flow when the user says things like "record this", "remember this",
"write this into memory", "记录在案", "记住这个", "更新 memory", or gives a
meeting/call/interview note that clearly changes durable context.

1. Identify the source type: chat note, transcript, screenshot summary, customer
   interview, partner update, pricing analysis, strategy discussion, or action
   item.
2. Save a raw input under `founder-memory/raw-inputs/` unless the source already
   exists elsewhere in the vault.
3. Search existing concepts by title, tag, body, and linked IDs.
4. Prefer updating existing concepts. Create a new concept only when it is a
   distinct durable unit.
5. Use one concept type per durable unit:
   - `Question`: unresolved decision or uncertainty.
   - `Hypothesis`: testable belief with evidence/falsifier.
   - `Evidence`: source-backed fact or artifact.
   - `Decision`: committed direction.
   - `Experiment`: test with success criteria.
   - `CustomerSignal`: customer, prospect, partner, candidate, or market actor
     signal.
   - `ActionItem`: owner, due date if known, done criteria.
6. Add backlinks in frontmatter `links` and in the body when helpful.
7. Update `founder-memory/log.md`.
8. Regenerate `founder-memory/indexes/concepts.json`.

## Concept Shape

Frontmatter should remain simple YAML:

```yaml
---
id: cs_YYYYMMDD_short-slug
type: CustomerSignal
title: "Short title"
description: "One sentence."
domain: company
area: gtm
status: active
priority: high
tags: [company-name, customer, topic]
timestamp: YYYY-MM-DDT00:00:00.000Z
created: YYYY-MM-DD
updated: YYYY-MM-DD
confidence: medium
links: [related_concept_id]
summary: "One sentence."
---
```

`description` and `summary` should normally match. `description` is included for
OKF-compatible tooling, while `summary` is kept for the vault index/app.
Do not add new frontmatter fields unless they are first added to the repo schema
and validator.

Body sections should match the concept type. Keep them useful for future agents:
observation, interpretation, why it matters, risks, next actions, and citations.

## Query

Use this flow when the user asks what the company currently believes, what is
open, what happened with a customer, or asks for a synthesis.

1. Read `founder-memory/index.md` and `founder-memory/indexes/concepts.json`.
2. Search for relevant names, tags, and concepts.
3. Read the actual concept pages before answering.
4. Separate facts from inference.
5. Cite local file paths or concept IDs.
6. If the answer creates a new durable synthesis, ask or offer to write it back.

## Update

Use this flow when a status changes.

1. Find the existing concept.
2. Update frontmatter status/updated/confidence if needed.
3. Add the new information to the body without erasing historical context unless
   the user explicitly asks to replace it.
4. Update links when the new information connects concepts.
5. Log the update.
6. Regenerate the index.

## Weekly Review

Inspect:

- open questions without next actions
- hypotheses without evidence
- stale decisions
- experiments without success criteria or results
- action items that should be closed, reassigned, or clarified
- GTM claims detached from customer/partner evidence
- duplicate concepts that should be merged

Return a short prioritized review, then write back only if asked.
