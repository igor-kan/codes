# Envelope Wrapper

Wrap an application message in an **envelope** that carries infrastructure
metadata (routing, security, correlation, expiry) without changing the payload.

```
{ header: { id, correlationId, timestamp, auth }, body: <payload> }
```

## Uses

- Headers for routing and filtering.
- Security tokens and signatures.
- Correlation IDs for tracing.
- Version and content-type negotiation.

## Trade-offs

Envelope bloat, header leakage of internal details, and coupling to middleware
formats. Prefer a stable, minimal header schema.

Related: Message Translator, Correlation Identifier, Wire Tap.
