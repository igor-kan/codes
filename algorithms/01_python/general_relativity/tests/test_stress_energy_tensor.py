import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from stress_energy_tensor import calculate_stress_energy_tensor, StressEnergyTensor

class TestStressEnergyTensor(unittest.TestCase):
    def test_calculate_stress_energy_tensor(self):
        self.assertAlmostEqual(calculate_stress_energy_tensor(10.0), 10.0)

    def test_stress_energy_tensor_class(self):
        obj = StressEnergyTensor(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
