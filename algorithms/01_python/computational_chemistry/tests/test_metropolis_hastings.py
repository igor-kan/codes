import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from metropolis_hastings import calculate_metropolis_hastings, MetropolisHastings

class TestMetropolisHastings(unittest.TestCase):
    def test_calculate_metropolis_hastings(self):
        self.assertAlmostEqual(calculate_metropolis_hastings(10.0), 10.0)

    def test_metropolis_hastings_class(self):
        obj = MetropolisHastings(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
