"""Simplified TLS-1.3-like handshake with Diffie-Hellman key exchange."""
from dataclasses import dataclass
import hashlib
import random

P = 2 ** 127 - 1  # Mersenne prime as a stand-in for the real MODP group
G = 5


def dh_keypair(seed: int) -> tuple[int, int]:
    private = random.Random(seed).randint(2, P - 2)
    public = pow(G, private, P)
    return private, public


def shared_secret(peer_public: int, private: int) -> int:
    return pow(peer_public, private, P)


def derive_key(secret: int, length: int = 16) -> str:
    return hashlib.sha256(str(secret).encode()).hexdigest()[:length]


@dataclass
class Session:
    client_key: str
    server_key: str

    @property
    def established(self) -> bool:
        return self.client_key == self.server_key


def handshake(seed_c: int = 1, seed_s: int = 2) -> Session:
    priv_c, pub_c = dh_keypair(seed_c)
    priv_s, pub_s = dh_keypair(seed_s)
    return Session(derive_key(shared_secret(pub_s, priv_c)),
                   derive_key(shared_secret(pub_c, priv_s)))


if __name__ == "__main__":
    session = handshake()
    assert session.established
    print("derived shared key:", session.client_key)
