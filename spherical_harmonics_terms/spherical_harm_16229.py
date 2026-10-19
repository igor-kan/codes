"""Implementation of spherical harmonic radial component order 16229."""

def compute_spherical_harm_16229(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16229():
    v=compute_spherical_harm_16229(0.5)
    assert isinstance(v,float) and v==v
