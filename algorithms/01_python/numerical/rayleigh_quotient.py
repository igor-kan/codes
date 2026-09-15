"""Rayleigh quotient iteration for the dominant eigenpair."""
def rayleigh_quotient(matrix, vector, iterations=100):
    n = len(matrix)
    x = [value / max(abs(v) for v in vector) for value in vector]
    eigenvalue = 0.0
    for _ in range(iterations):
        product = [sum(matrix[i][j] * x[j] for j in range(n)) for i in range(n)]
        norm = max(abs(value) for value in product)
        x = [value / norm for value in product]
        numerator = sum(x[i] * sum(matrix[i][j] * x[j] for j in range(n)) for i in range(n))
        denominator = sum(value * value for value in x)
        new_eigenvalue = numerator / denominator
        if abs(new_eigenvalue - eigenvalue) < 1e-12:
            return new_eigenvalue, x
        eigenvalue = new_eigenvalue
    return eigenvalue, x


if __name__ == "__main__":
    eigenvalue, _ = rayleigh_quotient([[2, 1], [1, 2]], [1, 0])
    assert abs(eigenvalue - 3.0) < 1e-9
    print("rayleigh quotient ok")
