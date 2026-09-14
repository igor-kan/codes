"""TCP client with framing by newline."""
import socket


def send_lines(host: str, port: int, lines: list[str]) -> str:
    with socket.create_connection((host, port), timeout=5) as sock:
        payload = "\n".join(lines) + "\n"
        sock.sendall(payload.encode())
        sock.shutdown(socket.SHUT_WR)
        return sock.recv(65536).decode()


def frame(message: str) -> bytes:
    return (message + "\n").encode()


def unframe(buffer: bytes) -> list[str]:
    return buffer.decode().splitlines()


if __name__ == "__main__":
    assert unframe(frame("hello")) == ["hello"]
    print("tcp framing ok")
