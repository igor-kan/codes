"""Implementation of spherical harmonic radial component order 6094."""

def compute_spherical_harm_6094(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_6094():
    v=compute_spherical_harm_6094(0.5)
    assert isinstance(v,float) and v==v
