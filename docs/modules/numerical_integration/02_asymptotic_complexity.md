# Asymptotic Complexity Analysis: Adaptive Gauss-Legendre Quadrature

## 1. Time and Space Bounds

| Operation / Routine | Best Case | Average Case | Worst Case | Space (Auxiliary) |
| :--- | :--- | :--- | :--- | :--- |
| **Initialization & Setup** | $\mathcal{O}(1)$ | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Primary Transformation** | $\mathcal{O}(N)$ | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N)$ |
| **State Query / Evaluation** | $\mathcal{O}(1)$ | $\mathcal{O}(\log N)$ | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| **Batch Reduction** | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

## 2. Recurrence Relation & Master Theorem

The computational recurrence governing the core divide-and-conquer processing step satisfies:

$$T(N) = a T(N/b) + f(N)$$

where $a = 2$, $b = 2$, and $f(N) = \Theta(N)$. Since $\log_b a = 1$, Case 2 of the Master Theorem applies:

$$T(N) = \Theta(N^{\log_b a} \log N) = \Theta(N \log N)$$

## 3. Scalability Profiling

Auxiliary memory allocation strictly follows an in-place or scratchpad model, ensuring that the total working set remains within L2 cache bounds ($< 1$ MiB) for problem sizes up to $N = 10^5$.
