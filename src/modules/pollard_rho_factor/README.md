# Pollard Rho & Brent Cycle Integer Factorization (`pollard_rho_factor`)

> Category: **Number Theory** | Language: **C++20**

## Overview

Combines Brent's batched GCD cycle acceleration with deterministic Miller-Rabin primality testing to split arbitrary 64-bit integers into sorted prime factors.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N^(1/4))` |
| **Space Complexity** | `O(log N)` |

## Mathematical & Safety Invariants

- Product of returned prime factors strictly equals input N.
- Every returned factor satisfies deterministic primality.

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
