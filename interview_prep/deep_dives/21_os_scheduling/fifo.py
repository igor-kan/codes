"""First-In First-Out scheduling."""
from dataclasses import dataclass


@dataclass
class Job:
    name: str
    arrival: int
    runtime: int
    start: int = 0
    completion: int = 0


def fifo(jobs: list[Job]) -> list[Job]:
    time = 0
    for job in sorted(jobs, key=lambda j: j.arrival):
        time = max(time, job.arrival)
        job.start = time
        time += job.runtime
        job.completion = time
    return jobs


if __name__ == "__main__":
    jobs = [Job("A", 0, 5), Job("B", 0, 3), Job("C", 0, 2)]
    fifo(jobs)
    assert [j.name for j in jobs] == ["A", "B", "C"]
    assert jobs[-1].completion == 10
    print("fifo avg turnaround:", sum(j.completion - j.arrival for j in jobs) / 3)
