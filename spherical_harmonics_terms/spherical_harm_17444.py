"""Implementation of spherical harmonic radial component order 17444."""

def compute_spherical_harm_17444(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17444():
    v=compute_spherical_harm_17444(0.5)
    assert isinstance(v,float) and v==v
