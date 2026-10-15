# Git Rhythm

Commit after material changes or batches of memory updates.

## Commit When

- a customer, partner, candidate, or investor interview is captured
- a strategy, pricing, fundraising, product, or GTM synthesis is added
- multiple concept pages or action items are updated
- schema, docs, onboarding, skill, app code, or agent instructions change
- handing work to another teammate
- memory changed during an active working day

## Before Commit

1. Regenerate the index.
2. Run the index and validation commands documented in the target repository.
   Use the following only when the repository actually defines these scripts:

```bash
npm run check
npm test
```

3. Review `git status --short` and `git diff --stat`.
4. Ensure generated or local clutter such as `.DS_Store` is ignored.

## Commit Messages

Use concrete messages:

```bash
git commit -m "Capture customer interview signal"
git commit -m "Update product pricing strategy"
git commit -m "Document bilingual teammate onboarding"
git commit -m "Create company operating memory skill"
```

## Push

Do not push unless the user explicitly asks or the team workflow requires it.
When pushing a private company memory repo, remind the user if sensitive data may
be uploaded to a remote.
