import numpy as np
from rayleigh_buoyancy_interface_mhd import atwood_number, rayleigh_buoyancy_growth_rate


def test_buoyancy_instability():
    rho1 = 1.0
    rho2 = 3.0
    g = 9.81
    k = 2.0

    assert atwood_number(rho1, rho2) == 0.5
    # Unmagnetized has positive growth rate
    gamma_unmag = rayleigh_buoyancy_growth_rate(rho1, rho2, g, k, B_parallel=0.0)
    assert gamma_unmag > 0

    # Heavy magnetic field completely suppresses RT mode
    gamma_mag = rayleigh_buoyancy_growth_rate(rho1, rho2, g, k, B_parallel=0.05)
    assert gamma_mag == 0.0
