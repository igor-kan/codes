"""Round-robin scheduling with a configurable quantum."""
from collections import deque
from dataclasses import dataclass


@dataclass
class Job:
    name: str
    remaining: int
    start: int | None = None
    completion: int | None = None


def round_robin(jobs: list[Job], quantum: int) -> list[tuple[int, str]]:
    queue = deque(jobs)
    time = 0
    timeline = []
    while queue:
        job = queue.popleft()
        if job.start is None:
            job.start = time
        run = min(quantum, job.remaining)
        for _ in range(run):
            timeline.append((time, job.name))
            time += 1
        job.remaining -= run
        if job.remaining == 0:
            job.completion = time
        else:
            queue.append(job)
    return timeline


if __name__ == "__main__":
    jobs = [Job("A", 3), Job("B", 3)]
    timeline = round_robin(jobs, quantum=2)
    assert timeline[0][1] == "A" and timeline[2][1] == "B"
    print("rr timeline:", [name for _, name in timeline])
