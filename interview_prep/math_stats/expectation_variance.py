"""Expectation, variance, covariance and correlation."""
import math


def mean(values: list[float]) -> float:
    return sum(values) / len(values)


def variance(values: list[float]) -> float:
    m = mean(values)
    return sum((v - m) ** 2 for v in values) / len(values)


def covariance(xs: list[float], ys: list[float]) -> float:
    mx, my = mean(xs), mean(ys)
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / len(xs)


def correlation(xs: list[float], ys: list[float]) -> float:
    return covariance(xs, ys) / math.sqrt(variance(xs) * variance(ys))


if __name__ == "__main__":
    xs = [1, 2, 3, 4, 5]
    ys = [2, 4, 6, 8, 10]
    assert abs(mean(xs) - 3) < 1e-9
    assert abs(variance(xs) - 2) < 1e-9
    assert abs(correlation(xs, ys) - 1) < 1e-9
    print("moments ok")
