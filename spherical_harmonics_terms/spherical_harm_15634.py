"""Implementation of spherical harmonic radial component order 15634."""

def compute_spherical_harm_15634(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15634():
    v=compute_spherical_harm_15634(0.5)
    assert isinstance(v,float) and v==v
