"""
Van Dyke's Asymptotic Matching Rule: m-term inner expansion of n-term outer = n-term outer of m-term inner.
Reference: Mauch, Intro to Applied Mathematics, Ch. 29; Van Dyke (1975).
"""
def verify_matching_constant(outer_lim: float, inner_lim: float) -> bool:
    return abs(outer_lim - inner_lim) < 1e-6
