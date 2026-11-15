# Johnson Sparse All-Pairs Shortest Paths with Bellman-Ford Potentials (`johnson_apsp_reweight`)

> Category: **Graph Shortest Paths** | Language: **C++20**

## Overview

Computes exact all-pairs shortest distances on sparse negative-weight graphs by adding a virtual super-source to compute Bellman-Ford vertex potentials h(v), reweighting every edge non-negatively w'(u,v)=w(u,v)+h(u)-h(v), and running Dijkstra from each vertex.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(V E + V^2 log V)` |
| **Space Complexity** | `O(V^2)` |

## Mathematical & Safety Invariants

- Reweighted edges satisfy w'(u,v) >= 0 everywhere when no negative cycle exists.
- Original shortest path distance d(u,v) = d'(u,v) - h(u) + h(v).

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
