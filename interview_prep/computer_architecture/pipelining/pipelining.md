# Pipelining

Overlap instruction execution in stages (fetch, decode, execute, memory,
write-back) so throughput approaches one instruction per cycle.

## Hazards

- **Structural:** two instructions need the same hardware.
- **Data:** RAW (true), WAR and WAW (false, handled by renaming).
- **Control:** branches change the next PC.

## Solutions

- Forwarding/bypassing for ALU results.
- Stalls and bubbles when forwarding is impossible (load-use).
- Branch prediction and speculation.
- Register renaming eliminates false dependencies.
- Reorder buffers enable out-of-order completion with in-order retirement.

## Limits

- Pipeline depth limited by latch overhead and mispredict penalties.
- Not every program has enough ILP to fill a wide pipeline.
- Power and thermal constraints cap clock scaling.
