"""Rail fence (zig-zag) transposition cipher."""
def encrypt(text: str, rails: int) -> str:
    if rails == 1:
        return text
    rows = [[] for _ in range(rails)]
    rail, direction = 0, 1
    for ch in text:
        rows[rail].append(ch)
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction
    return "".join("".join(row) for row in rows)


def decrypt(cipher: str, rails: int) -> str:
    if rails == 1:
        return cipher
    pattern = []
    rail, direction = 0, 1
    for _ in cipher:
        pattern.append(rail)
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction
    counts = [pattern.count(r) for r in range(rails)]
    rows, index = [], 0
    for count in counts:
        rows.append(list(cipher[index:index + count]))
        index += count
    pointers = [0] * rails
    result = []
    for r in pattern:
        result.append(rows[r][pointers[r]])
        pointers[r] += 1
    return "".join(result)


if __name__ == "__main__":
    encrypted = encrypt("WEAREDISCOVEREDFLEEATONCE", 3)
    assert decrypt(encrypted, 3) == "WEAREDISCOVEREDFLEEATONCE"
    print("rail fence ok")
