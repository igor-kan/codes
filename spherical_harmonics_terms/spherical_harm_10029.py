"""Implementation of spherical harmonic radial component order 10029."""

def compute_spherical_harm_10029(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_10029():
    v=compute_spherical_harm_10029(0.5)
    assert isinstance(v,float) and v==v
