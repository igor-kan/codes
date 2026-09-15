# Network Security and TLS

## Goals

- **Confidentiality:** encryption in transit.
- **Integrity:** detect tampering (AEAD: AES-GCM, ChaCha20-Poly1305).
- **Authentication:** prove server (and optionally client) identity.

## Symmetric vs asymmetric

- Symmetric (AES) is fast; the key must be shared.
- Asymmetric (RSA, ECDH, Ed25519) solves key exchange and signatures, but is
  slower.

## TLS 1.3 handshake (1-RTT)

1. ClientHello with key share, supported versions, SNI.
2. ServerHello with its key share, certificate, Finished.
3. Both derive handshake keys via HKDF; client Finished completes.
4. Application data flows with AEAD.

0-RTT resumption is possible but replay-sensitive.

## Certificates and PKI

- X.509 certificates bind names to public keys, signed by a CA.
- Chain of trust to a root store; revocation via OCSP/CRLs.
- Certificate Transparency logs detect mis-issuance.

## Common attacks

MITM without validation, downgrade attacks, replay, session hijacking; defenses
are HSTS, certificate pinning, and forward secrecy (ephemeral keys).
