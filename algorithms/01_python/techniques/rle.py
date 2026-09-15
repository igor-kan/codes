"""Run-length encoding and decoding."""
def encode(text: str) -> str:
    if not text:
        return ""
    result = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result.append(f"{text[i - 1]}{count}")
            count = 1
    result.append(f"{text[-1]}{count}")
    return "".join(result)


def decode(text: str) -> str:
    result = []
    i = 0
    while i < len(text):
        char = text[i]
        i += 1
        count = ""
        while i < len(text) and text[i].isdigit():
            count += text[i]
            i += 1
        result.append(char * int(count))
    return "".join(result)


if __name__ == "__main__":
    assert encode("aaabbcccc") == "a3b2c4"
    assert decode("a3b2c4") == "aaabbcccc"
    print("rle ok")
