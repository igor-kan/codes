"""Codeforces 1A - Theatre Square."""
def theatre_square(n, m, a):
    return ((n + a - 1) // a) * ((m + a - 1) // a)


if __name__ == "__main__":
    assert theatre_square(6, 6, 4) == 4
    assert theatre_square(1, 1, 1) == 1
    assert theatre_square(1000000000, 1000000000, 1) == 10 ** 18
    print("1A theatre square ok")
