import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from hodge_dual_forms import hodge_dual_2form_minkowski

def test_double_hodge_dual():
    # In 4D Lorentzian signature, **F = -F for 2-forms
    F = np.zeros((4, 4))
    F[0, 1] = -2.0; F[1, 0] = 2.0
    F[2, 3] = 1.5; F[3, 2] = -1.5
    
    star_F = hodge_dual_2form_minkowski(F)
    star_star_F = hodge_dual_2form_minkowski(star_F)
    assert np.allclose(star_star_F, -F)
