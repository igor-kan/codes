# Idempotent Sparse Table for O(1) Range Minimum Queries (`sparse_table_rmq_d60`)

> Category: **Range Queries** | Language: **C++20**

## Overview

Precomputes power-of-two block minima so overlapping idempotent minimum queries over arbitrary closed ranges answer in constant time.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N log N) build and O(1) idempotent RMQ` |
| **Space Complexity** | `O(N log N)` |

## Mathematical & Safety Invariants

- Query(l, r) equals min_{l <= i <= r} A[i] for all 0 <= l <= r < N.

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
