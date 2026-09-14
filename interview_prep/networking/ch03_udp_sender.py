"""UDP sender and datagram framing."""
import socket


def send(message: str, host: str = "127.0.0.1", port: int = 9) -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        return sock.sendto(message.encode(), (host, port))


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("127.0.0.1", 0))
    receiver_port = sock.getsockname()[1]
    sent = send("datagram", port=receiver_port)
    data, _ = sock.recvfrom(1024)
    assert data == b"datagram" and sent == 8
    sock.close()
    print("udp send ok")
