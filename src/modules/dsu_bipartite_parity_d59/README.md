# Online Bipartite Parity Disjoint Set Union (`dsu_bipartite_parity_d59`)

> Category: **Graph Connectivity** | Language: **C++20**

## Overview

Tracks mod-2 parity offsets to DSU roots cleanly accepting even cycles while immediately flagging odd-cycle bipartiteness violations.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(alpha(N)) per edge validation` |
| **Space Complexity** | `O(N)` |

## Mathematical & Safety Invariants

- Even length cycles stay bipartite whereas odd cycles cleanly violate bipartiteness.

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
