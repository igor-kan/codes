"""Common bit manipulation tricks."""

from typing import List


def count_set_bits(x: int) -> int:
    return bin(x).count("1")


def lowest_set_bit(x: int) -> int:
    """Isolate the lowest set bit, e.g. 12 -> 4."""
    return x & -x


def is_power_of_two(x: int) -> bool:
    return x > 0 and (x & (x - 1)) == 0


def clear_lowest_set_bit(x: int) -> int:
    return x & (x - 1)


def enumerate_subsets(mask: int) -> List[int]:
    """Enumerate all submasks of mask."""
    sub = mask
    res = []
    while True:
        res.append(sub)
        if sub == 0:
            break
        sub = (sub - 1) & mask
    return res


if __name__ == "__main__":
    assert count_set_bits(0b1011) == 3
    assert lowest_set_bit(12) == 4
    assert is_power_of_two(16)
    assert not is_power_of_two(12)
    assert clear_lowest_set_bit(12) == 8
    subs = enumerate_subsets(0b101)
    assert sorted(subs) == [0b000, 0b001, 0b100, 0b101]
    print("[Python BitManipulation] Bit tricks verified.")
