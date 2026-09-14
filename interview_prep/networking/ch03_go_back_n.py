"""Go-Back-N sender simulation with a sliding window."""
from collections import deque


def go_back_n(messages: list[str], window: int, lost_indices: set[int]) -> tuple[list[str], int]:
    base = 0
    next_seq = 0
    received: list[str] = []
    transmissions = 0

    while base < len(messages):
        while next_seq < base + window and next_seq < len(messages):
            transmissions += 1
            if next_seq not in lost_indices:
                pass  # simulated ACK for this frame would advance base
            next_seq += 1
        # Simple model: retransmit the whole window until the base advances.
        if base in lost_indices:
            lost_indices = {i for i in lost_indices if i <= base}
            transmissions += 1
        received.append(messages[base])
        base += 1
        next_seq = max(next_seq, base)
    return received, transmissions


if __name__ == "__main__":
    delivered, transmissions = go_back_n(["m1", "m2", "m3"], window=2, lost_indices={1})
    assert delivered == ["m1", "m2", "m3"] and transmissions >= 3
    print("transmissions:", transmissions)
