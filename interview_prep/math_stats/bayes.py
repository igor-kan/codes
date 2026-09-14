"""Bayes' theorem and base-rate reasoning."""


def bayes(prior: float, likelihood: float, false_positive: float) -> float:
    """P(disease | positive) from P(disease), P(+ | disease), P(+ | healthy)."""
    evidence = likelihood * prior + false_positive * (1 - prior)
    return likelihood * prior / evidence


def sequential_update(prior: float, likelihood: float, false_positive: float, tests: int) -> float:
    posterior = prior
    for _ in range(tests):
        posterior = bayes(posterior, likelihood, false_positive)
    return posterior


if __name__ == "__main__":
    # A rare disease (1 in 1000) with a 99% sensitive and 5% false-positive test.
    posterior = bayes(prior=0.001, likelihood=0.99, false_positive=0.05)
    assert 0.01 < posterior < 0.05
    assert sequential_update(0.001, 0.99, 0.05, 2) > posterior
    print(f"posterior after one positive: {posterior:.4f}")
