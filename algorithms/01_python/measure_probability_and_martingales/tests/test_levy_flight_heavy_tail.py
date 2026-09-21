import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from levy_flight_heavy_tail import simulate_levy_steps

def test_levy_shape():
    steps = simulate_levy_steps(alpha=1.5, n_steps=500, seed=42)
    assert len(steps) == 500
