import sqlite3
import os
from typing import Optional, Tuple

DB_PATH = os.getenv("CHAT_DB_PATH", os.path.join(os.path.dirname(__file__), "fintalk.sqlite3"))


def init_db() -> None:
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS chats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_message TEXT NOT NULL,
                bot_reply TEXT NOT NULL,
                mode TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """
        )


def log_chat(user_message: str, bot_reply: str, mode: Optional[str] = None) -> None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO chats(user_message, bot_reply, mode) VALUES (?,?,?)",
            (user_message, bot_reply, mode),
        )


def recent_chats(limit: int = 20) -> list[Tuple[int, str, str, Optional[str], str]]:
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.execute(
            "SELECT id, user_message, bot_reply, mode, created_at FROM chats ORDER BY id DESC LIMIT ?",
            (limit,),
        )
        return list(cur.fetchall())



