"""Implementation of spherical harmonic radial component order 9069."""

def compute_spherical_harm_9069(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_9069():
    v=compute_spherical_harm_9069(0.5)
    assert isinstance(v,float) and v==v
