# Binary-Split Bounded Multi-Item Knapsack (`knapsack_bounded_dp_d57`)

> Category: **Combinatorial DP** | Language: **C++20**

## Overview

Converts bounded multiplicity item bundles via power-of-two decomposition into 0/1 sub-items for compact exact capacity-W value maximization.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(W * sum(log count_i))` |
| **Space Complexity** | `O(W)` |

## Mathematical & Safety Invariants

- Optimal value stays monotonic across capacity limits and dominates single-bundle takes.

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
