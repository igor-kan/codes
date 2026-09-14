# High-Throughput Packet Processing

## Constraints

- Line rate: 10/40/100 Gbps means millions of packets per second per port.
- Per-packet work must fit in a few hundred cycles.
- Head-of-line blocking and lock contention kill throughput.

## Techniques

- **Batching:** process many packets per syscall/iteration.
- **Kernel bypass:** DPDK, AF_XDP, RDMA.
- **Zero-copy:** DMA to user space, no intermediate copies.
- **Flow steering:** RSS to distribute flows across cores.
- **Lock-free queues** between RX, workers and TX threads.
- **CPU affinity and NUMA-local memory.**

## Pipeline

```
NIC -> RSS -> RX ring -> flow lookup -> state update -> TX ring -> NIC
```

State (flow tables, counters) is sharded per core to avoid contention; periodic
aggregation merges per-core state.

## Observability

- Sample rather than instrument every packet.
- Track drops, backlog, and per-queue latencies.
