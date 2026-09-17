# How to Use This Repository

A task-oriented guide. Every module is independent; run only what you need.
For a map of what exists, see [`STRUCTURE.md`](STRUCTURE.md).

## 1. Prerequisites and toolchain

Nothing is required to browse the code. To *run* it, install the toolchains you
care about:

| Module | Tools |
|:---|:---|
| Python algorithms/scripts | `python3` (3.11+), `pyyaml`, `wasmtime` (WASM only) |
| C / C++ | `gcc`, `g++`, `make` |
| Assembly | GNU `as`/`ld` (x86-64), `clang` with `--target=aarch64-linux-gnu` / `riscv64-linux-gnu` |
| Java | `javac`, `java` |
| Rust | `rustc` |
| Go | `go` |
| JavaScript / TypeScript / React / Vue | `node`, `npm`/`npx` (`sass`, `esbuild`, `graphql` used for validation) |
| Fortran | `gfortran` |
| CUDA / PTX / SASS | CUDA Toolkit (`nvcc`, `ptxas`, `nvdisasm`) and a GPU — optional; sources are reference material |
| LLVM IR | `clang`, `opt`, `llvm-as`, `lli` |
| Lean 4 modules | `elan`/`lake` + **Mathlib** (downloaded on first build) |
| Web HTML/XML validation | Python `html5lib`, `xml`; `sass` for CSS/SCSS |
| DevOps | `python3` + `pyyaml`; shell scripts with `bash` |

Missing tools cause the relevant `make` target to **skip** rather than fail (for
example CUDA and the Lean modules when Mathlib is not present).

## 2. Sparse checkout & `languages/`

The repository stores ~3 GB upstream source in `languages/` (Linux, LLVM, V8,
PyTorch, Spark, GHC, …). It is hidden locally by Git sparse-checkout.

```bash
./scripts/sparse_checkout.sh status    # what is checked out now + disk usage
./scripts/sparse_checkout.sh list      # all available modules
./scripts/sparse_checkout.sh minimal   # reset to the small core tree
./scripts/sparse_checkout.sh add languages/02_c/linux_kernel
./scripts/sparse_checkout.sh remove languages/02_c/linux_kernel
./scripts/sparse_checkout.sh all       # check out everything (~3 GB)
```

Use `languages/` as a **reading/diffing corpus** for real-world implementations
of the same ideas the `algorithms/` and `architectures/` modules implement in
isolation.

## 3. Algorithms (`algorithms/`)

Every file is standalone and (for most languages) executable. Read the file's
header for its build/run line, or use the Makefile.

```bash
# Run one example directly
python3 algorithms/01_python/graphs/dijkstra_full.py
gcc -O2 algorithms/02_c/math/miller_rabin.c -o /tmp/mr -lm && /tmp/mr
rustc -O algorithms/09_rust/math/miller_rabin.rs -o /tmp/mr && /tmp/mr
go run algorithms/11_golang/graphs/dijkstra_full.go

# Or run whole suites
make test-python test-c test-cpp test-java test-rust test-go
make test-competitive     # DSU, binary search, DP, number theory, graphs, techniques
make test-algorithms      # FFT, Dijkstra, A*, KMP, Huffman, convex hull, …
make test-dsu test-dp-advanced test-graphs-advanced test-datastructures
```

Low-level tiers have their own targets and READMEs:

```bash
make test-asm        # assemble + run the x86-64 examples; assemble AArch64/RISC-V
make test-llvm-ir    # opt -passes=verify every generated .ll
make test-wasm       # validate every .wat with wasmtime
make test-cuda       # compile one NVIDIA sample (needs nvcc; otherwise skipped)
```

**How to use each tier**

- `01_python` … `25_lean4` — copy the algorithm you need into your project, or
  use a file as a reference implementation while reading the matching upstream
  source in `languages/`.
- `26_cuda` — GPU reference kernels; build with the CUDA Toolkit
  (`nvcc -arch=sm_90 …`) if you have a GPU.
- `27_assembly` — minimal, fully commented programs; ideal for reading the
  instruction-level version of an algorithm.
- `28_ptx` — the GPU virtual ISA; assemble with `ptxas -arch=sm_90` to see the
  generated SASS.
- `29_sass` — annotated machine listings for study; not assembler input.
- `30_llvm_ir` — compiler IR; interpret with `lli file.ll` or optimize with
  `opt -O3`.
- `31_wasm` — WebAssembly text; run with `wasmtime` or compile with `wat2wasm`.

## 4. Architectures & design patterns (`architectures/`)

Patterns are small runnable demos or focused notes, grouped by family. Start at
each family's `index.md`.

```bash
make test-architectures      # Java, Go, Rust demos + the Python pattern families

# Run a single pattern demo
python3 architectures/enterprise_patterns/saga.py
python3 architectures/ddd_patterns/aggregate.py
python3 architectures/resilience_patterns/circuit_breaker.py
```

Use them as **templates**: read the intent, copy the skeleton, and adapt names.
The `templates/` family (ADR, RFC, design doc, runbook, C4 diagrams) is meant to
be dropped into real projects; `principles/`, `clean_architecture/` and
`api_design/` are reading material.

## 5. Web platform (`web/`)

