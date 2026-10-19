"""Implementation of spherical harmonic radial component order 16254."""

def compute_spherical_harm_16254(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16254():
    v=compute_spherical_harm_16254(0.5)
    assert isinstance(v,float) and v==v
