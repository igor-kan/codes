# Concurrency Model & Memory Ordering: codes

This document details the multi-threading model, synchronization primitives, and memory ordering guarantees enforced across `codes`.

## Memory Consistency & Ordering

We adhere strictly to sequentially consistent or acquire-release semantics to avoid hardware-level data races:

$$\text{Thread 1: Store-Release} \longrightarrow \text{Synchronizes-With} \longrightarrow \text{Thread 2: Load-Acquire}$$

- **Relaxed Ordering (`memory_order_relaxed`)**: Restricted solely to independent statistics and monotonic counters.
- **Acquire-Release (`memory_order_acquire` / `memory_order_release`)**: Used for publish-subscribe synchronization across lock-free rings and status flags.
- **Sequential Consistency (`memory_order_seq_cst`)**: Standard default for state transitions and barrier synchronizations.

## Deadlock Prevention Rules

1. **Strict Lock Hierarchy**: If multiple locks must be acquired, they must always be acquired in a globally defined lexicographical order.
2. **Non-Blocking Fallbacks**: Where possible, algorithms utilize wait-free atomic primitives or lock-free retry loops with exponential backoff.
3. **No Lock Inversion**: Callbacks and user-provided lambdas must never be invoked while holding internal synchronization locks.
