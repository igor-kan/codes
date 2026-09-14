"""Monte Carlo estimation of pi and integrals."""
import random


def estimate_pi(samples: int = 200_000, seed: int = 0) -> float:
    rng = random.Random(seed)
    inside = 0
    for _ in range(samples):
        x, y = rng.random(), rng.random()
        if x * x + y * y <= 1:
            inside += 1
    return 4 * inside / samples


def integrate(f, low: float, high: float, samples: int = 200_000, seed: int = 0) -> float:
    rng = random.Random(seed)
    total = 0.0
    for _ in range(samples):
        total += f(rng.uniform(low, high))
    return (high - low) * total / samples


if __name__ == "__main__":
    pi = estimate_pi()
    assert abs(pi - 3.14159) < 0.05
    area = integrate(lambda x: x * x, 0, 1)  # integral of x^2 = 1/3
    assert abs(area - 1 / 3) < 0.01
    print(f"pi={pi:.4f} integral={area:.4f}")
