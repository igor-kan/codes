"""Saga: coordinate distributed transactions with compensating actions."""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field


@dataclass
class Step:
    name: str
    action: Callable[[], None]
    compensate: Callable[[], None]


@dataclass
class Saga:
    steps: list[Step] = field(default_factory=list)
    completed: list[Step] = field(default_factory=list)

    def add(self, step: Step) -> None:
        self.steps.append(step)

    def run(self) -> None:
        try:
            for step in self.steps:
                print(f"executing {step.name}")
                step.action()
                self.completed.append(step)
        except Exception as exc:  # noqa: BLE001
            print(f"failed at {step.name}: {exc}; compensating")
            self._compensate()

    def _compensate(self) -> None:
        for step in reversed(self.completed):
            print(f"compensating {step.name}")
            step.compensate()


if __name__ == "__main__":
    saga = Saga()
    saga.add(Step("reserve-stock", lambda: print("  stock reserved"), lambda: print("  stock released")))
    saga.add(Step("charge-card", lambda: (_ for _ in ()).throw(RuntimeError("declined")), lambda: print("  refunded")))
    saga.run()
