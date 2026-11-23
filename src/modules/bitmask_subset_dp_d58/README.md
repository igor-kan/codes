# Exact N-Agent Task Assignment Bitmask DP (`bitmask_subset_dp_d58`)

> Category: **Bitmask Dynamic Programming** | Language: **C++20**

## Overview

Finds exact minimum-cost one-to-one bijection between N agents and N tasks via popcount-indexed bitmask DP transitions.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N * 2^N)` |
| **Space Complexity** | `O(2^N)` |

## Mathematical & Safety Invariants

- Optimal bijection cost strictly <= identity diagonal sum.

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
