import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from shallow_water_1d import shallow_water_step

def test_dam_break_step():
    h = np.where(np.arange(50) < 25, 2.0, 1.0)
    hu = np.zeros(50)
    h_next, hu_next = shallow_water_step(h, hu, dx=0.1, dt=0.001)
    assert np.all(h_next > 0.0)
