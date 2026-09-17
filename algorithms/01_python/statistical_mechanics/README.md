# Statistical Mechanics & Thermodynamic Simulation Algorithms

A Python library implementing classical and quantum statistical mechanics, non-equilibrium stochastic thermodynamics, and critical phenomena simulation algorithms.

## Table of Contents

| Category | Module / Class | Theoretical Reference |
| :--- | :--- | :--- |
| **Spin Models & Critical Phenomena** | [`Ising2DMetropolis`](file:///home/igorkan/repos/codes/algorithms/01_python/statistical_mechanics/ising_2d_metropolis.py) | 2D Ising model Metropolis sampling near Onsager $T_c \approx 2.269$ |
| | [`WolffIsing2D`](file:///home/igorkan/repos/codes/algorithms/01_python/statistical_mechanics/ising_wolff_cluster.py) | Wolff single-cluster algorithm with bond probability $p = 1 - e^{-2\beta J}$ |
| | [`PottsSwendsenWang`](file:///home/igorkan/repos/codes/algorithms/01_python/statistical_mechanics/potts_swendsen_wang.py) | $q$-state Potts model and Swendsen-Wang multi-cluster percolation |
| | [`TransferMatrix1D`](file:///home/igorkan/repos/codes/algorithms/01_python/statistical_mechanics/transfer_matrix_1d.py) | Exact 1D Ising chain solution via $2 \times 2$ transfer matrix eigenvalues |
| | [`LandauGinzburgMeanField`](file:///home/igorkan/repos/codes/algorithms/01_python/statistical_mechanics/mean_field_landau_ginzburg.py) | Landau-Ginzburg mean field theory and spontaneous magnetization $m \propto (T_c - T)^{1/2}$ |
| **Ensembles & Thermodynamics** | [`MicrocanonicalEntropy`](file:///home/igorkan/repos/codes/algorithms/01_python/statistical_mechanics/microcanonical_entropy.py) | Boltzmann entropy $S = k_B \ln \Omega(E)$ and temperature $1/T = \partial S / \partial E$ |
| | [`CanonicalEnsemble`](file:///home/igorkan/repos/codes/algorithms/01_python/statistical_mechanics/canonical_ensemble_gibbs.py) | Partition function $Z(\beta)$, free energy $F$, and heat capacity $C_V = k_B \beta^2 \langle(\Delta E)^2\rangle$ |
| | [`GrandCanonicalEnsemble`](file:///home/igorkan/repos/codes/algorithms/01_python/statistical_mechanics/grand_canonical_ensemble.py) | Grand potential $\Phi = -k_B T \ln \Xi$ and particle number fluctuations |
| | [`DebyeSolid`](file:///home/igorkan/repos/codes/algorithms/01_python/statistical_mechanics/debye_solid_heat_capacity.py) | Debye phonon heat capacity: $T^3$ low-temperature scaling and Dulong-Petit limit $3 N k_B$ |
| **Quantum Gases** | [`MaxwellBoltzmannGas`](file:///home/igorkan/repos/codes/algorithms/01_python/statistical_mechanics/maxwell_boltzmann_gas.py) | Classical molecular speed distribution $f(v)$, $v_p$, $\langle v \rangle$, and $v_{\text{rms}}$ |
| | [`BoseEinsteinCondensation`](file:///home/igorkan/repos/codes/algorithms/01_python/statistical_mechanics/bose_einstein_condensate.py) | Critical condensation temperature $T_c$ and condensate fraction $N_0/N = 1 - (T/T_c)^3$ |
| | [`FermiDiracGas`](file:///home/igorkan/repos/codes/algorithms/01_python/statistical_mechanics/fermi_dirac_gas.py) | Degenerate Fermi gas, Fermi energy $E_F$, and Sommerfeld linear electronic heat capacity |
| **Stochastic Processes & Non-Equilibrium** | [`LangevinDynamics`](file:///home/igorkan/repos/codes/algorithms/01_python/statistical_mechanics/langevin_dynamics_sim.py) | Langevin SDE $m \dot{v} = -\gamma v + \sqrt{2\gamma k_B T}\xi(t)$ and fluctuation-dissipation theorem |
| | [`FokkerPlanck1D`](file:///home/igorkan/repos/codes/algorithms/01_python/statistical_mechanics/fokker_planck_1d.py) | Conservative finite difference solver for 1D Fokker-Planck probability evolution |
| | [`BrownianFirstPassage`](file:///home/igorkan/repos/codes/algorithms/01_python/statistical_mechanics/brownian_first_passage_time.py) | First-passage time distribution $f(t) = \frac{a}{\sqrt{4\pi D t^3}}e^{-a^2/4Dt}$ with absorbing boundary |
| | [`GillespieAlgorithm`](file:///home/igorkan/repos/codes/algorithms/01_python/statistical_mechanics/gillespie_stochastic_chemical.py) | Direct Stochastic Simulation Algorithm (SSA) for exact chemical master equations |
| | [`JarzynskiEquality`](file:///home/igorkan/repos/codes/algorithms/01_python/statistical_mechanics/jarzynski_nonequilibrium_work.py) | Non-equilibrium work theorem $\langle e^{-\beta W} \rangle = e^{-\beta \Delta F}$ |
| | [`BoltzmannBGK1D`](file:///home/igorkan/repos/codes/algorithms/01_python/statistical_mechanics/boltzmann_transport_bgk.py) | 1D kinetic Boltzmann transport equation with Bhatnagar-Gross-Krook relaxation |
| **Molecular Dynamics & Percolation** | [`LennardJonesMD`](file:///home/igorkan/repos/codes/algorithms/01_python/statistical_mechanics/molecular_dynamics_lennard_jones.py) | NVE microcanonical molecular dynamics with velocity Verlet and periodic boundary conditions |
| | [`HoshenKopelman2D`](file:///home/igorkan/repos/codes/algorithms/01_python/statistical_mechanics/percolation_hoshen_kopelman.py) | Union-Find connected cluster labeling algorithm on 2D percolation lattices |
