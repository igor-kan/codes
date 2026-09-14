# Application Layer (Ch. 2)

## HTTP

- Request/response over TCP; methods GET, POST, PUT, PATCH, DELETE.
- Stateless; cookies add state; caching via `Cache-Control`/`ETag`.
- HTTP/2 multiplexes streams; HTTP/3 runs over QUIC/UDP.

## DNS

- Distributed hierarchical database: root → TLD → authoritative.
- Record types: A, AAAA, CNAME, MX, NS, TXT, SOA.
- Iterative vs recursive resolution; TTL-based caching.

## Sockets programming

- TCP: `socket` → `connect`/`bind`+`listen`+`accept` → `send`/`recv`.
- UDP: connectionless `sendto`/`recvfrom`.

## Other protocols

- SMTP/IMAP for mail, FTP, WebSocket for bidirectional, QUIC for low-latency.
