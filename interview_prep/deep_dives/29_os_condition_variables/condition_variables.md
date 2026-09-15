# Condition Variables and Semaphores

## Condition variable

A queue of waiters plus an associated mutex; `wait` atomically releases the
lock and sleeps, `signal`/`broadcast` wake waiters.

```python
with cv:
    while not predicate():
        cv.wait()
    # predicate true
```

Always:
- Hold the lock when checking/changing state.
- Use `while`, not `if` (spurious wakeups; multiple waiters).
- Signal while holding or after releasing consistently (document it).

## Semaphores

A counter with `wait` (P) and `post` (V); can be binary (mutex) or counting.

- Binary semaphore ↔ lock.
- Counting semaphore ↔ resource pool or signalling.
- Ordering: producer `post`s an "item" semaphore the consumer `wait`s on.

## Choosing

- **Lock + CV:** state-based waiting with predicates.
- **Semaphore:** resource counting or simple signalling.
- **Queue:** when you also need buffering (often simpler and safer).
