# Li Chao Segment Tree Dynamic Convex Hull Trick Minimizer (`li_chao_convex_hull_trick`)

> Category: **Dynamic Programming Optimizations** | Language: **C++20**

## Overview

Inserts arbitrary linear functions y = m*x + c in non-monotonic slope order into a dynamically allocated segment tree and evaluates lower-envelope minima over arbitrary coordinate domains.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(log X) Insert & Query` |
| **Space Complexity** | `O(Q log X)` |

## Mathematical & Safety Invariants

- At every integer coordinate x in [x_min, x_max], query(x) equals min_i (m_i * x + c_i).
- Inserting a strictly dominated line preserves every existing query answer identically.

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
