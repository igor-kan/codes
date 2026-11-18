# Lengauer-Tarjan Flowgraph Immediate Dominator Solver (`dominator_tree_lengauer`)

> Category: **Compiler & Graph Analysis** | Language: **C++20**

## Overview

Computes immediate dominators idom[v] on directed control-flow graphs rooted at entry vertex r so every path from r to v passes through idom[v].

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(V * (V + E)) iterative bitset/parent fixed-point & Lengauer-Tarjan verification` |
| **Space Complexity** | `O(V + E)` |

## Mathematical & Safety Invariants

- Entry vertex dominates every reachable node.
- Dominator parent links form a rooted tree over reachable vertices.

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
