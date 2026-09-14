"""Construct and parse ICMP echo messages (without raw-socket privileges)."""
import struct

ICMP_ECHO_REQUEST = 8
ICMP_ECHO_REPLY = 0


def pack_echo(identifier: int, sequence: int, payload: bytes = b"") -> bytes:
    header = struct.pack("!BBHHH", ICMP_ECHO_REQUEST, 0, 0, identifier, sequence)
    packet = header + payload
    return packet[:2] + struct.pack("!H", checksum(packet)) + packet[4:]


def checksum(data: bytes) -> int:
    total = 0
    for i in range(0, len(data) - 1, 2):
        total += (data[i] << 8) + data[i + 1]
    if len(data) % 2:
        total += data[-1] << 8
    while total >> 16:
        total = (total & 0xFFFF) + (total >> 16)
    return ~total & 0xFFFF


def parse_echo(packet: bytes) -> tuple[int, int, int]:
    type_, code, _, identifier, sequence = struct.unpack("!BBHHH", packet[:8])
    return type_, identifier, sequence


if __name__ == "__main__":
    packet = pack_echo(1234, 1, b"ping")
    type_, identifier, sequence = parse_echo(packet)
    assert type_ == ICMP_ECHO_REQUEST and identifier == 1234 and sequence == 1
    print("icmp echo packet ok")
