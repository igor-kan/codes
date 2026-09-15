"""Fixed-point iteration (Numerical Recipes 9.5)."""
def fixed_point(g, x, tolerance=1e-12, max_iterations=200):
    for _ in range(max_iterations):
        nxt = g(x)
        if abs(nxt - x) < tolerance:
            return nxt
        x = nxt
    return x


if __name__ == "__main__":
    root = fixed_point(lambda x: 0.5 * (x + 2 / x), 1.0)
    assert abs(root - 2 ** 0.5) < 1e-9
    print("fixed point ok")
