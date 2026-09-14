# WebSockets

A long-lived, full-duplex connection over a single TCP connection, established
by an HTTP/1.1 upgrade handshake.

```
GET /chat HTTP/1.1
Host: example.com
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
Sec-WebSocket-Version: 13
```

The server responds `101 Switching Protocols` with a `Sec-WebSocket-Accept`
key derived from the client key. After that, frames carry text/binary data with
opcode, mask and payload-length fields.

## When to use

- Real-time bidirectional messaging: chat, collaborative editing, live scores.
- Lower per-message overhead than repeated HTTP requests.

## Alternatives

- **Server-Sent Events (SSE):** server → client only, simpler, plain HTTP.
- **HTTP/2 push / streaming:** multiplexed but not full-duplex.
- **QUIC/WebTransport:** modern transport for games and media.
