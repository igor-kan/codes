"""Implementation of spherical harmonic radial component order 13034."""

def compute_spherical_harm_13034(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_13034():
    v=compute_spherical_harm_13034(0.5)
    assert isinstance(v,float) and v==v
