"""Levenberg-Marquardt least-squares fitting (Numerical Recipes 15.5)."""
def levenberg_marquardt(model, jacobian, x_data, y_data, parameters,
                        damping=1e-3, tolerance=1e-12, max_iterations=200):
    parameters = list(parameters)
    n = len(x_data)
    for _ in range(max_iterations):
        residuals = [y_data[i] - model(x_data[i], parameters) for i in range(n)]
        jac = [jacobian(x_data[i], parameters) for i in range(n)]
        columns = len(parameters)
        jtj = [[sum(jac[i][a] * jac[i][b] for i in range(n)) for b in range(columns)] for a in range(columns)]
        jtr = [sum(jac[i][a] * residuals[i] for i in range(n)) for a in range(columns)]
        updated = [[jtj[a][b] + (damping if a == b else 0.0) for b in range(columns)] for a in range(columns)]
        delta = _solve(updated, jtr)
        candidate = [parameters[i] + delta[i] for i in range(columns)]
        cost = sum(r * r for r in residuals)
        candidate_cost = sum((y_data[i] - model(x_data[i], candidate)) ** 2 for i in range(n))
        if candidate_cost < cost:
            parameters = candidate
            damping = max(damping / 10.0, 1e-15)
            if sum(abs(d) for d in delta) < tolerance:
                break
        else:
            damping *= 10.0
    return parameters


def _solve(matrix, rhs):
    n = len(rhs)
    a = [row[:] + [rhs[i]] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(a[r][col]))
        a[col], a[pivot] = a[pivot], a[col]
        for r in range(col + 1, n):
            factor = a[r][col] / a[col][col]
            for k in range(col, n + 1):
                a[r][k] -= factor * a[col][k]
    x = [0.0] * n
    for r in range(n - 1, -1, -1):
        x[r] = (a[r][n] - sum(a[r][k] * x[k] for k in range(r + 1, n))) / a[r][r]
    return x


if __name__ == "__main__":
    xs = [0.0, 1.0, 2.0, 3.0, 4.0]
    ys = [1.0 + 2.0 * x + 3.0 * x * x for x in xs]
    model = lambda x, p: p[0] + p[1] * x + p[2] * x * x
    jacobian = lambda x, p: [1.0, x, x * x]
    fitted = levenberg_marquardt(model, jacobian, xs, ys, [0.0, 0.0, 0.0])
    assert abs(fitted[0] - 1.0) < 1e-6 and abs(fitted[1] - 2.0) < 1e-6 and abs(fitted[2] - 3.0) < 1e-6
    print("levenberg marquardt ok")
