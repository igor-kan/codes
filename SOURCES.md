# Upstream Open-Source Citations and Licenses

This repository incorporates open-source implementations, benchmarks, foundational algorithms, system kernels, compilers, and architectural patterns from external projects. In accordance with open-source licensing compliance, full upstream attribution and license details are documented below.

None of the imported code originates from private or personal repositories; all assets are derived strictly from public open-source software under permissive or standard open-source licenses (MIT, Apache-2.0, BSD-3-Clause, ISC, EPL, Public Domain, PSF).

---

## Source Directory Index

| Upstream Project | Remote URL | Author / Organization | License | Local Destination |
|:---|:---|:---|:---|:---|
| **TheAlgorithms/Python** | `https://github.com/TheAlgorithms/Python` | TheAlgorithms Community | MIT | `languages/01_python/algorithms/` |
| **SymPy** | `https://github.com/sympy/sympy` | SymPy Development Team | BSD-3-Clause | `languages/01_python/sympy/` |
| **scikit-learn** | `https://github.com/scikit-learn/scikit-learn` | scikit-learn developers | BSD-3-Clause | `languages/01_python/scikit_learn/` |
| **SciPy** | `https://github.com/scipy/scipy` | SciPy Developers | BSD-3-Clause | `languages/01_python/scipy/` |
| **AstroPy** | `https://github.com/astropy/astropy` | The Astropy Developers | BSD-3-Clause | `languages/01_python/astropy/` |
| **CPython Standard Library** | `https://github.com/python/cpython` | Python Software Foundation | PSF-2.0 | `languages/01_python/cpython_lib/` |
| **TheAlgorithms/C** | `https://github.com/TheAlgorithms/C` | TheAlgorithms Community | MIT | `languages/02_c/algorithms/` |
| **Linux Kernel Core** | `https://github.com/torvalds/linux` | Linus Torvalds & Kernel Authors | GPL-2.0 w/ syscall note | `languages/02_c/linux_kernel/` |
| **FreeBSD Subsystems** | `https://github.com/freebsd/freebsd-src` | The FreeBSD Project | BSD-2-Clause | `languages/02_c/freebsd_sys/` |
| **PostgreSQL Engine** | `https://github.com/postgres/postgres` | PostgreSQL Global Development Group | PostgreSQL / BSD | `languages/02_c/postgres/` |
| **SQLite** | `https://github.com/sqlite/sqlite` | D. Richard Hipp & SQLite Team | Public Domain | `languages/02_c/sqlite/` |
| **Redis** | `https://github.com/redis/redis` | Redis Authors & Community | BSD-3-Clause | `languages/02_c/redis/` |
| **Libsodium** | `https://github.com/jedisct1/libsodium` | Frank Denis & Libsodium Authors | ISC | `languages/02_c/libsodium/` |
| **curl** | `https://github.com/curl/curl` | Daniel Stenberg & curl Contributors | MIT/curl | `languages/02_c/curl/` |
| **CPython VM & Objects** | `https://github.com/python/cpython` | Python Software Foundation | PSF-2.0 | `languages/02_c/cpython_vm/`, `cpython_objects/` |
| **GCC Optimizer Core** | `https://github.com/gcc-mirror/gcc` | Free Software Foundation, Inc. | GPL-3.0 w/ Runtime Exception | `languages/02_c/gcc_optimizer/` |
| **TheAlgorithms/C-Plus-Plus** | `https://github.com/TheAlgorithms/C-Plus-Plus` | TheAlgorithms Community | MIT | `languages/03_cpp/algorithms/` |
| **LLVM Optimizer & Backend** | `https://github.com/llvm/llvm-project` | LLVM Project Authors | Apache-2.0 w/ LLVM Exception | `languages/03_cpp/llvm/` |
| **Clang AST & Parser** | `https://github.com/llvm/llvm-project` | LLVM Project Authors | Apache-2.0 w/ LLVM Exception | `languages/03_cpp/clang/` |
| **LLD Linker** | `https://github.com/llvm/llvm-project` | LLVM Project Authors | Apache-2.0 w/ LLVM Exception | `languages/03_cpp/lld/` |
| **DuckDB Analytical Engine** | `https://github.com/duckdb/duckdb` | DuckDB Foundation | MIT | `languages/03_cpp/duckdb/` |
| **ClickHouse DBMS** | `https://github.com/ClickHouse/ClickHouse` | ClickHouse, Inc. | Apache-2.0 | `languages/03_cpp/clickhouse/` |
| **PyTorch ATen & C10** | `https://github.com/pytorch/pytorch` | PyTorch Authors | BSD-3-Clause | `languages/03_cpp/pytorch_aten/`, `pytorch_c10/` |
| **V8 JavaScript & Wasm** | `https://github.com/v8/v8` | The V8 Project Authors | BSD-3-Clause | `languages/03_cpp/v8_engine/` |
| **TensorFlow Machine Learning** | `https://github.com/tensorflow/tensorflow` | The TensorFlow Authors | Apache-2.0 | `languages/03_cpp/tensorflow_core/` |
| **Zig Standard Library** | `https://github.com/ziglang/zig` | Zig Software Foundation | MIT | `languages/03_cpp/zig_std/` |
| **Abseil C++** | `https://github.com/abseil/abseil-cpp` | Google LLC | Apache-2.0 | `languages/03_cpp/abseil/` |
| **JSON for Modern C++** | `https://github.com/nlohmann/json` | Niels Lohmann | MIT | `languages/03_cpp/nlohmann_json/` |
| **Protocol Buffers** | `https://github.com/protocolbuffers/protobuf` | Google LLC | BSD-3-Clause | `languages/03_cpp/protobuf/` |
| **TheAlgorithms/Java** | `https://github.com/TheAlgorithms/Java` | TheAlgorithms Community | MIT | `languages/04_java/algorithms/` |
| **OpenJDK java.base** | `https://github.com/openjdk/jdk` | Oracle and/or its affiliates | GPL-2.0 w/ Classpath Exception | `languages/04_java/openjdk_base/` |
| **Apache Kafka** | `https://github.com/apache/kafka` | Apache Software Foundation | Apache-2.0 | `languages/04_java/kafka/` |
| **Apache Flink** | `https://github.com/apache/flink` | Apache Software Foundation | Apache-2.0 | `languages/04_java/flink/` |
| **Google Guava** | `https://github.com/google/guava` | Google LLC | Apache-2.0 | `languages/04_java/guava/` |
| **Apache Commons Math** | `https://github.com/apache/commons-math` | Apache Software Foundation | Apache-2.0 | `languages/04_java/commons_math/` |
| **TheAlgorithms/C-Sharp** | `https://github.com/TheAlgorithms/C-Sharp` | TheAlgorithms Community | MIT | `languages/05_csharp/algorithms/` |
| **.NET Base Class Library** | `https://github.com/dotnet/runtime` | .NET Foundation & Contributors | MIT | `languages/05_csharp/dotnet_bcl/` |
| **TheAlgorithms/JavaScript** | `https://github.com/TheAlgorithms/JavaScript` | TheAlgorithms Community | MIT | `languages/06_javascript/algorithms/` |
| **Node.js Core Modules** | `https://github.com/nodejs/node` | OpenJS Foundation & Node.js Authors | MIT | `languages/06_javascript/nodejs_lib/` |
| **Lodash** | `https://github.com/lodash/lodash` | OpenJS Foundation & Lodash Contributors | MIT | `languages/06_javascript/lodash/` |
| **D3** | `https://github.com/d3/d3` | Mike Bostock & D3 Contributors | ISC | `languages/06_javascript/d3/` |
| **TheAlgorithms/TypeScript** | `https://github.com/TheAlgorithms/TypeScript` | TheAlgorithms Community | MIT | `languages/07_typescript/algorithms/` |
| **RxJS** | `https://github.com/ReactiveX/rxjs` | ReactiveX & Ben Lesh | Apache-2.0 | `languages/07_typescript/rxjs/` |
| **TheAlgorithms/R** | `https://github.com/TheAlgorithms/R` | TheAlgorithms Community | MIT | `languages/08_r/algorithms/` |
| **R Core Interpretation Engine** | `https://github.com/wch/r-source` | The R Foundation | GPL-2.0 / GPL-3.0 | `languages/08_r/r_core/` |
| **TheAlgorithms/Rust** | `https://github.com/TheAlgorithms/Rust` | TheAlgorithms Community | MIT | `languages/09_rust/algorithms/` |
| **Rust Standard Library** | `https://github.com/rust-lang/rust` | The Rust Project Developers | MIT / Apache-2.0 | `languages/09_rust/library/` |
| **Rustc Compiler Internals** | `https://github.com/rust-lang/rust` | The Rust Project Developers | MIT / Apache-2.0 | `languages/09_rust/compiler/` |
| **Tokio** | `https://github.com/tokio-rs/tokio` | Tokio Contributors | MIT | `languages/09_rust/tokio/` |
| **Ripgrep** | `https://github.com/BurntSushi/ripgrep` | Andrew Gallant (BurntSushi) | MIT / Unlicense | `languages/09_rust/ripgrep/` |
| **TheAlgorithms/Go** | `https://github.com/TheAlgorithms/Go` | TheAlgorithms Community | MIT | `languages/11_golang/algorithms/` |
| **Go Standard Library** | `https://github.com/golang/go` | The Go Authors | BSD-3-Clause | `languages/11_golang/std/` |
| **Kubernetes Core & Client** | `https://github.com/kubernetes/kubernetes` | The Kubernetes Authors | Apache-2.0 | `languages/11_golang/kubernetes_pkg/`, `kubernetes_client/` |
| **TheAlgorithms/PHP** | `https://github.com/TheAlgorithms/PHP` | TheAlgorithms Community | MIT | `languages/12_php/algorithms/` |
| **PHP Zend Engine & Extensions** | `https://github.com/php/php-src` | The PHP Group | PHP-3.01 / Zend-2.0 | `languages/12_php/zend_engine/`, `extensions/` |
| **TheAlgorithms/Swift** | `https://github.com/TheAlgorithms/Swift` | TheAlgorithms Community | MIT | `languages/13_swift/algorithms/` |
| **Swift Standard Library & SIL** | `https://github.com/swiftlang/swift` | Apple Inc. & Swift Project Authors | Apache-2.0 w/ LLVM Exception | `languages/13_swift/stdlib/`, `lib/` |
| **TheAlgorithms/Julia** | `https://github.com/TheAlgorithms/Julia` | TheAlgorithms Community | MIT | `languages/14_julia/algorithms/` |
| **Julia Standard Library & Runtime** | `https://github.com/JuliaLang/julia` | Julia Contributors | MIT | `languages/14_julia/stdlib/`, `src/` |
| **OrdinaryDiffEq.jl** | `https://github.com/SciML/OrdinaryDiffEq.jl` | SciML Open Source Software Group | MIT | `languages/14_julia/ordinary_diffeq/` |
| **TheAlgorithms/Ruby** | `https://github.com/TheAlgorithms/Ruby` | TheAlgorithms Community | MIT | `languages/15_ruby/algorithms/` |
| **Ruby Standard Library & C Ext** | `https://github.com/ruby/ruby` | Yukihiro Matsumoto & Ruby Contributors | Ruby License / BSD-2-Clause | `languages/15_ruby/stdlib/`, `ext/` |
| **TheAlgorithms/Kotlin** | `https://github.com/TheAlgorithms/Kotlin` | TheAlgorithms Community | MIT | `languages/16_kotlin/algorithms/` |
| **Kotlin Standard Library** | `https://github.com/JetBrains/kotlin` | JetBrains s.r.o. | Apache-2.0 | `languages/16_kotlin/stdlib/` |
| **TheAlgorithms/MATLAB-Octave** | `https://github.com/TheAlgorithms/MATLAB-Octave` | TheAlgorithms Community | MIT | `languages/17_matlab/algorithms/` |
| **TheAlgorithms/OCaml** | `https://github.com/TheAlgorithms/OCaml` | TheAlgorithms Community | MIT | `languages/18_ocaml/algorithms/` |
| **OCaml Standard Library & Parser**| `https://github.com/ocaml/ocaml` | INRIA | LGPL-2.1 w/ linking exception | `languages/18_ocaml/stdlib/`, `parsing/` |
| **TheAlgorithms/Lua** | `https://github.com/TheAlgorithms/Lua` | TheAlgorithms Community | MIT | `languages/19_lua/algorithms/` |
| **Lua Core Engine** | `https://github.com/lua/lua` | Lua.org, PUC-Rio | MIT | `languages/19_lua/lua_core/` |
| **Clojure Standard Library** | `https://github.com/clojure/clojure` | Rich Hickey & Clojure Contributors | EPL-1.0 | `languages/20_lisp/clojure_std/` |
| **TheAlgorithms/Scala** | `https://github.com/TheAlgorithms/Scala` | TheAlgorithms Community | MIT | `languages/21_scala/algorithms/` |
| **Apache Spark Core & MLlib** | `https://github.com/apache/spark` | Apache Software Foundation | Apache-2.0 | `languages/21_scala/spark/` |
| **TheAlgorithms/Haskell** | `https://github.com/TheAlgorithms/Haskell` | TheAlgorithms Community | MIT | `languages/22_haskell/algorithms/` |
| **Glasgow Haskell Compiler (GHC)**| `https://github.com/ghc/ghc` | GHC Team | BSD-3-Clause | `languages/22_haskell/ghc_compiler/`, `base_lib/` |
| **TheAlgorithms/Elixir** | `https://github.com/TheAlgorithms/Elixir` | TheAlgorithms Community | MIT | `languages/23_elixir/algorithms/` |
| **Elixir Standard Library** | `https://github.com/elixir-lang/elixir` | Plataformatec / Dashbit | Apache-2.0 | `languages/23_elixir/std/` |
| **TheAlgorithms/Fortran** | `https://github.com/TheAlgorithms/Fortran` | TheAlgorithms Community | MIT | `languages/24_fortran/algorithms/` |
| **Fortran Standard Library** | `https://github.com/fortran-lang/stdlib` | Fortran-lang Community | MIT | `languages/24_fortran/stdlib/` |
| **Lean 4 Mathlib** | `https://github.com/leanprover-community/mathlib4` | Lean Community | Apache-2.0 | `languages/25_lean4/mathlib4/` |
| **Dart SDK Core & Packages** | `https://github.com/dart-lang/sdk` | Google LLC & The Dart Project Authors | BSD-3-Clause | `architectures/dart_systems/` |
| **NVIDIA CUDA Samples** | `https://github.com/NVIDIA/cuda-samples` | NVIDIA Corporation | BSD-3-Clause | `algorithms/26_cuda/` |

