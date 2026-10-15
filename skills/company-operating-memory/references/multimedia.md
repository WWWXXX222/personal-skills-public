# Multimedia Handling

Treat multimedia as raw evidence, not as the final memory.

## Screenshots And Images

For screenshots of chats, emails, dashboards, competitor pages, customer
feedback, or contracts:

1. Inspect the image.
2. Extract the facts, names, dates, numbers, asks, objections, decisions, and
   action items.
3. Save a raw input markdown summary. If the image itself must be preserved, use
   `founder-memory/raw-inputs/assets/` and link to it from the raw input.
4. Create or update structured concepts from the extracted facts.
5. Do not rely on the screenshot alone as the searchable memory.

Suggested asset path:

```text
founder-memory/raw-inputs/assets/YYYY-MM-DD_short-description.png
```

## Video

Do not commit large videos by default. Prefer an external link plus structured
notes.

For demos, calls, screen recordings, or product walkthroughs:

1. Identify the purpose: customer interview, product demo, bug report, competitor
   research, sales call, or internal review.
2. Extract transcript or summary when available.
3. Capture key timestamps and screenshots only when they carry durable evidence.
4. Convert durable learnings into `CustomerSignal`, `Evidence`, `Question`,
   `Decision`, `Experiment`, or `ActionItem`.
5. Store the source link in raw input.

## Audio

For audio or meeting recordings:

1. Prefer transcript or structured meeting notes.
2. Extract direct customer language only when it is important and short.
3. Preserve decisions, objections, budget, timeline, stakeholders, risks, and
   next actions.

## Large Files

Avoid committing large binary files to the repo. Use links to Drive, Loom,
Granola, Notion, or the system of record, then store summaries and extracted
concepts in the vault.
