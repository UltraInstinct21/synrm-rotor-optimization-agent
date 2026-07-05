---
name: paper-reading
description: "How to read, summarize, and ingest a research paper into the wiki"
metadata:
  phase: future
---

# paper-reading

## Purpose

Extract engineering knowledge from research papers and store it durably in the wiki.

## Flow

1. **Locate paper** — file path or URL.
2. **Read abstract + conclusions first** — determine relevance.
3. **Scan key sections** — methodology, equations, results, assumptions.
4. **Extract structured findings** — equations, constraints, parameter values, conventions.
5. **Cross-reference with wiki** — check what our wiki already says. Flag conflicts.
6. **Write paper summary** to `workspace/wiki/papers/<paper>.md`.
7. **Update relevant domain pages** in `motorcad/` if the paper adds actionable knowledge.

## Paper page template

```markdown
# <Paper Title>

## Summary
...

## Key equations
- ...

## Design implications
- ...

## Conflicts with current assumptions
- ...

## Source
<url or path>
```
