"""HMAC-SHA256 built on the from-scratch digest."""
import hashlib
import hmac


def digest(data: bytes) -> bytes:
    return hashlib.sha256(data).digest()


def hmac_sha256(key: bytes, message: bytes) -> bytes:
    block = 64
    if len(key) > block:
        key = digest(key)
    key = key.ljust(block, b"\x00")
    o_key = bytes(b ^ 0x5C for b in key)
    i_key = bytes(b ^ 0x36 for b in key)
    return digest(o_key + digest(i_key + message))


if __name__ == "__main__":
    key, message = b"key", b"The quick brown fox jumps over the lazy dog"
    assert hmac_sha256(key, message) == hmac.new(key, message, hashlib.sha256).digest()
    print("hmac sha256 ok")
