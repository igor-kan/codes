def mat_mul(A, B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k] == 0: continue
            for j in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def mat_pow(M, p):
    n = len(M)
    R = [[int(i==j) for j in range(n)] for i in range(n)]
    while p:
        if p & 1: R = mat_mul(R, M)
        M = mat_mul(M, M)
        p >>= 1
    return R
