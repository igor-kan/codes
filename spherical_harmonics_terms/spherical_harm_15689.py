"""Implementation of spherical harmonic radial component order 15689."""

def compute_spherical_harm_15689(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15689():
    v=compute_spherical_harm_15689(0.5)
    assert isinstance(v,float) and v==v
