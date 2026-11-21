# Knuth-Morris-Pratt Prefix Border Automaton (`kmp_border_automaton_d56`)

> Category: **String Algorithms** | Language: **C++20**

## Overview

Computes exact prefix-function border lengths pi[i] and finds all zero-indexed pattern match offsets with minimal fallback transitions.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(|P| + |T|)` |
| **Space Complexity** | `O(|P|)` |

## Mathematical & Safety Invariants

- Every prefix border satisfies pi[i] <= i and KMP matches match naive substring offsets.

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
