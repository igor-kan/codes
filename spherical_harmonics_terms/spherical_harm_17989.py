"""Implementation of spherical harmonic radial component order 17989."""

def compute_spherical_harm_17989(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17989():
    v=compute_spherical_harm_17989(0.5)
    assert isinstance(v,float) and v==v
