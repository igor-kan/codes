import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ramsey_arrow_partition import ramsey_r33

def test_ramsey():
    assert ramsey_r33() == 6
