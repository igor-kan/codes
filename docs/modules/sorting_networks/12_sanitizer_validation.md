# Sanitizer Validation & Runtime Audits: Bitonic and Batcher Sorting Networks

## 1. Continuous Sanitizer Configurations

All test suites for `sorting_networks` are built and executed under the following sanitizers:

- **AddressSanitizer (`-fsanitize=address`)**: Validates spatial and temporal memory safety, guaranteeing no out-of-bounds reads/writes or heap memory leaks.
- **UndefinedBehaviorSanitizer (`-fsanitize=undefined`)**: Detects integer overflows, zero divisions, misaligned accesses, and null dereferences.
- **ThreadSanitizer (`-fsanitize=thread`)**: Detects unsynchronized concurrent memory accesses.

## 2. Automated Regression Gates

Any commit triggering a sanitizer panic or violation fails CI instantly. Zero sanitizer suppressions are permitted in core mathematical and memory routines.
