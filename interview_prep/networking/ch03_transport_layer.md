# Transport Layer (Ch. 3)

## Multiplexing

Ports identify processes; a connection is the 4-tuple (src IP, src port,
dst IP, dst port).

## UDP

- Connectionless datagram: no handshake, no ordering, no retransmission.
- 8-byte header (src port, dst port, length, checksum).
- Use for DNS, media streaming, games; add reliability if needed.

## TCP

- **Connection-oriented** three-way handshake (SYN, SYN-ACK, ACK).
- **Reliable** via sequence numbers, cumulative ACKs, retransmission timers.
- **Flow control** with a receive window; **congestion control** with cwnd.
- **Ordered byte stream**; head-of-line blocking.

## Reliable data transfer

- Stop-and-wait: one outstanding frame, timeout + retransmit.
- Pipelining: go-back-N and selective repeat.
- ARQ is built on checksum, sequence number, ACK, timeout.
