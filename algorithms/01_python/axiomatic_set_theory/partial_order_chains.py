"""
Poset Chains, Antichains, and Height Decomposition.
Reference: Jech, Set Theory, Ch. 4.
"""
from typing import List, Set, Tuple

def find_maximal_chain(elements: List[int], rel_leq: Set[Tuple[int, int]]) -> List[int]:
    """Greedily constructs a maximal chain in the poset."""
    chain = []
    for x in sorted(elements):
        if not chain or all((c, x) in rel_leq for c in chain):
            chain.append(x)
    return chain
