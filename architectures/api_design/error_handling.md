# API Error Handling

## Problem details (RFC 9457)

```json
{
  "type": "https://example.com/problems/validation-error",
  "title": "Validation failed",
  "status": 422,
  "detail": "The email field is not a valid address.",
  "instance": "/orders",
  "errors": [
    { "field": "email", "code": "invalid_format", "message": "must be an email" }
  ],
  "traceId": "4bf92f3577b34da6a3ce929d0e0e4736"
}
```

## Principles

- **One error shape** across the API, regardless of endpoint.
- Machine-readable `code`/`type` plus human-readable `title`/`detail`.
- Never expose stack traces, SQL, or internal identifiers.
- Include a correlation `traceId` for support and log correlation.
- Use the correct status code; do not return `200` with an error body.

## Client behavior

- Retry `429` and `5xx` with exponential backoff and jitter.
- Do not retry `4xx` (except `408`/`429`); fix the request instead.
- Respect `Retry-After` when provided.

Related: REST Guidelines, Retry with Backoff, Observability.
