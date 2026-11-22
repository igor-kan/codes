# Bellman-Ford Shortest Paths With Negative Cycle Flag (`bellman_ford_spfa_d57`)

> Category: **Graph Shortest Paths** | Language: **C++20**

## Overview

Relaxes directed weighted edges up to V - 1 rounds to resolve negative-weight shortest paths and runs a V-th witness pass to flag negative cycles.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(V * E)` |
| **Space Complexity** | `O(V)` |

## Mathematical & Safety Invariants

- Absence of reachable negative cycles preserves all relaxed shortest distances.

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
