"""Multi-Level Feedback Queue scheduler simulation."""
from dataclasses import dataclass, field


@dataclass
class Job:
    pid: str
    remaining: int
    level: int = 0
    used_quantum: int = 0


class MLFQ:
    def __init__(self, quanta: list[int], boost_after: int = 20) -> None:
        self.quanta = quanta
        self.boost_after = boost_after
        self.queues: list[list[Job]] = [[] for _ in quanta]
        self.time = 0
        self.timeline: list[tuple[int, str]] = []

    def add(self, job: Job) -> None:
        self.queues[0].append(job)

    def run(self) -> list[tuple[int, str]]:
        while any(self.queues):
            job = self._pick()
            if job is None:
                self.time += 1
                continue
            quantum = self.quanta[job.level]
            run_time = min(quantum, job.remaining)
            for _ in range(run_time):
                self.timeline.append((self.time, job.pid))
                self.time += 1
            job.remaining -= run_time
            if job.remaining == 0:
                continue
            job.level = min(job.level + 1, len(self.quanta) - 1)
            self.queues[job.level].append(job)
        return self.timeline

    def _pick(self) -> Job | None:
        for queue in self.queues:
            if queue:
                return queue.pop(0)
        return None


if __name__ == "__main__":
    scheduler = MLFQ(quanta=[2, 4, 8])
    for pid, runtime in [("A", 4), ("B", 2)]:
        scheduler.add(Job(pid, runtime))
    timeline = scheduler.run()
    assert timeline and timeline[0][1] == "A"
    print("first 6 slots:", [pid for _, pid in timeline[:6]])
