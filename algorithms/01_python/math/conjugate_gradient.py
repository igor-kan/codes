"""
Conjugate Gradient Linear Solver in Python (Numerical Recipes 3rd Ed. Chapter 2.7).
"""

import math

def dot(a, b):
    return sum(x * y for x, y in zip(a, b))

def mat_vec(A, v):
    return [dot(row, v) for row in A]

def conjugate_gradient(A, b, tol=1e-8, max_iter=50):
    n = len(b)
    x = [0.0] * n
    r = list(b)
    p = list(r)
    rs_old = dot(r, r)

    for _ in range(max_iter):
        if math.sqrt(rs_old) < tol:
            break
        Ap = mat_vec(A, p)
        alpha = rs_old / dot(p, Ap)
        for i in range(n):
            x[i] += alpha * p[i]
            r[i] -= alpha * Ap[i]
        rs_new = dot(r, r)
        for i in range(n):
            p[i] = r[i] + (rs_new / rs_old) * p[i]
        rs_old = rs_new
    return x

if __name__ == "__main__":
    A = [[4.0, 1.0], [1.0, 3.0]]
    b = [1.0, 2.0]
    x = conjugate_gradient(A, b)
    assert abs(x[0] - 1.0 / 11.0) < 1e-5
    print("Python Conjugate Gradient verified.")
