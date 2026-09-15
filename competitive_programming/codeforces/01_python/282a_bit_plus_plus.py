"""Codeforces 282A - Bit++."""
def bit_plus_plus(operations):
    value = 0
    for operation in operations:
        value += 1 if "++" in operation else -1
    return value


if __name__ == "__main__":
    assert bit_plus_plus(["++X", "X++", "--X"]) == 1
    assert bit_plus_plus(["X++", "X++", "X++", "X--"]) == 2
    print("282A bit++ ok")
