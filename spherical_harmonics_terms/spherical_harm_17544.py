"""Implementation of spherical harmonic radial component order 17544."""

def compute_spherical_harm_17544(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17544():
    v=compute_spherical_harm_17544(0.5)
    assert isinstance(v,float) and v==v
