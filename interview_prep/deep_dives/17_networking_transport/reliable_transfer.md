# Reliable Data Transfer (RDT)

Build reliability on an unreliable channel using checksums, sequence numbers,
ACKs, and timeouts.

## Stop-and-wait

- Send one packet, wait for ACK, timeout and retransmit.
- Handles corruption and loss; poor utilization.

## Pipelining

- **Go-Back-N:** sliding window; a loss causes retransmission of the window.
- **Selective Repeat:** receiver buffers out-of-order packets; only lost packets
  are retransmitted.

## Key mechanisms

- Checksum for bit errors.
- Sequence numbers for ordering and duplicate detection.
- ACK / NAK feedback.
- Countdown timer for loss.
- Window for flow and congestion control.

## Utilization

`utilization = (window_size × packet_size) / (RTT + transmission_time)` — the
bandwidth-delay product tells you how large the window must be to fill the pipe.
