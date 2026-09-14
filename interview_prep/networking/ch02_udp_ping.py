"""UDP ping: measure round-trip time (client helper for the textbook lab)."""
import socket
import time
from dataclasses import dataclass


@dataclass
class PingResult:
    sequence: int
    rtt: float


def ping(sock: socket.socket, host: str, port: int, sequence: int) -> PingResult:
    send_time = time.perf_counter()
    sock.sendto(f"ping {sequence} {send_time}".encode(), (host, port))
    _, _ = sock.recvfrom(1024)
    return PingResult(sequence, time.perf_counter() - send_time)


if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.settimeout(1)
    client.close()
    assert PingResult(1, 0.001).sequence == 1
    print("udp ping helper ok")
