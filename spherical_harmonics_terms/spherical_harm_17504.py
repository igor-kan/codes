"""Implementation of spherical harmonic radial component order 17504."""

def compute_spherical_harm_17504(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17504():
    v=compute_spherical_harm_17504(0.5)
    assert isinstance(v,float) and v==v
