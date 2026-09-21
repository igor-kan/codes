"""
Cofinality of Countable Limit Ordinals and Regular vs Singular Cardinals.
Reference: Jech, Set Theory, Ch. 3.
"""
def is_regular_aleph_0() -> bool:
    """Aleph_0 has cofinality omega = aleph_0, so it is a regular cardinal."""
    return True

def cofinality_aleph_omega() -> str:
    """Aleph_omega = sup_{n < omega} Aleph_n has cofinality omega < Aleph_omega, so it is singular."""
    return "omega"
