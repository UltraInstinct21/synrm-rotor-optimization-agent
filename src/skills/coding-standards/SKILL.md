---
name: coding-standards
description: "Coding standards for repo inspection and editing"
---

# coding-standards

## Principles

1. **Inspect before edit** — always read relevant files before making changes.
2. **Minimal changes** — change only what the task requires. Do not refactor adjacent code.
3. **Preserve style** — match existing conventions (naming, imports, comment density, error handling).
4. **Validate** — run syntax checks, imports, or existing tests after changes.
5. **Surface uncertainty** — if unsure about an edit point, say so rather than guessing.

## Code inspection workflow

1. Understand the goal — what specifically needs to be found or changed?
2. Search — use grep or file listing to find relevant modules.
3. Read — read the identified files to understand current behavior.
4. Plan — identify exact edit points before modifying anything.
5. Edit — make surgical changes.
6. Validate — run `python -c "import module"` or `pytest` if available.
7. Report — return a `CodeReport` with what was inspected, changed, and what follow-up is needed.

## Edit rules

- Single-responsibility changes per commit/request.
- No speculative abstractions ("we might need this later").
- Error handling: add it only for realistic failure modes, not exhaustive coverage.
- Comments: update them if the code changes meaning.
