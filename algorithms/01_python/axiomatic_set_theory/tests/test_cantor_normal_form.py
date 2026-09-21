import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cantor_normal_form import format_cantor_normal_form

def test_formatting():
    cnf = [(2, 3), (1, 1), (0, 5)]
    s = format_cantor_normal_form(cnf)
    assert s == "w^2*3 + w + 5"
