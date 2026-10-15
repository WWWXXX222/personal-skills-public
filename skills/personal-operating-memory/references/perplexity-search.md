# Perplexity Search And Sonar

Use this reference when a personal memory task needs current external evidence,
public web research, market/company lookup, current finance/travel/life-admin
context, or source-backed claims beyond the local vault.

## Routing

Search local memory first when the question is about the user. Use Perplexity
only when the answer depends on current or external facts.

Use Perplexity Search API when you need:

- ranked raw web results
- URLs and snippets for later inspection
- simple discovery before deciding what to read
- market, company, product, venue, or public-person lookup

Use Perplexity Sonar when you need:

- a cited web-grounded synthesis
- a short research memo with sources
- current comparative context
- public evidence summarized before deciding whether to save memory

Do not use Perplexity for:

- private personal facts already in the vault
- credentials, account access, hidden personal data, or invasive lookup
- medical, legal, financial, or tax decisions without clear caveats and user
  confirmation

## Secrets

Read the API key from `PERPLEXITY_API_KEY`.

Never write the real key into:

- the skill folder
- `personal-memory/`
- raw inputs
- concept pages
- committed env files
- chat summaries intended for persistence

If the key is missing, tell the user to set it locally instead of asking them to
paste it into a file.

## Script

Prefer the bundled script for direct calls:

```bash
python ~/.codex/skills/personal-operating-memory/scripts/perplexity_search.py \
  search "latest IRS mileage rate" --max-results 5
```

```bash
python ~/.codex/skills/personal-operating-memory/scripts/perplexity_search.py \
  sonar "Summarize current Roth IRA contribution limits with citations" \
  --model sonar-pro --recency year
```

Useful options:

- `--domain example.com` to restrict to one or more domains
- `--recency hour|day|week|month|year`
- `--language en` or `--language zh`
- `--country US`
- `--context low|medium|high`

## API Shapes

Perplexity Search API:

- endpoint: `POST https://api.perplexity.ai/search`
- body includes `query`, optional `max_results`, domain/date/language filters,
  and context or token controls
- response returns `results[]` with `title`, `url`, `snippet`, and optional
  `date` and `last_updated`

Perplexity Sonar API:

- endpoint: `POST https://api.perplexity.ai/v1/sonar`
- body includes `model`, `messages`, and optional search controls
- recommended default model: `sonar-pro`
- supported models include `sonar`, `sonar-pro`, `sonar-deep-research`, and
  `sonar-reasoning-pro`
- response follows chat completion shape and may include `citations` and
  `search_results`

## Research-To-Memory Rules

External research is not automatically durable memory.

Before writing it to `personal-memory/`, decide whether it should become:

- `Evidence`: source-backed public fact relevant to the user
- `Question`: unresolved research or decision question
- `Decision`: a user-confirmed choice or policy
- `Snapshot`: time-bound external context, such as monthly market/finance state
- `ActionItem`: next step based on research

When saving external research:

1. Save the query, date, and key source URLs.
2. Preserve snippets or summaries, not full copyrighted articles.
3. Mark what is source-backed versus inferred.
4. Use `sensitivity: private` unless it is clearly low-risk public context.
5. Link the saved evidence to any affected personal concept.

## Citations And Response Discipline

Always cite URLs used in the answer.

For finance, tax, legal, medical, and safety-adjacent topics:

- identify source dates when available
- say when facts are current as of the search date
- do not turn web research into personalized professional advice
- ask for confirmation before actions like trades, borrowing, filings, medical
  decisions, or legal commitments

For people and relationship research:

- avoid invasive lookup
- use only public, relevant sources
- avoid storing sensitive third-party details unless the user explicitly asks and
  the information is necessary for a legitimate personal workflow
