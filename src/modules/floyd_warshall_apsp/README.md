# Floyd-Warshall All-Pairs Shortest Path & Negative-Cycle Detector (`floyd_warshall_apsp`)

> Category: **Graph Shortest Paths** | Language: **C++20**

## Overview

Computes exact all-pairs shortest distances and parent next-hop matrices over weighted directed graphs supporting negative edges, identifying negative-weight cycles via negative main-diagonal entries.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(V^3)` |
| **Space Complexity** | `O(V^2)` |

## Mathematical & Safety Invariants

- Triangle inequality dist[i][j] <= dist[i][k] + dist[k][j] holds for all triples without negative cycles.
- Diagonal dist[v][v] < 0 strictly characterizes vertices on or reachable through negative cycles.

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
