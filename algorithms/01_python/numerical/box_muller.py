"""Box-Muller transform for normal deviates (Numerical Recipes 7.2)."""
import math
import random


def box_muller(rng: random.Random) -> tuple[float, float]:
    u1, u2 = rng.random(), rng.random()
    radius = math.sqrt(-2.0 * math.log(u1))
    theta = 2.0 * math.pi * u2
    return radius * math.cos(theta), radius * math.sin(theta)


if __name__ == "__main__":
    rng = random.Random(0)
    samples = [box_muller(rng)[0] for _ in range(20_000)]
    mean = sum(samples) / len(samples)
    variance = sum((s - mean) ** 2 for s in samples) / len(samples)
    assert abs(mean) < 0.1 and abs(variance - 1.0) < 0.1
    print("box-muller ok")
