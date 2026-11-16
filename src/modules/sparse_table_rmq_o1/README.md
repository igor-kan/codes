# Static Sparse Table O(1) Idempotent Range Minimum Query Engine (`sparse_table_rmq_o1`)

> Category: **Range Query Structures** | Language: **C++20**

## Overview

Precomputes overlapping power-of-two interval minima and bit-width log2 lookup tables so arbitrary static subrange [l, r] queries answer in constant O(1) time without branching recursion.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N log N) Build, O(1) Query` |
| **Space Complexity** | `O(N log N)` |

## Mathematical & Safety Invariants

- Query(l, r) returns the exact minimum of arr[l..r] for all 0 <= l <= r < N.
- Table level k stores exact min over window [i, i + 2^k - 1] for all valid starts i.

## Module Architecture

| File | Lifecycle Role |
| :--- | :--- |
| `types.hpp` | Stage 01 |
| `errors.hpp` | Stage 02 |
| `interface.hpp` | Stage 03 |
| `core.cpp` | Stage 04 |
| `validation.cpp` | Stage 05 |
| `fast_path.cpp` | Stage 06 |
| `concurrent.cpp` | Stage 07 |
| `invariants.cpp` | Stage 08 |
| `unit_tests.cpp` | Stage 09 |
| `property_tests.cpp` | Stage 10 |
| `benchmark.cpp` | Stage 11 |
| `README.md` | Stage 12 |

## Verification & Execution Example

```text
g++ -std=c++20 -O2 -Wall -Wextra -Werror -pthread core.cpp validation.cpp fast_path.cpp concurrent.cpp invariants.cpp unit_tests.cpp -o test_bin && ./test_bin
```

---
© 2026 Igor Kan
