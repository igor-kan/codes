import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tight_binding import calculate_tight_binding, TightBinding

class TestTightBinding(unittest.TestCase):
    def test_calculate_tight_binding(self):
        self.assertAlmostEqual(calculate_tight_binding(10.0), 10.0)

    def test_tight_binding_class(self):
        obj = TightBinding(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
