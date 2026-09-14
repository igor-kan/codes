"""Hypothesis testing with a normal approximation z-test."""
import math


def z_test(sample_mean: float, mu0: float, sigma: float, n: int) -> float:
    standard_error = sigma / math.sqrt(n)
    return (sample_mean - mu0) / standard_error


def two_sided_p_value(z: float) -> float:
    # Normal CDF via the error function.
    return 2 * (1 - 0.5 * (1 + math.erf(abs(z) / math.sqrt(2))))


def reject_null(z: float, alpha: float = 0.05) -> bool:
    return two_sided_p_value(z) < alpha


if __name__ == "__main__":
    z = z_test(sample_mean=5.2, mu0=5.0, sigma=1.0, n=100)
    assert abs(z - 2.0) < 1e-9
    assert reject_null(z, alpha=0.05)
    assert not reject_null(1.0, alpha=0.05)
    print(f"z={z:.2f} p={two_sided_p_value(z):.4f}")
