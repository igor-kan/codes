"""Golden-section search for a 1D minimum (Numerical Recipes 10.1)."""
def golden_section(f, a: float, b: float, tol: float = 1e-9, iterations: int = 200) -> float:
    inv_phi = (5 ** 0.5 - 1) / 2
    c = b - inv_phi * (b - a)
    d = a + inv_phi * (b - a)
    fc, fd = f(c), f(d)
    for _ in range(iterations):
        if b - a < tol:
            break
        if fc < fd:
            b, d, fd = d, c, fc
            c = b - inv_phi * (b - a)
            fc = f(c)
        else:
            a, c, fc = c, d, fd
            d = a + inv_phi * (b - a)
            fd = f(d)
    return (a + b) / 2


if __name__ == "__main__":
    assert abs(golden_section(lambda x: (x - 3) ** 2, -10, 10) - 3) < 1e-6
    print("golden section ok")
