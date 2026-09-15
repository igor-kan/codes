"""Simplified AES (S-AES) for teaching, 16-bit blocks."""
SBOX = [0x9, 0x4, 0xA, 0xB, 0xD, 0x1, 0x8, 0x5, 0x6, 0x2, 0x0, 0x3, 0xC, 0xE, 0xF, 0x7]
INV_SBOX = [SBOX.index(i) for i in range(16)]


def _sub_word(word: int) -> int:
    result = 0
    for shift in (12, 8, 4, 0):
        nibble = (word >> shift) & 0xF
        result |= SBOX[nibble] << shift
    return result


def _rot_word(word: int) -> int:
    return ((word << 4) | (word >> 4)) & 0xFFFF


def key_expansion(key: int) -> list[int]:
    rcon = [0x80, 0x30]
    words = [key]
    for i in range(2):
        temp = _sub_word(_rot_word(words[-1])) ^ (rcon[i] << 8)
        words.append(words[-1] ^ temp)
    return words


def _add_round_key(state: int, key: int) -> int:
    return state ^ key


def _shift_rows(state: int) -> int:
    high = (state >> 8) & 0xFF
    low = state & 0xFF
    high = ((high << 4) | (high >> 4)) & 0xFF
    return (high << 8) | low


def encrypt(block: int, key: int) -> int:
    words = key_expansion(key)
    state = block ^ words[0]
    for word in words[1:]:
        state = _sub_word(state) ^ word
    return state


def decrypt(block: int, key: int) -> int:
    words = key_expansion(key)
    state = block
    for word in reversed(words[1:]):
        state = _inv_sub(state ^ word)
    return state ^ words[0]


def _inv_sub(state: int) -> int:
    result = 0
    for shift in (12, 8, 4, 0):
        result |= INV_SBOX[(state >> shift) & 0xF] << shift
    return result


if __name__ == "__main__":
    key = 0x2D55
    block = 0x1234
    assert decrypt(encrypt(block, key), key) == block
    print("simplified aes ok")
