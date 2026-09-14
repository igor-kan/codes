# Zero-Copy I/O

Avoid copying data between kernel and user space (and within memory) to reduce
CPU and memory bandwidth usage.

## Techniques

- `mmap` files to read/write without copying.
- `sendfile`, `splice` and `tee` for kernel-space piping.
- `MSG_ZEROCOPY` / `SO_ZEROCOPY` for socket sends.
- DMA and pinned (page-locked) buffers.
- Shared memory between processes.

## Traditional path

```
read(): disk -> kernel page cache -> user buffer
write(): user buffer -> kernel socket buffer -> NIC
```

## Zero-copy path

```
sendfile(): disk -> kernel page cache -> NIC
```

## Caveats

- Page pinning costs and memory pressure.
- Completion notification for "zero-copy" sends (`MSG_ZEROCOPY`)
  must be handled.
- Alignment, huge pages, and IOMMU considerations.
