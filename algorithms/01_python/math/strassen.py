from typing import List

Matrix = List[List[float]]


def add_matrix(A: Matrix, B: Matrix) -> Matrix:
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]


def sub_matrix(A: Matrix, B: Matrix) -> Matrix:
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]


def strassen(A: Matrix, B: Matrix) -> Matrix:
    n = len(A)
    if n <= 2:
        # Base case standard multiply
        C = [[0.0] * n for _ in range(n)]
        for i in range(n):
            for k in range(n):
                for j in range(n):
                    C[i][j] += A[i][k] * B[k][j]
        return C

    half = n // 2
    A11 = [row[:half] for row in A[:half]]
    A12 = [row[half:] for row in A[:half]]
    A21 = [row[:half] for row in A[half:]]
    A22 = [row[half:] for row in A[half:]]

    B11 = [row[:half] for row in B[:half]]
    B12 = [row[half:] for row in B[:half]]
    B21 = [row[:half] for row in B[half:]]
    B22 = [row[half:] for row in B[half:]]

    # 7 Strassen products
    M1 = strassen(add_matrix(A11, A22), add_matrix(B11, B22))
    M2 = strassen(add_matrix(A21, A22), B11)
    M3 = strassen(A11, sub_matrix(B12, B22))
    M4 = strassen(A22, sub_matrix(B21, B11))
    M5 = strassen(add_matrix(A11, A12), B22)
    M6 = strassen(sub_matrix(A21, A11), add_matrix(B11, B12))
    M7 = strassen(sub_matrix(A12, A22), add_matrix(B21, B22))

    # Recombine sub-matrices
    C11 = add_matrix(sub_matrix(add_matrix(M1, M4), M5), M7)
    C12 = add_matrix(M3, M5)
    C21 = add_matrix(M2, M4)
    C22 = add_matrix(add_matrix(sub_matrix(M1, M2), M3), M6)

    C = []
    for i in range(half):
        C.append(C11[i] + C12[i])
    for i in range(half):
        C.append(C21[i] + C22[i])
    return C


if __name__ == "__main__":
    A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 1, 2, 3], [4, 5, 6, 7]]
    B = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    C = strassen(A, B)
    assert C == A
    print("[Python Strassen] Strassen divide-and-conquer verified against identity.")
