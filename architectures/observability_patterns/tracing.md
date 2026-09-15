# Distributed Tracing

Propagate a trace context across services to reconstruct a request's path and
timing.

## Concepts

- **Trace:** end-to-end request; **span:** one unit of work.
- Context propagation via headers (W3C `traceparent`).
- Sampling (head-based or tail-based).

## Value

- Pinpoint latency bottlenecks and error sources.
- Understand cross-service dependencies.

## Practices

- Instrument at boundaries (HTTP, gRPC, DB, queues).
- Correlate traces with logs and metrics via trace IDs.
- Use OpenTelemetry for vendor-neutral instrumentation.

Related: Metrics, Logging, Correlation IDs.
