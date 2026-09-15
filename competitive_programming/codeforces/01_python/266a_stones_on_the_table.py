"""Codeforces 266A - Stones on the Table."""
def stones_on_table(row):
    return sum(1 for i in range(1, len(row)) if row[i] == row[i - 1])


if __name__ == "__main__":
    assert stones_on_table("RRG") == 1
    assert stones_on_table("RRRRR") == 4
    assert stones_on_table("BRBG") == 0
    print("266A stones on the table ok")
