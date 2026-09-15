"""Build and inspect ICMP error/echo messages without raw sockets."""
import struct

TYPES = {0: "echo-reply", 3: "destination-unreachable", 8: "echo-request",
         11: "time-exceeded"}


def build_echo(identifier: int, sequence: int, payload: bytes = b"") -> bytes:
    header = struct.pack("!BBHHH", 8, 0, 0, identifier, sequence)
    packet = header + payload
    return packet[:2] + struct.pack("!H", checksum(packet)) + packet[4:]


def checksum(data: bytes) -> int:
    if len(data) % 2:
        data += b"\x00"
    total = sum((data[i] << 8) + data[i + 1] for i in range(0, len(data), 2))
    while total >> 16:
        total = (total & 0xFFFF) + (total >> 16)
    return ~total & 0xFFFF


def describe(packet: bytes) -> str:
    type_, code, _, identifier, sequence = struct.unpack("!BBHHH", packet[:8])
    return f"{TYPES.get(type_, type_)} code={code} id={identifier} seq={sequence}"


if __name__ == "__main__":
    packet = build_echo(42, 7, b"ping")
    assert describe(packet) == "echo-request code=0 id=42 seq=7"
    print("icmp ok")
