"""Codeforces 4A - Watermelon."""
def watermelon(weight):
    return "YES" if weight % 2 == 0 and weight > 2 else "NO"


if __name__ == "__main__":
    assert watermelon(8) == "YES"
    assert watermelon(2) == "NO"
    assert watermelon(3) == "NO"
    print("4A watermelon ok")
