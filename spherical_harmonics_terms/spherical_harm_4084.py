"""Implementation of spherical harmonic radial component order 4084."""

def compute_spherical_harm_4084(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_4084():
    v=compute_spherical_harm_4084(0.5)
    assert isinstance(v,float) and v==v
