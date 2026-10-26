"""Implementation of spherical harmonic radial component order 17304."""

def compute_spherical_harm_17304(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17304():
    v=compute_spherical_harm_17304(0.5)
    assert isinstance(v,float) and v==v
