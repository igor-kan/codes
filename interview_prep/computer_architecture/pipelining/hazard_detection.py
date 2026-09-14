"""Detect RAW data hazards in a small in-order pipeline model."""
from dataclasses import dataclass


@dataclass
class Instruction:
    mnemonic: str
    dest: str | None
    sources: tuple[str, ...]


def raw_hazards(program: list[Instruction]) -> list[tuple[int, int, str]]:
    hazards = []
    for i, instr in enumerate(program):
        # Look back up to two instructions for in-flight writes.
        for j in range(max(0, i - 2), i):
            producer = program[j]
            if producer.dest and producer.dest in instr.sources:
                hazards.append((j, i, producer.dest))
    return hazards


if __name__ == "__main__":
    program = [
        Instruction("lw", "t0", ("0(sp)",)),
        Instruction("add", "t1", ("t0", "t2")),   # RAW on t0
        Instruction("sub", "t2", ("t1", "t3")),   # RAW on t1
    ]
    hazards = raw_hazards(program)
    assert (0, 1, "t0") in hazards
    print("hazards:", hazards)