---

## Originally Authored and Derived Material

The following modules were written for this repository or generated locally
from its own sources; they are not copied from external repositories.

| Module | Nature | Reference |
|:---|:---|:---|
| `algorithms/27_assembly/` | Hand-written Linux syscall programs | *Intel 64 and IA-32 Architectures SDM*, *Arm Architecture Reference Manual*, *The RISC-V Instruction Set Manual* |
| `algorithms/28_ptx/` | Hand-written PTX kernels | *Parallel Thread Execution ISA*, NVIDIA |
| `algorithms/29_sass/` | Annotated SASS reference listings | *CUDA Binary Utilities* (`nvdisasm`/`cuobjdump`), NVIDIA |
| `algorithms/30_llvm_ir/` | LLVM IR generated with `clang -O2 -emit-llvm` | LLVM Project |
| `algorithms/31_wasm/` | Hand-written WebAssembly text | *WebAssembly Core Specification*, W3C |
| `web/` | Hand-written HTML, CSS, Sass, Tailwind, JavaScript, TypeScript, React, Vue, Web Components, JSON, XML, GraphQL examples | WHATWG HTML, W3C CSS, Sass, Tailwind CSS, ECMAScript, TypeScript, React, Vue, JSON Schema, W3C XML, GraphQL specifications |
| `databases/` | Hand-written queries and schemas | Cypher (Neo4j), Gremlin (Apache TinkerPop), SPARQL (W3C), Datalog, MongoDB MQL, Cassandra CQL, Redis, Elasticsearch Query DSL, Flux (InfluxData), PromQL (Prometheus), pgvector |
| `architectures/enterprise_patterns/`, `ddd_patterns/`, `cloud_patterns/`, `system_design/`, `principles/`, `clean_architecture/`, `templates/`, `api_design/` | Hand-written pattern implementations, system design notes, templates and guidelines | Hohpe & Woolf *Enterprise Integration Patterns*; Evans *Domain-Driven Design*; Nygard *Release It!*; Newman *Building Microservices*; Martin *Clean Architecture*; fielding/HTTP RFCs; W3C/CNCF documentation |
| `devops/` | Hand-written CI/CD, container, orchestration, IaC, configuration and monitoring examples | GitHub Actions, GitLab CI, Jenkins, Docker, Kubernetes, Terraform (HashiCorp), Ansible (Red Hat), Helm, Prometheus, Grafana, OpenTelemetry, Loki, Blackbox Exporter |
| `interview_prep/` | Hand-written study material, implementations and notes (including the numbered `deep_dives/`) | LeetCode/competitive-programming patterns; *A Tour of C++*, *Effective C++*, *Effective Modern C++* (Meyers); *C++ Concurrency in Action* (Williams); *Fluent Python* (Ramalho); *Computer Networking: A Top-Down Approach* (Kurose & Ross); *Operating Systems: Three Easy Pieces* (Arpaci-Dusseau); *Designing Data-Intensive Applications* (Kleppmann); Alex Xu *System Design Interview*; ISO C++20 specifications; standard probability/statistics texts |
| `formal_physics/` | Lean 4 formalization of classical variational, Lagrangian and Hamiltonian mechanics using the Mathlib library | Analytical Mechanics; [Mathlib4](https://github.com/leanprover-community/mathlib4) (Apache-2.0); Lean 4 (Apache-2.0) |
| `formal_statistics/` | Lean 4 formalization of linear statistical models and ordinary least squares using the Mathlib library | Linear Statistical Models; [Mathlib4](https://github.com/leanprover-community/mathlib4) (Apache-2.0); Lean 4 (Apache-2.0) |
| Additional algorithms in `algorithms/01_python`, `02_c`, `03_cpp`, `04_java`, `09_rust`, `11_golang` | Hand-written implementations (radix/bucket/shell sort, Floyd-Warshall, Bellman-Ford, Prim, Kruskal, Fenwick tree, LRU cache, skip list, Rabin-Karp, edit distance, coin change) | *Introduction to Algorithms* (CLRS); standard algorithm references |

---

## License Notices

All copied files preserve their original author copyrights and license declarations. Individual directories retain their respective upstream licenses:
- **MIT License**: Copyright (c) The respective authors and contributors as detailed above.
- **Apache License, Version 2.0**: Licensed under the Apache License, Version 2.0.
- **BSD 2-Clause / 3-Clause Licenses**: Copyright (c) The respective authors and contributors.
- **ISC License**: Copyright (c) The respective authors and contributors.
- **Python Software Foundation License (PSF-2.0)**: Copyright (c) 2001-2026 Python Software Foundation.
- **Public Domain**: SQLite code is dedicated to the public domain.
