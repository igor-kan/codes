# Scalability Fundamentals

## Vertical vs horizontal

- **Vertical (scale up):** bigger machine; simple but bounded and expensive.
- **Horizontal (scale out):** more machines; needs statelessness, sharding,
  coordination, and observability.

## Principles

- Keep services **stateless**; push state to databases/caches.
- **Partition** data and load; avoid hotspots.
- **Asynchrony** decouples slow work (queues, events).
- **Caching** at every layer; invalidate deliberately.
- **Backpressure** protects overloaded components.

## Metrics and SLOs

- Latency percentiles (p50/p95/p99), throughput, error rate, saturation.
- Availability budgets: 99.9% ≈ 8.8 h/year; 99.99% ≈ 52 min/year.

## Bottleneck mindset

Find the constraint (CPU, memory, disk, network, lock, or dependency) and move
it. Amdahl's law: speedup is limited by the serial fraction.
