"""
Moran Stochastic Birth-Death Process in Finite Populations.
Reference: Campbell Biology (12th Ed.), Ch. 23; Nowak, Evolutionary Dynamics.
"""
def moran_fixation_probability(N: int, relative_fitness_r: float) -> float:
    """
    Exact probability that a single mutant with relative fitness r reaches fixation in population N:
    rho = (1 - 1/r) / (1 - 1/r^N)  for r != 1
    rho = 1 / N                    for r = 1 (neutral)
    """
    if relative_fitness_r == 1.0:
        return 1.0 / N
    r = relative_fitness_r
    return float((1.0 - 1.0 / r) / (1.0 - (1.0 / r)**N))
