# Leader Election

Ensure exactly one node acts as leader for a task (single writer, coordination).

## Approaches

- **Consensus-based:** Raft/Paxos (etcd, ZooKeeper, Consul) elect a leader with
  a term/epoch.
- **Bully/ring algorithms:** deterministic but sensitive to membership changes.
- **Lease-based:** leader holds a time-bound lease; must renew before expiry.

## Safety concerns

- **Split brain:** two leaders after a partition — mitigated by quorums and
  fencing tokens.
- **Clock skew:** leases must use bounded clock drift (or logical clocks).
- **Graceful handover:** release leadership on shutdown to reduce downtime.

Related: Raft, Fencing Token, Quorum.
