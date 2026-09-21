import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from nuclear_shell_model import is_doubly_magic, is_magic_nucleus

def test_lead_208():
    # Lead-208 has Z=82, N=126 -> Doubly magic
    assert is_doubly_magic(82, 126)
    assert is_magic_nucleus(20, 20)  # Calcium-40
