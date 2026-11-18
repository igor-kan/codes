# Exact Minimum Enclosing Circle (Circumcircle & 2-Point Diameter) (`min_enclosing_circle_welzl`)

> Category: **Computational Geometry** | Language: **C++20**

## Overview

Finds the unique minimum-radius disk enclosing a 2D point cloud by testing boundary diameter pairs and circumcircles of non-collinear triples.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N) expected Welzl disk check / exact 2- and 3-point boundary solver` |
| **Space Complexity** | `O(N)` |

## Mathematical & Safety Invariants

- Every input point lies within radius + 1e-9 of the disk center.
- Radius is minimal among all valid enclosing disks.

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
