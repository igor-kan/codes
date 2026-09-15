"""LZW compression and decompression."""
def compress(text: str) -> tuple[list[int], dict[str, int]]:
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    result = []
    current = ""
    for ch in text:
        combined = current + ch
        if combined in dictionary:
            current = combined
        else:
            result.append(dictionary[current])
            dictionary[combined] = next_code
            next_code += 1
            current = ch
    if current:
        result.append(dictionary[current])
    return result, dictionary


def decompress(codes: list[int]) -> str:
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256
    result = []
    previous = chr(codes[0])
    result.append(previous)
    for code in codes[1:]:
        entry = dictionary.get(code, previous + previous[0])
        result.append(entry)
        dictionary[next_code] = previous + entry[0]
        next_code += 1
        previous = entry
    return "".join(result)


if __name__ == "__main__":
    text = "TOBEORNOTTOBEORTOBEORNOT"
    codes, _ = compress(text)
    assert decompress(codes) == text
    print("lzw ok")
