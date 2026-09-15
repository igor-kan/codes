"""LeetCode 13 - Roman to Integer."""
VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman_to_integer(text):
    total = 0
    for i, character in enumerate(text):
        value = VALUES[character]
        if i + 1 < len(text) and value < VALUES[text[i + 1]]:
            total -= value
        else:
            total += value
    return total


if __name__ == "__main__":
    assert roman_to_integer("III") == 3
    assert roman_to_integer("LVIII") == 58
    assert roman_to_integer("MCMXCIV") == 1994
    print("13 roman to integer ok")
