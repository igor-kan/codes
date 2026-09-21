import numpy as np
from timoshenko_beam_deflection import timoshenko_midspan_deflection


def test_timoshenko_vs_euler():
    # For a slender beam (L >> h), shear deflection is negligible
    E = 200.0e9
    G = 80.0e9
    b = 0.1
    h = 0.1
    L_slender = 5.0
    w_e, w_s, w_tot = timoshenko_midspan_deflection(1000.0, L_slender, E, G, b, h)
    assert w_s / w_e < 0.01  # less than 1% shear correction

    # For a deep beam (L ~ h), shear deflection is significant
    L_deep = 0.3
    w_ed, w_sd, _ = timoshenko_midspan_deflection(1000.0, L_deep, E, G, b, h)
    assert w_sd / w_ed > 0.10
