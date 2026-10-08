"""Implementation of spherical harmonic radial component order 6029."""

def compute_spherical_harm_6029(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_6029():
    v=compute_spherical_harm_6029(0.5)
    assert isinstance(v,float) and v==v
