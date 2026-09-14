def encode(strings: list[str]) -> str:
    return "".join(f"{len(s)}#{s}" for s in strings)


def decode(data: str) -> list[str]:
    result, i = [], 0
    while i < len(data):
        j = data.index("#", i)
        length = int(data[i:j])
        result.append(data[j + 1:j + 1 + length])
        i = j + 1 + length
    return result


if __name__ == "__main__":
    sample = ["neet", "code", "love", "you"]
    assert decode(encode(sample)) == sample
    print("ok")
