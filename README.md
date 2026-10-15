# Personal Skills

个人维护的 Codex skills，涵盖公司经营记忆、个人知识与记忆、通用多 agent 自主迭代、公司 OKR 迭代和关系沟通。工作流与实际数据分开：这里保存通用方法，个人和公司资料留在各自的工作区。

| Skill | 内容 | 文件数 |
| --- | --- | ---: |
| [company-operating-memory](skills/company-operating-memory/README.md) | 公司经营记忆：整理会议、客户反馈、证据、决策与待办，支持查询、复盘、交接和独立初始化 | 9 |
| [personal-operating-memory](skills/personal-operating-memory/SKILL.md) | 个人记忆与知识目录：沉淀工作、生活和阅读资料，关联来源、洞见、决定及行动 | 9 |
| [multi-agent-iterate](skills/multi-agent-iterate/README.md) | 通用多 agent 自主迭代：结构挑战、独立提案、分工、证据评审及文档/代码验收 | 11 |
| [company-okr-iterate](skills/company-okr-iterate/SKILL.md) | 公司级 OKR 自主迭代：独立提案、证据评审、有限轮次修订及结构检查 | 11 |
| [goutoujunshi](skills/goutoujunshi/SKILL.md) | 狗头军师：关系分析、情绪支持、沟通话术与行动建议，保留本地定制和原许可证 | 68 |

## 公司经营记忆：分享给同事

**`company-operating-memory`**，中文名为“公司经营记忆”。它适用于不同公司的创始人、管理者和团队。

可直接转发这段介绍：

> Company Operating Memory（公司经营记忆）是一个用 Codex 维护团队知识的 skill。它把会议、客户反馈、业务判断、决策和待办整理成有出处、可查询、可复盘的 Markdown 资料库，帮助团队保留“当时为什么这样决定”和“接下来谁做什么”。每家公司使用自己的独立资料库；skill 只提供通用工作流，不附带其他公司的数据。

[介绍与安装](skills/company-operating-memory/README.md) · [操作规则](skills/company-operating-memory/SKILL.md)

安装完整目录后，在 Codex 中打开一个空文件夹并说：

```text
使用 $company-operating-memory，为我的公司建立经营记忆库。
公司名是「你的公司名」，资料保存在当前文件夹。
```

本仓库公开可访问，可直接分享 GitHub 链接，也可以单独提供 `skills/company-operating-memory/` 的完整副本或压缩包。

现有 `founder-memory/` 资料目录无需改名。

## 快照范围

完整保留以上 skill 目录及下属文件。符号链接已展开为实际文件，方便迁移。
不包含原仓库的 `.git` 历史、`.DS_Store`、缓存和依赖目录。
本仓库只收录 skill 文件；个人和公司记忆库的数据不在此快照范围内。

`snapshot-manifest.json` 记录每个文件的 SHA-256，用于核对快照完整性；`source` 使用通用安装路径，分发目录名以 `name` 为准。

## 安装或恢复

将 `skills/` 下所需的完整 skill 目录复制到 `~/.codex/skills/`，然后重新打开 Codex 会话。
如目标目录已存在，请先备份或比较差异。外部工具与 API 凭据按各 skill 的文档单独配置。

## Multi-Agent Iterate

公开仓库：[WWWXXX222/multi-agent-iterate](https://github.com/WWWXXX222/multi-agent-iterate)。可直接分享此链接。

使用 `$multi-agent-iterate`，提供任务、现稿或输入资料、约束及迭代预算。例如：

> 用 $multi-agent-iterate 改善这份方案，最多两轮，保留预算和上线日期，自行评审、修订和验证，最后给我推荐稿与待决项。

根据任务选择 arena（独立候选）、swarm（分片协作）或评审修订，不强制每次跑完整流水线。默认方向未定时2个候选、最多3轮修订；主控统一裁决，评审上下文独立，输出绑定真实验证证据。小改动直接完成，不扩成多 agent 项目。

复杂开放任务可在第一轮加入结构挑战，从原始资料独立拆解并与现稿比较；重要反馈需包含影响、具体改法与验证办法。文档、coding 和混合任务分别验收，固定已确认约束，保留调整分类、层级和解法的空间。Skill 维护时可用隔离回放检查主动发现能力，不将已知案例当作盲测。

补充 Boris Cherny 公开实践中的计划、验证、自主排障与经验复用：前提失效时局部重规划，保留有效工作及剩余预算；文档保留可辨认版本、差异和恢复入口。

方法借鉴 [pstack](https://github.com/backnotprop/pstack)、用户提供的视频及 Boris 的公开分享，具体归因、核验限制和适配差异见 [provenance.md](skills/multi-agent-iterate/references/provenance.md)。无需安装 pstack，不硬编码跨厂商模型，也不绑定 OKR、飞书或网站发布。`company-okr-iterate` 保留为公司规划的专用版本。

## Company OKR Iterate

调用 `$company-okr-iterate`，提供公司、周期、现有 OKR 和资料范围。默认一个主控加最多三个并行子 agent，三份独立提案、最多三轮修订和一次最终验收。支持仅设计、仅评审和恢复运行。

安装或创建 skill 不会启动 OKR 迭代。公司资料和运行产物保存在业务工作区，不放入此仓库。结构检查不等于战略验证；未知数据与未确认目标会单独列出。

本 skill 自包含，无需安装 pstack。其轻量检查脚本仅依赖 Python 3 标准库。维护者可运行 `python3 -B -m unittest discover -s skills/company-okr-iterate/tests -p 'test_*.py' -v` 验证脚本。

## 来源与许可

- `company-operating-memory` 和 `personal-operating-memory` 为个人维护的记忆工作流。
- `goutoujunshi` 基于 [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi)，保留本机对 `SKILL.md` 和 `tests/tactical-reply-scenarios.md` 的修改。原作者和许可信息保留在该目录的 `LICENSE`、`LICENSE.zh-CN.md` 及相关文档中。
- `multi-agent-iterate` 为独立编写的通用迭代工作流，公开方法来源见其 provenance.md；不包含公司业务资料或视频字幕。
- `company-okr-iterate` 为个人维护的通用公司规划工作流，方法参考见 [provenance.md](skills/company-okr-iterate/references/provenance.md)。
- 本仓库不为第三方内容重新授权；各目录的原有许可继续适用。
