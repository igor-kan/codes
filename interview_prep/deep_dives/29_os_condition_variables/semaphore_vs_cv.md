# Semaphores vs Condition Variables

| Aspect | Semaphore | Condition variable |
|:---|:---|:---|
| State | internal counter | external predicate |
| Wait | blocks if counter 0 | blocks until signalled |
| Signal | increments counter | wakes waiter(s) |
| Predicate | implicit (count) | explicit, re-checked in a loop |
| Risk | forgotten `post`, imbalance | lost wakeups, missed predicate |
| Typical use | resource pools, signalling | state-based coordination |

## Rule of thumb

- Use a **condition variable** when threads wait for a *condition* on shared
  state they manage themselves.
- Use a **semaphore** when the resource count *is* the state (e.g. N slots,
  N connections).
- Both must be paired correctly; prefer higher-level queues/futures when they
  fit, since they encode the pattern safely.

## Common pitfalls

- `if` instead of `while` around `wait` → spurious wakeup bugs.
- Signalling before the waiter sleeps without holding the lock → lost wakeup.
- Holding a lock while doing long work → convoying.
