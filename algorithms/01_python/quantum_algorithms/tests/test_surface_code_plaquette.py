"""Unit tests for Surface Code."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from surface_code_plaquette import SurfaceCodePlaquette


class TestSurfaceCode(unittest.TestCase):
    def test_anyonic_excitation_detection(self):
        # Star operator with single flip has eigenvalue -1 (electric charge anyon)
        star_val = SurfaceCodePlaquette.star_operator_eigenvalue([1, 1, -1, 1])
        self.assertEqual(star_val, -1)


if __name__ == "__main__":
    unittest.main()
