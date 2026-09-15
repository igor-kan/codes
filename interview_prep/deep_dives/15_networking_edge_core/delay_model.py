"""Nodal and end-to-end delay model."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Link:
    length_m: float
    rate_bps: float
    propagation_mps: float = 2.0e8
    processing_s: float = 0.0002
    queue_s: float = 0.0

    def transmission_s(self, packet_bits: int) -> float:
        return packet_bits / self.rate_bps

    def propagation_s(self) -> float:
        return self.length_m / self.propagation_mps

    def nodal_s(self, packet_bits: int) -> float:
        return (self.processing_s + self.queue_s
                + self.transmission_s(packet_bits) + self.propagation_s())


def end_to_end(links: list[Link], packet_bits: int) -> float:
    return sum(link.nodal_s(packet_bits) for link in links)


if __name__ == "__main__":
    links = [Link(1_000_000, 10e6), Link(500_000, 100e6)]
    delay = end_to_end(links, 1500 * 8)
    assert delay > 0
    print(f"end-to-end delay: {delay * 1000:.3f} ms")
