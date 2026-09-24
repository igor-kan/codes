from rayleigh_benard_convection_rolls import critical_rayleigh_number_rigid


def test_ra_crit():
    ra = critical_rayleigh_number_rigid()
    assert 1700 < ra < 1715
