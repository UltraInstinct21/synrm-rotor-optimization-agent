"""Session persistence — save/load/list/export conversations."""

from __future__ import annotations

import json
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path


@dataclass
class Session:
    """A single conversation session."""

    id: str = field(default_factory=lambda: uuid.uuid4().hex[:12])
    created: str = field(default_factory=lambda: datetime.now().isoformat())
    messages: list[dict] = field(default_factory=list)
    todos: list[dict] = field(default_factory=list)
    path: Path | None = None

    @property
    def title(self) -> str:
        """Derive a title from the first user message, or default."""
        for msg in self.messages:
            if msg.get("role") == "user" and msg.get("content"):
                clean = msg["content"].strip().replace("\n", " ")
                return clean[:45] + ("..." if len(clean) > 45 else "")
        return "Empty Session"

    @property
    def message_count(self) -> int:
        return len(self.messages)

    def add(self, role: str, content: str) -> None:
        """Append a message and auto-save if path is set."""
        self.messages.append({"role": role, "content": content})
        if self.path is not None:
            self.save(self.path.parent)

    def add_todo(self, task: str, status: str = "pending") -> dict:
        """Add a new TODO item to session."""
        todo_id = len(self.todos) + 1
        item = {"id": str(todo_id), "task": task.strip(), "status": status}
        self.todos.append(item)
        if self.path is not None:
            self.save(self.path.parent)
        return item

    def update_todo(self, todo_id: str | int, status: str) -> bool:
        """Update status of a TODO item ('pending', 'in_progress', 'completed')."""
        target_id = str(todo_id)
        for item in self.todos:
            if item["id"] == target_id:
                item["status"] = status
                if self.path is not None:
                    self.save(self.path.parent)
                return True
        return False

    def clear_todos(self) -> None:
        """Clear all TODO items."""
        self.todos.clear()
        if self.path is not None:
            self.save(self.path.parent)

    def get_todos(self) -> list[dict]:
        """Return list of TODO items."""
        return self.todos

    def save(self, directory: Path) -> Path:
        """Write session to disk. Returns the file path."""
        directory.mkdir(parents=True, exist_ok=True)
        path = directory / f"{self.id}.json"
        path.write_text(
            json.dumps(
                {
                    "id": self.id,
                    "created": self.created,
                    "title": self.title,
                    "messages": self.messages,
                    "todos": self.todos,
                },
                indent=2,
            ),
            encoding="utf-8",
        )
        self.path = path
        return path

    def export_markdown(self, output_path: Path) -> Path:
        """Export session transcript to a Markdown document."""
        lines = [
            f"# motor-deepagent Transcript — Session {self.id}",
            f"**Created:** {self.created}",
            f"**Total Messages:** {self.message_count}",
            "\n---",
        ]
        for msg in self.messages:
            role = msg.get("role", "unknown").upper()
            content = msg.get("content", "")
            lines.append(f"\n### 👤 {role}" if role == "USER" else f"\n### ⚡ {role}")
            lines.append(content)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text("\n".join(lines), encoding="utf-8")
        return output_path

    @classmethod
    def load(cls, path: Path) -> Session:
        """Load a session from a JSON file safely, recovering from corruption if needed."""
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            return cls(
                id=data.get("id", path.stem),
                created=data.get("created", datetime.now().isoformat()),
                messages=data.get("messages", []),
                todos=data.get("todos", []),
                path=path,
            )
        except Exception:
            # Back up corrupted file before overwriting
            backup_path = path.with_suffix('.json.bak')
            try:
                if path.exists():
                    path.rename(backup_path)
            except Exception:
                pass
            return cls(
                id=path.stem,
                created=datetime.now().isoformat(),
                messages=[{"role": "system", "content": f"[Recovered session file after read/decode error. Backup: {backup_path.name}]"}],
                path=path,
            )


class SessionStore:
    """Manages session files on disk."""

    def __init__(self, directory: Path) -> None:
        self.directory = directory
        self.directory.mkdir(parents=True, exist_ok=True)

    def new(self) -> Session:
        """Create and persist a new session."""
        session = Session()
        session.save(self.directory)
        return session

    def list_sessions(self, limit: int = 10) -> list[Session]:
        """Return the most recent sessions, newest first."""
        files = sorted(
            self.directory.glob("*.json"),
            key=lambda f: f.stat().st_mtime,
            reverse=True,
        )
        return [Session.load(f) for f in files[:limit]]

    def load_session(self, session_id: str) -> Session | None:
        """Load a session by its ID (first 8 chars of UUID)."""
        path = self.directory / f"{session_id}.json"
        if path.exists():
            return Session.load(path)
        return None

    def delete_session(self, session_id: str) -> bool:
        """Delete a session file by ID."""
        path = self.directory / f"{session_id}.json"
        if path.exists():
            path.unlink()
            return True
        return False
