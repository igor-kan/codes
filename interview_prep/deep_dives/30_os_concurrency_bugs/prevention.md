# Deadlock Prevention and Avoidance

## Prevention (structural)

- **Global lock ordering:** always acquire locks by a fixed rank; use a
  hierarchical mutex to detect violations.
- **One lock:** protect multiple resources with a single lock.
- **Try-lock with backoff:** release and retry instead of blocking.
- **Lock-free data structures** with atomic CAS where suitable.
- **Atomic lock acquisition:** `std::scoped_lock`/`lock()` acquire many mutexes
  without deadlock (uses try-and-backoff internally).

## Avoidance (dynamic)

- **Banker's algorithm:** grant a request only if the system stays in a safe
  state; requires declared maximum resource needs.
- **Resource ordering** combined with admission control.

## Detection and recovery

- Build a wait-for graph and detect cycles.
- Preempt a victim (rollback its work) and retry.
- Set timeouts on lock acquisition as a coarse safety net.

## Livelock and starvation

- Randomized/exponential backoff to break lockstep retries.
- Fair queues (ticket/MCS) to prevent starvation.
- Avoid holding locks while waiting on other locks.
