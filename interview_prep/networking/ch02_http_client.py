"""A minimal HTTP/1.1 client over raw TCP."""
import socket


def get(host: str, path: str = "/", port: int = 80) -> str:
    with socket.create_connection((host, port), timeout=5) as sock:
        request = (
            f"GET {path} HTTP/1.1\r\n"
            f"Host: {host}\r\n"
            "Connection: close\r\n"
            "User-Agent: interview-prep\r\n\r\n"
        )
        sock.sendall(request.encode())
        chunks = []
        while data := sock.recv(4096):
            chunks.append(data)
    return b"".join(chunks).decode(errors="replace")


def parse_status(response: str) -> int:
    return int(response.split(" ", 2)[1])


if __name__ == "__main__":
    raw = "HTTP/1.1 200 OK\r\nContent-Length: 0\r\n\r\n"
    assert parse_status(raw.splitlines()[0]) == 200
    print("http client helpers ok")
