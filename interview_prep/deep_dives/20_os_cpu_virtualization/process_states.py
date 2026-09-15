"""A process state machine with allowed transitions."""
from dataclasses import dataclass, field
from enum import Enum, auto


class State(Enum):
    NEW = auto()
    READY = auto()
    RUNNING = auto()
    BLOCKED = auto()
    TERMINATED = auto()


TRANSITIONS = {
    (State.NEW, "admit"): State.READY,
    (State.READY, "dispatch"): State.RUNNING,
    (State.RUNNING, "interrupt"): State.READY,
    (State.RUNNING, "block"): State.BLOCKED,
    (State.RUNNING, "exit"): State.TERMINATED,
    (State.BLOCKED, "wake"): State.READY,
}


@dataclass
class Process:
    pid: int
    state: State = State.NEW
    history: list[State] = field(default_factory=list)

    def event(self, name: str) -> None:
        self.state = TRANSITIONS.get((self.state, name), self.state)
        self.history.append(self.state)


if __name__ == "__main__":
    process = Process(1)
    for event in ["admit", "dispatch", "block", "wake", "dispatch", "exit"]:
        process.event(event)
    assert process.state is State.TERMINATED
    print("states:", [s.name for s in process.history])
