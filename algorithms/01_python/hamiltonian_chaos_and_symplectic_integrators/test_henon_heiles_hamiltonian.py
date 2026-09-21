import numpy as np
from henon_heiles_hamiltonian import henon_heiles_hamiltonian, henon_heiles_force, px_from_energy
from yoshida_fourth_order import yoshida4_step


def test_henon_heiles_conservation():
    E_target = 0.10  # moderately chaotic regime below escape 1/6
    x0, y0, py0 = 0.0, 0.1, 0.1
    px0 = px_from_energy(E_target, x0, y0, py0)

    q = np.array([x0, y0])
    p = np.array([px0, py0])

    dt = 0.05
    for _ in range(200):
        q, p = yoshida4_step(q, p, dt, henon_heiles_force)
        E_curr = henon_heiles_hamiltonian(q[0], q[1], p[0], p[1])
        assert np.isclose(E_curr, E_target, atol=1e-5)
