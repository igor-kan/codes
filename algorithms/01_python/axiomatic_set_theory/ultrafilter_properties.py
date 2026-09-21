"""
Filters and Ultrafilters on Finite and Countable Sets.
Reference: Jech, Set Theory, Ch. 7 (Filters and Large Cardinals).
"""
from typing import Set, FrozenSet

def is_filter(family: Set[FrozenSet[int]], base_set: FrozenSet[int]) -> bool:
    """
    A family F subset P(X) is a filter if:
    1. Empty set not in F, and X in F
    2. A in F and A subset B implies B in F (upper closed)
    3. A, B in F implies A cap B in F (finite intersections)
    """
    if frozenset() in family:
        return False
    if base_set not in family:
        return False
    # Check intersection closure
    for A in family:
        for B in family:
            if (A & B) not in family:
                return False
    return True
