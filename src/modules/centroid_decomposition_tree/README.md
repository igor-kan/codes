# Centroid Decomposition with Distance Oracle Queries (`centroid_decomposition_tree`)

> Category: **Tree Algorithms** | Language: **C++20**

## Overview

Builds a balanced centroid decomposition tree of depth <= log2(N) supporting O(log N) dynamic node activation and minimum shortest-path queries via cached ancestor distances.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N log N) decomposition build, O(log N) distance/nearest-active update` |
| **Space Complexity** | `O(N log N)` |

## Mathematical & Safety Invariants

- Centroid parent depth never exceeds floor(log2(N)) + 1.
- Nearest active distance oracle matches BFS oracle on unweighted trees.

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
