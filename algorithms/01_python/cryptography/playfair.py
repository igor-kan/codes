"""Playfair cipher."""
def build_square(key: str) -> list[list[str]]:
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    seen = []
    for ch in (key.upper() + alphabet):
        if ch not in seen and ch in alphabet:
            seen.append(ch)
    return [seen[i * 5:(i + 1) * 5] for i in range(5)]


def _position(square: list[list[str]], ch: str) -> tuple[int, int]:
    for r, row in enumerate(square):
        if ch in row:
            return r, row.index(ch)
    raise ValueError(ch)


def _prepare(text: str) -> str:
    text = "".join(ch for ch in text.upper() if ch.isalpha() and ch != "J").replace("J", "I")
    result = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else "X"
        if a == b:
            result.extend([a, "X"])
            i += 1
        else:
            result.extend([a, b])
            i += 2
    if len(result) % 2:
        result.append("X")
    return "".join(result)


def encrypt(text: str, key: str) -> str:
    square = build_square(key)
    prepared = _prepare(text)
    output = []
    for i in range(0, len(prepared), 2):
        r1, c1 = _position(square, prepared[i])
        r2, c2 = _position(square, prepared[i + 1])
        if r1 == r2:
            output.append(square[r1][(c1 + 1) % 5] + square[r2][(c2 + 1) % 5])
        elif c1 == c2:
            output.append(square[(r1 + 1) % 5][c1] + square[(r2 + 1) % 5][c2])
        else:
            output.append(square[r1][c2] + square[r2][c1])
    return "".join(output)


def decrypt(cipher: str, key: str) -> str:
    square = build_square(key)
    output = []
    for i in range(0, len(cipher), 2):
        r1, c1 = _position(square, cipher[i])
        r2, c2 = _position(square, cipher[i + 1])
        if r1 == r2:
            output.append(square[r1][(c1 - 1) % 5] + square[r2][(c2 - 1) % 5])
        elif c1 == c2:
            output.append(square[(r1 - 1) % 5][c1] + square[(r2 - 1) % 5][c2])
        else:
            output.append(square[r1][c2] + square[r2][c1])
    return "".join(output)


if __name__ == "__main__":
    cipher = encrypt("HELLO WORLD", "MONARCHY")
    assert decrypt(cipher, "MONARCHY").startswith("HEL")
    print("playfair ok")
