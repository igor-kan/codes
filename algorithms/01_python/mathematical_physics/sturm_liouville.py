"""
Sturm-Liouville Eigenvalue Solver.
Solves -(p(x) y')' + q(x) y = lambda * w(x) y on [a, b]
References: Arfken, Weber, Harris - Mathematical Methods for Physicists (Ch. 8, 10).
"""
import numpy as np

class SturmLiouvilleSolver:
    def __init__(self, p_func, q_func, w_func, a=0.0, b=1.0, n_points=200):
        self.p_func = p_func
        self.q_func = q_func
        self.w_func = w_func
        self.a = a
        self.b = b
        self.n_points = n_points
        self.x = np.linspace(a, b, n_points)
        self.dx = self.x[1] - self.x[0]

    def solve_dirichlet(self, num_eigenvalues=5):
        """Solve with Dirichlet BC: y(a) = y(b) = 0."""
        n = self.n_points - 2
        x_int = self.x[1:-1]
        h = self.dx

        p_half_plus = self.p_func(x_int + 0.5 * h)
        p_half_minus = self.p_func(x_int - 0.5 * h)
        q_vals = self.q_func(x_int)
        w_vals = self.w_func(x_int)

        diag = (p_half_plus + p_half_minus) / (h**2) + q_vals
        off_diag = -p_half_plus[:-1] / (h**2)

        A = np.diag(diag) + np.diag(off_diag, 1) + np.diag(off_diag, -1)
        W = np.diag(w_vals)

        # Generalized symmetric eigenvalue problem: A y = lambda W y
        W_inv_sqrt = np.diag(1.0 / np.sqrt(w_vals))
        A_sym = W_inv_sqrt @ A @ W_inv_sqrt

        eigvals, eigvecs = np.linalg.eigh(A_sym)
        y_vecs = W_inv_sqrt @ eigvecs

        # Normalize with respect to weight function: int y_i y_j w dx = delta_ij
        normalized_eigenfunctions = []
        for i in range(num_eigenvalues):
            vec = np.zeros(self.n_points)
            vec[1:-1] = y_vecs[:, i]
            norm = np.sqrt(np.trapezoid(vec**2 * self.w_func(self.x), self.x))
            if norm > 1e-12:
                vec /= norm
            normalized_eigenfunctions.append(vec)

        return eigvals[:num_eigenvalues], np.array(normalized_eigenfunctions)
