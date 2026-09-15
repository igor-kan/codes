"""Jacobi eigenvalue algorithm for real symmetric matrices (Numerical Recipes 11.1)."""
import math


def jacobi_eigenvalue(matrix, tolerance=1e-12, max_iterations=100):
    n = len(matrix)
    a = [row[:] for row in matrix]
    vectors = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(max_iterations):
        p, q, largest = 0, 1, 0.0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(a[i][j]) > largest:
                    largest, p, q = abs(a[i][j]), i, j
        if largest < tolerance:
            break
        theta = 0.5 * math.atan2(2.0 * a[p][q], a[q][q] - a[p][p])
        c, s = math.cos(theta), math.sin(theta)
        for k in range(n):
            akp, akq = a[k][p], a[k][q]
            a[k][p] = c * akp - s * akq
            a[k][q] = s * akp + c * akq
        for k in range(n):
            apk, aqk = a[p][k], a[q][k]
            a[p][k] = c * apk - s * aqk
            a[q][k] = s * apk + c * aqk
        for k in range(n):
            vkp, vkq = vectors[k][p], vectors[k][q]
            vectors[k][p] = c * vkp - s * vkq
            vectors[k][q] = s * vkp + c * vkq
    return [a[i][i] for i in range(n)], vectors


if __name__ == "__main__":
    matrix = [[4.0, 1.0, 0.0], [1.0, 3.0, 1.0], [0.0, 1.0, 2.0]]
    eigenvalues, vectors = jacobi_eigenvalue(matrix)
    assert abs(sum(eigenvalues) - 9.0) < 1e-9
    product = 1.0
    for eigenvalue in eigenvalues:
        product *= eigenvalue
    assert abs(product - 18.0) < 1e-9
    for index, eigenvalue in enumerate(eigenvalues):
        residual = [sum(matrix[i][j] * vectors[j][index] for j in range(3)) - eigenvalue * vectors[i][index]
                    for i in range(3)]
        assert all(abs(r) < 1e-9 for r in residual)
    print("jacobi eigenvalue ok")
