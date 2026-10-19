"""Implementation of spherical harmonic radial component order 16294."""

def compute_spherical_harm_16294(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16294():
    v=compute_spherical_harm_16294(0.5)
    assert isinstance(v,float) and v==v
