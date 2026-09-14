"""Lottery scheduling with tickets for proportional share."""
import random
from dataclasses import dataclass


@dataclass
class Process:
    pid: str
    tickets: int
    runtime: int = 0


def schedule(processes: list[Process], rounds: int, seed: int = 0) -> dict[str, int]:
    rng = random.Random(seed)
    total = sum(p.tickets for p in processes)
    for _ in range(rounds):
        winner = rng.randint(1, total)
        cumulative = 0
        for process in processes:
            cumulative += process.tickets
            if winner <= cumulative:
                process.runtime += 1
                break
    return {p.pid: p.runtime for p in processes}


if __name__ == "__main__":
    processes = [Process("A", 75), Process("B", 25)]
    result = schedule(processes, rounds=10_000, seed=42)
    assert result["A"] > result["B"]
    print(result)
