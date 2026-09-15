# Event-Based Concurrency

Instead of one thread per connection, a single thread runs an **event loop**:
it waits for events (I/O readiness, timers, messages) and dispatches handlers.

## Model

```
while running:
    events = poll()          # block until something is ready
    for event in events:
        dispatch(event.handler)
```

## Advantages

- No data races by construction (single-threaded core).
- No per-connection thread stacks; scales to many connections.
- Explicit control over interleaving.

## Challenges

- A blocking handler stalls the whole loop.
- CPU-bound work must be offloaded to workers.
- Callback-heavy code can be hard to follow (fixed by async/await).

## Building blocks

- `select`/`poll` (portable, O(n)).
- `epoll` (Linux), `kqueue` (BSD/macOS), IOCP (Windows).
- Timers as a priority queue; signals via a self-pipe or signalfd.
