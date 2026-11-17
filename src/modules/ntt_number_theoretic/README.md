# Radix-2 Number Theoretic Transform (Mod 998244353) (`ntt_number_theoretic`)

> Category: **Algebraic & Polynomial** | Language: **C++20**

## Overview

Computes exact integer polynomial convolution modulo prime 998244353 using Cooley-Tukey iterative bit-reversed Number Theoretic Transform with primitive root 3 and exact modular inverse normalization.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N log N) exact modular convolution` |
| **Space Complexity** | `O(N)` |

## Mathematical & Safety Invariants

- Inverse NTT recovers exact input coefficients modulo 998244353.
- NTT polynomial product matches naive O(N*M) Cauchy convolution coefficient-wise.

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
