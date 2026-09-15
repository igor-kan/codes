# QUIC

A modern transport built on UDP that bundles reliability, encryption and stream
multiplexing, and is the basis of HTTP/3.

## Features

- **Multiplexed streams:** independent, ordered streams within one connection;
  a loss on one stream does not block others (no TCP head-of-line blocking).
- **Integrated TLS 1.3:** handshake and transport setup in one or zero RTT.
- **Connection migration:** connections survive IP/port changes via connection
  IDs (useful on mobile).
- **Improved loss recovery:** richer acknowledgments, per-packet pacing.
- **Pluggable congestion control:** NewReno, CUBIC, BBR.

## Why userspace

Deployed over UDP so it can evolve without kernel/OS upgrades, and encrypts
almost all transport metadata.

## Costs

- More CPU than plain TCP; userspace stack overhead.
- Middleboxes may throttle or block UDP.
- Debugging is harder because traffic is encrypted.

## Use cases

HTTP/3, Google services, CDNs, and gRPC over QUIC.
