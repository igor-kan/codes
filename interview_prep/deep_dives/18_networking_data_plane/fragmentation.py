"""IPv4 fragmentation into MTU-sized fragments."""
from dataclasses import dataclass


@dataclass
class Fragment:
    offset: int          # in 8-byte units
    more_fragments: bool
    payload: bytes


def fragment(payload: bytes, mtu: int = 1500, header_size: int = 20) -> list[Fragment]:
    max_payload = (mtu - header_size) // 8 * 8  # must be a multiple of 8
    fragments = []
    offset = 0
    while offset < len(payload):
        chunk = payload[offset:offset + max_payload]
        offset += len(chunk)
        fragments.append(Fragment(offset // 8 - len(chunk) // 8, offset < len(payload), chunk))
    return fragments


def reassemble(fragments: list[Fragment]) -> bytes:
    ordered = sorted(fragments, key=lambda f: f.offset)
    return b"".join(f.payload for f in ordered)


if __name__ == "__main__":
    data = bytes(range(256)) * 20  # 5120 bytes
    frags = fragment(data)
    assert all(len(f.payload) % 8 == 0 for f in frags[:-1])
    assert reassemble(frags) == data
    print(f"fragmented into {len(frags)} pieces")
