"""Bandwidth-delay product and TCP window sizing."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Path:
    bandwidth_bps: float
    rtt_s: float

    @property
    def bandwidth_delay_product_bits(self) -> float:
        return self.bandwidth_bps * self.rtt_s

    @property
    def max_throughput_single_window(self) -> float:
        return self.bandwidth_delay_product_bits

    def throughput_for_window(self, window_bits: float) -> float:
        return min(self.bandwidth_bps, window_bits / self.rtt_s)


if __name__ == "__main__":
    path = Path(bandwidth_bps=10e9, rtt_s=0.1)
    assert path.bandwidth_delay_product_bits == 1e9
    assert path.throughput_for_window(1e8) == 1e9
    print(f"BDP={path.bandwidth_delay_product_bits / 8 / 1e6:.1f} MB")
