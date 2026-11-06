# Error Propagation Bounds & Wilkinson Stability: Bitonic and Batcher Sorting Networks

## 1. Forward vs Backward Error Analysis

Using J.H. Wilkinson's backward error analysis framework, the computed result $\hat{y} = \text{alg}(x)$ is shown to be the exact solution of a slightly perturbed problem:

$$\hat{y} = f(x + \Delta x), \quad \frac{\|\Delta x\|}{\|x\|} \le \gamma_n u$$

where $u$ is machine precision and $\gamma_n = \frac{n u}{1 - n u} = n u + \mathcal{O}(u^2)$.

## 2. Accumulated Error Bound

For a sequence of $n$ floating-point operations in `sorting_networks`, the forward error bound satisfies:

$$\frac{\|\hat{y} - y\|}{\|y\|} \le \kappa(x) \cdot \gamma_n + \mathcal{O}(u^2)$$

This confirms that `sorting_networks` is **backward stable**, as the error is proportional only to the inherent conditioning $\kappa(x)$ of the problem.
