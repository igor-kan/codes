# Bellman-Ford & SPFA Single-Source Shortest Path Engine (`bellman_ford_spfa`)

> Category: **Graph Shortest Paths** | Language: **C++20**

## Overview

Implements edge-relaxation Bellman-Ford and queue-accelerated SPFA with relaxation-count negative-cycle termination and edge certificate invariants.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(V * E) worst / O(E) typical` |
| **Space Complexity** | `O(V + E)` |

## Mathematical & Safety Invariants

- If no reachable negative cycle exists, dist[v] <= dist[u] + w(u,v) for all reachable edges.
- Any vertex relaxed >= V times witnesses a reachable negative cycle.

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
