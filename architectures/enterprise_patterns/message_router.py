"""Message Router: decouple producers from consumers via a routing table."""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field


@dataclass
class Message:
    topic: str
    payload: dict


@dataclass
class MessageRouter:
    routes: dict[str, list[Callable[[Message], None]]] = field(default_factory=dict)

    def register(self, topic: str, handler: Callable[[Message], None]) -> None:
        self.routes.setdefault(topic, []).append(handler)

    def route(self, message: Message) -> None:
        for handler in self.routes.get(message.topic, []):
            handler(message)


if __name__ == "__main__":
    router = MessageRouter()
    router.register("orders", lambda m: print("billing", m.payload))
    router.register("orders", lambda m: print("analytics", m.payload))
    router.register("shipments", lambda m: print("logistics", m.payload))
    router.route(Message("orders", {"id": 1, "total": 42}))
    router.route(Message("shipments", {"id": 7}))
