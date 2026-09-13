# Code & Scripts Database

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Index](https://img.shields.io/badge/Index-Multi--Directory-green.svg)](#file-index--navigation-map)
[![Runner](https://img.shields.io/badge/Runner-Makefile-lightgrey.svg)](#execution--test-reference)

Repository index and directory navigation guide for stored source files, routines, and scripts.

---

## Directory Navigation

```
.
├── languages/                     # Language-specific source files
│   ├── 01_python/                 # Python (.py)
│   ├── 02_c/                      # C (.c)
│   ├── 03_cpp/                    # C++ (.hpp)
│   ├── 04_java/                   # Java (.java)
│   ├── 05_csharp/                 # C# (.cs)
│   ├── 06_javascript/             # JavaScript (.js)
│   ├── 07_typescript/             # TypeScript (.ts)
│   ├── 08_r/                      # R (.R)
│   ├── 09_rust/                   # Rust (.rs)
│   ├── 10_sql/                    # SQL (.sql)
│   ├── 11_golang/                 # Go (.go)
│   ├── 12_php/                    # PHP (.php)
│   ├── 13_swift/                  # Swift (.swift)
│   ├── 14_julia/                  # Julia (.jl)
│   ├── 15_ruby/                   # Ruby (.rb)
│   ├── 16_kotlin/                 # Kotlin (.kt)
│   ├── 17_matlab/                 # MATLAB (.m)
│   ├── 18_ocaml/                  # OCaml (.ml)
│   ├── 19_lua/                    # Lua (.lua)
│   ├── 20_lisp/                   # Common Lisp (.lisp)
│   ├── 21_scala/                  # Scala (.scala)
│   ├── 22_haskell/                # Haskell (.hs)
│   ├── 23_elixir/                 # Elixir (.ex)
│   └── 24_fortran/                # Fortran (.f90)
├── scripts/                       # Computational scripts by domain
│   ├── computer_science/          # Graph and text routines
│   ├── finance/                   # Valuation and cash flow routines
│   ├── mathematics/               # Number and matrix routines
│   └── physics/                   # Mechanics and tensor routines
├── Makefile                       # Execution and build harness
├── LICENSE                        # Repository license
└── README.md                      # Directory navigation index
```

---

## File Index & Navigation Map

### 1. Language Implementations (`languages/`)

| Directory | File | Runtime / Format | Primary Identifier / Symbol |
|:---|:---|:---|:---|
| `languages/01_python/` | `rk45_adaptive.py` | Python 3 | `rk45_step`, `solve_ode_rk45` |
| `languages/01_python/` | `disjoint_set.py` | Python 3 | `DisjointSetUnion` |
| `languages/02_c/` | `murmurhash3.c` | C (C99/C11) | `murmurhash3_32` |
| `languages/03_cpp/` | `lru_cache.hpp` | C++ (C++17) | `LRUCache<K, V>` |
| `languages/04_java/` | `Trie.java` | Java (JDK 17+) | `Trie`, `TrieNode` |
| `languages/05_csharp/` | `PriorityQueue.cs` | C# (.NET 8) | `PriorityQueue<T>` |
| `languages/06_javascript/` | `async_pipeline.js` | Node.js / ES2022 | `pMap`, `batchPipeline` |
| `languages/07_typescript/` | `bloom_filter.ts` | TypeScript 5 | `BloomFilter<T>` |
| `languages/08_r/` | `pca_decomposition.R` | R | `svd_pca`, `scree_ascii_plot` |
| `languages/09_rust/` | `ring_buffer.rs` | Rust (Cargo / rustc) | `SpscRingBuffer<T>` |
| `languages/10_sql/` | `sliding_window_volatility.sql` | SQL (Postgres / ANSI) | `daily_market_quotes`, analytical window |
| `languages/11_golang/` | `worker_pool.go` | Go 1.21+ | `WorkerPool`, `Process` |
| `languages/12_php/` | `EventDispatcher.php` | PHP 8.2+ | `EventDispatcher`, `ListenerProvider` |
| `languages/13_swift/` | `BinarySearchTree.swift` | Swift 5.9+ | `BinarySearchTree<Element>` |
| `languages/14_julia/` | `velocity_verlet.jl` | Julia 1.9+ | `Particle`, `velocity_verlet_step!` |
| `languages/15_ruby/` | `rate_limiter.rb` | Ruby 3.2+ | `TokenBucketRateLimiter` |
| `languages/16_kotlin/` | `FlowPipeline.kt` | Kotlin 1.9+ | `FlowPipeline`, `SharedFlow` |
| `languages/17_matlab/` | `kalman_filter.m` | MATLAB / Octave | `kalman_filter` |
| `languages/18_ocaml/` | `red_black_tree.ml` | OCaml 5.x | `MakeSet`, `balance`, `insert` |
| `languages/19_lua/` | `coroutine_scheduler.lua` | Lua 5.4 / LuaJIT | `Scheduler`, `create_task` |
| `languages/20_lisp/` | `a_star_pathfinding.lisp` | Common Lisp (SBCL) | `a-star-search`, `reconstruct-path` |
| `languages/21_scala/` | `ReactivePipeline.scala` | Scala 3 | `ReactivePipeline`, `Future` composition |
| `languages/22_haskell/` | `MonadicParser.hs` | Haskell (GHC 9.6+) | `Parser a`, `parseAndEval` |
| `languages/23_elixir/` | `priority_queue_server.ex` | Elixir / OTP | `PriorityQueueServer` |
| `languages/24_fortran/` | `conjugate_gradient.f90` | Fortran 2008 (gfortran) | `conjugate_gradient_solver` |

### 2. Computational Scripts (`scripts/`)

| Directory | File | Topic / Identifier |
|:---|:---|:---|
| `scripts/mathematics/` | `euclidean_algorithms.py` | Euclidean routines, modular inverse, lattice reduction |
| `scripts/mathematics/` | `finite_geometry_fano.py` | Finite geometry incidence matrices, Latin squares |
| `scripts/mathematics/` | `multilinear_algebra.py` | Multilinear tensor pairings and contractions |
| `scripts/mathematics/` | `perfect_numbers_factorization.py` | Prime and factor decompositions |
| `scripts/mathematics/` | `test_euclid_algorithms.py` | Mathematics verification routines |
| `scripts/mathematics/` | `test_multilinear_algebra.py` | Tensor verification routines |
| `scripts/physics/` | `curvilinear_tensors.py` | Metric tensors and coordinate transformations |
| `scripts/physics/` | `rigid_body_inertia.py` | Matrix moments and tensor diagonalization |
| `scripts/physics/` | `symbolic_euler_lagrange.py` | Variational derivative routines |
| `scripts/physics/` | `test_tensor_identities.py` | Physics verification routines |
| `scripts/finance/` | `corporate_valuation_dcf.py` | Financial statement and cash flow computations |
| `scripts/finance/` | `dividend_gordon_growth.py` | Equity return and growth factor routines |
| `scripts/computer_science/` | `k4_planar_graph.py` | Planar graph layout and crossing routines |
| `scripts/computer_science/` | `major_system_cipher.py` | Phonetic encoding lookup routines |

---

## Execution & Test Reference

Use `make` with target names to run specific scripts and test suites:

```bash
# Run all configured test targets
make test

# Target specific modules
make test-python    # Run Python scripts
make test-c         # Build and run C routines
make test-cpp       # Build and run C++ routines
make test-java      # Build and run Java routines
make test-lua       # Run Lua routines
make test-rust      # Build and run Rust routines
make test-fortran   # Build and run Fortran routines
make test-js        # Run JavaScript routines
make test-go        # Run Go routines
make test-scripts   # Run computational scripts suite
```

---

## License

MIT License. See [LICENSE](LICENSE) for details.
