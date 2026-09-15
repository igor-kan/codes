"""Send and parse an HTTP response over a raw socket (loopback only)."""
import socket


def build_request(host: str, path: str = "/") -> bytes:
    return (
        f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
    ).encode()


def parse_response(raw: bytes) -> tuple[int, dict[str, str], bytes]:
    header_block, _, body = raw.partition(b"\r\n\r\n")
    lines = header_block.decode(errors="replace").split("\r\n")
    status = int(lines[0].split(" ")[1])
    headers = dict(
        line.split(": ", 1) for line in lines[1:] if ": " in line
    )
    return status, headers, body


if __name__ == "__main__":
    raw = b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 2\r\n\r\nhi"
    status, headers, body = parse_response(raw)
    assert status == 200 and headers["Content-Type"] == "text/plain" and body == b"hi"
    print("http parsing ok")
