"""Unit tests for Dielectric Permittivity Tensor."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dielectric_permittivity_tensor import DielectricPermittivityTensor


class TestDielectricPermittivityTensor(unittest.TestCase):
    def test_calcite_uniaxial(self):
        # Calcite: n_o = 1.658, n_e = 1.486 => eps = diag(n_o^2, n_o^2, n_e^2)
        no = 1.658
        ne = 1.486
        mat = np.diag([no**2, no**2, ne**2])
        dpt = DielectricPermittivityTensor(mat)
        self.assertEqual(dpt.optical_classification(), "uniaxial")


if __name__ == "__main__":
    unittest.main()
