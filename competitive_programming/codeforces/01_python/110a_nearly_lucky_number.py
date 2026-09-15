"""Codeforces 110A - Nearly Lucky Number."""
def nearly_lucky_number(number):
    count = sum(1 for digit in str(number) if digit in "47")
    return "YES" if count in (4, 7) else "NO"


if __name__ == "__main__":
    assert nearly_lucky_number(47) == "NO"
    assert nearly_lucky_number(7747774) == "YES"
    assert nearly_lucky_number(40047) == "NO"
    print("110A nearly lucky number ok")
