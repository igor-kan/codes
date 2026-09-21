"""
Wright-Fisher Stochastic Model of Genetic Drift in Finite Diploid Populations.
Reference: Campbell Biology (12th Ed.), Ch. 23.
"""
import numpy as np

def simulate_wright_fisher(N_diploid: int, initial_p: float, generations: int, seed: int = 42) -> np.ndarray:
    """
    Simulates allele trajectory over generations via binomial sampling:
    i_{t+1} ~ Binomial(2N, i_t / 2N).
    """
    rng = np.random.default_rng(seed)
    two_N = 2 * N_diploid
    p_traj = np.zeros(generations)
    current_count = int(round(initial_p * two_N))
    p_traj[0] = current_count / two_N
    
    for g in range(1, generations):
        if current_count == 0 or current_count == two_N:
            # Fixation or loss
            p_traj[g:] = current_count / two_N
            break
        current_count = rng.binomial(two_N, current_count / two_N)
        p_traj[g] = current_count / two_N
        
    return p_traj
