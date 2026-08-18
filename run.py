"""motor-deepagent launcher — creates a Deep Agents instance with Motor-CAD tools."""

from src.agent.factory import build_agent

if __name__ == "__main__":
    import sys

    agent, tools = build_agent()

    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        result = agent.invoke({"messages": [("user", query)]})
        print(result["messages"][-1].content)
    else:
        print("motor-deepagent ready. Usage: python run.py 'your question'")
        print("Tools loaded:", len(tools))
