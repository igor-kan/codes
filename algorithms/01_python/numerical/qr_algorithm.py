"""QR algorithm for eigenvalues of a symmetric matrix (Numerical Recipes 11.3)."""
import math


def qr_decomposition(matrix):
    n = len(matrix)
    q = [[0.0] * n for _ in range(n)]
    r = [[0.0] * n for _ in range(n)]
    for j in range(n):
        v = [matrix[i][j] for i in range(n)]
        for i in range(j):
            r[i][j] = sum(q[k][i] * v[k] for k in range(n))
            v = [v[k] - r[i][j] * q[k][i] for k in range(n)]
        r[j][j] = math.sqrt(sum(value * value for value in v))
        for k in range(n):
            q[k][j] = v[k] / r[j][j]
    return q, r


def qr_algorithm(matrix, iterations=1000):
    n = len(matrix)
    current = [row[:] for row in matrix]
    for _ in range(iterations):
        q, r = qr_decomposition(current)
        current = [[sum(r[i][k] * q[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    return sorted(current[i][i] for i in range(n))


if __name__ == "__main__":
    eigenvalues = qr_algorithm([[2.0, 1.0], [1.0, 2.0]])
    assert abs(eigenvalues[0] - 1.0) < 1e-6 and abs(eigenvalues[1] - 3.0) < 1e-6
    print("qr algorithm ok")
