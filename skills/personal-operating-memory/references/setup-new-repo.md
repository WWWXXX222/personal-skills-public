# Setup New Personal Memory Repo

Use this flow when the user asks to set up Personal Operating Memory from zero,
initialize an empty folder, create a clean personal memory repo, or repair a
missing `personal-memory/` structure.

## Required Inputs

Before writing files, know:

- target repo path
- owner/profile label, defaulting to "personal" if the user does not care
- whether to initialize git and make a first commit
- whether to include a Perplexity API setup reminder

If the target path is missing, inspect the current working directory. If it is
empty or lacks `personal-memory/`, assume the current directory is the target
unless the user says otherwise.

## Setup Wizard

Use this compact wizard when the user gives only a short setup request:

```text
I can initialize this folder as a clean Personal Operating Memory repo. Please tell me:
1. Target path? Default: current folder.
2. Owner/profile label? Default: personal.
3. Initialize git and create the first commit? (yes/no)
4. Include a Perplexity API key setup reminder for external search? (yes/no)
```

Use these defaults when the user does not specify:

- target path: current working directory
- owner/profile label: `personal`
- git: initialize and commit only after explicit confirmation
- push: never push during setup unless explicitly asked
- Perplexity reminder: include if the user says yes; skip if they say no or
  want the smallest possible setup

If the current directory is not empty, inspect it and continue only when
existing files are harmless or clearly related to initialization. Ask before
overwriting user files.

## Isolation Rules

Treat any existing personal vault as a template, not as a data source.

Never copy:

- `personal-memory/raw-inputs/**`
- existing `personal-memory/life/**` concept pages or media
- populated `personal-memory/indexes/concepts.json`
- existing `personal-memory/log.md` history
- `.git/**`
- `.env*`, secrets, credentials, local caches, or dependency folders

Create or copy only generic files:

- `personal-memory/CHATBOT.md`
- `personal-memory/SCHEMA.md`
- `personal-memory/templates/**`
- empty `personal-memory/index.md`
- empty `personal-memory/log.md`
- empty `personal-memory/indexes/concepts.json`
- empty `personal-memory/indexes/sources.json`
- empty `personal-memory/indexes/topics.json`
- optional generic `AGENTS.md`

Run a text search after copying to catch leaked private names, dates of birth,
relationships, employers, account data, or other private facts from the source
vault. Rewrite or remove matches.

## Target Vault Shape

Create:

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
  indexes/
    concepts.json
    sources.json
    topics.json
  templates/
    concept.md
    source-digest.md
    claim.md
    idea.md
    topic-map.md
  CHATBOT.md
  SCHEMA.md
  index.md
  log.md
```

Initialize `indexes/concepts.json` as:

```json
[]
```

Initialize `indexes/sources.json` and `indexes/topics.json` as empty arrays.

## Optional Perplexity Search Setup

If the user wants stronger external search, remind them to configure
`PERPLEXITY_API_KEY` locally.

Handle the key as a secret:

- never write the real key into `personal-memory/`, concept pages, raw inputs,
  the skill folder, `AGENTS.md`, `README.md`, or committed files
- do not ask the user to paste the real key into the repo
- prefer the shell environment, a local secret manager, or an uncommitted
  `.env.local`
- if creating env helper files, create only placeholders such as `.env.example`
  and ensure real-key files are ignored

External search results should be cited and kept separate from durable personal
memory until the user asks to save them.

## AGENTS.md Requirements

If creating `AGENTS.md`, include:

- this repo is a local-first personal operating memory system
- `personal-memory/` is the source of truth
- `raw-inputs/` stores source material
- `life/` stores maintained concept pages
- `indexes/concepts.json` is derived or manually maintained from frontmatter
- `knowledge-catalog/` stores OKF-style source digests and derived reading
  knowledge for articles, videos, reports, papers, books, and transcripts
- `indexes/sources.json` and `indexes/topics.json` are derived from the
  knowledge catalog
- the current chatbot conversation is the primary interface
- memory scope is personal operating judgment, not an archive of every thought
- supported concept types are `Question`, `Insight`, `Evidence`, `Signal`,
  `Snapshot`, `Decision`, `Experiment`, and `ActionItem`
- supported catalog types are `Source`, `Claim`, `Idea`, and `TopicMap`
- keep therapy, emergency, investment, tax, legal, and credential boundaries
- optional external research keys such as `PERPLEXITY_API_KEY` are local
  secrets and must never be committed or written into the memory vault

## Preferred Initialization Flow

1. Create or confirm the target repo directory.
2. Create empty vault directories.
3. Write generic `CHATBOT.md`, `SCHEMA.md`, `index.md`, `log.md`, and templates.
4. Write `indexes/concepts.json`, `indexes/sources.json`, and
   `indexes/topics.json` as empty arrays.
5. Add optional generic `AGENTS.md`.
6. Validate that index JSON files parse as JSON.
7. Search for source-vault private residue and remove it.
8. Initialize git and commit only if the user asked for it.

## Completion Report

When done, report:

- target repo path
- owner/profile label
- validation commands run and results
- confirmation that no source raw inputs, concept pages, populated indexes, or
  historical logs were copied
- whether Perplexity setup was included
- the short daily command the user can say in a new chat

Example:

```text
Use $personal-operating-memory. Start personal daily memory mode.
```
