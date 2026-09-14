# Address Spaces (OSTEP)

## The problem

Give each process the illusion of a large, private, contiguous memory space,
while multiplexing physical memory and providing isolation.

## Components

- **Code**, **heap** (grows up), **stack** (grows down), and **data**.
- **Virtual addresses** translated by the MMU to physical addresses.
- **Base and bounds:** simplest relocation; add a bound check for protection.
- **Segmentation:** base/bounds per segment (code, heap, stack).
- **Paging:** fixed-size pages and page tables; enables sharing and swap.

## Goals

- **Transparency:** the process is unaware of virtualization.
- **Efficiency:** minimal time and space overhead (TLB, multi-level tables).
- **Protection:** processes cannot access each other's memory.

## Mechanisms to know

- Page-table entries with valid, present, dirty, accessed, protection bits.
- Multi-level page tables and inverted page tables.
- TLB and its replacement policies.
- Demand paging, swap, and page-fault handling.
