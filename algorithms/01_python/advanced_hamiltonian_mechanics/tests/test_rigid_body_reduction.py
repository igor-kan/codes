import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from rigid_body_reduction import so3_casimir, so3_poisson_bracket

def test_casimir_bracket_vanishes():
    # Casimir bracket with any function vanishes: {C, g} = 0
    L = np.array([1.0, 2.0, 3.0])
    grad_C = 2.0 * L
    grad_g = np.array([0.5, -1.0, 0.2])
    # grad C x grad g is perpendicular to L, so L . (grad C x grad g) = 0
    assert np.isclose(so3_poisson_bracket(grad_C, grad_g, L), 0.0)
