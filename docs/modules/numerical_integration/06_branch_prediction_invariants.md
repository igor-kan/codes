# Branch Prediction & Branchless Design: Adaptive Gauss-Legendre Quadrature

## 1. Branch Misprediction Penalty

On modern superscalar out-of-order processors, a branch misprediction flushes the execution pipeline, incurring a penalty of **15 to 20 cycles**. In high-frequency computational loops, random branch behavior severely degrades instructions-per-cycle (IPC).

## 2. Branchless Selection Primitives

Conditionals in `numerical_integration` are transformed into branchless select operations via bitwise masks or conditional moves:

```c
// Instead of:
// if (x > threshold) val = a; else val = b;

// Branchless implementation:
uint64_t mask = -(uint64_t)(x > threshold);
val = (a & mask) | (b & ~mask);
```

## 3. Predictor Friendly Loop Bounds

All loops utilize compile-time or loop-invariant trip counts, allowing the Branch Target Buffer (BTB) to achieve $> 99.5\%$ prediction accuracy.
