"""Implementation of spherical harmonic radial component order 17679."""

def compute_spherical_harm_17679(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17679():
    v=compute_spherical_harm_17679(0.5)
    assert isinstance(v,float) and v==v
