"""
Ideals in Boolean Algebras and Duality with Filters.
Reference: Jech, Set Theory, Ch. 7.
"""
from typing import Set, FrozenSet

def is_ideal(family: Set[FrozenSet[int]], base_set: FrozenSet[int]) -> bool:
    """Dually to a filter: contains empty set, closed under subsets and finite unions."""
    if frozenset() not in family:
        return False
    if base_set in family:
        return False
    for A in family:
        for B in family:
            if (A | B) not in family:
                return False
    return True
