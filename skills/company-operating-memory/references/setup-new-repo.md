# Setup New Repo

Use this flow to initialize a clean founder/company memory vault. The shareable
skill works without the author's original repository or any proprietary app.

## Confirm Scope

Before writing, confirm the company display name and target folder. When the
user opened an empty folder and asks to initialize it, use that folder as the
proposed target and ask only for missing information.

A compact setup question can be:

```text
What company is this memory vault for? Shall I use the current folder?
Do you want local Git version history, or just a folder of Markdown files?
```

Defaults:

- Skill name: `company-operating-memory`.
- Interface: the current Codex conversation.
- Storage: Markdown and a derived local JSON index.
- Git: initialize/commit only with permission; no remote push by default.
- External search and API keys: optional, not required for setup or daily capture.
- Template repository: optional and only if the user provides one.

Inspect a nonempty folder before writing. Reuse compatible existing files and
schema. Do not overwrite unrelated work or create a duplicate vault silently.

## Two Setup Paths

### Standalone setup — default for this distribution

Read `standalone-vault.md` in this references folder. Create the minimal vault
documents, empty index and concept templates described there. Create a small
local index generator and checks appropriate to the available runtime. Explain
any runtime needed to run those checks.

Do not require `app/lib/founderMemory.js`, a website, a server, an API key or a
copy of the author's workspace. The skill is a workflow; the agent generates
the user's vault when setup is requested.

### Existing template repository — only if supplied

Reuse only generic schema, workflow, templates, tests and index-generation code.
Inspect each copied file for company-specific facts and rewrite target-facing
documents. Run app-specific commands only if that app and its dependencies
actually exist. A template app is optional, not part of this skill package.

## Isolation Rules

Do not copy source-company facts into a new company's vault. Never copy:

- populated `raw-inputs/`, concept pages, source screenshots or media
- populated indexes or historical logs
- credentials, `.env*`, caches, dependency folders or `.git/`

Generic templates must use fictional placeholders, not real source-company
names, customers or personal paths. Check for residue before delivery.

## Target Vault Shape

```text
AGENTS.md
README.md
founder-memory/
  CHATBOT.md
  SCHEMA.md
  index.md
  log.md
  raw-inputs/
  company/
    index.md
    strategy/
    product/
    gtm/
    fundraising/
    customers/
    competitors/
    decisions/
    questions/
    experiments/
    evidence/
    action-items/
  indexes/
    concepts.json
  templates/
```

Raw inputs are source evidence; concept pages are maintained interpretations.
Keep the source evidence unchanged, and record corrections in the concepts.
Only the `company/` concept pages feed the concept index, not templates or raw
inputs. Start `concepts.json` as `[]`.

## Repository Instructions

Write a short `AGENTS.md` and `README.md` for the target company that explain:

- the vault is the source of truth; the conversation is its interface
- supported concept types and where sources, concepts and indexes live
- facts, interpretations, proposals and confirmed decisions stay distinct
- queries/reviews do not mutate memory unless the user asks to save changes
- capture updates existing concepts before creating duplicates
- the index is generated, not independently edited
- exact local index/validation commands created during setup
- Git behavior agreed with the user; no automatic remote upload
- secrets stay outside the vault and the skill

## Completion Checks

Verify the empty index parses and contains no concepts. Run any new generator
and checks. Confirm references and templates resolve. Search new generic files
for source-company names or private paths. Do not report Git or checks as done
unless they actually ran.

Report the target path, what was created, any dependencies, and this prompt:

```text
Use $company-operating-memory. Start daily memory mode.
```
