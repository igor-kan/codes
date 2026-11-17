# GF(2) Linear XOR Basis with Rank, Max-XOR & K-th Query (`gaussian_xor_basis`)

> Category: **Algebraic & Bitwise** | Language: **C++20**

## Overview

Maintains a canonical triangular basis over GF(2)^62 supporting subset XOR span membership, global maximum subset XOR, k-th smallest distinct subset XOR, and basis merge.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(62) insertion & query over 64-bit integers` |
| **Space Complexity** | `O(62) fixed basis array` |

## Mathematical & Safety Invariants

- Basis size rank <= 62 and every nonzero basis pivot has a unique highest set bit.
- Number of distinct representable XOR values equals 2^rank.

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
