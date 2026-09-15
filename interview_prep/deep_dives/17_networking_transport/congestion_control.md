# TCP Congestion Control

Regulate sending rate to avoid overwhelming the network; distinct from flow
control which protects the receiver.

## Core variables

- `cwnd`: congestion window (sender-side estimate).
- `ssthresh`: slow-start threshold.
- `rwnd`: receiver window.
- Effective window = `min(cwnd, rwnd)`.

## Reno phases

1. **Slow start:** `cwnd` doubles each RTT until `ssthresh`.
2. **Congestion avoidance:** `cwnd += 1 MSS` per RTT (additive increase).
3. **Fast retransmit/recovery:** three dup ACKs halve `cwnd` (multiplicative
   decrease), then grow linearly. Timeout resets to slow start.

## Loss vs delay signals

| Signal | Example |
|:---|:---|
| Loss-based | Reno, CUBIC — treat loss as congestion |
| Delay-based | Vegas — react to RTT growth |
| Model-based | BBR — estimate bandwidth and min RTT |

## Fairness and bufferbloat

AIMD converges toward fairness; oversized buffers cause high latency
(bufferbloat). AQM (CoDel, FQ-CoDel) and ECN mitigate it.
