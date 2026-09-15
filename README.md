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
| `algorithms/` | Polyglot algorithms across 25 languages plus CUDA, assembly, PTX, SASS, LLVM IR and WebAssembly | [algorithms/README.md](algorithms/README.md) |
| `architectures/` | Design patterns, DDD, enterprise integration, cloud, system design, principles and templates | [architectures/README.md](architectures/README.md) |
| `devops/` | CI/CD, Docker, Kubernetes, Terraform, Ansible, Helm, monitoring and operations scripts | [devops/README.md](devops/README.md) |
| `interview_prep/` | Interview study vault: algorithms, C++, concurrency, Python, networking, OS, architecture, system design, behavioral, math | [interview_prep/README.md](interview_prep/README.md) |
| `web/` | Web platform: HTML, CSS, Sass, Tailwind, JS/TS, React, Vue, Web Components, JSON, XML, GraphQL | [web/README.md](web/README.md) |
| `databases/` | Graph/NoSQL query languages: Cypher, Gremlin, SPARQL, Datalog, MongoDB, Cassandra, Redis, Elasticsearch, Flux, PromQL, pgvector | [databases/README.md](databases/README.md) |
| `scripts/` | Computational scripts (math, physics, ML, finance) and utilities | `scripts/` |
| `languages/` | Upstream source code from major open-source projects (sparse checkout) | `languages/` |

---

## Multi-Language Algorithms Suite

The `algorithms/` directory hosts standalone, production-ready algorithm implementations across all 25 canonical languages, plus six systems/GPU tiers that go below the language level: CUDA, assembly (x86-64 / AArch64 / RISC-V), PTX, SASS, LLVM IR and WebAssembly. Each language directory (`01_python/` through `25_lean4/`, and `26_cuda/` through `31_wasm/`) contains implementations organized by category: sorting, graphs, dynamic programming, strings, data structures, math, cryptography, and machine learning.

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
| 26 | `algorithms/26_cuda/` | CUDA | 175 upstream NVIDIA samples: vectorAdd, reduction, scan, matrixMul, streams, cooperative groups, cuBLAS/cuFFT/Thrust, tensor-core kernels |
| 27 | `algorithms/27_assembly/` | Assembly | x86-64 (25), AArch64 (8), RISC-V 64 (6) syscall programs: sorts, GCD, Fibonacci, SIMD, CPUID, RDTSC |
| 28 | `algorithms/28_ptx/` | PTX | 20 kernels: vectorAdd, saxpy, reduction, tiled matmul, warp vote/shuffle, atomics, `cp.async` |
| 29 | `algorithms/29_sass/` | SASS | 9 annotated sm_90 (Hopper) disassembly listings plus reference notes |
| 30 | `algorithms/30_llvm_ir/` | LLVM IR | 47 modules lowered from the C reference suite |
| 31 | `algorithms/31_wasm/` | WebAssembly (WAT) | 18 modules: control flow, linear memory, SIMD, tables, multi-value |

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
| `architectures/enterprise_patterns/` | Message router, splitter, aggregator, outbox, saga, dead letter channel |
| `architectures/ddd_patterns/` | Entity, value object, aggregate, repository, domain event, specification |
| `architectures/cloud_patterns/` | Circuit breaker, bulkhead, retry/backoff, cache-aside, sidecar, strangler fig |
| `architectures/system_design/` | Rate limiter, load balancer, LRU cache, WAL, sharding, CDN, CAP, Bloom guard |
| `architectures/principles/` | SOLID, DRY/KISS/YAGNI, separation of concerns, Law of Demeter, twelve-factor |
| `architectures/clean_architecture/` | Hexagonal, onion, layered, dependency inversion, ports and adapters |
| `architectures/templates/` | ADR, RFC, design doc, runbook, C4 (Mermaid) |
| `architectures/api_design/` | REST guidelines, versioning, pagination, error handling, GraphQL vs REST |

---

## GPU, Assembly & Intermediate Representations

Beyond the high-level language suites, `algorithms/` follows the GPU and systems toolchain from parallel source down to machine instructions.

