"""Steffensen's method (Aitken-accelerated fixed point)."""
def steffensen(g, x, tolerance=1e-12, max_iterations=100):
    for _ in range(max_iterations):
        x1 = g(x)
        x2 = g(x1)
        denominator = x2 - 2 * x1 + x
        if abs(denominator) < 1e-15:
            return x2
        nxt = x - (x1 - x) ** 2 / denominator
        if abs(nxt - x) < tolerance:
            return nxt
        x = nxt
    return x


if __name__ == "__main__":
    root = steffensen(lambda x: 0.5 * (x + 2 / x), 1.0)
    assert abs(root - 2 ** 0.5) < 1e-12
    print("steffensen ok")
