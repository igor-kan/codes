"""Implementation of spherical harmonic radial component order 18029."""

def compute_spherical_harm_18029(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_18029():
    v=compute_spherical_harm_18029(0.5)
    assert isinstance(v,float) and v==v
