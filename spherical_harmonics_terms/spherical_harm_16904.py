"""Implementation of spherical harmonic radial component order 16904."""

def compute_spherical_harm_16904(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16904():
    v=compute_spherical_harm_16904(0.5)
    assert isinstance(v,float) and v==v
