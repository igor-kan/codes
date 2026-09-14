"""Power iteration for the dominant eigenvalue/vector."""
import math


def matvec(matrix: list[list[float]], vector: list[float]) -> list[float]:
    return [sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix]


def normalize(vector: list[float]) -> list[float]:
    norm = math.sqrt(sum(v * v for v in vector))
    return [v / norm for v in vector]


def power_iteration(matrix: list[list[float]], iterations: int = 500) -> tuple[float, list[float]]:
    n = len(matrix)
    vector = [1.0 / math.sqrt(n)] * n
    eigenvalue = 0.0
    for _ in range(iterations):
        product = matvec(matrix, vector)
        eigenvalue = sum(product[i] * vector[i] for i in range(n))  # Rayleigh quotient
        vector = normalize(product)
    return eigenvalue, vector


if __name__ == "__main__":
    matrix = [[2, 0], [0, 3]]
    eigenvalue, vector = power_iteration(matrix)
    assert abs(eigenvalue - 3) < 1e-6
    assert abs(abs(vector[1]) - 1) < 1e-6
    print(f"dominant eigenvalue: {eigenvalue:.4f}")
