# Deterministic 64-Bit Miller-Rabin Primality Test (`miller_rabin_primality`)

> Category: **Number Theory** | Language: **C++20**

## Overview

Performs deterministic primality proving across all unsigned 64-bit integers using 12 prime witness bases {2,3,5,7,11,13,17,19,23,29,31,37} and overflow-free 128-bit modular multiplication.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(k log^3 N)` |
| **Space Complexity** | `O(1)` |

## Mathematical & Safety Invariants

- Zero false positives or false negatives on any 64-bit unsigned integer.
- Matches trial division deterministically for small integers [0, 10000].

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
