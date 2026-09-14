"""DNS resolution and record types via the standard library."""
import socket


def resolve(host: str) -> list[str]:
    return sorted({info[4][0] for info in socket.getaddrinfo(host, None)})


def reverse_lookup(ip: str) -> str:
    try:
        return socket.gethostbyaddr(ip)[0]
    except (socket.herror, OSError):
        return ip


if __name__ == "__main__":
    # Documented example ranges resolve locally without external network.
    assert resolve("localhost")
    print("localhost addresses:", resolve("localhost"))
