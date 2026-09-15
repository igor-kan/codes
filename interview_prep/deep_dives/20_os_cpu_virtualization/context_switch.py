"""Simulate a context switch between process register sets."""
from dataclasses import dataclass, field


@dataclass
class Process:
    pid: int
    registers: dict[str, int] = field(default_factory=dict)
    state: str = "READY"


@dataclass
class CPU:
    running: Process | None = None
    saved: dict[int, dict[str, int]] = field(default_factory=dict)

    def switch_to(self, process: Process) -> None:
        if self.running is not None:
            self.saved[self.running.pid] = dict(self.running.registers)
            self.running.state = "READY"
        process.registers = dict(self.saved.get(process.pid, process.registers))
        process.state = "RUNNING"
        self.running = process


if __name__ == "__main__":
    cpu = CPU()
    a = Process(1, {"pc": 10, "r0": 1})
    b = Process(2, {"pc": 20, "r0": 2})
    cpu.switch_to(a)
    a.registers["pc"] = 14
    cpu.switch_to(b)
    assert cpu.saved[1]["pc"] == 14 and b.state == "RUNNING"
    cpu.switch_to(a)
    assert a.registers["pc"] == 14 and a.state == "RUNNING"
    print("context switch ok")
