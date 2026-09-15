# The Application Layer: HTTP

## Request/response

```
GET /index.html HTTP/1.1
Host: example.com
Accept: text/html
```

```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 42
```

## Versions

- **HTTP/1.0:** one request per connection.
- **HTTP/1.1:** persistent connections, pipelining (limited), chunked encoding.
- **HTTP/2:** binary framing, multiplexed streams, header compression (HPACK).
- **HTTP/3:** runs over QUIC/UDP; no TCP head-of-line blocking.

## Caching

`Cache-Control`, `ETag`/`If-None-Match`, `Last-Modified`/`If-Modified-Since`,
`Vary`, and conditional `304 Not Modified`.

## Cookies and sessions

`Set-Cookie` with `HttpOnly`, `Secure`, `SameSite`; server-side sessions vs
signed tokens (JWT).

## REST and idempotency

Methods have semantics: GET/PUT/DELETE idempotent, POST not. Use idempotency keys
for safe retries.

## Security headers

CSP, HSTS, X-Content-Type-Options, CORS policy.
