# Capacity-Scaling Dinic Blocking-Flow Network Solver (`dinic_scaling_maxflow`)

> Category: **Network Flow** | Language: **C++20**

## Overview

Accelerates Dinic maximum flow on high-capacity networks by filtering residual edges above power-of-two threshold delta = 2^k down to 1.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(E * V * log(U)) bit-scaled BFS level graphs + DFS blocking flow` |
| **Space Complexity** | `O(V + E)` |

## Mathematical & Safety Invariants

- Max flow equals minimum s-t cut capacity.
- Flow conservation holds at every internal vertex.

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
