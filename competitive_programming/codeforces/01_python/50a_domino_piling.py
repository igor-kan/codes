"""Codeforces 50A - Domino Piling."""
def domino_piling(m, n):
    return (m * n) // 2


if __name__ == "__main__":
    assert domino_piling(2, 4) == 4
    assert domino_piling(3, 3) == 4
    print("50A domino piling ok")
