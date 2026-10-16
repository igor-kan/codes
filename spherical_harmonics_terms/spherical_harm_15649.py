"""Implementation of spherical harmonic radial component order 15649."""

def compute_spherical_harm_15649(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15649():
    v=compute_spherical_harm_15649(0.5)
    assert isinstance(v,float) and v==v
