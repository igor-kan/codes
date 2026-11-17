# 2-SAT Linear-Time Tarjan SCC Solver & Implication Witness (`two_sat_implication`)

> Category: **Graph & Logic Algorithms** | Language: **C++20**

## Overview

Solves 2-CNF satisfiability formulas by constructing an implication digraph on 2N literals, condensing strongly connected components with Tarjan's algorithm, and deriving a satisfying Boolean assignment.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(V + M) clauses via Kosaraju/Tarjan SCC` |
| **Space Complexity** | `O(V + M)` |

## Mathematical & Safety Invariants

- Formula is unsatisfiable iff variable x and negation ~x occupy the same SCC.
- Returned assignment satisfies every disjunctive clause (a OR b).

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
