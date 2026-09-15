"""Matrix exponentiation to compute Fibonacci numbers."""
def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def matpow(matrix: list[list[int]], power: int) -> list[list[int]]:
    n = len(matrix)
    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    while power:
        if power & 1:
            result = matmul(result, matrix)
        matrix = matmul(matrix, matrix)
        power >>= 1
    return result


def fib(n: int) -> int:
    if n == 0:
        return 0
    return matpow([[1, 1], [1, 0]], n - 1)[0][0]


if __name__ == "__main__":
    assert [fib(i) for i in range(10)] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    print("matrix exponentiation ok")
