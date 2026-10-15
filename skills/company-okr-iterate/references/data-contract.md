# 结构化检查输入

`okr.json` 与推荐稿是一组产物，用稳定 O/KR ID 对齐。`assets/okr.example.json` 是完全虚构的单 KR 示例，不是公司事实或建议目标。

## 字段

- `schema_version`: 数字 1。
- `company`: 非空公司名称。
- `period`: `start`、`end`，ISO 日期 `YYYY-MM-DD`。
- `sources`: 数组，每项 `id` 和 `locator`。locator 为可回溯的路径/行号、URL/段落或源记录 ID；不在此放凭据。
- `objectives`: 非空数组，每项 `id`、`title`、非空 `krs`。
- 每个 KR：`id`、`title`、`kind`（`outcome`/`enabler`/`experiment`）、`metric`、`owner`、`baseline`、`target`、`deadline`、`verification`、`dependencies`、`supports`、`open_questions`。
- `metric`: 非空的 `definition`、`unit`、`population`、`window`。不知道时用 JSON null，脚本会列为缺口，不要填“待定”伪装完整。里程碑写明验收状态和目标对象，单位可以为 `acceptance-state`。
- `owner`、`baseline`、`target`: 均为 `value`、`status`、`source_ids`。status 为 `confirmed`/`proposed`/`unknown`。unknown 时 value 必须为 null；confirmed 需要值和至少一个来源。owner.value 是唯一负责人的名称；其他 value 可以是非空字符串或有限数字。proposed 是显式建议或估计，不能当作实际基线；已有支持资料仍应引用。
- `deadline`: 周期内 ISO 日期或 null。超出周期的长期依赖应另列，不伪装成本季度 KR。
- `verification`: 验收方法与数据获取方式，非空字符串或 null。
- `dependencies`: 依赖的 KR ID 数组；必须存在、不能自依赖或成环。外部依赖写到 context.md 并在验收方法引用。
- `supports`: 本 KR 支持的其他 KR ID。enabler 至少关联一个被支持的 KR，由评审核验它最终如何支撑业务结果或探索；其他类型可为空。不得自指。
- `open_questions`: 未解决问题的字符串数组；内容进入 handoff.md。已知无问题时为空。

O 与 KR 的 ID 在文件内唯一；sources 的 ID 在 sources 内唯一。源文件存在不代表内容成立；脚本不解析源文件。目标 rationale、资源表、预算、质量护栏、历史变化和取舍记录保留在 Markdown，由评审核验。

## 运行与解释

```bash
python3 <skill-dir>/scripts/check_okr.py <run-dir>/okr.json > <run-dir>/verification.json
```

输出包含 `structure`、`readiness` 和 findings。结构错误返回退出码 1；输入读取/JSON 解析失败返回 2；无结构错误返回 0。

- `structure=PASS` 只表示已实现的结构和引用检查通过。
- `readiness=DATA_GAPS` 表示仍有未知、建议或开放问题；它们不是事实错误，但不能被称为已确认。
- `readiness=REVIEW_REQUIRED` 表示未发现上述缺口，仍必须进行证据、资源与经营逻辑评审。
- `readiness=NOT_CHECKED` 表示结构失败。

没有任何脚本状态代表最终 OKR 已批准或战略已验证。原始信息不足时不要以通过脚本为目标编数字。
