# TCP Congestion Control

Congestion control limits how fast a sender injects data to avoid overwhelming
the network, distinct from flow control (protecting the receiver).

## Phases

1. **Slow start:** `cwnd` starts at ~1 MSS and doubles each RTT (exponential).
2. **Congestion avoidance:** after `ssthresh`, `cwnd` grows by ~1 MSS per RTT
   (AIMD — additive increase, multiplicative decrease).
3. **Fast retransmit / fast recovery:** three duplicate ACKs trigger retransmit
   without a full timeout; Reno halves `cwnd`.

## Key variables

- `cwnd`: congestion window.
- `ssthresh`: slow-start threshold.
- `rwnd`: receiver-advertised window (flow control).
- Effective window = `min(cwnd, rwnd)`.

## Variants

| Variant | Loss signal | Behavior |
|:---|:---|:---|
| Tahoe | timeout / dup ACKs | reset to slow start |
| Reno | dup ACKs | fast recovery, halve |
| CUBIC | loss | cubic growth function (Linux default) |
| BBR | bandwidth/RTT model | model-based, less loss-driven |

Also see: delay-based control, ECN, and QUIC's pluggable congestion control.
