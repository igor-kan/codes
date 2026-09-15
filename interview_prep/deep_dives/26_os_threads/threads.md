# Threads

A thread is an execution context within a process: its own registers, PC and
stack, sharing the address space and file descriptors with sibling threads.

## Why threads

- Parallelism on multicore.
- Overlap I/O with computation.
- Responsiveness in interactive programs.
- Cheaper than processes to create and context switch.

## Problems

- **Data races:** unsynchronized access with at least one write.
- **Atomicity:** high-level operations are multiple instructions.
- **Ordering:** the scheduler and memory system reorder.
- **Deadlock** and **starvation**.

## Thread models

- Kernel threads (1:1), user threads (N:1), hybrid (M:N).
- Coroutines/green threads for massive concurrency.

## API surface

`pthread_create`/`join`, C++ `std::thread`/`jthread`, Python `threading`,
Go goroutines, Java `Thread`/virtual threads.
