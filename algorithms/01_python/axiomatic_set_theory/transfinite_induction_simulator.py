"""
Transfinite Sequence Generator and Limit Ordinal Accumulator.
Reference: Jech, Set Theory, Ch. 2.
"""
from typing import Callable, List

def simulate_transfinite_sequence(step_func: Callable[[int, float], float],
                                  limit_func: Callable[[List[float]], float],
                                  initial_val: float, length: int) -> List[float]:
    seq = [initial_val]
    for alpha in range(1, length):
        if alpha % 4 == 0:  # Mock limit ordinals at multiples of 4
            seq.append(limit_func(seq))
        else:
            seq.append(step_func(alpha, seq[-1]))
    return seq
