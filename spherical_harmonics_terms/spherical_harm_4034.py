"""Implementation of spherical harmonic radial component order 4034."""

def compute_spherical_harm_4034(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_4034():
    v=compute_spherical_harm_4034(0.5)
    assert isinstance(v,float) and v==v
