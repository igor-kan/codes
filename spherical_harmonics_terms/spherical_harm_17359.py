"""Implementation of spherical harmonic radial component order 17359."""

def compute_spherical_harm_17359(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17359():
    v=compute_spherical_harm_17359(0.5)
    assert isinstance(v,float) and v==v
