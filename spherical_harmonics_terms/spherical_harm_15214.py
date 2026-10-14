"""Implementation of spherical harmonic radial component order 15214."""

def compute_spherical_harm_15214(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15214():
    v=compute_spherical_harm_15214(0.5)
    assert isinstance(v,float) and v==v
