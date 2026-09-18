import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tolman_oppenheimer_volkoff import calculate_tolman_oppenheimer_volkoff, TolmanOppenheimerVolkoff

class TestTolmanOppenheimerVolkoff(unittest.TestCase):
    def test_calculate_tolman_oppenheimer_volkoff(self):
        self.assertAlmostEqual(calculate_tolman_oppenheimer_volkoff(10.0), 10.0)

    def test_tolman_oppenheimer_volkoff_class(self):
        obj = TolmanOppenheimerVolkoff(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
