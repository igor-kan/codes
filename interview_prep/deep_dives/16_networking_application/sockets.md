# Sockets Programming

## TCP server lifecycle

```
socket() -> bind() -> listen() -> accept() -> recv()/send() -> close()
```

## TCP client

```
socket() -> connect() -> send()/recv() -> close()
```

## UDP

```
socket(AF_INET, SOCK_DGRAM) -> sendto()/recvfrom()
```

## Blocking vs non-blocking

- **Blocking:** simplest; one thread per connection or a thread pool.
- **Non-blocking + `select`/`poll`/`epoll`/`kqueue`:** multiplex many connections.
- **Async I/O:** io_uring (Linux), IOCP (Windows) for scalability.

## Framing

TCP is a byte stream: you must frame messages yourself (length prefix,
delimiter, or self-describing format like HTTP).

## Common pitfalls

- Partial reads/writes; always loop.
- Ignoring `EINTR`/`EAGAIN`.
- Not setting timeouts; leaking file descriptors.
- Byte order: use network order (`htons`/`htonl`).
