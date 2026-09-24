from percolation_bethe_lattice import bethe_percolation_threshold


def test_bethe():
    p_c = bethe_percolation_threshold(z_coordination=3)
    assert p_c == 0.5
