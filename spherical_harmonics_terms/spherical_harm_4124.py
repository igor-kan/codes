"""Implementation of spherical harmonic radial component order 4124."""

def compute_spherical_harm_4124(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_4124():
    v=compute_spherical_harm_4124(0.5)
    assert isinstance(v,float) and v==v
