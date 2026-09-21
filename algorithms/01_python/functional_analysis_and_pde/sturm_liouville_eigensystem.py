"""
Sturm-Liouville Boundary Value Problem Eigenvalue Solver.
Reference: Hassani, Mathematical Methods for Physics, Ch. 19; Blennow, Ch. 7.
"""
import numpy as np

def sturm_liouville_fd_eigenvalues(p_func, q_func, w_func, x_span=(0.0, 1.0), n_pts=200, n_eigs=5):
    """
    Solves [-(p(x) y')' + q(x) y = lambda w(x) y] with Dirichlet boundary conditions y(a)=y(b)=0.
    """
    x = np.linspace(x_span[0], x_span[1], n_pts)
    h = x[1] - x[0]
    n_inner = n_pts - 2
    x_int = x[1:-1]
    
    A = np.zeros((n_inner, n_inner))
    B = np.zeros((n_inner, n_inner))
    
    for i in range(n_inner):
        xi = x_int[i]
        p_half_plus = p_func(xi + 0.5 * h)
        p_half_minus = p_func(xi - 0.5 * h)
        
        A[i, i] = (p_half_plus + p_half_minus) / (h**2) + q_func(xi)
        if i > 0:
            A[i, i-1] = -p_half_minus / (h**2)
        if i < n_inner - 1:
            A[i, i+1] = -p_half_plus / (h**2)
            
        B[i, i] = w_func(xi)
        
    eigs = np.linalg.eigvals(np.linalg.inv(B) @ A)
    return np.sort(eigs.real)[:n_eigs]
