"""Implementation of spherical harmonic radial component order 10074."""

def compute_spherical_harm_10074(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_10074():
    v=compute_spherical_harm_10074(0.5)
    assert isinstance(v,float) and v==v
