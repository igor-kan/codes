"""Multi-level feedback queue with periodic priority boost."""
from dataclasses import dataclass, field


@dataclass
class Job:
    name: str
    remaining: int
    level: int = 0


class MLFQ:
    def __init__(self, quanta: list[int], boost_after: int | None = None) -> None:
        self.quanta = quanta
        self.boost_after = boost_after
        self.queues: list[list[Job]] = [[] for _ in quanta]
        self.time = 0
        self.timeline: list[tuple[int, str]] = []
        self.since_boost = 0

    def add(self, job: Job) -> None:
        self.queues[0].append(job)

    def boost(self) -> None:
        for level in range(1, len(self.queues)):
            for job in self.queues[level]:
                job.level = 0
                self.queues[0].append(job)
            self.queues[level] = []

    def run(self) -> list[tuple[int, str]]:
        while any(self.queues):
            job = next((q.pop(0) for q in self.queues if q), None)
            if job is None:
                self.time += 1
                continue
            run_time = min(self.quanta[job.level], job.remaining)
            for _ in range(run_time):
                self.timeline.append((self.time, job.name))
                self.time += 1
            self.since_boost += run_time
            job.remaining -= run_time
            if job.remaining > 0:
                job.level = min(job.level + 1, len(self.quanta) - 1)
                self.queues[job.level].append(job)
            if self.boost_after and self.since_boost >= self.boost_after:
                self.boost()
                self.since_boost = 0
        return self.timeline


if __name__ == "__main__":
    mlfq = MLFQ(quanta=[2, 4, 8], boost_after=20)
    for name, runtime in [("A", 10), ("B", 2)]:
        mlfq.add(Job(name, runtime))
    timeline = mlfq.run()
    assert timeline and timeline[0][1] == "A"
    print("mlfq first 6:", [name for _, name in timeline[:6]])
