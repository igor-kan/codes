# Segmentation

Instead of one base/bounds pair, use a pair **per logical segment** (code, heap,
stack), each with its own base and size.

## Translation

```
offset = virtual_address - segment_base
physical = segments[segment].base + offset
if offset >= segments[segment].size: fault
```

A top-bit or explicit segment register selects the segment.

## Pros and cons

- **Pros:** sparse address spaces are efficient; per-segment protection and
  sharing; stack/heap can grow independently.
- **Cons:** external fragmentation of physical memory; complex free-space
  management; variable-size allocation.

## Free-space allocation

- First-fit, best-fit, worst-fit, buddy allocation.
- **Compaction** to coalesce holes (costly).
- Segmentation plus paging combines the benefits (e.g. x86 originally).
