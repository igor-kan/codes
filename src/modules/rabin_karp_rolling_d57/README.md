# Dual-Prime Rabin-Karp Exact Rolling Substring Search (`rabin_karp_rolling_d57`)

> Category: **Rolling Hash Matching** | Language: **C++20**

## Overview

Computes paired 64-bit modular rolling hashes mod 1e9+7 and 1e9+9 across sliding text windows and verifies exact substring slices on hash hits.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(|T| + |P|) expected with exact char confirm` |
| **Space Complexity** | `O(1)` |

## Mathematical & Safety Invariants

- Returned hit offsets match exact naive substring equality cleanly.

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
