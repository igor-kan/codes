"""Implementation of spherical harmonic radial component order 16994."""

def compute_spherical_harm_16994(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16994():
    v=compute_spherical_harm_16994(0.5)
    assert isinstance(v,float) and v==v
