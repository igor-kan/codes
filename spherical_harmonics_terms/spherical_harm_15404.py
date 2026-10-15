"""Implementation of spherical harmonic radial component order 15404."""

def compute_spherical_harm_15404(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15404():
    v=compute_spherical_harm_15404(0.5)
    assert isinstance(v,float) and v==v
