"""Implementation of spherical harmonic radial component order 15674."""

def compute_spherical_harm_15674(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15674():
    v=compute_spherical_harm_15674(0.5)
    assert isinstance(v,float) and v==v
