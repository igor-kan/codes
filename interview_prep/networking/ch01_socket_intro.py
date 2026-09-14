"""Sockets: address families, socket types and byte order."""
import socket


def describe(host: str, port: int) -> str:
    infos = socket.getaddrinfo(host, port, proto=socket.IPPROTO_TCP)
    family, socktype, proto, _, sockaddr = infos[0]
    names = {socket.AF_INET: "IPv4", socket.AF_INET6: "IPv6"}
    return f"{names.get(family, family)} {socktype} {proto} {sockaddr}"


if __name__ == "__main__":
    # 'localhost' resolves without network access.
    assert "IPv" in describe("localhost", 80)
    print("socket address resolution works")
