# Address Spaces

Each process sees a contiguous virtual address space; the MMU maps pages to
physical frames.

## Layout (Linux x86-64)

```
0x0000...  text (code)
           data (globals)
           heap        (grows up)
           ...
           mmap region
           ...
0x7fff...  stack       (grows down)
0xffff...  kernel
```

## Goals

- **Transparency:** the process cannot tell it is virtualized.
- **Protection:** isolation between processes and from the kernel.
- **Efficiency:** low time/space overhead via TLB and multi-level tables.

## Mechanisms

- Base and bounds (simplest), segmentation, paging.
- Page tables translated by the MMU; TLB caches translations.
- Demand paging, swap, copy-on-write, shared libraries.
