"""Codeforces 617A - Elephant."""
def elephant(position):
    return (position + 4) // 5


if __name__ == "__main__":
    assert elephant(5) == 1
    assert elephant(12) == 3
    assert elephant(1) == 1
    print("617A elephant ok")
