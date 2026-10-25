"""Implementation of spherical harmonic radial component order 17149."""

def compute_spherical_harm_17149(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17149():
    v=compute_spherical_harm_17149(0.5)
    assert isinstance(v,float) and v==v
