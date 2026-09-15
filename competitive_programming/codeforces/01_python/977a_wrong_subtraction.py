"""Codeforces 977A - Wrong Subtraction."""
def wrong_subtraction(number, steps):
    for _ in range(steps):
        if number % 10 == 0:
            number //= 10
        else:
            number -= 1
    return number


if __name__ == "__main__":
    assert wrong_subtraction(512, 4) == 50
    assert wrong_subtraction(1000000000, 9) == 1
    print("977A wrong subtraction ok")
