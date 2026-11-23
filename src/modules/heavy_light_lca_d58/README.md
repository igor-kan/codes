# Binary-Lifting O(log N) LCA & Tree Path Distance (`heavy_light_lca_d58`)

> Category: **Tree Queries** | Language: **C++20**

## Overview

Precomputes 2^k ancestor jump tables across rooted trees to resolve arbitrary lowest common ancestors and simple path edge distances in logarithmic time.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N log N) preprocess, O(log N) LCA/distance` |
| **Space Complexity** | `O(N log N)` |

## Mathematical & Safety Invariants

- Distance dist(u, v) satisfies symmetry and triangle equality at every internal ancestor.

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
