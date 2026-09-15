"""Pipes and Filters: compose processing steps into a pipeline."""
from collections.abc import Callable


def pipeline(*filters: Callable[[dict], dict | None]):
    def run(message: dict) -> dict | None:
        current: dict | None = message
        for process in filters:
            if current is None:
                break
            current = process(current)
        return current

    return run


def add_timestamp(message: dict) -> dict:
    return {**message, "timestamp": 0}


def require_total(message: dict) -> dict | None:
    return message if "total" in message else None


def apply_tax(message: dict) -> dict:
    return {**message, "total": message["total"] * 1.2}


if __name__ == "__main__":
    process = pipeline(add_timestamp, require_total, apply_tax)
    assert process({"total": 100})["total"] == 120
    assert process({}) is None
    print("pipes and filters ok")
