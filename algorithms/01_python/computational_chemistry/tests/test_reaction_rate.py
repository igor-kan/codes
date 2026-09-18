import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from reaction_rate import calculate_reaction_rate, ReactionRate

class TestReactionRate(unittest.TestCase):
    def test_calculate_reaction_rate(self):
        self.assertAlmostEqual(calculate_reaction_rate(10.0), 10.0)

    def test_reaction_rate_class(self):
        obj = ReactionRate(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
