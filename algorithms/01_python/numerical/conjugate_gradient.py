"""Conjugate gradient for symmetric positive-definite systems (Numerical Recipes 2.10)."""
def conjugate_gradient(matrix: list[list[float]], rhs: list[float],
                       iterations: int = 100, tol: float = 1e-12) -> list[float]:
    n = len(rhs)
    x = [0.0] * n
    r = rhs[:]
    p = r[:]
    rs_old = sum(v * v for v in r)
    for _ in range(iterations):
        if rs_old ** 0.5 < tol:
            break
        ap = [sum(matrix[i][j] * p[j] for j in range(n)) for i in range(n)]
        alpha = rs_old / sum(p[i] * ap[i] for i in range(n))
        x = [x[i] + alpha * p[i] for i in range(n)]
        r = [r[i] - alpha * ap[i] for i in range(n)]
        rs_new = sum(v * v for v in r)
        p = [r[i] + (rs_new / rs_old) * p[i] for i in range(n)]
        rs_old = rs_new
    return x


if __name__ == "__main__":
    x = conjugate_gradient([[4, 1], [1, 3]], [1, 2])
    assert abs(x[0] - 1 / 11) < 1e-9 and abs(x[1] - 7 / 11) < 1e-9
    print("conjugate gradient ok")
