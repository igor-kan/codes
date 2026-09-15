"""Codeforces 339A - Helpful Maths."""
def helpful_maths(expression):
    return "+".join(sorted(expression.split("+")))


if __name__ == "__main__":
    assert helpful_maths("3+2+1") == "1+2+3"
    assert helpful_maths("1+1+3+1+3") == "1+1+1+3+3"
    print("339A helpful maths ok")
