"""CRC-32 using the standard library and a manual implementation."""
import binascii


def crc32_table() -> list[int]:
    table = []
    for byte in range(256):
        crc = byte
        for _ in range(8):
            crc = (crc >> 1) ^ 0xEDB88320 if crc & 1 else crc >> 1
        table.append(crc)
    return table


TABLE = crc32_table()


def crc32(data: bytes) -> int:
    crc = 0xFFFFFFFF
    for byte in data:
        crc = (crc >> 8) ^ TABLE[(crc ^ byte) & 0xFF]
    return crc ^ 0xFFFFFFFF


if __name__ == "__main__":
    sample = b"123456789"
    assert crc32(sample) == binascii.crc32(sample) & 0xFFFFFFFF == 0xCBF43926
    print(hex(crc32(sample)))
