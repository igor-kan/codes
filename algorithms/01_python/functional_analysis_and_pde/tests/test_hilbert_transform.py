import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from hilbert_transform import compute_hilbert_transform

def test_hilbert_cosine_to_sine():
    # Hilbert transform of cos(t) is sin(t)
    t = np.linspace(0, 4*np.pi, 256, endpoint=False)
    x = np.cos(t)
    hx = compute_hilbert_transform(x)
    assert np.allclose(hx, np.sin(t), atol=1e-10)
