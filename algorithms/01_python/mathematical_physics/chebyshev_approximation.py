"""
Chebyshev Polynomial Approximation and Economization.
References: Press et al. - Numerical Recipes (Ch. 5).
"""
import numpy as np

class ChebyshevApproximation:
    def __init__(self, func, a: float, b: float, n_terms: int = 20):
        self.a = a
        self.b = b
        self.n_terms = n_terms
        
        # Chebyshev nodes on [-1, 1]
        k = np.arange(n_terms)
        x_nodes = np.cos(np.pi * (k + 0.5) / n_terms)
        # Map to [a, b]
        x_mapped = 0.5 * (x_nodes * (b - a) + (b + a))
        f_vals = func(x_mapped)
        
        # Compute Chebyshev coefficients c_j = (2/N) sum f(x_k) T_j(x_k)
        self.coeffs = np.zeros(n_terms)
        for j in range(n_terms):
            self.coeffs[j] = (2.0 / n_terms) * np.sum(f_vals * np.cos(np.pi * j * (k + 0.5) / n_terms))
            
    def evaluate(self, x: np.ndarray) -> np.ndarray:
        """Clenshaw's recurrence algorithm for Chebyshev series evaluation."""
        x = np.asarray(x, dtype=float)
        # Map x from [a, b] to y in [-1, 1]
        y = (2.0 * x - (self.a + self.b)) / (self.b - self.a)
        
        d = np.zeros_like(y)
        dd = np.zeros_like(y)
        for j in range(self.n_terms - 1, 0, -1):
            sv = d.copy()
            d = 2.0 * y * d - dd + self.coeffs[j]
            dd = sv
            
        return y * d - dd + 0.5 * self.coeffs[0]
