"""Common distributions implemented without external libraries."""
import math
import random


def binomial_pmf(n: int, k: int, p: float) -> float:
    return math.comb(n, k) * p ** k * (1 - p) ** (n - k)


def poisson_pmf(k: int, lam: float) -> float:
    return lam ** k * math.exp(-lam) / math.factorial(k)


def normal_pdf(x: float, mu: float = 0.0, sigma: float = 1.0) -> float:
    return math.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * math.sqrt(2 * math.pi))


def sample_normal(rng: random.Random, n: int, mu: float, sigma: float) -> list[float]:
    return [rng.gauss(mu, sigma) for _ in range(n)]


if __name__ == "__main__":
    assert abs(sum(binomial_pmf(10, k, 0.5) for k in range(11)) - 1) < 1e-9
    assert abs(sum(poisson_pmf(k, 3.0) for k in range(50)) - 1) < 1e-6
    assert normal_pdf(0) > normal_pdf(3)
    print("distributions ok")
