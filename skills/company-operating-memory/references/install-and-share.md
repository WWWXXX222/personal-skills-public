# Install And Share

This skill can live inside a repo for version control, then be copied or linked
into a teammate's Codex skills directory.

Share the complete `company-operating-memory/` directory, including `references/`
and `agents/`. No company memory data is included in the skill. The GitHub source
is [WWWXXX222/personal-skills](https://github.com/WWWXXX222/personal-skills/tree/main/skills/company-operating-memory).
That repository is private: recipients need repository access, or a standalone
copy/archive of this skill folder.

## Repo-Local Use

If the skill is inside the repo at:

```text
skills/company-operating-memory/
```

Tell Codex:

```text
Use $company-operating-memory from skills/company-operating-memory for this repo.
```

## Install For Auto-Discovery

Copy or symlink the skill folder into the Codex skills directory.

Typical destination:

```text
~/.codex/skills/company-operating-memory
```

Example:

```bash
mkdir -p ~/.codex/skills
ln -s /path/to/founder-memory/skills/company-operating-memory ~/.codex/skills/company-operating-memory
```

If symlinks are inconvenient, copy the folder instead.

## Empty Folder Setup

After opening an empty target folder in Codex, say:

```text
Use $company-operating-memory to set this up.
```

The skill should inspect the folder, ask for the missing company name and target
path, initialize an empty vault using `setup-new-repo.md` and
`standalone-vault.md`, and report what it created. A source company repository,
API key, database server, and proprietary app are not required.

## Teammate Daily Prompt

After opening the memory repo in Codex:

```text
Use $company-operating-memory. Start daily memory mode.
```
