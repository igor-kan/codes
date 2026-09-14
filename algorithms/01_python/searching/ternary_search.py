"""Ternary search for the maximum/minimum of a unimodal function."""

from typing import Callable


def ternary_search_max(f: Callable[[float], float], lo: float, hi: float, eps: float = 1e-9) -> float:
    """Find x maximizing unimodal f on [lo, hi]."""
    while hi - lo > eps:
        m1 = lo + (hi - lo) / 3
        m2 = hi - (hi - lo) / 3
        if f(m1) < f(m2):
            lo = m1
        else:
            hi = m2
    return (lo + hi) / 2


def ternary_search_min(f: Callable[[float], float], lo: float, hi: float, eps: float = 1e-9) -> float:
    """Find x minimizing unimodal f on [lo, hi]."""
    while hi - lo > eps:
        m1 = lo + (hi - lo) / 3
        m2 = hi - (hi - lo) / 3
        if f(m1) > f(m2):
            lo = m1
        else:
            hi = m2
    return (lo + hi) / 2


if __name__ == "__main__":
    # f(x) = -(x-3)^2 + 10, max at x=3
    f_max = lambda x: -(x - 3) ** 2 + 10
    assert abs(ternary_search_max(f_max, -10, 10) - 3.0) < 1e-6

    # g(x) = (x+2)^2 + 1, min at x=-2
    g_min = lambda x: (x + 2) ** 2 + 1
    assert abs(ternary_search_min(g_min, -10, 10) - (-2.0)) < 1e-6
    print("[Python TernarySearch] Unimodal max/min verified.")
