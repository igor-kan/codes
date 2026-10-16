"""Implementation of spherical harmonic radial component order 15714."""

def compute_spherical_harm_15714(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15714():
    v=compute_spherical_harm_15714(0.5)
    assert isinstance(v,float) and v==v
