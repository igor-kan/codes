"""Multiplex sockets with select (portable, O(n))."""
import select
import socket


def serve_once(server: socket.socket, timeout: float = 1.0) -> list[bytes]:
    readable, _, _ = select.select([server], [], [], timeout)
    received = []
    for ready in readable:
        conn, _ = ready.accept()
        with conn:
            received.append(conn.recv(1024))
    return received


if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 0))
    server.listen()
    port = server.getsockname()[1]

    with socket.create_connection(("127.0.0.1", port), timeout=5) as client:
        client.sendall(b"hello")
        assert serve_once(server) == [b"hello"]
    server.close()
    print("select/poll ok")
