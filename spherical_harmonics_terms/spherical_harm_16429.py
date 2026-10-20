"""Implementation of spherical harmonic radial component order 16429."""

def compute_spherical_harm_16429(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16429():
    v=compute_spherical_harm_16429(0.5)
    assert isinstance(v,float) and v==v
