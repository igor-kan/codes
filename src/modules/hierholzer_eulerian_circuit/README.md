# Hierholzer Linear-Time Eulerian Circuit & Trail Reconstructor (`hierholzer_eulerian_circuit`)

> Category: **Graph Algorithms** | Language: **C++20**

## Overview

Computes directed and undirected Eulerian circuits or trails via iterative stack-based Hierholzer traversal, handling self-loops, multi-edges, and disconnected degree-0 vertices.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(V + E)` |
| **Space Complexity** | `O(V + E)` |

## Mathematical & Safety Invariants

- Every input edge index appears exactly once across the reconstructed circuit.
- Consecutive vertices along the returned path share a directed or undirected incidence edge.
- Directed circuits exist if and only if in_deg[v] == out_deg[v] and edges lie in one weak component.

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
