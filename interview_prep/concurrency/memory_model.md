# The C++ Memory Model

## Happens-before

An operation A *happens-before* B if A is sequenced-before B in the same thread,
or A synchronizes-with B across threads. Data races occur when two threads access
the same location, at least one writes, and they are not ordered.

## Orders

| Order | Guarantee |
|:---|:---|
| `relaxed` | atomicity only; no ordering |
| `consume` | dependent reads (deprecated in practice) |
| `acquire` | later reads/writes cannot move before the load |
| `release` | earlier reads/writes cannot move after the store |
| `acq_rel` | both, for read-modify-write operations |
| `seq_cst` | a single total order over all seq_cst operations |

## Release/acquire pattern

```cpp
// producer
data = 42;
flag.store(true, std::memory_order_release);

// consumer
while (!flag.load(std::memory_order_acquire)) {}
assert(data == 42);
```

## Guidelines

- Default to `seq_cst` until measurement proves otherwise.
- Use `relaxed` for statistics counters where ordering is irrelevant.
- Prefer higher-level primitives (`mutex`, `atomic<T>`, `future`) over hand-rolled
  lock-free code; correctness is subtle and ABA/leaks are easy to introduce.
- Verify concurrent code with ThreadSanitizer (`-fsanitize=thread`).
