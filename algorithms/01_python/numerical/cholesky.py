"""Cholesky decomposition ``A = L Lᵀ`` for SPD matrices (Numerical Recipes 2.9)."""
import math


def cholesky(matrix: list[list[float]]) -> list[list[float]]:
    n = len(matrix)
    lower = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            total = matrix[i][j] - sum(lower[i][k] * lower[j][k] for k in range(j))
            if i == j:
                lower[i][j] = math.sqrt(total)
            else:
                lower[i][j] = total / lower[j][j]
    return lower


if __name__ == "__main__":
    a = [[4, 12, -16], [12, 37, -43], [-16, -43, 98]]
    l = cholesky(a)
    assert abs(l[0][0] - 2) < 1e-9 and abs(l[2][2] - 3) < 1e-9
    print("cholesky ok")
