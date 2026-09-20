"""
Lie Transforms and Canonical Perturbation Theory.
References: V. I. Arnold - Mathematical Methods of Classical Mechanics.
"""
import numpy as np

def lie_transform_generator_step(f_val: float, w_generator_bracket: float, epsilon: float = 0.01) -> float:
    """First order Lie transformation: exp(eps L_W) f = f + eps {f, W}."""
    return f_val + epsilon * w_generator_bracket
