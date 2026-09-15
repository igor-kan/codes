"""UDP echo over loopback."""
import socket


def echo_roundtrip(message: bytes) -> bytes:
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(("127.0.0.1", 0))
    port = server.getsockname()[1]

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
        client.sendto(message, ("127.0.0.1", port))
        data, address = server.recvfrom(65535)
        server.sendto(data, address)
        reply, _ = client.recvfrom(65535)
    server.close()
    return reply


if __name__ == "__main__":
    assert echo_roundtrip(b"ping") == b"ping"
    print("udp echo ok")
