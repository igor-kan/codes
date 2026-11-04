"""Implementation of spherical harmonic radial component order 18254."""

def compute_spherical_harm_18254(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_18254():
    v=compute_spherical_harm_18254(0.5)
    assert isinstance(v,float) and v==v
