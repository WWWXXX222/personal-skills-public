# Capture, Query, Update, And Review

Use this reference for day-to-day operation of a personal memory vault.

## Capture

Capture when the user says things like:

- "记住这个"
- "把这个写进 personal memory"
- "这个结论以后要记得"
- "变成 action item"
- "帮我复盘并沉淀"
- "更新一下我的预算/工作/情绪模式"
- "把这篇文章/视频/报告做成文摘"
- "存到 knowledge catalog"
- "以后我能搜到这个观点"

Process:

1. Identify the durable concept, if any.
2. Decide whether raw input belongs in `raw-inputs/`.
3. Search for related existing concepts.
4. Update existing concepts before creating new ones.
5. Create only the concepts that will be useful later.
6. Add bidirectional markdown links when helpful and frontmatter IDs in `links`.
7. Append a concise log entry.
8. Update `indexes/concepts.json`.

Do not permanently store every emotional fluctuation. Prefer raw journaling in
`raw-inputs/emotion/` only when the user asks or when the source is important
evidence. Promote to concepts only recurring patterns, triggers, boundaries,
effective responses, unanswered questions, decisions, experiments, or actions.

For article, video, report, paper, book, transcript, or reading-note capture,
read `source-digest.md` and write to `personal-memory/knowledge-catalog/`
unless the source directly changes personal memory.

### Raw File Handling

When the user provides a local file path, attachment, transcript, exported
HTML, spreadsheet, document, deck, source file, dataset, or other reusable
artifact and asks to record, remember, preserve, update, or edit it later:

1. Copy the original file into `personal-memory/raw-inputs/<area>/`, preserving
   the original extension and preferably grouping related files in a dated
   slug directory.
2. Preserve the raw file as-is. Do not rewrite it for style or convert it to a
   summary-only artifact.
3. Record the original external location, vault raw-copy path, file size,
   modified time when available, and checksum when practical.
4. Create or update the maintained concept page with a concise summary and a
   link to the raw copy.
5. Use the vault raw copy as the durable source for future memory queries,
   comparison, rendering, editing, or re-export unless the user points to a
   newer external working file.

Only skip the raw copy when the source is trivial, inaccessible, unsafe to
store, or the user explicitly says not to preserve it.

## Query

Process:

1. Read `personal-memory/indexes/concepts.json`.
2. Search concept titles, summaries, tags, and bodies.
3. Read the most relevant pages before answering.
4. Answer with source file references.
5. Separate remembered facts from inference.
6. If the answer produces a new durable synthesis, ask or offer to write it back.

Example query shapes:

- "我最近为什么工作很消耗？"
- "今年钱主要漏在哪里？"
- "我每次换方向的共同原因是什么？"
- "我有哪些 open action items？"
- "最近三个月情绪 trigger 的共同点是什么？"
- "我看过哪些关于 AI agent memory 的资料？"
- "把我看过的俄乌战争资料按可信度分组。"
- "哪些文章支持这个观点，哪些反对？"

## Update

Use updates for changed state:

1. Find the existing concept by ID, title, tag, or search.
2. Update frontmatter `updated`, `status`, `confidence`, `priority`, `links`,
   and `summary` when needed.
3. Keep prior context in the body unless it is wrong; mark superseded material
   clearly.
4. Add a log entry.
5. Update the index.

## Periodic Review

For weekly or monthly review, inspect:

- high-priority questions without next actions
- insights without enough evidence
- decisions due for review
- experiments missing results
- open action items
- finance snapshots missing recent data
- recurring emotional or work signals that deserve a synthesis
- source digests without topic tags
- repeated claims that deserve a topic map
- open research questions without follow-up sources

Return a short review with:

- strongest patterns
- unresolved questions
- stale decisions or experiments
- next actions
- suggested memory cleanup

## Response Shape After Writes

When a write happens, end with:

- what changed
- which files changed
- whether the index was updated
- the next useful question or action
