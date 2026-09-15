"""Base64 encode/decode from scratch."""
import base64

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def encode(data: bytes) -> str:
    result = []
    for i in range(0, len(data), 3):
        chunk = data[i:i + 3]
        bits = int.from_bytes(chunk.ljust(3, b"\x00"), "big")
        chars = [(bits >> 18) & 63, (bits >> 12) & 63, (bits >> 6) & 63, bits & 63]
        result.extend(ALPHABET[c] for c in chars)
        if len(chunk) < 3:
            pad = 3 - len(chunk)
            result[-pad:] = ["="] * pad
    return "".join(result)


def decode(text: str) -> bytes:
    text = text.rstrip("=")
    bits = 0
    for ch in text:
        bits = (bits << 6) | ALPHABET.index(ch)
    total_bits = len(text) * 6
    nbytes = total_bits // 8
    shift = total_bits - nbytes * 8
    return (bits >> shift).to_bytes(nbytes, "big")


if __name__ == "__main__":
    for sample in [b"", b"f", b"fo", b"foo", b"foobar"]:
        assert encode(sample) == base64.b64encode(sample).decode()
        assert decode(encode(sample)) == sample
    print("base64 ok")
