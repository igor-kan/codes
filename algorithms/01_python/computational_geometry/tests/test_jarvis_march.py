import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from jarvis_march import calculate_jarvis_march, JarvisMarch

class TestJarvisMarch(unittest.TestCase):
    def test_calculate_jarvis_march(self):
        self.assertAlmostEqual(calculate_jarvis_march(10.0), 10.0)

    def test_jarvis_march_class(self):
        obj = JarvisMarch(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
