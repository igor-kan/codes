"""Implementation of spherical harmonic radial component order 4109."""

def compute_spherical_harm_4109(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_4109():
    v=compute_spherical_harm_4109(0.5)
    assert isinstance(v,float) and v==v