| Directory | Level | Description |
|:---|:---|:---|
| `algorithms/26_cuda/` | parallel C++ | Curated [NVIDIA/cuda-samples](https://github.com/NVIDIA/cuda-samples) (BSD-3-Clause) organized by sample category |
| `algorithms/27_assembly/` | machine code | Hand-written Linux syscall programs for x86-64 (AT&T/Intel), AArch64 and RISC-V 64 |
| `algorithms/28_ptx/` | virtual ISA | Standalone PTX 8.x kernels (thread indexing, shared memory, warp intrinsics, atomics, `cp.async`) |
| `algorithms/29_sass/` | device ISA | Annotated sm_90 (Hopper) SASS disassembly listings (`nvdisasm` reference) |
| `algorithms/30_llvm_ir/` | compiler IR | LLVM IR lowered from the C reference algorithms; verify with `opt`, run with `lli` |
| `algorithms/31_wasm/` | stack machine | WebAssembly text modules validated with `wasmtime` |

---

## Web Platform

The `web/` directory collects markup, styling, scripting, component and data-format examples.

| Directory | Content |
|:---|:---|
| `web/html/` | Semantic HTML5, forms, ARIA, tables, canvas, inline SVG, responsive images, `<dialog>` |
| `web/css/` | Reset, flexbox, grid, custom properties, animations, container queries, scroll-driven effects |
| `web/scss/` | Sass variables, nesting, mixins, functions, placeholders, loops, maps, `@use` modules |
| `web/tailwind/` | Tailwind configuration, `@apply` component layers and responsive utility components |
| `web/webcomponents/` | Custom elements, shadow DOM, templates and adopted stylesheets |
| `web/javascript/` | Modern JavaScript: DOM, fetch, promises, ESM, closures, classes, observers, workers |
| `web/typescript/` | Generics, discriminated unions, utility/mapped/conditional types, decorators |
| `web/react/` | React 19 function components, hooks, context, reducers and error boundaries |
| `web/vue/` | Vue 3 Composition and Options APIs, props/emit, `v-model` |
| `web/json/` | JSON/JSONL, JSON Schema, JSON-LD, GeoJSON, JSON Patch, OpenAPI |
| `web/xml/` | Sitemaps, RSS/Atom, SVG, XSLT, XSD, SOAP and configuration |
| `web/graphql/` | GraphQL SDL, queries, mutations, subscriptions, fragments, federation |

---

## Databases & Query Languages

`databases/` covers graph and NoSQL engines plus time-series and vector search; the relational suite remains in `algorithms/10_sql/`.

| Directory | Engine | Language |
|:---|:---|:---|
| `databases/graph/cypher/` | Neo4j | Cypher |
| `databases/graph/gremlin/` | Apache TinkerPop | Gremlin |
| `databases/graph/sparql/` | RDF stores | SPARQL 1.1 |
| `databases/graph/datalog/` | Souffle / DDlog | Datalog |
| `databases/document/mongodb/` | MongoDB | MQL / mongosh |
| `databases/wide_column/cassandra/` | Apache Cassandra | CQL |
| `databases/key_value/redis/` | Redis | RESP / Lua |
| `databases/search/elasticsearch/` | Elasticsearch | Query DSL |
| `databases/timeseries/` | InfluxDB / Prometheus | Flux / PromQL |
| `databases/vector/` | PostgreSQL + pgvector | SQL |

---

## DevOps & Platform Engineering

The `devops/` directory holds runnable pipeline, infrastructure and operational
configuration.

| Directory | Tooling |
|:---|:---|
| `devops/ci/github_actions/` | CI, matrix builds, CD with OIDC, release please, CodeQL, Docker publish, reusable workflows |
| `devops/ci/gitlab/` | staged pipelines, manual deploy, per-MR review apps |
| `devops/ci/jenkins/` | declarative pipeline, multibranch, shared library |
| `devops/docker/` | Node/Python/Go images, multi-stage and distroless builds, Compose |
| `devops/kubernetes/` | Deployment, Service, ConfigMap, Secret, Ingress, HPA, StatefulSet, DaemonSet, Job/CronJob, RBAC, NetworkPolicy, PDB, probes |
| `devops/terraform/` | provider/backend, variables, outputs, VPC, EC2, S3 + ALB |
| `devops/ansible/` | playbook, inventory, groups and roles |
| `devops/helm/` | chart metadata, values and templated workloads |
| `devops/monitoring/` | Prometheus, alert rules, Loki, Grafana, OpenTelemetry, blackbox |
| `devops/scripts/` | deploy, backup, healthcheck, rolling restart, log rotation |
| `devops/make/` | application, Python and self-documenting task runners |

---

## Interview Preparation

The `interview_prep/` directory is a study vault built around a concurrent
algorithms-plus-systems plan, with runnable examples and focused notes.

| Directory | Track | Contents |
|:---|:---|:---|
| `interview_prep/algorithms/` | Algorithms (see also `algorithms/`) | LeetCode patterns: arrays, strings, linked lists, trees, graphs, DP, heap/trie/bit, techniques |
| `interview_prep/cpp/` | C++ | STL components from scratch, *A Tour of C++*, *Effective C++* examples, 100 questions + answer programs |
| `interview_prep/concurrency/` | Concurrency | threads, locks, condition variables, atomics, lock-free stacks/queues, futures, thread pools |
| `interview_prep/python/` | Python | *Fluent Python*: data model, generators, decorators, descriptors, metaclasses, asyncio |
| `interview_prep/networking/` | Networking | top-down Ch. 1-5: application, transport, network, link, sockets and simulations |
| `interview_prep/operating_systems/` | Operating Systems | OSTEP: CPU/memory virtualization, concurrency, persistence |
| `interview_prep/computer_architecture/` | Architecture | caches, branch prediction, memory hierarchy, pipelining |
| `interview_prep/system_design/` | System Design | scalability, low-level/high-throughput, DDIA notes, worked designs |
| `interview_prep/behavioral/` | Behavioral | STAR method, story banks, leadership and question bank |
| `interview_prep/math_stats/` | Math & Stats | probability, statistics, linear algebra, Markov chains, Monte Carlo |
| `interview_prep/deep_dives/` | Deep dives | numbered C++20, STL, smart-pointer, reimplementation, networking (15-19) and OS (20-31) topics |

Run the self-checks with `make test-interview`.

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
make test-asm           # x86-64 assembly (assemble + run)
make test-llvm-ir       # Verify generated LLVM IR
make test-wasm          # Validate WebAssembly text modules
make test-web           # HTML/CSS/SCSS/JS/TS/JSON/GraphQL validation
make test-cuda          # NVIDIA samples (requires nvcc; skipped when absent)
make test-devops        # Validate DevOps YAML and shell scripts
make test-interview     # Run interview-prep self-checks (Python + C++)

# Clean build artifacts
make clean
```

---

## Upstream Licenses & Attribution

All imported code preserves original author attributions, notices, and copyright statements. Complete upstream repository links, author organizations, and license terms are detailed in [SOURCES.md](SOURCES.md).

---

© 2026 Igor Kan