"""LeetCode 7 - Reverse Integer."""
def reverse_integer(x):
    sign = -1 if x < 0 else 1
    reversed_value = sign * int(str(abs(x))[::-1])
    return reversed_value if -(2 ** 31) <= reversed_value <= 2 ** 31 - 1 else 0


if __name__ == "__main__":
    assert reverse_integer(123) == 321
    assert reverse_integer(-123) == -321
    assert reverse_integer(120) == 21
    assert reverse_integer(1534236469) == 0
    print("7 reverse integer ok")
