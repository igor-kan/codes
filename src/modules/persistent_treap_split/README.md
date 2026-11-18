# Path-Copied Persistent Implicit Treap Sequence (`persistent_treap_split`)

> Category: **Persistent Data Structures** | Language: **C++20**

## Overview

Maintains immutable sequence versions via functional treap split and merge that copy only root-to-split-path nodes while sharing unmodified subtrees.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(log N) time and space per functional split, merge, and insert` |
| **Space Complexity** | `O(N + Q log N) arena nodes` |

## Mathematical & Safety Invariants

- Older roots remain completely immutable across subsequent updates.
- Subtree sizes and sums equal exact child aggregates.

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
