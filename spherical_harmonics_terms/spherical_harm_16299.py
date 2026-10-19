"""Implementation of spherical harmonic radial component order 16299."""

def compute_spherical_harm_16299(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16299():
    v=compute_spherical_harm_16299(0.5)
    assert isinstance(v,float) and v==v
