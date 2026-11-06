# Microbenchmarking Protocols & Profiling: Memory-Efficient Dynamic Programming

## 1. Measurement Methodology

Accurate microbenchmarks require eliminating non-deterministic system noise:

1. **CPU Frequency Pinning**: Governors set to `performance` mode; turbo boost disabled to ensure constant cycle frequency.
2. **Warmup Phase**: At least $10^4$ warmup iterations are executed to prime CPU instruction and data caches (L1/L2).
3. **Statistical Outlier Rejection**: RTT timings use Interquartile Range (IQR) filtering across at least 100 sample batches.

## 2. Benchmark Metric Targets

| Metric | Target | Measurement Tool |
| :--- | :--- | :--- |
| **Cycles Per Element** | $\le 1.8$ cycles | `perf stat -e cycles,instructions` |
| **Instructions Per Cycle (IPC)** | $\ge 2.5$ IPC | Hardware Performance Counters |
| **L1 Data Cache Miss Rate** | $< 0.5\%$ | `perf stat -e L1-dcache-load-misses` |
| **Branch Misprediction Rate**| $< 0.1\%$ | `perf stat -e branch-misses` |
