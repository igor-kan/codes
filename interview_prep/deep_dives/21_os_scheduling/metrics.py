"""Turnaround, response and waiting-time metrics."""
from dataclasses import dataclass


@dataclass
class Job:
    name: str
    arrival: int
    runtime: int
    start: int | None = None
    completion: int | None = None

    @property
    def turnaround(self) -> int:
        return (self.completion or 0) - self.arrival

    @property
    def response(self) -> int:
        return (self.start or 0) - self.arrival


def summarize(jobs: list[Job]) -> dict[str, float]:
    n = len(jobs)
    return {
        "avg_turnaround": sum(j.turnaround for j in jobs) / n,
        "avg_response": sum(j.response for j in jobs) / n,
    }


if __name__ == "__main__":
    jobs = [Job("A", 0, 5, 0, 5), Job("B", 0, 3, 5, 8)]
    stats = summarize(jobs)
    assert stats["avg_turnaround"] == 6.5
    print(stats)
