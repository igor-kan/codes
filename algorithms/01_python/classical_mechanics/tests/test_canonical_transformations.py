"""Unit tests for Canonical Transformations."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from canonical_transformations import CanonicalTransformation


class TestCanonicalTransformations(unittest.TestCase):
    def test_identity_transformation_f2(self):
        # Identity generating function: F_2(q, P) = q . P => p = P, Q = q
        ct = CanonicalTransformation(degrees_of_freedom=2)
        f2 = lambda q, p_new: float(np.dot(q, p_new))
        q = [2.0, -3.0]
        p_new = [5.0, 7.0]
        p, q_new = ct.from_f2(f2, q, p_new)
        np.testing.assert_allclose(p, p_new, atol=1e-5)
        np.testing.assert_allclose(q_new, q, atol=1e-5)


if __name__ == "__main__":
    unittest.main()
