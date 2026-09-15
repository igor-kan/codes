"""Publish/Subscribe with topic subscriptions."""
from collections import defaultdict
from collections.abc import Callable


class EventBus:
    def __init__(self) -> None:
        self.subscribers: dict[str, list[Callable[[dict], None]]] = defaultdict(list)

    def subscribe(self, topic: str, handler: Callable[[dict], None]) -> None:
        self.subscribers[topic].append(handler)

    def publish(self, topic: str, message: dict) -> None:
        for handler in self.subscribers.get(topic, []):
            handler(message)


if __name__ == "__main__":
    bus = EventBus()
    received: list[str] = []
    bus.subscribe("orders", lambda m: received.append(f"billing:{m['id']}"))
    bus.subscribe("orders", lambda m: received.append(f"analytics:{m['id']}"))
    bus.publish("orders", {"id": 7})
    assert received == ["billing:7", "analytics:7"]
    print("publish/subscribe ok")
