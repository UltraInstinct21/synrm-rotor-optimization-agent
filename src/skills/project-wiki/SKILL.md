---
name: project-wiki
description: "Wiki management skill — how to read, update, and maintain the project wiki"
---

# project-wiki

## Purpose

Maintain a durable, structured project knowledge base at `workspace/wiki/`.

## Wiki location

```
workspace/wiki/
├── project_overview.md     # goals, scope, high-level decisions
├── codebase_map.md         # module layout, file roles, data flow
├── known_issues.md         # bugs, limitations, unresolved problems
├── active_tasks.md         # current work items and their status
├── architecture/           # design decisions, component docs
├── motorcad/               # Motor-CAD parameters, workflow, result fields
│   ├── workflow.md
│   ├── parameters.md
│   ├── result_fields.md
│   └── experiments/        # experiment logs
└── papers/                 # research paper summaries
```

## Page schema

Every page uses standard markdown with sections:

```markdown
# Page title

## Summary
...

## Key facts
- ...
- ...

## Relevant files / scripts
- ...

## Assumptions / conventions
- ...

## Open questions
- ...

## Source links
- ...
```

## Update rules

1. **Check before creating** — always list existing pages first. Never duplicate.
2. **Merge, don't replace** — append new findings to existing sections. Preserve what's there.
3. **Separate knowledge from questions** — accepted facts go in "Key facts". Uncertainties go in "Open questions".
4. **Record sources** — every new fact should have a source link if possible.
5. **Keep pages scoped** — one topic per page. If a page gets long, split into sub-pages.

## Update workflow

1. `list_pages()` — see current structure
2. `read_page(path)` — check existing content for the target page
3. Build a `WikiUpdatePlan` with new sections or edits
4. `apply_update_plan(plan)` — execute the plan
5. Report what changed
