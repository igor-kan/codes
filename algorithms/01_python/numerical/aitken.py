"""Aitken's delta-squared acceleration."""
def aitken(x0, x1, x2):
    denominator = x2 - 2 * x1 + x0
    if abs(denominator) < 1e-15:
        return x2
    return x2 - (x2 - x1) ** 2 / denominator


if __name__ == "__main__":
    assert abs(aitken(1.0, 0.5, 0.25)) < 1e-12
    sequence = [2 - 2 * (0.5 ** n) for n in range(3)]
    assert abs(aitken(sequence[0], sequence[1], sequence[2]) - 2.0) < 1e-12
    print("aitken ok")
