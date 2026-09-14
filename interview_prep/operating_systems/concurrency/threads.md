# Threads and Concurrency (OSTEP)

## Thread abstraction

A thread is an execution context within a process, sharing address space and
file descriptors but with its own registers, program counter and stack.

## Why concurrency is hard

- **Atomicity:** instructions interleave; `x += 1` is load/add/store.
- **Ordering:** compilers and CPUs reorder memory operations.
- **Data races:** unsynchronized access with at least one write.

## Synchronization primitives

- **Mutex / lock:** mutual exclusion; `lock`/`unlock`.
- **Condition variable:** wait/notify on a predicate.
- **Semaphore:** counting and signalling.
- **Barrier:** rendezvous for a group.
- **Read-write lock:** many readers or one writer.

## Correctness

- Invariants must hold for all interleavings.
- Prefer message passing or immutable data where possible.
- Test with sanitizers and stress harnesses.
