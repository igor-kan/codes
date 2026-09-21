import numpy as np
from kam_torus_action_angle import is_diophantine_non_resonant, golden_mean_frequency_ratio


def test_diophantine():
    # Golden ratio is maximally non-resonant
    sigma = golden_mean_frequency_ratio()
    assert is_diophantine_non_resonant(1.0, sigma, gamma=0.005, tau=2.0, max_k=10)

    # Rational ratio 1:2 fails resonance immediately
    assert not is_diophantine_non_resonant(1.0, 0.5, gamma=0.01, tau=2.0, max_k=10)
