"""Unit tests for Jarzynski Equality."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from jarzynski_nonequilibrium_work import JarzynskiEquality


class TestJarzynski(unittest.TestCase):
    def test_quasistatic_limit(self):
        # In reversible process, all W = Delta F
        works = np.full(50, 4.0)
        df = JarzynskiEquality.free_energy_difference(works, beta=1.0)
        self.assertAlmostEqual(df, 4.0)


if __name__ == "__main__":
    unittest.main()
