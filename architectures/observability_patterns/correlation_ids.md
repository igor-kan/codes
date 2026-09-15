# Correlation IDs

A unique identifier per request/trace that ties together logs, metrics, and
events across services.

## Practices

- Generate at the edge (gateway) if absent; propagate on every hop.
- Include in all log records and error payloads.
- Return to clients for support (in a header, not a leaky body).
- Keep opaque, bounded, and non-sensitive.

Related: Tracing, Structured Logging, Envelope Wrapper.
