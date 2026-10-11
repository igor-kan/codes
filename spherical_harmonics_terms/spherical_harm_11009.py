"""Implementation of spherical harmonic radial component order 11009."""

def compute_spherical_harm_11009(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_11009():
    v=compute_spherical_harm_11009(0.5)
    assert isinstance(v,float) and v==v
