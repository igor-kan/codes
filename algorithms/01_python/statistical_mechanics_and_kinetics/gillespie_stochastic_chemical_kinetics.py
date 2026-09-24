"""Gillespie Direct Stochastic Simulation Algorithm (SSA) for Chemical Master Equation."""
import numpy as np


def gillespie_birth_death(k_birth: float, k_death: float, x0: int, t_max: float, seed: int = 42) -> tuple:
    """Simulate single-species birth-death process."""
    np.random.seed(seed)
    t = 0.0
    x = x0
    times = [t]
    trajs = [x]
    
    while t < t_max:
        a1 = k_birth
        a2 = k_death * x
        a0 = a1 + a2
        if a0 <= 0:
            break
        dt = np.random.exponential(1.0 / a0)
        t += dt
        if t > t_max:
            break
        if np.random.rand() < a1 / a0:
            x += 1
        else:
            x = max(0, x - 1)
        times.append(t)
        trajs.append(x)
        
    return np.array(times), np.array(trajs)
