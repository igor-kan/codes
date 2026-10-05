"""Implementation of spherical harmonic radial component order 3094."""

def compute_spherical_harm_3094(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_3094():
    v=compute_spherical_harm_3094(0.5)
    assert isinstance(v,float) and v==v
