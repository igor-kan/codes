"""Transactional Outbox: publish events atomically with the domain write."""
from __future__ import annotations

import sqlite3
from dataclasses import dataclass


@dataclass
class Outbox:
    conn: sqlite3.Connection

    def setup(self) -> None:
        self.conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS users (id TEXT PRIMARY KEY, email TEXT);
            CREATE TABLE IF NOT EXISTS outbox (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                aggregate_id TEXT,
                event_type TEXT,
                payload TEXT,
                published INTEGER DEFAULT 0
            );
            """
        )

    def create_user(self, user_id: str, email: str) -> None:
        with self.conn:  # single transaction
            self.conn.execute("INSERT INTO users VALUES (?, ?)", (user_id, email))
            self.conn.execute(
                "INSERT INTO outbox (aggregate_id, event_type, payload) VALUES (?, ?, ?)",
                (user_id, "UserCreated", '{"email": "%s"}' % email),
            )

    def unpublished(self) -> list[tuple]:
        return self.conn.execute(
            "SELECT id, event_type, payload FROM outbox WHERE published = 0"
        ).fetchall()

    def mark_published(self, event_id: int) -> None:
        with self.conn:
            self.conn.execute("UPDATE outbox SET published = 1 WHERE id = ?", (event_id,))


if __name__ == "__main__":
    outbox = Outbox(sqlite3.connect(":memory:"))
    outbox.setup()
    outbox.create_user("u1", "ada@example.com")
    events = outbox.unpublished()
    print(events)
    outbox.mark_published(events[0][0])
    print("remaining:", outbox.unpublished())
