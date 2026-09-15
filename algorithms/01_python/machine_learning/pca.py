"""Principal component analysis via power iteration (no NumPy)."""
import math


def mean_vector(data: list[list[float]]) -> list[float]:
    n = len(data)
    return [sum(row[j] for row in data) / n for j in range(len(data[0]))]


def center(data: list[list[float]]) -> list[list[float]]:
    mean = mean_vector(data)
    return [[x - m for x, m in zip(row, mean)] for row in data]


def covariance(data: list[list[float]]) -> list[list[float]]:
    n = len(data)
    centered = center(data)
    d = len(centered[0])
    return [[sum(centered[i][a] * centered[i][b] for i in range(n)) / (n - 1)
             for b in range(d)] for a in range(d)]


def power_iteration(matrix: list[list[float]], iterations: int = 100) -> tuple[float, list[float]]:
    d = len(matrix)
    vector = [1 / math.sqrt(d)] * d
    for _ in range(iterations):
        product = [sum(matrix[i][j] * vector[j] for j in range(d)) for i in range(d)]
        norm = math.sqrt(sum(p * p for p in product)) or 1e-12
        vector = [p / norm for p in product]
    eigenvalue = sum(vector[i] * sum(matrix[i][j] * vector[j] for j in range(d)) for i in range(d))
    return eigenvalue, vector


if __name__ == "__main__":
    data = [[2.5, 2.4], [0.5, 0.7], [2.2, 2.9], [1.9, 2.2], [3.1, 3.0], [2.3, 2.7]]
    cov = covariance(data)
    eigenvalue, vector = power_iteration(cov)
    assert eigenvalue > 0.5
    assert abs(abs(vector[0]) - abs(vector[1])) < 0.1
    print("pca ok")
