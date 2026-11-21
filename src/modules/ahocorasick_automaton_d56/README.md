# Aho-Corasick Multi-Pattern Failure Automaton (`ahocorasick_automaton_d56`)

> Category: **String Matching** | Language: **C++20**

## Overview

Builds a deterministic trie automaton over lowercase ASCII patterns with BFS failure links and terminal counts for simultaneous multi-pattern occurrence counting.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(|text| + sum(|patterns|) + matches)` |
| **Space Complexity** | `O(states * alphabet)` |

## Mathematical & Safety Invariants

- Total matched occurrences across patterns is invariant under distinct pattern ordering.

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
