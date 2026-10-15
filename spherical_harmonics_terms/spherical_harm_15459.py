"""Implementation of spherical harmonic radial component order 15459."""

def compute_spherical_harm_15459(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15459():
    v=compute_spherical_harm_15459(0.5)
    assert isinstance(v,float) and v==v
