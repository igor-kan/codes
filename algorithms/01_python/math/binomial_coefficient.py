"""Binomial coefficients with Pascal's triangle and modular computation."""
def pascal(rows: int) -> list[list[int]]:
    triangle = [[1]]
    for i in range(1, rows):
        prev = triangle[-1]
        triangle.append([1, *[prev[j - 1] + prev[j] for j in range(1, i)], 1])
    return triangle


def ncr_mod(n: int, r: int, mod: int) -> int:
    if r < 0 or r > n:
        return 0
    numerator = denominator = 1
    for i in range(r):
        numerator = numerator * (n - i) % mod
        denominator = denominator * (i + 1) % mod
    return numerator * pow(denominator, mod - 2, mod) % mod


if __name__ == "__main__":
    assert pascal(5)[4] == [1, 4, 6, 4, 1]
    assert ncr_mod(10, 3, 1_000_000_007) == 120
    print("binomial coefficient ok")
