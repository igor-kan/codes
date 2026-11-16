# Successive Shortest Augmenting Path Min-Cost Max-Flow Solver (`min_cost_max_flow_spfa`)

> Category: **Network Flow Optimization** | Language: **C++20**

## Overview

Computes exact integer minimum-cost maximum flow in directed capacitated graphs via Shortest Path Faster Algorithm (SPFA) residual augmentation and Johnson-potential Dijkstra acceleration.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(F * E * V) worst-case, sublinear typical via SPFA + Dijkstra potentials` |
| **Space Complexity** | `O(V + E)` |

## Mathematical & Safety Invariants

- Flow along every edge satisfies 0 <= flow[e] <= cap[e].
- Net flow divergence at every intermediate node v not in {source, sink} is identically 0.
- Final residual network contains no negative-cost augmenting cycle of positive capacity.

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
