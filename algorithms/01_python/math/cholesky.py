"""
Cholesky LL^T Decomposition in Python (Numerical Recipes 3rd Ed. Chapter 2.6).
"""

import math

def cholesky(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1):
            s = sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                val = A[i][i] - s
                if val <= 0:
                    raise ValueError("Matrix not positive definite")
                L[i][j] = math.sqrt(val)
            else:
                L[i][j] = (A[i][j] - s) / L[j][j]
    return L

if __name__ == "__main__":
    A = [
        [4, 12, -16],
        [12, 37, -43],
        [-16, -43, 98]
    ]
    L = cholesky(A)
    assert abs(L[0][0] - 2.0) < 1e-6
    print("Python Cholesky verified.")
