# Gomory-Hu All-Pairs Minimum s-t Cut Tree (`gomory_hu_cut_tree`)

> Category: **Network Flow** | Language: **C++20**

## Overview

Constructs an equivalent flow tree on N vertices using Gusfield's simplified Gomory-Hu algorithm, returning tree edges where the minimum-weight edge on any u-v tree path equals the global max flow / min cut between u and v.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(V * T_maxflow) via Gusfield's uncontracted method` |
| **Space Complexity** | `O(V + E)` |

## Mathematical & Safety Invariants

- The Gomory-Hu tree spans all N vertices with N-1 positive-or-zero weighted edges.
- Bottleneck edge weight between u and v in the tree matches full Dinic max-flow between u and v.

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
