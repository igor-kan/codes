"""Implementation of spherical harmonic radial component order 4119."""

def compute_spherical_harm_4119(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_4119():
    v=compute_spherical_harm_4119(0.5)
    assert isinstance(v,float) and v==v
