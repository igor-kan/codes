# CAP, PACELC and Consistency Models

## CAP

During a network **P**artition you must choose **C**onsistency or **A**vailability;
without a partition you can have both.

## PACELC

If **P**, choose **A** or **C**; **E**lse choose **L**atency or **C**onsistency.

## Consistency spectrum

| Model | Guarantee |
|:---|:---|
| Linearizable | operations appear atomic in real time |
| Sequential | a total order consistent with each client |
| Causal | preserves cause→effect ordering |
| Read-your-writes | a client sees its own writes |
| Monotonic reads | never go backwards in time |
| Eventual | replicas converge given no new writes |

## In practice

- Spanner: externally consistent with bounded clock uncertainty.
- DynamoDB/Cassandra: tunable quorum consistency.
- Choose per-operation: only invariants that need it should be linearizable.
