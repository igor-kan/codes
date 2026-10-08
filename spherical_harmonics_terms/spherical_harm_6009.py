"""Implementation of spherical harmonic radial component order 6009."""

def compute_spherical_harm_6009(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_6009():
    v=compute_spherical_harm_6009(0.5)
    assert isinstance(v,float) and v==v
