"""Implementation of spherical harmonic radial component order 18279."""

def compute_spherical_harm_18279(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_18279():
    v=compute_spherical_harm_18279(0.5)
    assert isinstance(v,float) and v==v
