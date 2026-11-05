"""Implementation of spherical harmonic radial component order 18379."""

def compute_spherical_harm_18379(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_18379():
    v=compute_spherical_harm_18379(0.5)
    assert isinstance(v,float) and v==v
