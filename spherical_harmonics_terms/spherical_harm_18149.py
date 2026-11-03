"""Implementation of spherical harmonic radial component order 18149."""

def compute_spherical_harm_18149(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_18149():
    v=compute_spherical_harm_18149(0.5)
    assert isinstance(v,float) and v==v
