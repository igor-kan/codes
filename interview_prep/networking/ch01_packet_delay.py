"""Model of nodal delay: processing + queueing + transmission + propagation."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Link:
    length_m: float
    rate_bps: float
    propagation_mps: float = 2.0e8


def transmission_delay(packet_bits: int, link: Link) -> float:
    return packet_bits / link.rate_bps


def propagation_delay(link: Link) -> float:
    return link.length_m / link.propagation_mps


def total_delay(packet_bits: int, link: Link, processing=0.0005, queueing=0.001) -> float:
    return (processing + queueing + transmission_delay(packet_bits, link)
            + propagation_delay(link))


if __name__ == "__main__":
    link = Link(length_m=1_000_000, rate_bps=10e6)
    delay = total_delay(1500 * 8, link)
    assert 0.005 < delay < 0.01
    print(f"total delay: {delay * 1000:.2f} ms")
