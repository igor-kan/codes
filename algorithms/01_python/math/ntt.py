"""Number-theoretic transform modulo 998244353."""
MOD = 998244353
ROOT = 3


def ntt(a: list[int], invert: bool = False) -> list[int]:
    n = len(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            a[i], a[j] = a[j], a[i]
    length = 2
    while length <= n:
        wlen = pow(ROOT, (MOD - 1) // length, MOD)
        if invert:
            wlen = pow(wlen, MOD - 2, MOD)
        for i in range(0, n, length):
            w = 1
            for k in range(i, i + length // 2):
                u, v = a[k], a[k + length // 2] * w % MOD
                a[k] = (u + v) % MOD
                a[k + length // 2] = (u - v) % MOD
                w = w * wlen % MOD
        length <<= 1
    if invert:
        inv_n = pow(n, MOD - 2, MOD)
        a[:] = [x * inv_n % MOD for x in a]
    return a


def convolve(a: list[int], b: list[int]) -> list[int]:
    size = 1
    while size < len(a) + len(b) - 1:
        size <<= 1
    fa = a + [0] * (size - len(a))
    fb = b + [0] * (size - len(b))
    ntt(fa)
    ntt(fb)
    fc = [x * y % MOD for x, y in zip(fa, fb)]
    ntt(fc, invert=True)
    return fc[: len(a) + len(b) - 1]


if __name__ == "__main__":
    assert convolve([1, 2, 3], [4, 5, 6]) == [4, 13, 28, 27, 18]
    print("ntt ok")
