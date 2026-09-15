# Proactor Pattern

Completion-based I/O: the application submits an operation and the OS performs
it asynchronously, notifying completion.

## Flow

1. Submit an asynchronous read/write (e.g. `io_uring`, IOCP, `aio_read`).
2. The kernel/DMA performs the transfer.
3. A completion event is queued; the loop drains completions and invokes
   callbacks (or resumes coroutines).

## Reactor vs proactor

| Aspect | Reactor | Proactor |
|:---|:---|:---|
| Notification | readiness | completion |
| Who does I/O | application | kernel/OS |
| Portability | select/poll/epoll | IOCP, io_uring, POSIX AIO |
| Buffers | app-owned | often kernel-owned until completion |

## Linux io_uring

- Shared ring buffers (SQ/CQ) avoid syscalls per operation.
- Supports I/O, timeouts, and even `openat`/`accept`.
- Powerful but requires careful buffer lifetime management.

## Pitfalls

- Buffer ownership until completion.
- Cancellation semantics and partial completion.
- Complexity vs. epoll in practice.
