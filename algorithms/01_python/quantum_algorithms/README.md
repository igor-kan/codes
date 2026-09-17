# Quantum Algorithms & Quantum Information Processing

A rigorous, typed Python library implementing core quantum algorithms, quantum error-correcting codes, circuit simulation, and quantum information protocols.

## Table of Contents

| Category | Module / Class | Theoretical Reference |
| :--- | :--- | :--- |
| **Qubit & Density Operators** | [`QubitState`](file:///home/igorkan/repos/codes/algorithms/01_python/quantum_algorithms/qubit_state.py) | Pure state $|\psi\rangle$, Born probabilities, and Bloch sphere coordinates |
| | [`DensityMatrix`](file:///home/igorkan/repos/codes/algorithms/01_python/quantum_algorithms/density_matrix.py) | Mixed states $\rho$, purity $\gamma = \text{Tr}(\rho^2)$, von Neumann entropy $S$, and partial trace |
| | [`EntanglementMeasures`](file:///home/igorkan/repos/codes/algorithms/01_python/quantum_algorithms/quantum_entanglement_measures.py) | Negativity, logarithmic negativity, and concurrence |
| **Gates & Circuits** | [`QuantumGates`](file:///home/igorkan/repos/codes/algorithms/01_python/quantum_algorithms/quantum_gates.py) | Unitary Pauli $X, Y, Z$, Hadamard $H$, Phase $S, T$, $\text{CNOT}$, $\text{CZ}$, $\text{SWAP}$ |
| | [`QuantumCircuit`](file:///home/igorkan/repos/codes/algorithms/01_python/quantum_algorithms/quantum_circuit.py) | Multi-qubit statevector propagation and Born rule measurement |
| **Algorithms** | [`DeutschJozsaAlgorithm`](file:///home/igorkan/repos/codes/algorithms/01_python/quantum_algorithms/deutsch_jozsa.py) | Constant vs balanced boolean oracle query distinction in $\mathcal{O}(1)$ |
| | [`BernsteinVaziraniAlgorithm`](file:///home/igorkan/repos/codes/algorithms/01_python/quantum_algorithms/bernstein_vazirani.py) | Deterministic hidden bitstring recovery in 1 query |
| | [`SimonAlgorithm`](file:///home/igorkan/repos/codes/algorithms/01_python/quantum_algorithms/simon_algorithm.py) | Period finding for $f(x \oplus s) = f(x)$ with exponential speedup |
| | [`QuantumFourierTransform`](file:///home/igorkan/repos/codes/algorithms/01_python/quantum_algorithms/quantum_fourier_transform.py) | $n$-qubit discrete Quantum Fourier Transform (QFT) matrix |
| | [`QuantumPhaseEstimation`](file:///home/igorkan/repos/codes/algorithms/01_python/quantum_algorithms/quantum_phase_estimation.py) | Eigenphase extraction $\theta$ for unitary operator $U$ |
| | [`ShorAlgorithm`](file:///home/igorkan/repos/codes/algorithms/01_python/quantum_algorithms/shor_algorithm.py) | Factorization of composite integers via order finding |
| | [`GroverSearch`](file:///home/igorkan/repos/codes/algorithms/01_python/quantum_algorithms/grover_search.py) | Amplitude amplification and unstructured search in $\mathcal{O}(\sqrt{N})$ |
| **Protocols & Non-Locality** | [`QuantumTeleportation`](file:///home/igorkan/repos/codes/algorithms/01_python/quantum_algorithms/quantum_teleportation.py) | Unknown state teleportation via EPR pair and 2 classical bits |
| | [`SuperdenseCoding`](file:///home/igorkan/repos/codes/algorithms/01_python/quantum_algorithms/superdense_coding.py) | Transmitting 2 classical bits with 1 physical qubit |
| | [`BellCHSHInequality`](file:///home/igorkan/repos/codes/algorithms/01_python/quantum_algorithms/bell_chsh_inequality.py) | CHSH correlator violation $S = 2\sqrt{2} > 2$ (Tsirelson bound) |
| **Quantum Error Correction** | [`Shor9QubitCode`](file:///home/igorkan/repos/codes/algorithms/01_python/quantum_algorithms/quantum_error_correction_shor9.py) | 9-qubit concatenated bit-flip and phase-flip error correction |
| | [`SteaneCode7Qubit`](file:///home/igorkan/repos/codes/algorithms/01_python/quantum_algorithms/steane_code_7qubit.py) | CSS [[7, 1, 3]] stabilizer code with Hamming parity decoding |
| | [`SurfaceCodePlaquette`](file:///home/igorkan/repos/codes/algorithms/01_python/quantum_algorithms/surface_code_plaquette.py) | Toric code star $A_s = \prod X_i$ and face $B_p = \prod Z_j$ stabilizers |
| **Variational & Optimization** | [`VQESolver`](file:///home/igorkan/repos/codes/algorithms/01_python/quantum_algorithms/vqe_ground_state.py) | Variational Quantum Eigensolver for molecular and spin ground states |
| | [`QAOAMaxCut`](file:///home/igorkan/repos/codes/algorithms/01_python/quantum_algorithms/qaoa_maxcut.py) | Quantum Approximate Optimization Algorithm for graph partitioning |
| **Walks & Wave Equations** | [`DiscreteQuantumWalk1D`](file:///home/igorkan/repos/codes/algorithms/01_python/quantum_algorithms/quantum_walk_discrete.py) | 1D Hadamard coin discrete walk demonstrating ballistic dispersion |
| | [`ContinuousQuantumWalk`](file:///home/igorkan/repos/codes/algorithms/01_python/quantum_algorithms/quantum_walk_continuous.py) | Graph Laplacian continuous walk $U(t) = \exp(-i L t)$ |
| | [`WignerFunction`](file:///home/igorkan/repos/codes/algorithms/01_python/quantum_algorithms/wigner_quasiprobability.py) | Continuous-variable phase space Wigner quasiprobability distribution |
| | [`CrankNicolsonSchrodinger`](file:///home/igorkan/repos/codes/algorithms/01_python/quantum_algorithms/schrodinger_crank_nicolson.py) | Unconditionally unitary PDE solver for 1D time-dependent Schrödinger equation |
| | [`HartreeFockRoothaan`](file:///home/igorkan/repos/codes/algorithms/01_python/quantum_algorithms/hartree_fock_roothaan.py) | Roothaan-Hall Self-Consistent Field (SCF) molecular electronic structure |
