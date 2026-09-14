# codes

Comprehensive polyglot code repository, foundational algorithms, system kernels, compilers, and architectural patterns.

---

## Local Storage Optimization & Sparse-Checkout

This repository contains over **3.0 GB** of curated codebases and 400,000+ files safely preserved on GitHub. To keep your local machine footprint minimal (< 50 MB), the repository utilizes Git's native **Sparse-Checkout** mechanism.

### Quick Checkout Commands

Use the helper utility `scripts/sparse_checkout.sh`:

```bash
# 1. Reset local checkout to minimal footprint (< 50 MB: algorithms, architectures, scripts)
./scripts/sparse_checkout.sh minimal

# 2. Check out a specific language or system to local disk on demand
./scripts/sparse_checkout.sh add languages/01_python
./scripts/sparse_checkout.sh add languages/02_c/linux_kernel
./scripts/sparse_checkout.sh add languages/09_rust

# 3. Remove a language or system from local disk (safely preserved on GitHub remote)
./scripts/sparse_checkout.sh remove languages/02_c/linux_kernel

# 4. View current local checked-out directories
./scripts/sparse_checkout.sh status

# 5. List all available modules in the repository
./scripts/sparse_checkout.sh list
```

---

## Directory Index

| Top-Level Directory | Description | See |
|:---|:---|:---|
| `algorithms/` | Polyglot algorithm reference implementations across 25 languages | [algorithms/README.md](algorithms/README.md) |
| `architectures/` | Design patterns, concurrency primitives, distributed patterns | [architectures/README.md](architectures/README.md) |
| `scripts/` | Computational scripts (math, physics, ML, finance) and utilities | `scripts/` |
| `languages/` | Upstream source code from major open-source projects (sparse checkout) | `languages/` |

---

## Multi-Language Algorithms Suite

The `algorithms/` directory hosts standalone, production-ready algorithm implementations across all 25 canonical languages. Each language directory (`01_python/` through `25_lean4/`) contains implementations organized by category: sorting, graphs, dynamic programming, strings, data structures, math, cryptography, and machine learning.

Full coverage matrix: [algorithms/README.md](algorithms/README.md)

| # | Directory | Language | Key Algorithms |
|:--|:---|:---|:---|
| 1 | `algorithms/01_python/` | Python | 5 sorts, 12 graph algos (BFS/DFS/Dijkstra/A*/Kosaraju/ConvexHull/TopoSort), 7 DP, FFT, Miller-Rabin, Strassen, KMP, Huffman, k-means, Caesar |
| 2 | `algorithms/02_c/` | C | 3 sorts, BFS/DFS/Dijkstra, DP, KMP, 4 data structures, Miller-Rabin, matmul_tiled |
| 3 | `algorithms/03_cpp/` | C++ | 2 sorts, BFS/Dijkstra/A*/Kosaraju/ConvexHull/TopoSort, FFT, Huffman, KMP, k-means |
| 4 | `algorithms/04_java/` | Java | 3 sorts, BFS/Dijkstra/A*, SegmentTree, Trie, KMP, Huffman, MathUtils |
| 5 | `algorithms/05_csharp/` | C# | 3 sorts, BFS/DFS/Dijkstra, DP, KMP, Trie, math |
| 6 | `algorithms/06_javascript/` | JavaScript | 3 sorts, BFS/Dijkstra, DP, KMP, math |
| 7 | `algorithms/07_typescript/` | TypeScript | 2 sorts, BFS, DP (LCS+Levenshtein), KMP, math |
| 8 | `algorithms/08_r/` | R | 3 sorts, BFS/DFS/Dijkstra, DP, KMP, k-means, math |
| 9 | `algorithms/09_rust/` | Rust | 3 sorts, BFS/DFS/Dijkstra/A*/ConvexHull/TopoSort, Trie, FFT, Huffman, Miller-Rabin, Caesar, Vigenere |
| 10 | `algorithms/10_sql/` | SQL | 6 analytical query patterns (recursive CTEs, windows, gaps & islands, pivots) |
| 11 | `algorithms/11_golang/` | Go | 3 sorts, BFS/DFS/Dijkstra/A*/Kosaraju/ConvexHull/TopoSort, Trie, Stack, Worker Pool, KMP |
| 12 | `algorithms/12_php/` | PHP | 2 sorts, BFS/Dijkstra, LCS, KMP, Trie, math |
| 13 | `algorithms/13_swift/` | Swift | 2 sorts, BFS, LCS, KMP, Trie, math |
| 14 | `algorithms/14_julia/` | Julia | 2 sorts, BFS, LCS, FFT, linear regression, math |
| 15 | `algorithms/15_ruby/` | Ruby | 2 sorts, BFS/Dijkstra, LCS, KMP, math |
| 16 | `algorithms/16_kotlin/` | Kotlin | 2 sorts, BFS, LCS, KMP, Trie, math |
| 17 | `algorithms/17_matlab/` | MATLAB | 2 sorts, BFS, LCS, KMP, math |
| 18 | `algorithms/18_ocaml/` | OCaml | Merge sort, Quick sort, BFS, LCS, KMP, math |
| 19 | `algorithms/19_lua/` | Lua | Bubble sort, BFS, LCS, Knapsack, KMP, math |
| 20 | `algorithms/20_lisp/` | Common Lisp | Bubble sort, BFS, LCS, KMP, math |
| 21 | `algorithms/21_scala/` | Scala | 2 sorts, BFS, LCS, math |
| 22 | `algorithms/22_haskell/` | Haskell | 2 sorts, BFS, LCS (naive + DP), math |
| 23 | `algorithms/23_elixir/` | Elixir | 2 sorts, BFS, LCS, math |
| 24 | `algorithms/24_fortran/` | Fortran | Bubble sort, BFS, Knapsack, GCD, matmul_blocked |
| 25 | `algorithms/25_lean4/` | Lean 4 | GCD (computational + formal proof), Fibonacci, Insertion sort, BFS (with termination proofs) |

