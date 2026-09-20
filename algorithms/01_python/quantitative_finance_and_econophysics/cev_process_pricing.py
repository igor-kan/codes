"""
Constant Elasticity of Variance (CEV) Process Simulator.
References: Jovanovic - Econophysics and Financial Economics.
"""
import numpy as np

def simulate_cev_path(S0: float, mu: float, sigma: float, gamma: float, dt: float, n_steps: int) -> np.ndarray:
    """Simulate CEV model: dS_t = mu S_t dt + sigma S_t^gamma dW_t."""
    S = np.zeros(n_steps)
    S[0] = S0
    for i in range(1, n_steps):
        s_prev = max(1e-6, S[i - 1])
        vol = sigma * (s_prev**gamma)
        diff = vol * np.sqrt(dt) * np.random.normal()
        S[i] = max(1e-6, s_prev + mu * s_prev * dt + diff)
    return S
