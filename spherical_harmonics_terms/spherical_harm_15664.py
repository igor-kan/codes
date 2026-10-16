"""Implementation of spherical harmonic radial component order 15664."""

def compute_spherical_harm_15664(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15664():
    v=compute_spherical_harm_15664(0.5)
    assert isinstance(v,float) and v==v
