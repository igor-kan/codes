# Kernel Bypass

Standard socket I/O involves syscalls, copies and interrupts, limiting
throughput. Kernel bypass removes the kernel from the fast path.

## Approaches

| Technology | Mechanism | Use case |
|:---|:---|:---|
| DPDK | PMD drivers, huge pages, poll mode | packet processing appliances |
| AF_XDP | zero-copy sockets with eBPF steering | userspace networking |
| io_uring | async syscall batching | storage and networking |
| RDMA | NIC-to-NIC memory access | HPC, storage, AI clusters |
| XDP/eBPF | in-kernel hook at the driver | filtering, load balancing |
| io_uring + `MSG_ZEROCOPY` | avoid copies | high-throughput sends |

## Trade-offs

- Polling burns CPU cycles; need dedicated cores.
- Loses kernel safety/features (TCP stack, firewalling) unless reimplemented.
- Complex deployment and hardware dependence.

## When not to bypass

If you are not I/O bound, the complexity is unjustified; optimize the algorithm
and data layout first.
