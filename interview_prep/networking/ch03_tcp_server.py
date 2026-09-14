"""Threaded TCP echo server."""
import socket
import threading


def handle(conn: socket.socket) -> None:
    with conn:
        while data := conn.recv(4096):
            conn.sendall(data)  # echo


def serve(host: str = "127.0.0.1", port: int = 0) -> tuple[socket.socket, int]:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen()
    return server, server.getsockname()[1]


if __name__ == "__main__":
    server, port = serve()
    threading.Thread(target=lambda: handle(server.accept()[0]), daemon=True).start()
    with socket.create_connection(("127.0.0.1", port), timeout=5) as client:
        client.sendall(b"ping")
        assert client.recv(4) == b"ping"
    server.close()
    print("tcp echo works")
