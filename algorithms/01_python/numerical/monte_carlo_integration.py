"""Monte Carlo integration (Numerical Recipes 7.6)."""
def monte_carlo_integration(f, a, b, samples=100000, seed=42):
    state = seed
    total = 0.0
    for _ in range(samples):
        state = (1103515245 * state + 12345) % (2 ** 31)
        x = a + (b - a) * (state / (2 ** 31))
        total += f(x)
    return (b - a) * total / samples


if __name__ == "__main__":
    estimate = monte_carlo_integration(lambda x: x * x, 0.0, 1.0)
    assert abs(estimate - 1.0 / 3.0) < 0.01
    print("monte carlo integration ok")
