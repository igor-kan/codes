"""Unit tests for Contact Geometry."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from contact_geometry import ContactGeometry


class TestContactGeometry(unittest.TestCase):
    def test_reeb_field_normalization(self):
        cg = ContactGeometry(degrees_of_freedom=1)
        r = cg.reeb_vector_field()
        # Evaluate alpha(R) with q=0, p=0, ds=1, dq=0, dp=0
        val = cg.standard_contact_form(q=[0.0], p=[0.0], ds=1.0, dq=[0.0], dp=[0.0])
        self.assertAlmostEqual(val, 1.0)


if __name__ == "__main__":
    unittest.main()
