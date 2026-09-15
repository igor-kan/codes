"""Selective-repeat sliding window sender simulation."""
from dataclasses import dataclass


@dataclass
class Sender:
    window: int

    def send(self, total: int, dropped: set[int]) -> tuple[list[int], int]:
        base = 0
        next_seq = 0
        acked: set[int] = set()
        transmissions = 0
        while base < total:
            while next_seq < base + self.window and next_seq < total:
                transmissions += 1
                if next_seq not in dropped:
                    acked.add(next_seq)
                next_seq += 1
            if base in acked:
                base += 1
            else:
                transmissions += 1  # retransmit the lost frame
                acked.add(base)
        return sorted(acked), transmissions


if __name__ == "__main__":
    sender = Sender(window=4)
    acked, transmissions = sender.send(total=10, dropped={3, 7})
    assert acked == list(range(10)) and transmissions > 10
    print(f"acked={len(acked)} transmissions={transmissions}")
