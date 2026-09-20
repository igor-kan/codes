"""
Bulirsch-Stoer ODE Integrator with Modified Midpoint and Richardson Extrapolation.
References: Press et al. - Numerical Recipes (Ch. 17).
"""
import numpy as np

def modified_midpoint(derivs, y0, t0, H, n_substeps):
    """Modified midpoint step of total step size H divided into n_substeps."""
    h = H / n_substeps
    y = np.copy(y0)
    yn = y0 + h * derivs(t0, y0)
    t = t0 + h
    for _ in range(1, n_substeps):
        ynp1 = y + 2.0 * h * derivs(t, yn)
        y = yn
        yn = ynp1
        t += h
    # Final smoothing step
    y_final = 0.5 * (y + yn + h * derivs(t, yn))
    return y_final

def neville_extrapolate(x_seq, y_seq):
    """Neville polynomial extrapolation to x = 0."""
    n = len(x_seq)
    T = [[y for y in y_seq]]
    for col in range(1, n):
        T.append([])
        for row in range(n - col):
            x_i = x_seq[row]
            x_j = x_seq[row + col]
            P_right = T[col - 1][row + 1]
            P_left = T[col - 1][row]
            # Extrapolate to x = 0
            P_extrap = (x_i * P_right - x_j * P_left) / (x_i - x_j)
            T[col].append(P_extrap)
    return T[-1][0]

def bulirsch_stoer_step(derivs, y0, t0, H, n_seq=(2, 4, 6, 8, 12, 16)):
    """Bulirsch-Stoer extrapolation step."""
    tableau = []
    h_sq = []
    for n in n_seq:
        tableau.append(modified_midpoint(derivs, y0, t0, H, n))
        h_sq.append((H / n)**2)
    return neville_extrapolate(h_sq, tableau)