```bash
python3 web/javascript/fetch_api.mjs           # or: node web/javascript/fetch_api.mjs
npx esbuild web/typescript/generics.ts --outfile=/tmp/out.js   # parse/transform
npx sass web/scss/main.scss /tmp/main.css      # compile Sass
python3 -c "import json;json.load(open('web/json/package.json'))"
node web/webcomponents/custom_element.js
```

Validate the whole module (JSON/XML/Sass/HTML) with:

```bash
make test-web
```

Use `web/html`, `web/css`, `web/scss`, `web/tailwind` as drop-in starting points;
`web/react`, `web/vue` and `web/webcomponents` show component patterns;
`web/json`, `web/xml` and `web/graphql` are schema/format references.

## 6. Databases & query languages (`databases/`)

Each file is a runnable snippet for one engine's shell or driver.

```bash
mongosh databases/document/mongodb/aggregation_pipeline.js
redis-cli < databases/key_value/redis/streams.redis
psql -f databases/vector/similarity_search.sql
cypher-shell -f databases/graph/cypher/shortest_path.cypher
cqlsh -f databases/wide_column/cassandra/time_series.cql
curl -X POST localhost:9200/articles/_search -H 'Content-Type: application/json' \
     -d @databases/search/elasticsearch/bool_query.json
```

The Elasticsearch `bulk_index.ndjson` is newline-delimited JSON (one operation
per line), not a single document. Relational examples live in
`algorithms/10_sql/`.

## 7. DevOps & platform engineering (`devops/`)

```bash
make test-devops     # validate YAML + shell syntax

kubectl apply -f devops/kubernetes/deployment.yaml
helm install api devops/helm
terraform -chdir=devops/terraform init && terraform -chdir=devops/terraform plan
ansible-playbook -i devops/ansible/inventory.ini devops/ansible/playbook.yml
docker build -f devops/docker/node.Dockerfile .
docker compose -f devops/docker/docker-compose.yml up
```

Treat `devops/` as a **library of copy-paste-ready configuration**: CI workflows,
hardened container builds, Kubernetes workloads with probes/limits/RBAC,
infrastructure-as-code, and monitoring/alerting config.

## 8. Interview preparation (`interview_prep/`)

```bash
python3 interview_prep/algorithms/arrays/two_sum.py
g++ -std=c++20 -pthread interview_prep/concurrency/thread_pool.cpp -o /tmp/tp && /tmp/tp
make test-interview     # every Python self-check + the C++ suites
```

Use it as a **study vault**: each track maps to a core foundational topic
(`deep_dives/` is numbered to match a topic list). See
[`interview_prep/README.md`](../interview_prep/README.md) for the roadmap.

## 9. Formal mathematics (`formal_physics/`, `formal_statistics/`)

Both are Lean 4 projects on Mathlib. The first build downloads the prebuilt
Mathlib cache (several GB) and is slow; later builds are fast.

```bash
# One-time per project
cd formal_physics   && ./scripts/verify.sh
cd formal_statistics && ./scripts/verify.sh

# Or via make (builds only if a local Mathlib is already present)
make test-formal-physics
make test-formal-statistics

# Read/check a single file once Mathlib is cached
cd formal_physics && lake env lean FormalPhysics/Variations/Beltrami.lean
```

To build against a local Mathlib instead of fetching it, replace the `[[require]]`
block in the `lakefile.toml` with a `path` dependency (see the module READMEs).

## 10. Computational scripts (`scripts/`)

```bash
make test-scripts
python3 scripts/numerical_analysis/root_finding.py
python3 scripts/physics/curvilinear_tensors.py
python3 scripts/distributed_systems/consistent_hashing.py
```

## 11. Run everything

```bash
make test        # all suites; unavailable toolchains are skipped
make clean       # remove build artifacts, .olean, etc.
```

## 12. Conventions for adding content

- **One concept per file.** Keep dependencies minimal and self-contained.
- **A file should run.** Python files include a `if __name__ == "__main__":`
  self-check; C/C++/Rust have a `main` that asserts and prints `… ok`.
- **Match the layout.** Algorithms go in `algorithms/<NN_lang>/<category>/`;
  patterns in `architectures/<family>/`; designs in `web/`, `databases/`,
  `devops/`; study material in `interview_prep/`.
- **Attribute upstream code** in [`SOURCES.md`](../SOURCES.md) with repo, author
  and license.
- **Wire up a test target** in `Makefile` when you add a new module, and document
  it in this file and the module README.
- **Keep the outer repository clean.** Run Git from the relevant project
  directory; do not stage nested repositories or project folders into the outer
  index.

## 13. Troubleshooting

| Symptom | Fix |
|:---|:---|
| `make test-cuda` prints "nvcc not found" | Expected without a CUDA Toolkit; the samples are reference-only. |
| `make test-formal-physics` skips | No local Mathlib; run `formal_physics/scripts/verify.sh` once. |
| `sass` / `esbuild` not found | `npm install sass esbuild` (or use `npx`). |
| A path is "outside the sparse-checkout" | `./scripts/sparse_checkout.sh add <path>`. |
| `git status` shows huge untracked trees | They are outside the sparse cone; add deliberately or leave them. |
