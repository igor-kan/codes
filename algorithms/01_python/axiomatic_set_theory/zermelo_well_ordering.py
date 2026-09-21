"""
Zermelo's Well-Ordering Theorem Constructive Choice Simulation.
Reference: Jech, Set Theory, Ch. 5 (Axiom of Choice).
"""
from typing import List, Set, Any

def well_order_by_choice(elements: Set[Any]) -> List[Any]:
    """Uses canonical selection to order a finite set."""
    rem = set(elements)
    order = []
    while rem:
        chosen = min(rem)
        order.append(chosen)
        rem.remove(chosen)
    return order
