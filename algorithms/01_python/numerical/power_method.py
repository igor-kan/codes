"""Power iteration for the dominant eigenvalue (Numerical Recipes 11.1)."""
def power_method(matrix, tolerance=1e-12, max_iterations=1000):
    n = len(matrix)
    vector = [1.0] * n
    eigenvalue = 0.0
    for _ in range(max_iterations):
        product = [sum(matrix[i][j] * vector[j] for j in range(n)) for i in range(n)]
        norm = max(abs(value) for value in product)
        vector = [value / norm for value in product]
        if abs(norm - eigenvalue) < tolerance:
            eigenvalue = norm
            break
        eigenvalue = norm
    return eigenvalue, vector


if __name__ == "__main__":
    matrix = [[4.0, 1.0], [2.0, 3.0]]
    eigenvalue, vector = power_method(matrix)
    assert abs(eigenvalue - 5.0) < 1e-9
    residual = [sum(matrix[i][j] * vector[j] for j in range(2)) - eigenvalue * vector[i] for i in range(2)]
    assert all(abs(r) < 1e-9 for r in residual)
    print("power method ok")
