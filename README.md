# motor-deepagent

Terminal-first AI agent for electric motor design — PyMotorCAD simulation, spec-driven optimization, structured research, and wiki management.

Built with [LangChain DeepAgents](https://github.com/langchain-ai/deepagents) · [LangGraph](https://github.com/langchain-ai/langgraph) · [PyMotorCAD](https://motorcad.docs.pyansys.com/) · [Rich](https://github.com/Textualize/rich) · [Prompt Toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit)

## Demo

### Terminal Agent

https://github.com/user-attachments/assets/terminal_agent.mp4

<video src="assets/terminal_agent.mp4" controls width="100%"></video>

### Agent Brain — LLM Wiki & Knowledge System

https://github.com/user-attachments/assets/terminal_agent_brain.mp4

<video src="assets/terminal_agent_brain.mp4" controls width="100%"></video>

## Quick Start

```bash
git clone https://github.com/UltraInstinct21/synrm-rotor-optimization-agent.git
cd synrm-rotor-optimization-agent
pip install -e .

# configure .env (copy from .env.example)
motor
```

## Project Structure

```
├── apps/cli/          # Terminal UI (Rich + prompt-toolkit)
├── src/
│   ├── agent/         # DeepAgent factory & runtime
│   ├── motor/         # Spec, validation, scoring, sweep
│   ├── tools/         # Execution, wiki, search, motor tools
│   ├── research/      # Async LangGraph research subgraph
│   └── config/        # Settings & preflight
├── workspace/
│   ├── projects/      # Per-machine spec, ledger, models
│   └── wiki/          # Knowledge base + parameter database (13k+ params)
└── tests/
```

## License

[MIT](LICENSE)
