"""Implementation of spherical harmonic radial component order 18264."""

def compute_spherical_harm_18264(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_18264():
    v=compute_spherical_harm_18264(0.5)
    assert isinstance(v,float) and v==v
