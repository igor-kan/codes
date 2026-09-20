import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from colored_noise_generator import generate_colored_noise

def test_colored_noise_properties():
    np.random.seed(42)
    noise = generate_colored_noise(1024, alpha=1.0)
    assert len(noise) == 1024
    assert np.isclose(np.std(noise), 1.0, atol=1e-2)
