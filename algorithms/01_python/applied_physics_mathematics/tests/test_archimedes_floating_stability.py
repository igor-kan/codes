import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from archimedes_floating_stability import metacentric_height, is_floating_stable

def test_stability_ship():
    # Wide hull: high I / V
    assert is_floating_stable(1000.0, 500.0, 1.0)
    # Top-heavy: BG very large
    assert not is_floating_stable(100.0, 500.0, 2.0)
