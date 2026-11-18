# Simple Polygon Ear-Clipping Triangulation & Shoelace Area (`polygonal_ear_clipping`)

> Category: **Computational Geometry** | Language: **C++20**

## Overview

Decomposes any counterclockwise simple polygon of N vertices into N-2 triangles via ear clipping and verifies that triangle areas sum to the exact polygon area.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N^2) convex ear pruning + point-in-triangle guard` |
| **Space Complexity** | `O(N)` |

## Mathematical & Safety Invariants

- Emits exactly N-2 triangles for an N-vertex simple polygon.
- Sum of triangle areas equals exact Shoelace polygon area.

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
