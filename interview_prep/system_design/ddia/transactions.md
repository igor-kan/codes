# Transactions (DDIA Ch. 7)

Transactions group operations into an atomic, isolated unit with all-or-nothing
semantics.

## ACID

- **Atomicity**, **Consistency**, **Isolation**, **Durability**.

## Isolation levels

| Level | Reads | Phenomena allowed |
|:---|:---|:---|
| Read committed | committed only | lost update, write skew |
| Snapshot / repeatable read | consistent snapshot | write skew |
| Serializable | as if sequential | none |

## Concurrency control

- **2PL:** locks, deadlock detection; strong but contended.
- **MVCC:** readers see snapshots; writers create new versions.
- **SSI:** serializable snapshot isolation detects dangerous structures.
- **Serial execution:** single-threaded per partition (in-memory systems).

## Distributed transactions

- Two-phase commit (blocking), sagas (compensations), exactly-once via
  idempotency.
