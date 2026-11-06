# Verification Strategy & Sanitizer Compliance: codes

Quality assurance in `codes` is achieved through a multi-tiered defense-in-depth verification pipeline combining static analysis, runtime sanitizers, property-based testing, and formal invariants.

## Testing Matrix

```
+-----------------------------------------------------------+
|                   Formal Proofs / SMT                     |
+-----------------------------+-----------------------------+
                              |
+-----------------------------v-----------------------------+
|               Continuous Fuzzing (AFL++)                  |
+-----------------------------+-----------------------------+
                              |
+-----------------------------v-----------------------------+
|         Sanitizer Runs (ASan, UBSan, TSan, MSan)          |
+-----------------------------+-----------------------------+
                              |
+-----------------------------v-----------------------------+
|               Deterministic Unit & Integration            |
+-----------------------------------------------------------+
```

## Sanitizer Pass Criteria

1. **AddressSanitizer (ASan)**: Clean pass with zero buffer overflows, use-after-free, or memory leaks.
2. **UndefinedBehaviorSanitizer (UBSan)**: Zero signed integer overflows, misaligned pointer dereferences, or invalid bit shifts.
3. **ThreadSanitizer (TSan)**: Zero data races or deadlocks across multi-threaded test runs.
