"""Probability fundamentals: sample spaces, union, conditional, independence."""
from itertools import product

SAMPLE_SPACE = list(product([1, 2, 3, 4, 5, 6], repeat=2))


def prob(event) -> float:
    return sum(1 for outcome in SAMPLE_SPACE if event(outcome)) / len(SAMPLE_SPACE)


def union(a, b) -> float:
    return prob(lambda o: a(o) or b(o))


if __name__ == "__main__":
    is_seven = lambda o: o[0] + o[1] == 7
    is_double = lambda o: o[0] == o[1]
    assert abs(union(is_seven, is_double) - (6 + 6 - 0) / 36) < 1e-9
    p_seven = prob(is_seven)
    p_double_given_seven = prob(lambda o: is_double(o)) and 0
    assert abs(p_seven - 1 / 6) < 1e-9
    print(f"P(sum=7)={p_seven:.4f}")
