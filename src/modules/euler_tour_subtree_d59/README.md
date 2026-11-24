# Euler-Tour Subtree Flattening & Sum Query Engine (`euler_tour_subtree_d59`)

> Category: **Tree Data Structures** | Language: **C++20**

## Overview

Flattens rooted trees via DFS entry/exit timestamps [tin, tout] so every node's subtree sum collapses into a contiguous static prefix sum slice.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(V) flatten, O(1) subtree sum` |
| **Space Complexity** | `O(V)` |

## Mathematical & Safety Invariants

- Root subtree total strictly equals sum across all node weights.

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
