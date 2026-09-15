"""Gaussian elimination to solve a linear system."""
def solve(matrix: list[list[float]], vector: list[float]) -> list[float]:
    n = len(matrix)
    a = [row[:] + [vector[i]] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(a[r][col]))
        if abs(a[pivot][col]) < 1e-12:
            raise ValueError("singular matrix")
        a[col], a[pivot] = a[pivot], a[col]
        for row in range(col + 1, n):
            factor = a[row][col] / a[col][col]
            for k in range(col, n + 1):
                a[row][k] -= factor * a[col][k]
    solution = [0.0] * n
    for row in range(n - 1, -1, -1):
        total = a[row][n] - sum(a[row][k] * solution[k] for k in range(row + 1, n))
        solution[row] = total / a[row][row]
    return solution


if __name__ == "__main__":
    result = solve([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]], [8, -11, -3])
    assert all(abs(x - y) < 1e-9 for x, y in zip(result, [2, 3, -1]))
    print("gaussian elimination ok")
