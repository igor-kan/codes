"""Parse and build IPv4 headers."""
import struct
from dataclasses import dataclass

IPV4_HEADER = "!BBHHHBBH4s4s"


@dataclass(frozen=True)
class IPv4Header:
    version: int
    ihl: int
    tos: int
    total_length: int
    identification: int
    flags_fragment: int
    ttl: int
    protocol: int
    checksum: int
    source: str
    destination: str


def ip_to_bytes(address: str) -> bytes:
    return bytes(int(part) for part in address.split("."))


def pack(header: IPv4Header) -> bytes:
    version_ihl = (header.version << 4) | header.ihl
    return struct.pack(
        IPV4_HEADER, version_ihl, header.tos, header.total_length,
        header.identification, header.flags_fragment, header.ttl,
        header.protocol, header.checksum,
        ip_to_bytes(header.source), ip_to_bytes(header.destination),
    )


def unpack(data: bytes) -> IPv4Header:
    fields = struct.unpack(IPV4_HEADER, data[:20])
    version_ihl = fields[0]
    return IPv4Header(
        version=version_ihl >> 4, ihl=version_ihl & 0x0F, tos=fields[1],
        total_length=fields[2], identification=fields[3],
        flags_fragment=fields[4], ttl=fields[5], protocol=fields[6],
        checksum=fields[7],
        source=".".join(map(str, fields[8])),
        destination=".".join(map(str, fields[9])),
    )


if __name__ == "__main__":
    header = IPv4Header(4, 5, 0, 40, 1234, 0, 64, 6, 0, "10.0.0.1", "10.0.0.2")
    parsed = unpack(pack(header))
    assert parsed.version == 4 and parsed.ttl == 64 and parsed.protocol == 6
    assert parsed.source == "10.0.0.1" and parsed.destination == "10.0.0.2"
    print("ipv4 header ok")
