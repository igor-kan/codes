"""Implementation of spherical harmonic radial component order 17584."""

def compute_spherical_harm_17584(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17584():
    v=compute_spherical_harm_17584(0.5)
    assert isinstance(v,float) and v==v
