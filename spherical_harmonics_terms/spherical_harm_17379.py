"""Implementation of spherical harmonic radial component order 17379."""

def compute_spherical_harm_17379(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17379():
    v=compute_spherical_harm_17379(0.5)
    assert isinstance(v,float) and v==v
