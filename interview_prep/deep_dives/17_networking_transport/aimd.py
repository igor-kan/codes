"""Additive-increase / multiplicative-decrease congestion window simulation."""
from dataclasses import dataclass


@dataclass
class Aimd:
    cwnd: float = 1.0
    ssthresh: float = 32.0
    increase: float = 1.0
    decrease: float = 0.5

    def on_ack(self) -> None:
        if self.cwnd < self.ssthresh:
            self.cwnd *= 2          # slow start
        else:
            self.cwnd += self.increase

    def on_loss(self) -> None:
        self.ssthresh = max(self.cwnd * self.decrease, 2.0)
        self.cwnd = self.ssthresh


if __name__ == "__main__":
    aimd = Aimd()
    for _ in range(5):
        aimd.on_ack()
    peak = aimd.cwnd
    aimd.on_loss()
    assert aimd.cwnd < peak and aimd.ssthresh == max(peak * 0.5, 2.0)
    print(f"peak={peak} after loss cwnd={aimd.cwnd}")
