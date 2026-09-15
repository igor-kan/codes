# UDP: User Datagram Protocol

Connectionless, best-effort datagram transport.

## Header (8 bytes)

| Field | Size |
|:---|:---|
| Source port | 2 bytes |
| Destination port | 2 bytes |
| Length | 2 bytes |
| Checksum | 2 bytes |

## Properties

- No handshake, no ordering, no retransmission, no congestion control.
- Messages preserve boundaries; datagrams may be lost, duplicated, reordered.
- Checksum is optional in IPv4 (mandatory in IPv6).

## When to use

- DNS, DHCP, streaming media, online games, telemetry.
- Any case where low latency matters more than reliability, and the application
  can tolerate or repair loss (QUIC builds reliability atop UDP).

## Adding reliability

Applications implement their own ARQ, sequencing and congestion control, or use
a library (QUIC, RTP/RTCP, KCP).
