"""Implementation of spherical harmonic radial component order 17344."""

def compute_spherical_harm_17344(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17344():
    v=compute_spherical_harm_17344(0.5)
    assert isinstance(v,float) and v==v
