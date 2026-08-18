# workspace/

Isolated directory for files the agent operates on and produces.

```
workspace/
├── repo/             # Project codebase reference
├── wiki/             # Durable markdown knowledge base & parameter database
│   ├── index.md
│   ├── project_overview.md
│   ├── codebase_map.md
│   ├── active_tasks.md
│   ├── architecture/
│   └── motorcad/     # 13,000+ parameter database & PyMotorCAD documentation
├── scratch/          # Temporary sandboxed execution scripts (auto-cleaned)
└── exports/          # Session Markdown exports & response copies
```

---

## Safety & Sandboxing

- All dynamic Motor-CAD script creation (`create_run_file` / `execute_generated_motorcad_code`) operates strictly within `workspace/scratch/`.
- Path traversal guards enforce that file creation cannot break out of `workspace/scratch/`.
- Temporary scripts created by `execute_generated_motorcad_code` are automatically cleaned up after execution.
