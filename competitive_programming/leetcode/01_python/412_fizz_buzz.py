"""LeetCode 412 - Fizz Buzz."""
def fizz_buzz(n):
    result = []
    for value in range(1, n + 1):
        if value % 15 == 0:
            result.append("FizzBuzz")
        elif value % 3 == 0:
            result.append("Fizz")
        elif value % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(value))
    return result


if __name__ == "__main__":
    assert fizz_buzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert fizz_buzz(15)[-1] == "FizzBuzz"
    print("412 fizz buzz ok")
