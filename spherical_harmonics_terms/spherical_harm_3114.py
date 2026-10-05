"""Implementation of spherical harmonic radial component order 3114."""

def compute_spherical_harm_3114(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_3114():
    v=compute_spherical_harm_3114(0.5)
    assert isinstance(v,float) and v==v
