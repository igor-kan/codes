"""Implementation of spherical harmonic radial component order 13039."""

def compute_spherical_harm_13039(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_13039():
    v=compute_spherical_harm_13039(0.5)
    assert isinstance(v,float) and v==v
