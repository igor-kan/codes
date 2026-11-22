# Edmonds-Karp Shortest-Augmenting Max-Flow Solver (`edmonds_karp_flow_d57`)

> Category: **Network Flow** | Language: **C++20**

## Overview

Computes integral maximum s-t network flow via repeated BFS shortest residual augmenting paths and strict backward residual capacity updates.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(V * E^2)` |
| **Space Complexity** | `O(V + E)` |

## Mathematical & Safety Invariants

- Max flow matches sum of outgoing positive residual reductions leaving source s.

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
