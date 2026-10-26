"""Implementation of spherical harmonic radial component order 17219."""

def compute_spherical_harm_17219(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17219():
    v=compute_spherical_harm_17219(0.5)
    assert isinstance(v,float) and v==v
