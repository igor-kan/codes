def climb_stairs(n: int) -> int:
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    assert climb_stairs(5) == 8
    print("ok")
