# Locked Data Structures

Wrap shared structures with locks to make them safe, choosing the granularity.

## Patterns

- **Coarse-grained:** one lock for the whole structure (simple, low concurrency).
- **Fine-grained:** lock per node/bucket (more concurrency, more complexity).
- **Hand-over-hand locking:** acquire the next node's lock before releasing the
  current one; prevents gaps but serializes traversal.
- **Approximate structures:** trade exactness for scalability (approximate
  counters).

## Structures

| Structure | Locking approach |
|:---|:---|
| Counter | one lock, or per-CPU counters summed on read |
| List | coarse lock, or hand-over-hand, or lazy locking |
| Queue | head/tail locks (two-lock queue), or lock-free MPSC/SPSC |
| Hash table | lock striping by bucket; resize needs care |

## Correctness rules

- Never hold a lock while calling user code.
- Keep critical sections small.
- Avoid nested locks unless with a global order.
- Prefer immutability and message passing when possible.
