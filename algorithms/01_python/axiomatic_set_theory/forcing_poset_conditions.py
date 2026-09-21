"""
Cohen Forcing Poset: Conditions and Compatibility.
Reference: Jech, Set Theory, Ch. 14 (Forcing).
"""
from typing import Dict

def are_cohen_conditions_compatible(p: Dict[int, int], q: Dict[int, int]) -> bool:
    """Two partial functions p and q are compatible iff they agree on the intersection of their domains."""
    common_keys = set(p.keys()) & set(q.keys())
    return all(p[k] == q[k] for k in common_keys)
