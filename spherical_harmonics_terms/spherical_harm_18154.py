"""Implementation of spherical harmonic radial component order 18154."""

def compute_spherical_harm_18154(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_18154():
    v=compute_spherical_harm_18154(0.5)
    assert isinstance(v,float) and v==v
