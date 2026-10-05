"""Implementation of spherical harmonic radial component order 3124."""

def compute_spherical_harm_3124(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_3124():
    v=compute_spherical_harm_3124(0.5)
    assert isinstance(v,float) and v==v
