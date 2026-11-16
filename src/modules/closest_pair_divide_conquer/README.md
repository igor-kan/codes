# Shamos-Hoey O(N log N) Planar Closest Pair Divide-and-Conquer (`closest_pair_divide_conquer`)

> Category: **Computational Geometry** | Language: **C++20**

## Overview

Computes exact squared Euclidean distance and witness indices of the closest pair among N planar points via x-coordinate split recursion and y-sorted strip sweep (7-neighbor bound).

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N log N)` |
| **Space Complexity** | `O(N)` |

## Mathematical & Safety Invariants

- Returned pair distance squared matches exact O(N^2) exhaustive Euclidean oracle across collinear and duplicate points.
- Strip window compares at most 7 subsequent points in y-order per candidate.

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
