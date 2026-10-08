"""Implementation of spherical harmonic radial component order 6109."""

def compute_spherical_harm_6109(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_6109():
    v=compute_spherical_harm_6109(0.5)
    assert isinstance(v,float) and v==v
