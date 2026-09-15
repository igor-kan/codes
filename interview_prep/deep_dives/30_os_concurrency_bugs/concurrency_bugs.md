# Concurrency Bugs

## Categories

- **Atomicity violations:** interleaving breaks an invariant (`counter++`).
- **Order violations:** incorrect assumption about scheduling order.
- **Deadlock:** circular wait.
- **Livelock:** threads keep acting but make no progress.
- **Starvation:** a thread never gets a resource.
- **Race conditions:** outcome depends on timing.

## Non-deadlock bugs are common

Real systems see more atomicity and order violations than classic deadlocks.
They are harder to find because they are timing-dependent.

## Tooling

- ThreadSanitizer (`-fsanitize=thread`).
- Valgrind Helgrind/DRD.
- Model checkers (CHESS, JPF).
- Stress tests, deterministic record/replay.

## Prevention

- Minimize shared mutable state.
- Use immutable data and message passing.
- Encapsulate synchronization in well-tested primitives.
- Establish a lock ordering and document it.
