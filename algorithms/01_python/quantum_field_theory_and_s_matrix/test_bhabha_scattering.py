import numpy as np
from bhabha_scattering import bhabha_diff_cross_section_cm_ur


def test_bhabha_forward_peaking():
    # Forward scattering (small theta) is highly peaked due to t-channel photon pole
    s = 100.0  # 100 GeV^2
    ds_forward = bhabha_diff_cross_section_cm_ur(s, np.radians(10.0))
    ds_backward = bhabha_diff_cross_section_cm_ur(s, np.radians(90.0))
    assert ds_forward > 10.0 * ds_backward
