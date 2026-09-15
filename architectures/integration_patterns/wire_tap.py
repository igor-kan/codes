"""Wire Tap: copy messages to a monitoring channel without affecting flow."""
from collections.abc import Callable


class WireTap:
    def __init__(self, handler: Callable[[dict], None]) -> None:
        self._handler = handler
        self.messages: list[dict] = []

    def route(self, message: dict, destination: Callable[[dict], None]) -> None:
        destination(message)
        self._handler(message)


if __name__ == "__main__":
    tapped: list[dict] = []
    tap = WireTap(tapped.append)
    processed: list[dict] = []
    tap.route({"id": 1}, processed.append)
    assert processed == [{"id": 1}] and tapped == [{"id": 1}]
    print("wire tap ok")
