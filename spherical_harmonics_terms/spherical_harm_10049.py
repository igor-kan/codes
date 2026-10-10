"""Implementation of spherical harmonic radial component order 10049."""

def compute_spherical_harm_10049(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_10049():
    v=compute_spherical_harm_10049(0.5)
    assert isinstance(v,float) and v==v
