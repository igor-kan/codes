"""
Closed Unbounded (Club) Sets and Stationary Sets.
Reference: Jech, Set Theory, Ch. 8.
"""
from typing import Set

def is_unbounded(subset: Set[int], limit: int) -> bool:
    return any(x >= limit - 1 for x in subset)
