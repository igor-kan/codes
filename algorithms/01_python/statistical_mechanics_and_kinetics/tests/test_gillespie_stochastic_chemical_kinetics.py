from gillespie_stochastic_chemical_kinetics import gillespie_birth_death


def test_gillespie():
    times, counts = gillespie_birth_death(10.0, 1.0, 0, 5.0)
    assert len(times) > 0
    assert counts[-1] > 0
