import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from twistor_kinematics import Twistor

def test_null_twistor():
    # If omega is orthogonal to pi_prime in the hermitian sense
    omega = np.array([1.0j, 0.0])
    pi_prime = np.array([0.0, 1.0])
    z = Twistor(omega, pi_prime)
    assert z.is_null()
    assert np.isclose(z.helicity(), 0.0)

def test_non_null_twistor():
    omega = np.array([1.0, 0.0])
    pi_prime = np.array([1.0, 0.0])
    z = Twistor(omega, pi_prime)
    assert not z.is_null()
    assert np.isclose(z.helicity(), 1.0)
