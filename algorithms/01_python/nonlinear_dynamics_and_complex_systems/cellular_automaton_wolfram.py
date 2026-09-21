"""
Elementary 1D Cellular Automaton Simulation for All 256 Wolfram Rules.
Reference: Gershenfeld, The Nature of Mathematical Modeling, Ch. 15; Wolfram (1984).
"""
import numpy as np

def step_cellular_automaton_1d(state: np.ndarray, rule_number: int) -> np.ndarray:
    """Computes next state according to rule_number in 0..255 with periodic boundary."""
    n = len(state)
    next_state = np.zeros(n, dtype=int)
    for i in range(n):
        neighborhood = (state[(i - 1) % n] << 2) | (state[i] << 1) | state[(i + 1) % n]
        next_state[i] = (rule_number >> neighborhood) & 1
    return next_state
