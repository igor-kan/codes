"""Resolve names using the system resolver (no network required for localhost)."""
import socket


def a_records(host: str) -> list[str]:
    return sorted({info[4][0] for info in socket.getaddrinfo(host, None, socket.AF_INET)})


def canonical(host: str) -> str:
    return socket.getfqdn(host)


def reverse(ip: str) -> str:
    try:
        return socket.gethostbyaddr(ip)[0]
    except (socket.herror, OSError):
        return ip


if __name__ == "__main__":
    assert a_records("localhost") == ["127.0.0.1"]
    assert reverse("127.0.0.1") in ("localhost", "127.0.0.1")
    print("dns resolver ok")
