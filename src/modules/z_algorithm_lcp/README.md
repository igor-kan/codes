# Gusfield Linear-Time Z-Algorithm & LCP Substring Matcher (`z_algorithm_lcp`)

> Category: **String Algorithms** | Language: **C++20**

## Overview

Computes Gusfield's Z-array Z[i] (longest common prefix between s[0..] and s[i..]) in linear amortized comparisons using a dynamic [l, r] Z-box window, powering exact pattern localization.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N + M)` |
| **Space Complexity** | `O(N + M)` |

## Mathematical & Safety Invariants

- Every Z[i] satisfies s[0..Z[i]-1] == s[i..i+Z[i]-1] and terminates at boundary or mismatch.
- Sum of explicit character comparisons across Z-box advances is strictly bounded by 2 * N.

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
