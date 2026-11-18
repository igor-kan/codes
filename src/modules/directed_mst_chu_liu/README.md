# Chu-Liu / Edmonds Directed Minimum Spanning Arborescence (`directed_mst_chu_liu`)

> Category: **Graph Optimization** | Language: **C++20**

## Overview

Computes the minimum total cost of a rooted directed spanning arborescence in a weighted digraph by iteratively contracting minimum-incoming-edge cycles.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(V * E) zero-incoming cycle contraction` |
| **Space Complexity** | `O(V + E)` |

## Mathematical & Safety Invariants

- Arborescence cost is minimal across all directed spanning trees rooted at root.
- Returns -1 when any vertex is unreachable from root.

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
