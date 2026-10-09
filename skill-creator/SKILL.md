---
name: skill-creator
description: >
  Write or revise an Agent Skill (a directory containing SKILL.md). Use when
  asked to create, add, author, or improve a skill, skill description, or
  SKILL.md — including "make a skill for X" — even if the user never says
  "SKILL.md". Do not use for general docs, AGENTS.md, hooks, extensions, or tools.
---

# Skill creator

A skill is a folder loaded only when `description` matches the task. `name` and `description` are always in context. The body loads on activation. Other files load only if the body says to read them.

## Create

1. One skill = one workflow the agent would get wrong without it. If it already succeeds, do not add a skill.
2. Directory name is the skill name: `^[a-z0-9]+(-[a-z0-9]+)*$`, 1–64 characters. It must equal frontmatter `name`.
3. Write `description` before the body. It alone decides activation.
4. Put the skill at `<skills-root>/<name>/SKILL.md`. Discovery is one directory deep. Common roots: `.agents/skills/`, `.github/skills/`, a project or user `skills/`, and omp skill dirs. `group/<name>/SKILL.md` is not discovered unless the scan root is `group/`.

## Frontmatter

| Field | Required | Rule |
| --- | --- | --- |
| `name` | yes | Equals the directory. Lowercase letters, digits, single hyphens. No leading, trailing, or doubled hyphen. |
| `description` | yes | 1–1024 characters. What it does and when to use it. |

Omit the rest unless needed: `license`; `compatibility` (environment requirements, ≤500 characters); `metadata` (string-to-string map); `allowed-tools` (experimental, space-separated).

omp also reads `globs`, `alwaysApply`, `hide`, and `disable-model-invocation`. `hide` only drops the skill from the prompt list; `skill://<name>` still resolves it.

## Description

Imperative. Match user intent, not implementation. Include triggers where the user never names the domain. Name the near miss so adjacent work does not load it.

```yaml
description: >
  Extract text and tables from PDFs and fill PDF forms. Use when the user
  has a PDF to read, merge, or fill, even if they only say "this form" or
  "the attachment". Do not use for authoring a new PDF or for images.
```

Weak: `Helps with PDFs.`

## Body

Write only what the agent lacks: local conventions, exact commands, non-obvious gotchas, output shape. Cut definitions of ordinary tools and concepts.

- Default, not a menu. One path, one escape hatch.
- Be strict only where order or flags are fragile. Elsewhere say why.
- Keep gotchas in `SKILL.md`. A side file is skipped unless the trigger is obvious.
- Show output as a template, not a description of a template.
- Teach a reusable procedure, not the answer to one instance.
- Keep `SKILL.md` under 500 lines. Point at `references/<file>.md` with the condition that should load it. One level of references only.
- Scripts live in `scripts/`. Paths are relative to the skill root. No interactive prompts; take flags or stdin. Errors must say what failed and the next command.

## Minimum

```markdown
---
name: example-name
description: Do the concrete task. Use when the user asks to Y, even without saying "example". Do not use for Z.
---

# Example name

1. Run the default command.
2. Check the result against the invariant.

## Gotchas

- The concrete failure the agent will otherwise hit.
```

## Before finishing

- `name` equals the directory and matches the pattern.
- Description states the action, the trigger, and a near-miss exclusion, and is ≤1024 characters.
- Every referenced file exists. No `..` or absolute paths inside the skill.
- The body does not restate knowledge the agent already has.
