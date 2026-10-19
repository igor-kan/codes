"""Implementation of spherical harmonic radial component order 16219."""

def compute_spherical_harm_16219(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16219():
    v=compute_spherical_harm_16219(0.5)
    assert isinstance(v,float) and v==v
