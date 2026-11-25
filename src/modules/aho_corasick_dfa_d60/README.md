# Aho-Corasick Multi-Pattern Automaton over Lowercase ASCII (`aho_corasick_dfa_d60`)

> Category: **String Matching** | Language: **C++20**

## Overview

Builds a multi-pattern trie augmented with BFS failure links and dictionary match counts to tally all pattern occurrences in one pass.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(sum |pat| + |text|) linear multi-pattern scan` |
| **Space Complexity** | `O(26 * states)` |

## Mathematical & Safety Invariants

- Total matched occurrences equals sum of independent pattern scans across text.

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
