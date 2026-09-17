# Fluid Dynamics & Continuum Aerodynamics Algorithms

A Python computational library implementing foundational fluid mechanics, boundary layer theory, turbulent closures, shock wave jump conditions, and hydrodynamic instability analysis.

## Table of Contents

| Category | Module / Class | Theoretical Reference |
| :--- | :--- | :--- |
| **Navier-Stokes & Mesoscopic** | [`VorticityStreamfunction2D`](file:///home/igorkan/repos/codes/algorithms/01_python/fluid_dynamics/navier_stokes_2d_vorticity_streamfunction.py) | 2D incompressible Navier-Stokes in vorticity-streamfunction formulation |
| | [`LatticeBoltzmannD2Q9`](file:///home/igorkan/repos/codes/algorithms/01_python/fluid_dynamics/lattice_boltzmann_d2q9.py) | Lattice Boltzmann Method (LBM) with D2Q9 velocity stencil and BGK collision |
| | [`ReynoldsTransport`](file:///home/igorkan/repos/codes/algorithms/01_python/fluid_dynamics/reynolds_transport_theorem.py) | Reynolds Transport Theorem for deforming material control volumes |
| | [`RANSBoussinesq`](file:///home/igorkan/repos/codes/algorithms/01_python/fluid_dynamics/reynolds_averaged_navier_stokes.py) | Reynolds-Averaged Navier-Stokes with Boussinesq turbulent eddy viscosity closure |
| **Exact Flows & Boundary Layers** | [`BernoulliEquation`](file:///home/igorkan/repos/codes/algorithms/01_python/fluid_dynamics/bernoulli_flow.py) | Streamline energy conservation, Venturi tube effect, and Torricelli efflux |
| | [`BlasiusBoundaryLayer`](file:///home/igorkan/repos/codes/algorithms/01_python/fluid_dynamics/blasius_boundary_layer.py) | Laminar boundary layer non-linear ODE $2f''' + ff'' = 0$ over a flat plate |
| | [`ExactLaminarFlows`](file:///home/igorkan/repos/codes/algorithms/01_python/fluid_dynamics/couette_poiseuille_flow.py) | Plane Couette, plane Poiseuille, and Hagen-Poiseuille pipe flow profiles |
| **Compressible Flow & Shocks** | [`RankineHugoniotShock`](file:///home/igorkan/repos/codes/algorithms/01_python/fluid_dynamics/shock_jump_rankine_hugoniot.py) | 1D normal shock wave jump conditions and Mach number relations |
| | [`SodShockTubeBenchmark`](file:///home/igorkan/repos/codes/algorithms/01_python/fluid_dynamics/sod_shock_tube_riemann_solver.py) | Exact Riemann solver for Sod's shock tube benchmark problem |
| | [`AcousticHelmholtz`](file:///home/igorkan/repos/codes/algorithms/01_python/fluid_dynamics/acoustic_wave_equation_helmholtz.py) | Linear acoustic wave equation, characteristic impedance $Z = \rho c$, and wavenumber |
| **Geophysical & Free Surface** | [`ShallowWater1D`](file:///home/igorkan/repos/codes/algorithms/01_python/fluid_dynamics/shallow_water_equations_1d.py) | 1D Saint-Venant shallow water equations, gravity wave speed $c = \sqrt{gh}$, and Froude number |
| **Potential Flow & Aerodynamics** | [`ComplexPotentialFlow`](file:///home/igorkan/repos/codes/algorithms/01_python/fluid_dynamics/potential_flow_complex.py) | 2D complex potential $W(z)$, cylinder with circulation, and Kutta-Joukowski lift $L' = \rho U \Gamma$ |
| | [`ThinAirfoilTheory`](file:///home/igorkan/repos/codes/algorithms/01_python/fluid_dynamics/vortex_panel_method_airfoil.py) | Discrete vortex panel method and thin airfoil lift slope $c_l = 2\pi(\alpha - \alpha_0)$ |
| **Hydrodynamic Instabilities** | [`RayleighTaylorInstability`](file:///home/igorkan/repos/codes/algorithms/01_python/fluid_dynamics/rayleigh_taylor_instability.py) | Interfacial instability between fluids of different densities under gravity |
| | [`KelvinHelmholtzInstability`](file:///home/igorkan/repos/codes/algorithms/01_python/fluid_dynamics/kelvin_helmholtz_instability.py) | Shear layer interface instability and vortex sheet growth rate |
