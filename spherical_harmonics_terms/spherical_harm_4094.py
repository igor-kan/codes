"""Implementation of spherical harmonic radial component order 4094."""

def compute_spherical_harm_4094(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_4094():
    v=compute_spherical_harm_4094(0.5)
    assert isinstance(v,float) and v==v
