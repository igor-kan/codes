# Reactor Pattern

The reactor is the classic event-loop design: a demultiplexer dispatches ready
events to registered handlers.

## Components

- **Handle:** an OS resource (socket, file) with an associated handler.
- **Synchronous event demultiplexer:** `select`/`epoll` waits for readiness.
- **Dispatcher:** maps handles to handlers and invokes them.
- **Handlers:** non-blocking logic for read/write/accept.

## Flow

1. Handlers register interest (readable/writable).
2. Demultiplexer blocks until events are ready.
3. Dispatcher invokes the matching handler, which must not block.
4. Handler performs I/O and re-registers interest.

## Examples

- Node.js libuv, Python asyncio, Netty, Redis, nginx, libevent.

## Comparison to proactor

Reactor is **readiness-based** (you do the I/O); proactor is
**completion-based** (the OS does the I/O and notifies).
