"""Hashing, HMAC and an XOR stream cipher for demonstration."""
import hashlib
import hmac


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def authenticated(tag: bytes, message: bytes, key: bytes) -> bool:
    expected = hmac.new(key, message, hashlib.sha256).digest()
    return hmac.compare_digest(tag, expected)


def xor_stream(data: bytes, key: bytes) -> bytes:
    keystream = hashlib.shake_256(key).digest(len(data))
    return bytes(a ^ b for a, b in zip(data, keystream))


if __name__ == "__main__":
    key = b"secret-key"
    message = b"transfer 100"
    tag = hmac.new(key, message, hashlib.sha256).digest()
    assert authenticated(tag, message, key)
    ciphertext = xor_stream(message, key)
    assert xor_stream(ciphertext, key) == message
    print("crypto basics ok")
