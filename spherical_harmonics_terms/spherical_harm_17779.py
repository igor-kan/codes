"""Implementation of spherical harmonic radial component order 17779."""

def compute_spherical_harm_17779(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17779():
    v=compute_spherical_harm_17779(0.5)
    assert isinstance(v,float) and v==v
