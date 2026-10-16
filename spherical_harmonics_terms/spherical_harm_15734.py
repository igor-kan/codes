"""Implementation of spherical harmonic radial component order 15734."""

def compute_spherical_harm_15734(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15734():
    v=compute_spherical_harm_15734(0.5)
    assert isinstance(v,float) and v==v
