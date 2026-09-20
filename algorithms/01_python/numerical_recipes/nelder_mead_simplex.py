"""
Nelder-Mead Downhill Simplex Optimization.
References: Press et al. - Numerical Recipes (Ch. 10).
"""
import numpy as np

def nelder_mead(func, x0, tol=1e-6, max_iter=500):
    """Nelder-Mead simplex algorithm in N dimensions."""
    x0 = np.array(x0, dtype=float)
    dim = len(x0)
    
    # Initialize simplex
    simplex = [x0]
    for i in range(dim):
        point = x0.copy()
        point[i] += 0.05 if point[i] != 0 else 0.00025
        simplex.append(point)
    simplex = np.array(simplex)

    alpha, gamma, rho, sigma = 1.0, 2.0, 0.5, 0.5

    for _ in range(max_iter):
        f_vals = np.array([func(p) for p in simplex])
        order = np.argsort(f_vals)
        simplex = simplex[order]
        f_vals = f_vals[order]

        if np.max(np.abs(f_vals[1:] - f_vals[0])) < tol:
            break

        # Centroid of best points
        x_bar = np.mean(simplex[:-1], axis=0)

        # Reflection
        x_r = x_bar + alpha * (x_bar - simplex[-1])
        f_r = func(x_r)

        if f_vals[0] <= f_r < f_vals[-2]:
            simplex[-1] = x_r
        elif f_r < f_vals[0]:
            # Expansion
            x_e = x_bar + gamma * (x_r - x_bar)
            simplex[-1] = x_e if func(x_e) < f_r else x_r
        else:
            # Contraction
            x_c = x_bar + rho * (simplex[-1] - x_bar)
            if func(x_c) < f_vals[-1]:
                simplex[-1] = x_c
            else:
                # Shrink
                simplex[1:] = simplex[0] + sigma * (simplex[1:] - simplex[0])

    return simplex[0]
