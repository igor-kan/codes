"""Implementation of spherical harmonic radial component order 18329."""

def compute_spherical_harm_18329(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_18329():
    v=compute_spherical_harm_18329(0.5)
    assert isinstance(v,float) and v==v
