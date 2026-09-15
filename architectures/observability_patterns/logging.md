# Structured Logging

Emit logs as machine-parseable records (JSON) with consistent fields.

## Fields to standardize

`timestamp`, `level`, `service`, `trace_id`, `span_id`, `user_id`, `event`,
`duration_ms`, `error`.

## Practices

- Log at boundaries; avoid logging inside tight loops.
- Never log secrets, tokens, or PII.
- Use levels meaningfully (ERROR = actionable).
- Sample high-volume debug logs; keep errors complete.

Related: Tracing, Correlation IDs, PII Handling.
