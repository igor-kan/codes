# Edge Case Invariants & IEEE-754 Semantics: Bitonic and Batcher Sorting Networks

## 1. Exceptional Input Handling

The `sorting_networks` module defines explicit, mathematically sound behavior for all boundary conditions:

| Input Condition | Prescribed Handling | Return / State Invariant |
| :--- | :--- | :--- |
| **Empty Domain ($N = 0$)** | Immediate no-op | Returns zero / neutral element |
| **Subnormal Numbers** | Flushed to zero (FTZ/DAZ)| Prevents microcode slowdown |
| **Singular Matrix / Div-0** | Error status code | Safe failure without crash |
| **NaN / Infinity** | Defensive verification | Rejection at API boundary |

## 2. IEEE-754 Compliance

Unless specifically operating in fast-math modes, arithmetic strictly honors signed zero ($-0.0$) and IEEE-754 quiet NaN propagation rules.
