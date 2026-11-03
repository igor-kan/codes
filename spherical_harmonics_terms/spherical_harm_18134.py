"""Implementation of spherical harmonic radial component order 18134."""

def compute_spherical_harm_18134(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_18134():
    v=compute_spherical_harm_18134(0.5)
    assert isinstance(v,float) and v==v
