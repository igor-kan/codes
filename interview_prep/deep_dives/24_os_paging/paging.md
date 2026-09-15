# Paging

Divide the virtual address space into fixed-size **pages** and physical memory
into **frames**; a page table maps pages to frames.

## Address translation

```
virtual address = [ VPN | offset ]
physical address = [ PFN | offset ]
```

## Page-table entry bits

Valid/present, read/write/execute permissions, user/supervisor, accessed, dirty,
dirty/clean, and the physical frame number.

## Costs

- One memory access per translation (fixed by the TLB).
- Page tables consume memory: a 48-bit space with 4 KB pages needs huge tables,
  solved by multi-level tables.

## Huge pages

2 MB or 1 GB pages reduce TLB pressure and table size; good for large working
sets, at the cost of internal fragmentation.

## Page faults

Not-present accesses trap to the kernel, which loads the page (from disk/swap or
zero-fill), updates the PTE, and resumes.
