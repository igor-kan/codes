# Raft

A consensus algorithm for a replicated log, designed to be understandable.

## Roles

- **Follower:** passive; responds to leaders/candidates.
- **Candidate:** requests votes after an election timeout.
- **Leader:** accepts client writes, replicates entries.

## Core pieces

1. **Leader election:** randomized timeouts; majority vote; terms prevent stale
   leaders.
2. **Log replication:** leader appends and replicates; commits when a majority
   acknowledges.
3. **Safety:** a candidate cannot win without an up-to-date log; committed
   entries survive leader changes.
4. **Membership changes:** joint consensus for reconfiguration.

## Properties

- At most one leader per term.
- Committed entries are never lost.
- Replicated state machines apply the same log in order.

Used by etcd, Consul, CockroachDB, TiKV, and many control planes.

Related: Leader Election, Quorum, Fencing Token.
