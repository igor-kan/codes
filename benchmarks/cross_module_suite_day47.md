# Cross-Module Microbenchmark Suite: codes

## Benchmark Protocols

This suite aggregates end-to-end throughput and latency benchmarks across all computational modules in `codes`.

### Standardized Execution Matrix

- **Warmup Cycles**: $10^4$ iterations to saturate L1 instruction and data caches.
- **Sample Iterations**: $10^5$ operations per sample.
- **Statistical Filtering**: 99% confidence interval with IQR outlier rejection.

### Targets

- **Instructions Per Cycle (IPC)**: $\ge 2.4$ IPC.
- **L1 Cache Miss Ratio**: $< 0.4\%$.
- **Branch Misprediction Penalty**: $< 0.05\%$.
