# Successive Shortest-Path Min-Cost Max-Flow Engine (`min_cost_max_flow_d58`)

> Category: **Minimum Cost Flows** | Language: **C++20**

## Overview

Computes exact maximum s-t flow achieving global minimum total unit-weight cost via residual backward negative-cost edges and SPFA paths.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(F * E * V) SPFA augmenting passes` |
| **Space Complexity** | `O(V + E)` |

## Mathematical & Safety Invariants

- Achieved flow equals Edmonds-Karp max-flow capacity while minimizing edge transportation cost.

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
