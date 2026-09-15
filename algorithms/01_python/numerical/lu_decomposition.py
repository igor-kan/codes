"""LU decomposition with partial pivoting (Numerical Recipes 2.3)."""
def lu_solve(matrix: list[list[float]], rhs: list[float]) -> list[float]:
    n = len(matrix)
    a = [row[:] for row in matrix]
    b = rhs[:]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(a[r][col]))
        a[col], a[pivot] = a[pivot], a[col]
        b[col], b[pivot] = b[pivot], b[col]
        for row in range(col + 1, n):
            factor = a[row][col] / a[col][col]
            for k in range(col, n):
                a[row][k] -= factor * a[col][k]
            b[row] -= factor * b[col]
    x = [0.0] * n
    for row in range(n - 1, -1, -1):
        total = b[row] - sum(a[row][k] * x[k] for k in range(row + 1, n))
        x[row] = total / a[row][row]
    return x


if __name__ == "__main__":
    x = lu_solve([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]], [8, -11, -3])
    assert all(abs(a - b) < 1e-9 for a, b in zip(x, [2, 3, -1]))
    print("lu decomposition ok")
