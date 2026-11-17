# Sleator-Tarjan Link-Cut Tree with Path Aggregates (`link_cut_tree_splay`)

> Category: **Dynamic Trees** | Language: **C++20**

## Overview

Implements dynamic forest maintenance via splay-backed preferred paths with lazy subtree reversal for O(log N) amortized evert, link, cut, and path-max/sum aggregation.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(log N) amortized per link, cut, and path query` |
| **Space Complexity** | `O(N)` |

## Mathematical & Safety Invariants

- After link(u, v), u and v share the same root and query_path_sum(u, v) includes both endpoints.
- Cutting an edge splits the component cleanly without corrupting lazy flip propagation.

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
