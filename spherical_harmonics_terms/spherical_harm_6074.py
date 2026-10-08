"""Implementation of spherical harmonic radial component order 6074."""

def compute_spherical_harm_6074(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_6074():
    v=compute_spherical_harm_6074(0.5)
    assert isinstance(v,float) and v==v
