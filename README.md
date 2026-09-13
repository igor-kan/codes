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

| Top-Level Directory | Description | Primary Languages |
|:---|:---|:---|
| `algorithms/` | Multi-language algorithmic test suites & reference implementations | Python, C, C++, Rust, Go, Java, Fortran |
| `architectures/` | System design patterns, distributed systems, compilers, OS designs | C, C++, Go, Dart, Rust |
| `scripts/` | Ingestion utilities and sparse-checkout helpers | Python, Bash |
| `languages/01_python/` | SymPy, SciPy, Astropy, CPython objects | Python |
| `languages/02_c/` | Linux kernel, curl, gcc, SQLite, PostgreSQL, CPython VM | C |
| `languages/03_cpp/` | LLVM, Clang, V8, Zig std | C++ |
| `languages/04_java/` | Apache Flink, Kafka, OpenJDK base | Java |
| `languages/05_csharp/` | .NET BCL (CoreFX, runtime shims) | C# |
| `languages/06_javascript/` | D3.js, Lodash, Node.js lib | JavaScript |
| `languages/07_typescript/` | RxJS | TypeScript |
| `languages/08_r/` | R base / core (parser, main, libraries) | R |
| `languages/09_rust/` | Rust compiler, hashbrown, std lib, ripgrep, tokio | Rust |
| `languages/10_sql/` | SQL reference examples | SQL |
| `languages/11_golang/` | Go std lib, crypto, Kubernetes client & pkg, etcd/raft | Go |
| `languages/12_php/` | Zend engine, PHP extensions | PHP |
| `languages/13_swift/` | Swift stdlib, algorithms, compatibility toolchain | Swift |
| `languages/14_julia/` | Julia stdlib, ODE solvers, ForwardDiff, Distributions, Combinatorics | Julia |
| `languages/15_ruby/` | Ruby stdlib, RubyGems, C extensions | Ruby |
| `languages/16_kotlin/` | Kotlin stdlib (JVM, JS, WASM targets) | Kotlin |
| `languages/17_matlab/` | MATLAB reference scripts | MATLAB |
| `languages/18_ocaml/` | OCaml stdlib & parser | OCaml |
| `languages/19_lua/` | Lua 5.4 core | Lua |
| `languages/20_lisp/` | AIMA Lisp, Clojure core | Common Lisp, Clojure |
| `languages/21_scala/` | Cats (FP), Apache Spark | Scala |
| `languages/22_haskell/` | base lib, containers, GHC compiler | Haskell |
| `languages/23_elixir/` | Elixir stdlib | Elixir |
| `languages/24_fortran/` | Fortran stdlib | Fortran |
| `languages/25_lean4/` | Lean 4 mathlib4, std | Lean 4 |

## Polyglot Language Directory Index

| Directory | Language | Included Canonical Systems & Libraries |
|:---|:---|:---|
| `languages/01_python/` | Python | SciPy, AstroPy, CPython standard library, SymPy, scikit-learn |
| `languages/02_c/` | C | Linux Kernel Core (mm, fs, net, crypto), FreeBSD Subsystems, PostgreSQL Engine, SQLite, curl, GCC Optimizer Core |
| `languages/03_cpp/` | C++ | LLVM Optimizer, Clang AST, LLD Linker, DuckDB, ClickHouse DBMS, V8 Engine, PyTorch ATen, TensorFlow Core, Zig Std |
| `languages/04_java/` | Java | OpenJDK `java.base`, Apache Kafka Distributed Commit Log, Apache Flink Stream Engine, Google Guava, Commons Math |
| `languages/05_csharp/` | C# | .NET Base Class Library (BCL: System.Collections, Numerics, Memory, Threading, Text, Security) |
| `languages/06_javascript/` | JavaScript | Node.js Core Modules, Lodash, D3 Data-Driven Documents |
| `languages/07_typescript/` | TypeScript | TypeScript Compiler & Typechecker, RxJS Reactive Extensions |
| `languages/08_r/` | R | R Core Interpretation Engine & Standard Statistical Packages |
| `languages/09_rust/` | Rust | Rust Standard Library (`core`, `alloc`, `std`), Rustc Compiler Internals, Tokio Async Engine, Ripgrep |
| `languages/10_sql/` | SQL | PostgreSQL Schemas (Pagila), Analytical dbt Data Warehouse Models |
| `languages/11_golang/` | Go | Go Standard Library & Runtime, Kubernetes Core Controllers & Client-Go, etcd Raft Engine |
| `languages/12_php/` | PHP | PHP Zend Virtual Machine Engine & Core Standard Extensions |
| `languages/13_swift/` | Swift | Swift Standard Library, Swift Compiler & SIL Optimizer, Swift Algorithms |
| `languages/14_julia/` | Julia | Julia Standard Library & Numerical Runtime, OrdinaryDiffEq.jl, Distributions.jl |
| `languages/15_ruby/` | Ruby | Ruby Standard Library & Core C Extensions |
| `languages/16_kotlin/` | Kotlin | Kotlin Standard Library, Coroutine-ready Data Structures |
| `languages/17_matlab/` | MATLAB / Octave | Numerical Linear Algebra, Signal Processing Algorithms |
| `languages/18_ocaml/` | OCaml | OCaml Standard Library, Lexer & Parser Subsystems |
| `languages/19_lua/` | Lua | Lua Interpreter, Virtual Machine, and Incremental Garbage Collector |
| `languages/20_lisp/` | Common Lisp / Clojure | Clojure Standard Library, Common Lisp Competitive Algorithms, AIMA AI Implementations |
| `languages/21_scala/` | Scala | Apache Spark Distributed Computing Engine (Core, SQL, MLlib, Streaming, GraphX), Cats |
| `languages/22_haskell/` | Haskell | Glasgow Haskell Compiler (GHC), Haskell Base Library, Containers |
| `languages/23_elixir/` | Elixir | Elixir Standard Library, Actor Concurrency Primitives |
| `languages/24_fortran/` | Fortran | Fortran-lang Standard Library (stdlib), High-Performance BLAS / Matrix Routines |
| `languages/25_lean4/` | Lean 4 | Lean 4 Mathlib Formal Mathematics, Category Theory, Topology, and Logic Solvers |

---

## Upstream Licenses & Attribution

All imported code preserves original author attributions, notices, and copyright statements. Complete upstream repository links, author organizations, and license terms are detailed in [SOURCES.md](SOURCES.md).

---

© 2026 Igor Kan
