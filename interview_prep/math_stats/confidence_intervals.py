"""Confidence intervals for a population mean."""
import math


def confidence_interval(sample_mean: float, sigma: float, n: int, z: float = 1.96) -> tuple[float, float]:
    margin = z * sigma / math.sqrt(n)
    return sample_mean - margin, sample_mean + margin


def required_sample_size(sigma: float, margin: float, z: float = 1.96) -> int:
    return math.ceil((z * sigma / margin) ** 2)


if __name__ == "__main__":
    low, high = confidence_interval(sample_mean=10, sigma=2, n=100)
    assert low < 10 < high
    assert abs((high - low) - 2 * 1.96 * 2 / 10) < 1e-9
    assert required_sample_size(sigma=2, margin=0.5) == 62
    print(f"95% CI: [{low:.2f}, {high:.2f}]")
