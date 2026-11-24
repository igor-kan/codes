# Iterative 2N Bottom-Up Zkw Range-Sum Tree (`zkw_range_sum_d59`)

> Category: **Segment Trees** | Language: **C++20**

## Overview

Uses sentinel-padded 2N bottom-up Zkw binary indexing to perform non-recursive point additions and inclusive interval sums.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(log N) add and [l, r] closed sum` |
| **Space Complexity** | `O(N)` |

## Mathematical & Safety Invariants

- Closed range sum [l, r] matches brute elementwise totals cleanly.

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
