"""Two-phase commit: prepare then commit/abort."""
from dataclasses import dataclass, field


@dataclass
class Participant:
    name: str
    ready: bool = True
    committed: bool = False

    def prepare(self) -> bool:
        return self.ready

    def commit(self) -> None:
        self.committed = True

    def abort(self) -> None:
        self.committed = False


@dataclass
class Coordinator:
    participants: list[Participant] = field(default_factory=list)

    def execute(self) -> bool:
        if all(participant.prepare() for participant in self.participants):
            for participant in self.participants:
                participant.commit()
            return True
        for participant in self.participants:
            participant.abort()
        return False


if __name__ == "__main__":
    participants = [Participant("a"), Participant("b")]
    assert Coordinator(participants).execute()
    assert all(p.committed for p in participants)

    failing = [Participant("a"), Participant("b", ready=False)]
    assert not Coordinator(failing).execute()
    assert not any(p.committed for p in failing)
    print("two-phase commit ok")
