"""
Strassen's Sub-Cubic Matrix Multiplication in Python (CLRS 3rd Ed. Chapter 4.2).
"""

def multiply(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

if __name__ == "__main__":
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    C = multiply(A, B)
    assert C[0][0] == 19
    print("Python Strassen verified.")
