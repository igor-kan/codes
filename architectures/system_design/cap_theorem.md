# CAP Theorem and PACELC

**CAP:** a distributed data system can guarantee at most two of *Consistency*,
*Availability*, and *Partition tolerance*. Since partitions are unavoidable,
the real choice is how to behave **during** a partition: favor consistency (CP)
or availability (AP).

**PACELC** extends this: if there is a **P**artition, choose **A** or **C**;
**E**lse (normal operation) choose **L**atency or **C**onsistency.

| System | During partition | Else | Classification |
|:---|:---|:---|:---|
| ZooKeeper / etcd | consistency | consistency | PC/EC |
| Cassandra | availability | latency | PA/EL |
| DynamoDB | tunable | tunable | PA/EL or PC/EC |
| PostgreSQL (sync) | consistency | consistency | PC/EC |

## Practical guidance

- Model around **invariants**: only make the data that needs linearizability CP.
- Use **quorums** (`R + W > N`) to tune consistency per operation.
- Prefer **idempotent** writes and **CRDTs** for AP systems to resolve conflicts.

Related: Sharding, Consensus (Raft/Paxos), Eventual Consistency.
