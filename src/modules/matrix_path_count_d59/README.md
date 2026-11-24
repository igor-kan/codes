# O(V^3 log K) Directed Graph Exact Length-K Walk Counter (`matrix_path_count_d59`)

> Category: **Algebraic Graph Theory** | Language: **C++20**

## Overview

Computes exact numbers of directed paths of length K between every pair (u, v) via binary exponentiation of boolean adjacency matrices mod 1e9+7.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(V^3 log K)` |
| **Space Complexity** | `O(V^2)` |

## Mathematical & Safety Invariants

- Total length-K walks across out-degree-D regular graphs equal N * D^K mod 1e9+7.

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
