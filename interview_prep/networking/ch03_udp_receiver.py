"""UDP receiver that counts datagrams."""
import socket


def receive(sock: socket.socket, count: int) -> list[bytes]:
    messages = []
    for _ in range(count):
        data, _ = sock.recvfrom(65535)
        messages.append(data)
    return messages


if __name__ == "__main__":
    receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiver.bind(("127.0.0.1", 0))
    port = receiver.getsockname()[1]

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sender:
        sender.sendto(b"hello", ("127.0.0.1", port))
    assert receive(receiver, 1) == [b"hello"]
    receiver.close()
    print("udp receive ok")
