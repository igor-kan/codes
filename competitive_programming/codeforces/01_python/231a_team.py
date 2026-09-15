"""Codeforces 231A - Team."""
def team(problems):
    return sum(1 for a, b, c in problems if a + b + c >= 2)


if __name__ == "__main__":
    assert team([(1, 1, 0), (1, 1, 1), (1, 0, 0)]) == 2
    print("231A team ok")
