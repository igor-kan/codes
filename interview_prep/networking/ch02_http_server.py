"""A toy single-threaded HTTP server using the standard library."""
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802
        body = b'{"status": "ok"}'
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args) -> None:  # silence test output
        pass


def serve(port: int = 0) -> tuple[HTTPServer, int]:
    server = HTTPServer(("127.0.0.1", port), Handler)
    return server, server.server_address[1]


if __name__ == "__main__":
    import threading
    import urllib.request

    server, port = serve()
    threading.Thread(target=server.handle_request, daemon=True).start()
    with urllib.request.urlopen(f"http://127.0.0.1:{port}/") as response:
        assert response.status == 200
    server.server_close()
    print("http server works")
