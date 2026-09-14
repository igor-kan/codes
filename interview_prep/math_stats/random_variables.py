"""Discrete random variables: pmf, mean, variance."""
from collections import Counter
import random


def dice_sum_distribution(trials: int = 200_000, seed: int = 0) -> dict[int, float]:
    rng = random.Random(seed)
    counts: Counter = Counter(rng.randint(1, 6) + rng.randint(1, 6) for _ in range(trials))
    return {total: count / trials for total, count in sorted(counts.items())}


def mean_variance(pmf: dict[int, float]) -> tuple[float, float]:
    mean = sum(value * p for value, p in pmf.items())
    variance = sum((value - mean) ** 2 * p for value, p in pmf.items())
    return mean, variance


if __name__ == "__main__":
    pmf = dice_sum_distribution()
    mean, variance = mean_variance(pmf)
    assert abs(mean - 7.0) < 0.05
    assert 5.5 < variance < 6.2
    print(f"mean={mean:.3f} variance={variance:.3f}")
