"""
Propp-Wilson Coupling From The Past (CFTP) Exact Sampling for Finite Markov Chains.
Reference: Propp & Wilson (1996); Rosenthal (2000).
"""
import numpy as np
from typing import Callable, List

def run_monotone_cftp(update_fn: Callable[[int, float], int], n_states: int, seed: int = 42) -> int:
    """
    Runs backward monotone CFTP on states {0, ..., n_states-1}.
    """
    rng = np.random.default_rng(seed)
    T = 1
    random_numbers = []
    
    while True:
        # Prepend new random uniforms
        new_u = rng.uniform(0.0, 1.0, size=T - len(random_numbers)).tolist()
        random_numbers = new_u + random_numbers
        
        # Simulate from -T to 0
        top = n_states - 1
        bottom = 0
        for u in random_numbers:
            top = update_fn(top, u)
            bottom = update_fn(bottom, u)
            
        if top == bottom:
            return top
        T *= 2
