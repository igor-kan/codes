# Dinic Blocking-Flow Maximum s-t Network Flow Solver (`dinic_max_flow_d60`)

> Category: **Network Flow** | Language: **C++20**

## Overview

Constructs BFS shortest-augmenting-path level graphs and pushes blocking flows recursively via current-arc pointers.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(V^2 * E) worst-case, O(E * sqrt(V)) on unit networks` |
| **Space Complexity** | `O(V + E)` |

## Mathematical & Safety Invariants

- Maximum flow equals minimum s-t cut capacity across residual edges.

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
