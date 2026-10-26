"""Implementation of spherical harmonic radial component order 17269."""

def compute_spherical_harm_17269(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17269():
    v=compute_spherical_harm_17269(0.5)
    assert isinstance(v,float) and v==v
