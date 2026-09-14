"""Ordinary least squares for simple linear regression."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Line:
    slope: float
    intercept: float

    def predict(self, x: float) -> float:
        return self.slope * x + self.intercept


def fit(xs: list[float], ys: list[float]) -> Line:
    n = len(xs)
    mean_x = sum(xs) / n
    mean_y = sum(ys) / n
    covariance = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
    variance = sum((x - mean_x) ** 2 for x in xs)
    slope = covariance / variance
    return Line(slope, mean_y - slope * mean_x)


def r_squared(xs: list[float], ys: list[float], line: Line) -> float:
    mean_y = sum(ys) / len(ys)
    ss_res = sum((y - line.predict(x)) ** 2 for x, y in zip(xs, ys))
    ss_tot = sum((y - mean_y) ** 2 for y in ys)
    return 1 - ss_res / ss_tot


if __name__ == "__main__":
    xs = [1, 2, 3, 4, 5]
    ys = [2, 4, 6, 8, 10]
    line = fit(xs, ys)
    assert abs(line.slope - 2) < 1e-9 and abs(line.intercept) < 1e-9
    assert abs(r_squared(xs, ys, line) - 1) < 1e-9
    print(f"y = {line.slope:.2f}x + {line.intercept:.2f}")
