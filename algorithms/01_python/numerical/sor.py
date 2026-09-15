"""Successive over-relaxation (Numerical Recipes 19.5)."""
def sor(matrix: list[list[float]], rhs: list[float], omega: float = 1.1,
        iterations: int = 200, tol: float = 1e-12) -> list[float]:
    n = len(rhs)
    x = [0.0] * n
    for _ in range(iterations):
        error = 0.0
        for i in range(n):
            total = rhs[i] - sum(matrix[i][j] * x[j] for j in range(n) if j != i)
            new = (1 - omega) * x[i] + omega * total / matrix[i][i]
            error = max(error, abs(new - x[i]))
            x[i] = new
        if error < tol:
            break
    return x


if __name__ == "__main__":
    x = sor([[4, 1], [1, 3]], [1, 2])
    assert abs(x[0] - 1 / 11) < 1e-9 and abs(x[1] - 7 / 11) < 1e-9
    print("sor ok")
