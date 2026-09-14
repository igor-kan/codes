# Consistency and Consensus (DDIA Ch. 8-9)

## Ordering

- **Total order** vs **partial order** (causal).
- Lamport clocks and vector clocks capture causality.
- **Linearizability** is a strong real-time guarantee.

## Consensus

Getting nodes to agree on a value despite failures.

- **Raft:** leader election, log replication, safety, membership changes.
- **Paxos:** classic, harder to implement; Multi-Paxos for logs.
- **ZooKeeper/etcd:** consensus-backed coordination services.
- FLP result: deterministic consensus impossible with one faulty process in an
  asynchronous network; practical systems use timeouts/randomization.

## Use cases

- Leader election, distributed locks, configuration, unique IDs, atomic
  membership, and linearizable compare-and-set.

## Fencing

Use monotonically increasing tokens (fencing tokens) so stale leaders cannot
corrupt state after a pause.
