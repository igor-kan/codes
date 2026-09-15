# Metrics

Numeric aggregates sampled over time, cheap to store and query.

## Types

- **Counter:** monotonic totals (requests).
- **Gauge:** instantaneous value (queue depth).
- **Histogram/summary:** distributions (latency percentiles).

## Golden signals

Latency, traffic, errors, saturation.

## Practices

- Use labels judiciously (avoid high cardinality).
- Track SLOs with error budgets and alert on burn rate.
- Record RED/USE metrics per service and resource.

Related: Prometheus, Tracing, SLOs.
