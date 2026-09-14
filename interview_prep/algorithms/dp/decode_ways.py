def num_decodings(s: str) -> int:
    prev, cur = 1, 0 if s[0] == "0" else 1
    for i in range(1, len(s)):
        single = cur if s[i] != "0" else 0
        double = prev if 10 <= int(s[i - 1:i + 1]) <= 26 else 0
        prev, cur = cur, single + double
    return cur


if __name__ == "__main__":
    assert num_decodings("226") == 3
    print("ok")
