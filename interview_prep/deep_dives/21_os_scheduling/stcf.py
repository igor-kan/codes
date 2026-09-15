"""Shortest-Time-to-Completion-First (preemptive) scheduling."""
from dataclasses import dataclass


@dataclass
class Job:
    name: str
    arrival: int
    remaining: int
    start: int | None = None
    completion: int | None = None


def stcf(jobs: list[Job]) -> list[Job]:
    time = 0
    finished = 0
    while finished < len(jobs):
        ready = [j for j in jobs if j.arrival <= time and j.remaining > 0]
        if not ready:
            time += 1
            continue
        job = min(ready, key=lambda j: j.remaining)
        if job.start is None:
            job.start = time
        job.remaining -= 1
        time += 1
        if job.remaining == 0:
            job.completion = time
            finished += 1
    return jobs


if __name__ == "__main__":
    jobs = [Job("A", 0, 5), Job("B", 2, 3), Job("C", 4, 1)]
    stcf(jobs)
    assert all(j.completion is not None for j in jobs)
    print("stcf avg turnaround:", sum(j.completion - j.arrival for j in jobs) / len(jobs))