---

## Polyglot Language Directory Index

| Directory | Language | Included Canonical Systems & Libraries |
|:---|:---|:---|
| `languages/01_python/` | Python | SciPy, AstroPy, CPython standard library, SymPy, scikit-learn |
| `languages/02_c/` | C | Linux Kernel Core (mm, fs, net, crypto), FreeBSD Subsystems, PostgreSQL Engine, SQLite, curl, GCC Optimizer Core |
| `languages/03_cpp/` | C++ | LLVM Optimizer, Clang AST, LLD Linker, DuckDB, ClickHouse DBMS, V8 Engine, PyTorch ATen, TensorFlow Core, Zig Std |
| `languages/04_java/` | Java | OpenJDK `java.base`, Apache Kafka, Apache Flink, Google Guava, Commons Math |
| `languages/05_csharp/` | C# | .NET Base Class Library |
| `languages/06_javascript/` | JavaScript | Node.js Core Modules, Lodash, D3 |
| `languages/07_typescript/` | TypeScript | TypeScript Compiler & Typechecker, RxJS |
| `languages/08_r/` | R | R Core Interpretation Engine & Standard Statistical Packages |
| `languages/09_rust/` | Rust | Rust Standard Library, Rustc Compiler Internals, Tokio, Ripgrep |
| `languages/10_sql/` | SQL | PostgreSQL Schemas, Analytical dbt Models |
| `languages/11_golang/` | Go | Go Standard Library & Runtime, Kubernetes, etcd Raft |
| `languages/12_php/` | PHP | PHP Zend VM Engine & Core Standard Extensions |
| `languages/13_swift/` | Swift | Swift Standard Library, Swift Compiler & SIL Optimizer |
| `languages/14_julia/` | Julia | Julia Standard Library, OrdinaryDiffEq.jl, Distributions.jl |
| `languages/15_ruby/` | Ruby | Ruby Standard Library & Core C Extensions |
| `languages/16_kotlin/` | Kotlin | Kotlin Standard Library, Coroutine-ready Data Structures |
| `languages/17_matlab/` | MATLAB / Octave | Numerical Linear Algebra, Signal Processing |
| `languages/18_ocaml/` | OCaml | OCaml Standard Library, Lexer & Parser |
| `languages/19_lua/` | Lua | Lua Interpreter, Virtual Machine, Incremental GC |
| `languages/20_lisp/` | Common Lisp / Clojure | Clojure Standard Library, AIMA AI Implementations |
| `languages/21_scala/` | Scala | Apache Spark, Cats |
| `languages/22_haskell/` | Haskell | Glasgow Haskell Compiler (GHC), Haskell Base Library |
| `languages/23_elixir/` | Elixir | Elixir Standard Library, Actor Concurrency Primitives |
| `languages/24_fortran/` | Fortran | Fortran-lang Standard Library, BLAS / Matrix Routines |
| `languages/25_lean4/` | Lean 4 | Mathlib Formal Mathematics, Category Theory, Topology |

---

## Architectures

Design patterns across the Gang of Four (GoF), concurrency primitives, and distributed systems patterns. Full index: [architectures/README.md](architectures/README.md)

| Directory | Content |
|:---|:---|
| `architectures/cpp_patterns/` | 24 GoF patterns in classic C++ |
| `architectures/go_patterns/` | 24 GoF patterns with tests in Go |
| `architectures/python_patterns/` | GoF + pythonic patterns with linting and pytest |
| `architectures/java_patterns/` | Builder and Observer demos |
| `architectures/concurrency_patterns/` | Actor models, thread pools, worker pools |
| `architectures/distributed_patterns/` | Consistent hashing, circuit breaker |
| `architectures/typescript_patterns/` | Middleware pipeline, repository pattern |

---

## Scripts

Computational scripts across multiple domains:

| Domain | Scripts |
|:---|:---|
| `mathematics/` | Euclidean algorithms, finite geometry (Fano plane), multilinear algebra, perfect numbers |
| `physics/` | Curvilinear tensors, rigid body inertia, symbolic Euler-Lagrange |
| `machine_learning/` | k-means clustering, logistic regression |
| `finance/` | Corporate valuation (DCF), dividend growth models |
| `numerical_analysis/` | Root finding (bisection, Newton-Raphson, Brent) |
| `computer_science/` | K4 planar graphs, Major system cipher |
| `distributed_systems/` | Consistent hashing ring |

Utilities: `sparse_checkout.sh` (git sparse checkout manager), `ingest_10x.py` (bulk upstream ingestion).

---

## Build & Test

```bash
# Run everything
make test

# Run specific suites
make test-python        # Python algorithms
make test-c             # C algorithms
make test-cpp           # C++ algorithms
make test-java          # Java algorithms
make test-rust          # Rust algorithms
make test-go            # Go algorithms
make test-scripts       # Computational scripts
make test-algorithms    # All polyglot algorithm suites
make test-architectures # Design patterns and concurrency

# Clean build artifacts
make clean
```

---

## Upstream Licenses & Attribution

All imported code preserves original author attributions, notices, and copyright statements. Complete upstream repository links, author organizations, and license terms are detailed in [SOURCES.md](SOURCES.md).

---

© 2026 Igor Kan