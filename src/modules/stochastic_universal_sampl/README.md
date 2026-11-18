# Vose Alias Table & Stochastic Universal Resampler (`stochastic_universal_sampl`)

> Category: **Randomized Algorithms** | Language: **C++20**

## Overview

Constructs Vose's O(1) Alias Table from arbitrary unnormalized non-negative weights and provides low-variance equally-spaced Stochastic Universal Sampling.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N) Vose alias table construction + O(1) exact categorical sampling` |
| **Space Complexity** | `O(N)` |

## Mathematical & Safety Invariants

- Every alias bucket mixes at most two outcomes.
- SUS draw count equals exact requested sample count M.

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
