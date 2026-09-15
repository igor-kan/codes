"""Diffie-Hellman key exchange over a small prime group."""
import random

P = 23
G = 5


def keypair(seed: int) -> tuple[int, int]:
    private = random.Random(seed).randint(2, P - 2)
    return private, pow(G, private, P)


def shared(peer_public: int, private: int) -> int:
    return pow(peer_public, private, P)


if __name__ == "__main__":
    a_priv, a_pub = keypair(1)
    b_priv, b_pub = keypair(2)
    assert shared(b_pub, a_priv) == shared(a_pub, b_priv)
    print("diffie-hellman ok")
