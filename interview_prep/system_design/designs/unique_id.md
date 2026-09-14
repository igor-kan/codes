# Design: Distributed Unique ID Generation

## Requirements

- Globally unique, roughly time-ordered, high throughput, no coordination on
  the read path.

## Approaches

| Approach | Ordering | Notes |
|:---|:---|:---|
| UUIDv4 | random | no order, 128-bit |
| UUIDv7 / ULID | time-ordered | sortable, good default |
| DB auto-increment | ordered | single bottleneck |
| Ticket server | ordered | range allocation, SPOF |
| Snowflake | time-ordered | 41-bit time + machine + sequence |
| Segment/ranges | ordered | pre-allocate blocks |

## Snowflake layout (64-bit)

```
1 sign | 41 timestamp ms | 10 machine id | 12 sequence
```

- 4096 IDs per ms per machine; 1024 machines; ~69 years.
- Clock skew must be detected and rejected or waited out.

## Trade-offs

- Centralized clocks (TrueTime) vs local clocks with skew handling.
- Embedding metadata leaks information; hashing fixes privacy but loses order.
