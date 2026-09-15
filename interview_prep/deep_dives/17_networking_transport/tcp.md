# TCP: Transmission Control Protocol

Full-duplex, reliable, ordered byte stream with flow and congestion control.

## Connection lifecycle

- Three-way handshake: `SYN` → `SYN-ACK` → `ACK`.
- Teardown: `FIN`/`ACK` (both directions), `TIME_WAIT` for stray segments.

## Reliability

- Sequence and acknowledgment numbers count bytes.
- Cumulative ACKs; selective ACK (SACK) for holes.
- Fast retransmit on three duplicate ACKs; RTO timer as fallback.

## Flow control

Receiver advertises a window (`rwnd`); zero-window probes prevent deadlock.

## Congestion control

- Slow start, congestion avoidance (AIMD), fast recovery.
- Variants: Tahoe, Reno, CUBIC (Linux default), BBR (model-based).

## Header highlights

Source/dest ports, sequence/ack numbers, flags, window, checksum, options
(MSS, window scaling, SACK, timestamps).

## Head-of-line blocking

A lost byte stalls the stream; QUIC addresses this with independent streams over
UDP.
