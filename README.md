# Computational Polyglot Algorithms (`computational-polyglot-algorithms`)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Languages](https://img.shields.io/badge/Languages-24%20Polyglot-success.svg)](#supported-languages-matrix)
[![Mathematics](https://img.shields.io/badge/Domain-Scientific%20%26%20Mathematical-orange.svg)](#quarto-site-algorithms)

> **The Definitive Multi-Language Computational & Algorithmic Masterclass.**  
> Bridging theoretical physics, pure mathematics, corporate finance, and system architecture published on [Igor Kan's Quarto Research Site](https://igor-kan.github.io/quarto-writing/) with authentic, high-performance implementations across **24 major programming languages**.

---

## Architectural Philosophy: Language Strengths & Domain Affinities

Programming languages are not merely interchangeable syntax; they embody fundamentally different **computational models**, **memory semantics**, and **type-theoretic guarantees**:

1. **Bare-Metal & Systems (C, C++, Rust, Fortran):** Zero-cost abstractions, deterministic memory allocation, vectorization (SIMD), and mechanical sympathy for high-performance physics, cryptanalysis, and HPC.
2. **Scientific & Numerical Computing (Python, Julia, MATLAB, R):** First-class array primitives, differential equations, symplectic dynamics, and linear algebraic decomposition.
3. **Purely Functional & Type-Theoretic (Haskell, OCaml, Scala, Lisp):** Referential transparency, immutable algebraic data types, monadic parsing, and compile-time proofs of correctness.
4. **Concurrent, Reactive & Actor Systems (Go, Elixir, Kotlin, JavaScript):** Asynchronous event loops, CSP channels, actor message queues, and backpressure pipelines.
5. **Enterprise & Object-Oriented (Java, C#, Swift, PHP):** Robust generic collections, interface polymorphism, Sequence protocols, and PSR design standards.
6. **Declarative & Analytical (SQL):** Relational algebra, sliding window functions, and set-theoretic data transformations.

---

## 24-Language Algorithmic Matrix

| # | Language | Extension | Category / Paradigm | Implemented Module | Key Algorithmic & Architectural Focus |
|---|----------|-----------|---------------------|--------------------|---------------------------------------|
| 1 | **Python** | `.py` | Dynamic / Numerical | `rk45_adaptive.py`, `disjoint_set.py` | Adaptive Runge-Kutta-Fehlberg ODE integrator & Disjoint Set Union (DSU) |
| 2 | **C** | `.c` | Systems / Procedural | `murmurhash3.c`, `euclid_hpc.c` | High-performance non-cryptographic MurmurHash3 & SIMD binary GCD |
| 3 | **C++** | `.hpp` | Systems / Generic | `lru_cache.hpp` | Thread-safe generic LRU Cache using STL `std::list` & `std::unordered_map` |
| 4 | **Java** | `.java` | Enterprise / OOP | `Trie.java` | Prefix tree (Trie) with dictionary word search and prefix autocomplete |
| 5 | **C#** | `.cs` | Managed / Generic | `PriorityQueue.cs` | Generic binary heap min-priority queue with `IComparable<T>` |
| 6 | **JavaScript** | `.js` | Web / Asynchronous | `async_pipeline.js` | Concurrency-bounded asynchronous map and batch execution pipeline |
| 7 | **TypeScript** | `.ts` | Static / Structural | `bloom_filter.ts` | Probabilistic Bloom filter with optimal double-hashing distribution |
| 8 | **R** | `.R` | Statistical / Vectorized | `pca_decomposition.R` | SVD Principal Component Analysis, variance ratios & scree plots |
| 9 | **Rust** | `.rs` | Memory-Safe Systems | `ring_buffer.rs`, `avl_tree.rs` | Lock-free atomic ring buffer (SPSC) & self-balancing AVL search tree |
| 10 | **SQL** | `.sql` | Declarative / Relational | `sliding_window_volatility.sql` | Sliding window analytical functions for 20/50 SMA & annualized volatility |
| 11 | **Golang** | `.go` | Concurrent / CSP | `worker_pool.go` | Concurrent worker pool with channels, wait groups, and context cancellation |
| 12 | **PHP** | `.php` | Web / Modern OOP | `EventDispatcher.php` | PSR-14 compliant event dispatcher with priority listeners and sorting |
| 13 | **Swift** | `.swift` | Systems / Protocol-Oriented | `BinarySearchTree.swift` | Generic BST conforming to Swift's standard `Sequence` protocol |
| 14 | **Julia** | `.jl` | Technical / Multiple Dispatch | `velocity_verlet.jl` | Symplectic velocity-Verlet integrator preserving Hamiltonian phase space |
| 15 | **Ruby** | `.rb` | Dynamic / Object-Oriented | `rate_limiter.rb` | Thread-safe token bucket rate limiter with monotonic clock & burst smoothing |
| 16 | **Kotlin** | `.kt` | Modern JVM / Coroutines | `FlowPipeline.kt` | Coroutines SharedFlow reactive pipeline with backpressure buffer |
| 17 | **MATLAB** | `.m` | Matrix / Engineering | `kalman_filter.m` | Discrete linear time-invariant Kalman filter with optimal Kalman gain |
| 18 | **OCaml** | `.ml` | Functional / Type-Inference | `red_black_tree.ml` | Chris Okasaki purely functional red-black tree with 4-case rebalancing |
| 19 | **Lua** | `.lua` | Embedded / Coroutines | `coroutine_scheduler.lua` | Cooperative multitasking green-thread scheduler using coroutines |
| 20 | **Common Lisp** | `.lisp` | Symbolic / Multi-Paradigm | `a_star_pathfinding.lisp` | Common Lisp A* heuristic graph pathfinding with Manhattan distance |
| 21 | **Scala** | `.scala` | Functional / JVM | `ReactivePipeline.scala` | Functional reactive data pipeline with immutable case classes & Futures |
| 22 | **Haskell** | `.hs` | Purely Functional / Monadic | `MonadicParser.hs` | Hutton-Meijer monadic parser combinator library for arithmetic AST |
| 23 | **Elixir** | `.ex` | Actor / Fault-Tolerant OTP | `priority_queue_server.ex` | Supervised OTP GenServer priority message queue with `:queue` serialization |
| 24 | **Fortran** | `.f90` | Scientific / HPC (Fortran 2008) | `conjugate_gradient.f90` | Krylov subspace conjugate gradient iterative linear solver |

---

## Quarto Website Synchronized Algorithms

Extracted, expanded, and production-hardened from research articles on the Quarto site:
* **`quarto_website_code/mathematics/`**:
  * Euclidean Algorithm, Stein's Binary GCD, Extended Bézout Identity, and 2D Gauss-Lagrange Lattice Reduction.
  * Multilinear Algebra: Dual Space Pairings, Einstein Summation, Tensor Contractions, SVD Eckart-Young, and Tucker HOSVD.
  * Finite Geometries: $AG(2, q)$ and $PG(2, q)$ Fano Plane Incidence Matrices, Mutually Orthogonal Latin Squares (MOLS), and Bruck-Ryser-Chowla Number-Theoretic Sieve.
  * Number Theory: Mersenne Primes and Euclid-Euler Perfect Number Decompositions.
* **`quarto_website_code/physics/`**:
  * Levi-Civita Epsilon-Delta Contractions, Metric Determinants, and Curvilinear Coordinate Scales.
  * Symplectic Hamiltonian Phase-Space Volume Conservation.
  * Rigid Body 3D Inertia Tensor Diagonalization and Principal Axes of Rotation.
  * Variational Mechanics Symbolic Euler-Lagrange Equations Generator.
* **`quarto_website_code/finance/`**:
  * Corporate Financial Statement Modeling: P&L Waterfall, Working Capital, and Unlevered Free Cash Flow (FCFF).
  * DuPont 3-Step Return on Equity (ROE) Decomposition.
  * Weighted Average Cost of Capital (WACC) & Two-Stage Discounted Cash Flow (DCF) Valuation.
* **`quarto_website_code/computer_science/`**:
  * Complete Graph $K_4$ Planar Drawing, Fáry's Theorem, and Crossing Numbers.
  * Mnemonic Phonetic Major System and PAO Cipher Mapping.

---

## Repository Structure

```
computational-polyglot-algorithms/
├── languages/                    # 24 Polyglot language implementations
│   ├── 01_python/
│   ├── 02_c/
│   ├── 03_cpp/
│   ├── 04_java/
│   ├── 05_csharp/
│   ├── 06_javascript/
│   ├── 07_typescript/
│   ├── 08_r/
│   ├── 09_rust/
│   ├── 10_sql/
│   ├── 11_golang/
│   ├── 12_php/
│   ├── 13_swift/
│   ├── 14_julia/
│   ├── 15_ruby/
│   ├── 16_kotlin/
│   ├── 17_matlab/
│   ├── 18_ocaml/
│   ├── 19_lua/
│   ├── 20_lisp/
│   ├── 21_scala/
│   ├── 22_haskell/
│   ├── 23_elixir/
│   └── 24_fortran/
├── quarto_website_code/          # Research algorithms from Quarto site
│   ├── mathematics/
│   ├── physics/
│   ├── finance/
│   └── computer_science/
├── tests/                        # Polyglot verification harnesses
├── Makefile                      # Universal build and verification runner
├── LICENSE
└── README.md
```

---

## Verification & Testing Suite

The repository includes a comprehensive master `Makefile` executing smoke tests, builds, and invariant verifications across the polyglot stack:

```bash
# Run all locally available polyglot test suites:
make test

# Or run language-specific verification targets:
make test-python    # Verifies Adaptive RK45 ODE Integrator and Disjoint Set Union
make test-c         # Compiles & executes non-cryptographic MurmurHash3
make test-cpp       # Compiles & executes thread-safe template LRU Cache
make test-java      # Compiles & runs Trie prefix autocomplete
make test-rust      # Compiles & tests SPSC Atomic Ring Buffer
make test-fortran   # Compiles & executes Fortran 2008 Conjugate Gradient solver
make test-js        # Executes concurrency-bounded async pipeline
make test-go        # Runs concurrent worker pool with channel synchronization
make test-lua       # Executes cooperative coroutine green-thread scheduler
make test-quarto    # Runs full suite of mathematics, physics, finance & CS algorithms
```

---

## License & Attribution

Authored by **Igor Kan** (© 2026). Released under the [MIT License](LICENSE).
