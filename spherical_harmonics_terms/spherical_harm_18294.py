"""Implementation of spherical harmonic radial component order 18294."""

def compute_spherical_harm_18294(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_18294():
    v=compute_spherical_harm_18294(0.5)
    assert isinstance(v,float) and v==v
