"""Shortest-Job-First (non-preemptive) scheduling."""
from dataclasses import dataclass


@dataclass
class Job:
    name: str
    arrival: int
    runtime: int
    start: int = 0
    completion: int = 0


def sjf(jobs: list[Job]) -> list[Job]:
    pending = sorted(jobs, key=lambda j: j.arrival)
    time = 0
    order: list[Job] = []
    while pending:
        ready = [j for j in pending if j.arrival <= time]
        if not ready:
            time = pending[0].arrival
            continue
        job = min(ready, key=lambda j: j.runtime)
        job.start = time
        time += job.runtime
        job.completion = time
        order.append(job)
        pending.remove(job)
    return order


if __name__ == "__main__":
    jobs = [Job("A", 0, 8), Job("B", 0, 4), Job("C", 0, 2)]
    order = sjf(jobs)
    assert [j.name for j in order] == ["C", "B", "A"]
    print("sjf order:", [j.name for j in order])
