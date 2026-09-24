import numpy as np
from vasicek_interest_rate_model import vasicek_bond_price


def test_vasicek():
    P = vasicek_bond_price(r=0.03, tau=1.0, a=0.2, b=0.05, sigma=0.01)
    # Bond price with positive interest rate should be < 1.0 and > 0.0
    assert 0.0 < P < 1.0
