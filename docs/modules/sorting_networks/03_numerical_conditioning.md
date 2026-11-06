# Numerical Conditioning & Rounding Stability: Bitonic and Batcher Sorting Networks

## 1. Condition Number Quantification

The sensitivity of `sorting_networks` to perturbations in input data is quantified by the relative condition number $\kappa$:

$$\kappa = \lim_{\epsilon \to 0} \sup_{\|\delta x\| \le \epsilon} \left( \frac{\|\delta y\| / \|y\|}{\|\delta x\| / \|x\|} \right) = \frac{\|J(x)\| \cdot \|x\|}{\|f(x)\|}$$

- **Well-Conditioned Regime**: $\kappa \in [1, 10^2]$ — Standard IEEE-754 double precision maintains 14+ decimal digits of accuracy.
- **Ill-Conditioned Transition**: $\kappa \in (10^2, 10^8]$ — Extended precision or preconditioning transformations are dynamically applied.

## 2. Floating-Point Error Propagation

According to IEEE-754 arithmetic with unit roundoff $u = 2^{-53} \approx 1.11 \times 10^{-16}$ for binary64:

$$\text{fl}(x \odot y) = (x \odot y)(1 + \delta), \quad |\delta| \le u$$

To prevent catastrophic cancellation during subtraction of near-equal quantities, algebraic identities are reformulated into stable continued fraction or factorized representations.
