"""Roofline model: bound performance by compute or memory bandwidth."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Machine:
    peak_flops: float        # FLOP/s
    peak_bandwidth: float    # bytes/s

    @property
    def ridge_point(self) -> float:
        return self.peak_flops / self.peak_bandwidth

    def attainable(self, operational_intensity: float) -> float:
        """Arithmetic intensity = FLOPs per byte."""
        memory_bound = operational_intensity * self.peak_bandwidth
        return min(self.peak_flops, memory_bound)

    def classify(self, operational_intensity: float) -> str:
        return "compute-bound" if operational_intensity >= self.ridge_point else "memory-bound"


if __name__ == "__main__":
    gpu = Machine(peak_flops=20e12, peak_bandwidth=1.5e12)
    dense = Machine(peak_flops=1e12, peak_bandwidth=100e9)
    assert dense.classify(0.5) == "memory-bound"
    assert gpu.classify(100) == "compute-bound"
    print("ridge point:", dense.ridge_point, "FLOP/byte")
