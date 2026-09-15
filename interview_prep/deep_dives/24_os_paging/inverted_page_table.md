# Inverted Page Tables

Instead of one page table per process, keep a **single global table** with one
entry per physical frame, keyed by (pid, virtual page).

## Lookup

- Hash (pid, vpn) to find the frame; handle collisions via chaining.
- No per-process table memory; great for large virtual spaces.
- Lookups are slower (hash + compare), so a TLB is essential.

## Trade-offs

| Aspect | Standard tables | Inverted |
|:---|:---|:---|
| Memory | proportional to virtual space | proportional to physical frames |
| Lookup | page-table walk | hash + compare |
| Sharing | shared pages easy | sharing needs multiple entries |
| Use | x86-64, ARM | PowerPC, IA-64, some RISC |

## Variants

Hashed page tables with a page-table base register and clustered tables combine
hashing with per-process roots to support sharing.
