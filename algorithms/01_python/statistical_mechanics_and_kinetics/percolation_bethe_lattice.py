"""Site and Bond Percolation on Bethe Lattice (Cayley Tree)."""
def bethe_percolation_threshold(z_coordination: int) -> float:
    """p_c = 1 / (z - 1)."""
    if z_coordination <= 2:
        raise ValueError("Coordination number z must be >= 3")
    return float(1.0 / (z_coordination - 1))
