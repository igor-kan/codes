"""LeetCode 191 - Number of 1 Bits."""
def number_of_1_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


if __name__ == "__main__":
    assert number_of_1_bits(11) == 3
    assert number_of_1_bits(128) == 1
    assert number_of_1_bits(4294967293) == 31
    print("191 number of 1 bits ok")
