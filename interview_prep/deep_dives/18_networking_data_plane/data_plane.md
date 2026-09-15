# Network Layer: Data Plane

Per-packet forwarding from input to output port, driven by a forwarding table.

## Router components

- **Input ports:** physical link, framing, lookup, queueing.
- **Switching fabric:** memory, bus, or crossbar; moves packets to outputs.
- **Output ports:** buffering, scheduling, transmission.
- **Control plane:** routing protocols populate the forwarding table.

## Lookup

- Longest-prefix match over CIDR prefixes.
- TCAM hardware does parallel prefix matching.
- Fast paths use tries (binary/LC-trie) and caching.

## Queueing and scheduling

- FIFO, priority queueing, weighted fair queueing, round robin.
- Tail drop vs AQM (RED/CoDel) to control latency.
- Head-of-line blocking avoided with virtual output queues.

## SDN data plane

OpenFlow-style match+action tables enable programmable forwarding, with the
controller installing flows.
