import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from hartree_fock_scf import helium_hartree_fock_energy

def test_helium_ground_state():
    e = helium_hartree_fock_energy(1.6875, Z=2.0)
    # Exact variational energy is -2.84765625 a.u.
    assert np.isclose(e, -2.84765625)
