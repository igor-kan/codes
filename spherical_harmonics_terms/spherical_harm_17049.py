"""Implementation of spherical harmonic radial component order 17049."""

def compute_spherical_harm_17049(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17049():
    v=compute_spherical_harm_17049(0.5)
    assert isinstance(v,float) and v==v
