# Physics Tensors & Differential Geometry Algorithms

A comprehensive, rigorously typed library implementing tensor calculus, differential geometry, and physical tensor representations across General Relativity, Electrodynamics, Continuum Mechanics, and Material Physics.

## Overview

This module provides data structures and mathematical algorithms for rank-$k$ tensors with explicit tracking of covariant and contravariant indices, metric index lowering/raising, and physical tensor fields:

| Category | Tensor / Object | Description |
| :--- | :--- | :--- |
| **Foundations** | [`Tensor`](file:///home/igorkan/repos/codes/algorithms/01_python/physics_tensors/tensor_base.py) | General multi-index tensor with valence $(p, q)$, contractions, and tensor products |
| | [`MetricTensor`](file:///home/igorkan/repos/codes/algorithms/01_python/physics_tensors/metric_tensor.py) | Metric $g_{\mu\nu}$, inverse $g^{\mu\nu}$, signatures, and line elements $ds^2$ |
| | [`MinkowskiSpacetime`](file:///home/igorkan/repos/codes/algorithms/01_python/physics_tensors/minkowski_metric.py) | Flat spacetime metric $\eta_{\mu\nu}$, Lorentz boosts, and 4-vectors |
| **Curvature & Gravitation** | [`ChristoffelSymbols`](file:///home/igorkan/repos/codes/algorithms/01_python/physics_tensors/christoffel_symbols.py) | Affine connection coefficients $\Gamma^\lambda_{\mu\nu}$ and geodesic acceleration |
| | [`RiemannCurvatureTensor`](file:///home/igorkan/repos/codes/algorithms/01_python/physics_tensors/riemann_curvature_tensor.py) | Rank-4 Riemann tensor $R^\rho{}_{\sigma\mu\nu}$ with algebraic symmetry verification |
| | [`BianchiIdentities`](file:///home/igorkan/repos/codes/algorithms/01_python/physics_tensors/bianchi_identities.py) | Algebraic and contracted differential Bianchi identities $\nabla_\mu G^{\mu\nu} = 0$ |
| | [`RicciCurvature`](file:///home/igorkan/repos/codes/algorithms/01_python/physics_tensors/ricci_tensor_and_scalar.py) | Ricci tensor $R_{\mu\nu}$, curvature scalar $R$, and traceless Ricci tensor |
| | [`EinsteinTensor`](file:///home/igorkan/repos/codes/algorithms/01_python/physics_tensors/einstein_tensor.py) | Field tensor $G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2} R g_{\mu\nu} + \Lambda g_{\mu\nu}$ |
| | [`WeylCurvatureTensor`](file:///home/igorkan/repos/codes/algorithms/01_python/physics_tensors/weyl_tensor.py) | Conformal curvature tensor $C_{\rho\sigma\mu\nu}$ and conformal flatness check |
| | [`KretschmannScalar`](file:///home/igorkan/repos/codes/algorithms/01_python/physics_tensors/kretschmann_scalar.py) | Invariant curvature scalar $K = R^{abcd} R_{abcd}$ for singularity diagnostics |
| | [`TorsionTensor`](file:///home/igorkan/repos/codes/algorithms/01_python/physics_tensors/torsion_tensor.py) | Cartan torsion tensor $T^\lambda{}_{\mu\nu}$ in Einstein-Cartan gravity |
| | [`KillingTensor`](file:///home/igorkan/repos/codes/algorithms/01_python/physics_tensors/killing_tensor.py) | First and second rank Killing tensors and geodesic constants of motion |
| | [`LandauLifshitzPseudotensor`](file:///home/igorkan/repos/codes/algorithms/01_python/physics_tensors/landau_lifshitz_pseudotensor.py) | Gravitational energy-momentum pseudotensor $t_{\text{LL}}^{\mu\nu}$ |
| **Exact Spacetimes** | [`SchwarzschildMetric`](file:///home/igorkan/repos/codes/algorithms/01_python/physics_tensors/schwarzschild_metric.py) | Static spherically symmetric black hole, perihelion precession, and light bending |
| | [`KerrMetric`](file:///home/igorkan/repos/codes/algorithms/01_python/physics_tensors/kerr_metric.py) | Rotating black hole in Boyer-Lindquist coordinates, ergosphere, and frame dragging |
| | [`FLRWMetric`](file:///home/igorkan/repos/codes/algorithms/01_python/physics_tensors/flrw_metric.py) | Friedmann-Lemaître-Robertson-Walker cosmological metric and Friedmann acceleration |
| **Electrodynamics** | [`ElectromagneticFieldTensor`](file:///home/igorkan/repos/codes/algorithms/01_python/physics_tensors/electromagnetic_field_tensor.py) | Faraday 2-form $F_{\mu\nu}$, dual tensor $\tilde{F}^{\mu\nu}$, and Lorentz invariants |
| | [`MaxwellStressTensor`](file:///home/igorkan/repos/codes/algorithms/01_python/physics_tensors/maxwell_stress_tensor.py) | 3D Maxwell stress tensor $\sigma_{ij}$, Poynting flux vector $\mathbf{S}$, and energy density |
| | [`LeviCivitaTensor`](file:///home/igorkan/repos/codes/algorithms/01_python/physics_tensors/levi_civita_tensor.py) | Permutation symbols $\epsilon_{ijk}, \epsilon_{\mu\nu\rho\sigma}$ and Hodge star $\star$ |
| | [`VanDerWaerdenSymbols`](file:///home/igorkan/repos/codes/algorithms/01_python/physics_tensors/spinor_metric_van_der_waerden.py) | Infeld-van der Waerden symbols $\sigma^\mu_{A\dot{B}}$ and two-component Weyl spinors |
| **Mechanics & Continuum** | [`InertiaTensor`](file:///home/igorkan/repos/codes/algorithms/01_python/physics_tensors/inertia_tensor.py) | Rotational inertia tensor $I_{ij}$, principal axes diagonalization, and Steiner's theorem |
| | [`CauchyStressTensor`](file:///home/igorkan/repos/codes/algorithms/01_python/physics_tensors/cauchy_stress_tensor.py) | 3D Cauchy stress, hydrostatic/deviatoric split, and von Mises yield stress |
| | [`InfinitesimalStrainTensor`](file:///home/igorkan/repos/codes/algorithms/01_python/physics_tensors/infinitesimal_strain_tensor.py) | Symmetric strain tensor $\varepsilon_{ij}$ and antisymmetric rotation tensor $\omega_{ij}$ |
| | [`ElasticityStiffnessTensor`](file:///home/igorkan/repos/codes/algorithms/01_python/physics_tensors/elasticity_stiffness_tensor.py) | Rank-4 elasticity tensor $C_{ijkl}$, Voigt $6 \times 6$ notation, and Lamé parameters |
| | [`PiezoelectricTensor`](file:///home/igorkan/repos/codes/algorithms/01_python/physics_tensors/piezoelectric_tensor.py) | Rank-3 piezoelectric tensor $d_{ijk}$ linking polarization to stress |
| | [`ViscousStressTensor`](file:///home/igorkan/repos/codes/algorithms/01_python/physics_tensors/viscous_stress_tensor.py) | Navier-Stokes viscous deviatoric stress $\tau_{ij}$ and viscous dissipation rate $\Phi$ |
| **Material & Field Physics** | [`GyrationTensor`](file:///home/igorkan/repos/codes/algorithms/01_python/physics_tensors/gyration_tensor.py) | Macromolecular radius of gyration tensor $S_{mn}$, asphericity, and acylindricity |
| | [`QuadrupoleMomentTensor`](file:///home/igorkan/repos/codes/algorithms/01_python/physics_tensors/quadrupole_moment_tensor.py) | Traceless quadrupole tensor $Q_{ij}$ and gravitational wave emission power $\dot{E}$ |
| | [`DiffusionTensor`](file:///home/igorkan/repos/codes/algorithms/01_python/physics_tensors/diffusion_tensor.py) | Anisotropic diffusion tensor $D_{ij}$ and fractional anisotropy (FA) in DTI |
| | [`DielectricPermittivityTensor`](file:///home/igorkan/repos/codes/algorithms/01_python/physics_tensors/dielectric_permittivity_tensor.py) | Permittivity tensor $\boldsymbol{\varepsilon}_r$, optical indicatrix, and birefringence |
| | [`MagneticSusceptibilityTensor`](file:///home/igorkan/repos/codes/algorithms/01_python/physics_tensors/magnetic_susceptibility_tensor.py) | Magnetic susceptibility tensor $\chi_{ij}$ and magnetic anisotropy energy |
| | [`StressEnergyTensor`](file:///home/igorkan/repos/codes/algorithms/01_python/physics_tensors/stress_energy_tensor.py) | Perfect fluid $T^{\mu\nu}$, relativistic radiation, dust, and vacuum energy |
