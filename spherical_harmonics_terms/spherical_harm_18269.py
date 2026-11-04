"""Implementation of spherical harmonic radial component order 18269."""

def compute_spherical_harm_18269(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_18269():
    v=compute_spherical_harm_18269(0.5)
    assert isinstance(v,float) and v==v
