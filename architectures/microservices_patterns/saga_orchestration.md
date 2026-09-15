# Saga (Orchestration)

A central orchestrator drives a multi-step transaction and runs compensating
actions if a step fails.

```
orchestrator -> step1 -> step2 -> step3
                    \-> compensate step2, step1 on failure
```

## Orchestration vs Choreography

- **Orchestration:** explicit coordinator; easier to reason about and monitor.
- **Choreography:** services react to events; looser coupling, harder to trace.

## Design rules

- Every step has a compensating action (idempotent).
- Persist saga state for recovery after crashes.
- Use timeouts and retries; avoid distributed locks.

Related: `../enterprise_patterns/saga.py`, Outbox, Idempotent Receiver.
