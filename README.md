# Code and Scripts Database

Directory navigation index.

---

## Directory Tree

```
.
├── algorithms/
│   ├── dijkstra_shortest_path/
│   ├── dynamic_programming/
│   ├── fast_fourier_transform/
│   ├── formal_verification/
│   ├── matrix_multiplication/
│   ├── primality_factorization/
│   └── strongly_connected_components/
├── architectures/
│   ├── cpp_patterns/
│   ├── go_patterns/
│   ├── python_patterns/
│   └── rust_patterns/
├── languages/
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
│   ├── 24_fortran/
│   └── 25_lean4/
├── scripts/
│   ├── computer_science/
│   ├── finance/
│   ├── mathematics/
│   ├── physics/
│   └── shell_automation/
├── Makefile
├── SOURCES.md
├── LICENSE
└── README.md
```

---

## Section Index

### 1. Algorithms (`algorithms/`)

| Directory | Primary Formats | Index |
|:---|:---|:---|
| `algorithms/dijkstra_shortest_path/` | `.java`, `.cpp`, `.go`, `.py`, `.rs` | Graph shortest path routines |
| `algorithms/dynamic_programming/` | `.cs`, `.ts`, `.scala`, `.hs` | Dynamic programming routines |
| `algorithms/fast_fourier_transform/` | `.cpp`, `.jl`, `.py`, `.rs` | Discrete transform routines |
| `algorithms/formal_verification/` | `.lean` | Interactive theorem prover specifications |
| `algorithms/matrix_multiplication/` | `.f90`, `.c`, `.py` | Numerical linear algebra routines |
| `algorithms/primality_factorization/` | `.c`, `.py`, `.rs` | Number theoretic routines |
| `algorithms/strongly_connected_components/` | `.cpp`, `.go`, `.py` | Directed graph decomposition routines |

### 2. Software Architectures & Patterns (`architectures/`)

| Directory | Primary Formats | Index |
|:---|:---|:---|
| `architectures/cpp_patterns/` | `.cpp`, `.hpp` | Creational, structural, and behavioral patterns |
| `architectures/go_patterns/` | `.go` | Idiomatic Go concurrency and design patterns |
| `architectures/python_patterns/` | `.py` | Python design patterns and architectural idioms |
| `architectures/rust_patterns/` | `.rs` | Rust idioms, behavioral patterns, and design patterns |

### 3. Language Collections (`languages/`)

| Directory | Primary Extensions | Subdirectories |
|:---|:---|:---|
| `languages/01_python/` | `.py` | `algorithms/` |
| `languages/02_c/` | `.c`, `.h` | `algorithms/` |
| `languages/03_cpp/` | `.cpp`, `.hpp` | `algorithms/` |
| `languages/04_java/` | `.java` | `algorithms/` |
| `languages/05_csharp/` | `.cs` | `algorithms/` |
| `languages/06_javascript/` | `.js`, `.mjs` | `algorithms/` |
| `languages/07_typescript/` | `.ts` | `algorithms/` |
| `languages/08_r/` | `.R`, `.r` | `algorithms/` |
| `languages/09_rust/` | `.rs` | `algorithms/` |
| `languages/10_sql/` | `.sql` | `schemas/`, `models/` |
| `languages/11_golang/` | `.go` | `algorithms/` |
| `languages/12_php/` | `.php` | `algorithms/` |
| `languages/13_swift/` | `.swift` | `algorithms/`, `club/` |
| `languages/14_julia/` | `.jl` | `algorithms/` |
| `languages/15_ruby/` | `.rb` | `algorithms/` |
| `languages/16_kotlin/` | `.kt` | `algorithms/`, `club/` |
| `languages/17_matlab/` | `.m` | `algorithms/` |
| `languages/18_ocaml/` | `.ml` | `algorithms/` |
| `languages/19_lua/` | `.lua` | `algorithms/` |
| `languages/20_lisp/` | `.lisp`, `.cl` | `algorithms/`, `competitive/`, `rutils/` |
| `languages/21_scala/` | `.scala` | `algorithms/`, `scalacaster/` |
| `languages/22_haskell/` | `.hs` | `algorithms/` |
| `languages/23_elixir/` | `.ex`, `.exs` | `algorithms/` |
| `languages/24_fortran/` | `.f90`, `.f95` | `algorithms/` |
| `languages/25_lean4/` | `.lean` | `samples/` |

### 4. Scripts & Utilities (`scripts/`)

| Directory | Primary Formats | Index |
|:---|:---|:---|
| `scripts/computer_science/` | `.py` | Graph embeddings and cipher routines |
| `scripts/finance/` | `.py` | Valuation and financial modeling routines |
| `scripts/mathematics/` | `.py` | Number theory, algebra, and geometry scripts |
| `scripts/physics/` | `.py` | Tensors and mechanics scripts |
| `scripts/shell_automation/` | `.sh`, `.bash` | Portable shell and bash scripting references |

---

## Commands

```bash
# Execute local verification suite
make test

# Target specific modules
make test-algorithms
make test-scripts
make test-python
make test-c
make test-cpp
make test-java
make test-lua
make test-rust
make test-fortran
make test-js
make test-go

# Clean build artifacts
make clean
```

---

## Sources and Attribution

See [SOURCES.md](SOURCES.md) for upstream repository URLs, author credits, and license details.

---

## License

[MIT](LICENSE)
