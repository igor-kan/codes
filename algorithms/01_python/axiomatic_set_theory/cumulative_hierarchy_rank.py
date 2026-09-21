"""
Von Neumann Cumulative Hierarchy V_alpha and Set Rank.
Reference: Jech, Set Theory, Ch. 6.
"""
def rank_of_nested_tuple(obj) -> int:
    """Recursively computes the set-theoretic rank of nested tuples."""
    if not isinstance(obj, (tuple, list, set)):
        return 0
    if not obj:
        return 0
    return 1 + max(rank_of_nested_tuple(x) for x in obj)
