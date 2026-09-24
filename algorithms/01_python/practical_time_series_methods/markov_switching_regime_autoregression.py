"""Hamilton Markov-Switching 2-State Regime Model."""
import numpy as np


def two_state_markov_transition_step(prob_state1: float, p11: float, p22: float) -> float:
    """Compute updated state probability: P(S_{t+1}=1) = P(S_t=1)*p11 + P(S_t=2)*(1-p22)."""
    return prob_state1 * p11 + (1.0 - prob_state1) * (1.0 - p22)
