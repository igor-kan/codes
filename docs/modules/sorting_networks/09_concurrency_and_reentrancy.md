# Concurrency Guarantees & Reentrancy: Bitonic and Batcher Sorting Networks

## 1. Thread Safety Profile

The routines in `sorting_networks` adhere to the following concurrency classes:

- **Pure Reentrant**: All stateless functions operate strictly on caller-provided stack or heap buffers without accessing hidden global state.
- **Thread-Safe**: Multiple threads may read shared immutable state concurrently without synchronization locks.
- **Isolated Mutation**: In-place mutation routines require exclusive ownership (`&mut`) or thread-local arena allocation.

## 2. Deadlock & Race Freedom

Static analysis rules guarantee zero data races. Shared state updates employ lock-free atomic Compare-And-Swap (CAS) loops or localized critical sections guarded by exponential backoff spinlocks.
