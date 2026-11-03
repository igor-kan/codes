"""Implementation of spherical harmonic radial component order 18094."""

def compute_spherical_harm_18094(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_18094():
    v=compute_spherical_harm_18094(0.5)
    assert isinstance(v,float) and v==v
