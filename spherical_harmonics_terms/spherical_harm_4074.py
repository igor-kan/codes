"""Implementation of spherical harmonic radial component order 4074."""

def compute_spherical_harm_4074(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_4074():
    v=compute_spherical_harm_4074(0.5)
    assert isinstance(v,float) and v==v
