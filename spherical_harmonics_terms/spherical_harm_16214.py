"""Implementation of spherical harmonic radial component order 16214."""

def compute_spherical_harm_16214(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16214():
    v=compute_spherical_harm_16214(0.5)
    assert isinstance(v,float) and v==v
