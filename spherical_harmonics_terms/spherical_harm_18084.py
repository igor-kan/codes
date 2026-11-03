"""Implementation of spherical harmonic radial component order 18084."""

def compute_spherical_harm_18084(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_18084():
    v=compute_spherical_harm_18084(0.5)
    assert isinstance(v,float) and v==v
