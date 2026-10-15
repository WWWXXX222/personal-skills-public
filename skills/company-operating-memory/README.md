# Company Operating Memory · 公司经营记忆

把会议、客户反馈、业务判断、决策和待办，整理成可查询、可追溯、可交接的公司记忆。适合创始人、管理者和业务团队，用 Codex 对话维护 Markdown 资料库。

## 能做什么

- **记录**：从会议纪要、访谈、截图和文档中提取证据、客户信号、问题与行动项。
- **查询**：回答“当时为什么这么决定”“客户提出过哪些问题”，并引用原始资料或概念页面。
- **更新**：沿用已有记录，保留决策变化和证据来源，减少重复文档。
- **复盘与交接**：检查未解决的问题、缺乏证据的假设、过期待办，以及实验的进展和结果。
- **初始化**：为新公司建立空白资料库，不需要原公司的仓库或数据。

资料保存在使用者自己的 Markdown 文件中，可以用 Obsidian 阅读，也可以用 Git 做版本管理。Skill 只包含通用工作流，不附带作者公司的客户资料、会议记录或经营数据。安装 skill 本身不会创建公司档案或上传内容。

## 安装

取得本目录的完整副本，将它放到 `~/.codex/skills/company-operating-memory/`，保留 `SKILL.md`、`agents/` 和 `references/`。重新打开 Codex 会话后使用。

[GitHub 源码](https://github.com/WWWXXX222/personal-skills/tree/main/skills/company-operating-memory) 位于私有仓库，访问需要仓库权限。没有仓库权限的同事可以使用维护者提供的独立分享包，无需取得其他 personal skills。

## 第一次使用

在 Codex 中打开准备存放公司资料的空文件夹，然后说：

```text
使用 $company-operating-memory，为我的公司建立经营记忆库。
公司名是「你的公司名」，资料保存在当前文件夹。
```

只需安装这个 skill 即可开始初始化；不要求数据库、后台服务、API key 或作者的公司仓库。初始化时会根据本机环境生成索引工具并说明其运行依赖。

已有资料库时可以说：

```text
使用 $company-operating-memory，把这份会议纪要整理进公司记忆，更新已有记录并列出待办。
```

```text
使用 $company-operating-memory，回顾这个决策的演变、依据和仍未解决的问题。
```

资料目录沿用 `founder-memory/` 这一约定，兼容已有资料库；它不限定使用者必须是创始人。完整操作规则见 [SKILL.md](SKILL.md)，安装与分享细节见 [install-and-share.md](references/install-and-share.md)。
