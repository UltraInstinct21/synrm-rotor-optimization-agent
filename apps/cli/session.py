"""Session state — conversation history, Motor-CAD connection, stats."""

from __future__ import annotations

import json
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from src.config import settings

SESSION_DIR = settings.PROJECT_ROOT / ".motor-deepagent"
HISTORY_DIR = SESSION_DIR / "history"


@dataclass
class SessionStats:
    """Per-session counters."""
    request_count: int = 0
    total_tokens: int = 0
    start_time: float = field(default_factory=lambda: datetime.now(timezone.utc).timestamp())


@dataclass
class Session:
    """Persistent session state across REPL restarts."""
    conversation_id: str = field(default_factory=lambda: uuid.uuid4().hex[:12])
    thread_id: str = field(default_factory=lambda: uuid.uuid4().hex[:12])
    model: str = ""
    motor_instance: Any = field(default=None, repr=False)
    stats: SessionStats = field(default_factory=SessionStats)
    history: list[dict[str, Any]] = field(default_factory=list)

    # ── Persistence ───────────────────────────────────────────────
    def save(self) -> None:
        """Persist session metadata to disk."""
        SESSION_DIR.mkdir(parents=True, exist_ok=True)
        meta = {
            "conversation_id": self.conversation_id,
            "thread_id": self.thread_id,
            "model": self.model,
            "stats": {
                "request_count": self.stats.request_count,
                "total_tokens": self.stats.total_tokens,
                "start_time": self.stats.start_time,
            },
        }
        (SESSION_DIR / "session.json").write_text(
            json.dumps(meta, indent=2), encoding="utf-8"
        )

    def save_message(self, role: str, content: str) -> None:
        """Append a message to the conversation history file."""
        HISTORY_DIR.mkdir(parents=True, exist_ok=True)
        msg = {
            "role": role,
            "content": content,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        HISTORY_DIR.mkdir(parents=True, exist_ok=True)
        history_file = HISTORY_DIR / f"{self.conversation_id}.jsonl"
        with open(history_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(msg) + "\n")

    @classmethod
    def load(cls, model: str = "") -> Session:
        """Load the last session or create a new one."""
        meta_path = SESSION_DIR / "session.json"
        if meta_path.exists():
            try:
                meta = json.loads(meta_path.read_text(encoding="utf-8"))
                stats = SessionStats(
                    request_count=meta.get("stats", {}).get("request_count", 0),
                    total_tokens=meta.get("stats", {}).get("total_tokens", 0),
                    start_time=meta.get("stats", {}).get("start_time", 0),
                )
                return cls(
                    conversation_id=meta["conversation_id"],
                    thread_id=meta["thread_id"],
                    model=model or meta.get("model", ""),
                    stats=stats,
                )
            except (json.JSONDecodeError, KeyError):
                pass
        return cls(model=model)

    def uptime_str(self) -> str:
        """Human-readable uptime."""
        elapsed = datetime.now(timezone.utc).timestamp() - self.stats.start_time
        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)
        if minutes > 60:
            hours = minutes // 60
            minutes = minutes % 60
            return f"{hours}h {minutes}m"
        return f"{minutes}m {seconds}s"