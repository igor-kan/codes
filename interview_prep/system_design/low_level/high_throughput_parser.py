"""A batch-oriented length-prefixed frame parser with a rolling buffer."""
from dataclasses import dataclass, field


@dataclass
class FrameParser:
    buffer: bytearray = field(default_factory=bytearray)

    def feed(self, chunk: bytes) -> list[bytes]:
        self.buffer.extend(chunk)
        frames = []
        while True:
            if len(self.buffer) < 4:
                break
            length = int.from_bytes(self.buffer[:4], "big")
            if len(self.buffer) < 4 + length:
                break
            frames.append(bytes(self.buffer[4:4 + length]))
            del self.buffer[:4 + length]
        return frames


def encode(payload: bytes) -> bytes:
    return len(payload).to_bytes(4, "big") + payload


if __name__ == "__main__":
    parser = FrameParser()
    # Partial feed exercises the rolling buffer.
    assert parser.feed(encode(b"hello")[:3]) == []
    assert parser.feed(encode(b"hello")[3:] + encode(b"world")) == [b"hello", b"world"]
    print("frame parser ok")
