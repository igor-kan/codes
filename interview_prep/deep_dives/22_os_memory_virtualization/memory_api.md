# Memory API

## Stack vs heap

- **Stack:** automatic storage, LIFO, fast, limited size.
- **Heap:** explicit allocation (`malloc`/`free`, `new`/`delete`), flexible.

## Common pitfalls

- Memory leaks (forgot `free`).
- Use-after-free and double free.
- Buffer overflows.
- Uninitialized reads.

## Underlying calls (Linux)

- `brk`/`sbrk` grow the heap segment.
- `mmap` maps anonymous or file-backed regions.
- `munmap` unmaps; page faults populate pages lazily.

## Tools

- AddressSanitizer, Valgrind, Electric Fence.
- `malloc_usable_size`, arenas and `mallopt` tuning.

## Language support

RAII in C++, ownership in Rust, garbage collection in managed languages, and
arena/region allocators for performance.
