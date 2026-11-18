# Suffix Automaton Longest Common Substring & Distinct Count (`suffix_automaton_lcs`)

> Category: **String Automata** | Language: **C++20**

## Overview

Builds Blumer's minimal Suffix Automaton (DAWG) in O(N) time to count all distinct substrings and compute the longest common substring with a query string.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N) online state extension + O(M) streaming LCS match` |
| **Space Complexity** | `O(N) states and transitions` |

## Mathematical & Safety Invariants

- Total distinct substrings equals sum of len(u) - len(link(u)) over all states.
- LCS length matches exact maximal shared contiguous factor.

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
