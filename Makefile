# ==============================================================================
# Code & Scripts Repository: Master Build & Verification Harness
# ==============================================================================

CC ?= gcc
CXX ?= g++
AS ?= as
LD ?= ld
FC = gfortran
PYTHON ?= python3
NODE ?= node
RUSTC ?= rustc
GO ?= go
BUILD_DIR = build

.PHONY: all test clean help \
	test-python test-c test-cpp test-java test-rust test-fortran test-js test-go test-scripts \
	test-fft test-dijkstra test-primality test-matrix test-scc \
	test-astar test-kmp test-convexhull test-huffman test-toposort test-architectures \
	test-dsu test-binary-search test-dp-advanced test-number-theory \
	test-strings-advanced test-graphs-advanced test-techniques test-datastructures \
	test-competitive test-algorithms test-sparse \
	test-asm test-llvm-ir test-wasm test-web test-cuda test-devops test-interview test-formal-physics

all: test

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

help:
	@echo "Repository Build & Execution Matrix"
	@echo "Available test targets:"
	@echo "  make test-python        Run Python algorithm implementations"
	@echo "  make test-c             Compile and execute C algorithms"
	@echo "  make test-cpp           Compile and execute C++ algorithms"
	@echo "  make test-java          Compile and execute Java algorithms"
	@echo "  make test-rust          Compile and execute Rust algorithms"
	@echo "  make test-fortran       Compile and execute Fortran algorithms"
	@echo "  make test-js            Execute JavaScript algorithms"
	@echo "  make test-go            Execute Golang algorithms"
	@echo "  make test-scripts       Execute computational Python scripts"
	@echo "  make test-fft           Execute Fast Fourier Transform suite"
	@echo "  make test-dijkstra      Execute Dijkstra shortest path suite"
	@echo "  make test-primality     Execute Primality & Factorization suite"
	@echo "  make test-matrix        Execute Matrix Multiplication suite"
	@echo "  make test-scc           Execute Strongly Connected Components suite"
	@echo "  make test-astar         Execute A* Search pathfinding suite"
	@echo "  make test-kmp           Execute Knuth-Morris-Pratt string search suite"
	@echo "  make test-convexhull    Execute 2D Convex Hull geometric suite"
	@echo "  make test-huffman       Execute Huffman Data Compression suite"
	@echo "  make test-toposort      Execute DAG Topological Sorting suite"
	@echo "  make test-architectures Execute design pattern and concurrency suites"
	@echo "  make test-competitive   Execute competitive programming toolkit (DSU, binary search, DP, number theory, graphs)"
	@echo "  make test-sparse        Test sparse language implementations"
	@echo "  make test-asm           Assemble and run x86-64/AArch64/RISC-V assembly examples"
	@echo "  make test-llvm-ir       Verify generated LLVM IR modules"
	@echo "  make test-wasm          Validate WebAssembly text modules"
	@echo "  make test-web           Validate JSON, XML and Sass web assets"
	@echo "  make test-cuda          Build a CUDA sample (requires nvcc; skipped when absent)"
	@echo "  make test-devops        Validate DevOps YAML and shell scripts"
	@echo "  make test-interview     Run interview-prep self-checks (Python + C++)"
	@echo "  make test-formal-physics Verify the Lean 4 / Mathlib formal physics library"
	@echo "  make test-algorithms    Execute all core algorithm suites"
	@echo "  make test               Run full regression verification"

# --- Per-language algorithm tests ---

test-python:
	@echo ">>> Testing Python Algorithms..."
	$(PYTHON) algorithms/01_python/graphs/dijkstra_full.py
	$(PYTHON) algorithms/01_python/strings/kmp_full.py
	$(PYTHON) algorithms/01_python/math/miller_rabin.py

test-c: $(BUILD_DIR)
	@echo ">>> Compiling and Testing C Algorithms..."
	$(CC) -O3 -Wall -Wextra algorithms/02_c/math/miller_rabin.c -o $(BUILD_DIR)/mr_c_test -lm
	./$(BUILD_DIR)/mr_c_test
	$(CC) -O3 -Wall -Wextra algorithms/02_c/math/matmul_tiled.c -o $(BUILD_DIR)/matmul_c_test
	./$(BUILD_DIR)/matmul_c_test

test-cpp: $(BUILD_DIR)
	@echo ">>> Compiling and Testing C++ Algorithms..."
	$(CXX) -O3 -std=c++17 -Wall algorithms/03_cpp/graphs/dijkstra_full.cpp -o $(BUILD_DIR)/dijkstra_cpp_test
	./$(BUILD_DIR)/dijkstra_cpp_test

test-java: $(BUILD_DIR)
	@echo ">>> Compiling and Testing Java Algorithms..."
	javac -d $(BUILD_DIR) algorithms/04_java/strings/KMPFull.java
	java -cp $(BUILD_DIR) KMPFull
	javac -d $(BUILD_DIR) algorithms/04_java/graphs/DijkstraFull.java
	java -cp $(BUILD_DIR) DijkstraFull

test-rust: $(BUILD_DIR)
	@echo ">>> Compiling and Testing Rust Algorithms..."
	$(RUSTC) -O algorithms/09_rust/math/miller_rabin.rs -o $(BUILD_DIR)/mr_rust_test
	./$(BUILD_DIR)/mr_rust_test

test-fortran: $(BUILD_DIR)
	@echo ">>> Compiling and Testing Fortran Algorithms..."
	$(FC) -O3 algorithms/24_fortran/math/matmul_blocked.f90 -o $(BUILD_DIR)/matmul_f90_test
	./$(BUILD_DIR)/matmul_f90_test

test-js:
	@echo ">>> Executing JavaScript Algorithms..."
	$(NODE) algorithms/06_javascript/math/gcd.js

test-go:
	@echo ">>> Executing Golang Algorithms..."
	$(GO) run algorithms/11_golang/graphs/dijkstra_full.go

test-scripts:
	@echo ">>> Executing Computational Scripts..."
	$(PYTHON) scripts/mathematics/euclidean_algorithms.py
	$(PYTHON) scripts/mathematics/finite_geometry_fano.py
	$(PYTHON) scripts/mathematics/multilinear_algebra.py
	$(PYTHON) scripts/mathematics/perfect_numbers_factorization.py
	$(PYTHON) scripts/physics/curvilinear_tensors.py
	$(PYTHON) scripts/physics/rigid_body_inertia.py
	$(PYTHON) scripts/finance/corporate_valuation_dcf.py
	$(PYTHON) scripts/computer_science/k4_planar_graph.py
	$(PYTHON) scripts/machine_learning/kmeans_clustering.py
	$(PYTHON) scripts/machine_learning/logistic_regression.py
	$(PYTHON) scripts/numerical_analysis/root_finding.py
	$(PYTHON) scripts/distributed_systems/consistent_hashing.py

# --- Cross-language polyglot algorithm suites ---

test-fft: $(BUILD_DIR)
	@echo ">>> Testing Fast Fourier Transform implementations..."
	$(PYTHON) algorithms/01_python/math/fft.py
	$(CXX) -O3 algorithms/03_cpp/math/fft.cpp -o $(BUILD_DIR)/fft_cpp_test
	./$(BUILD_DIR)/fft_cpp_test
	$(RUSTC) -O algorithms/09_rust/math/fft.rs -o $(BUILD_DIR)/fft_rust_test
	./$(BUILD_DIR)/fft_rust_test

test-dijkstra: $(BUILD_DIR)
	@echo ">>> Testing Dijkstra shortest path implementations..."
	$(PYTHON) algorithms/01_python/graphs/dijkstra_full.py
	$(CXX) -O3 algorithms/03_cpp/graphs/dijkstra_full.cpp -o $(BUILD_DIR)/dijkstra_cpp_test
	./$(BUILD_DIR)/dijkstra_cpp_test
	$(GO) run algorithms/11_golang/graphs/dijkstra_full.go
	$(RUSTC) -O algorithms/09_rust/graphs/dijkstra_full.rs -o $(BUILD_DIR)/dijkstra_rust_test
	./$(BUILD_DIR)/dijkstra_rust_test
	javac -d $(BUILD_DIR) algorithms/04_java/graphs/DijkstraFull.java
	java -cp $(BUILD_DIR) DijkstraFull

test-primality: $(BUILD_DIR)
	@echo ">>> Testing Primality and Factorization implementations..."
	$(PYTHON) algorithms/01_python/math/miller_rabin.py
	$(CC) -O3 algorithms/02_c/math/miller_rabin.c -o $(BUILD_DIR)/mr_c_test -lm
	./$(BUILD_DIR)/mr_c_test
	$(RUSTC) -O algorithms/09_rust/math/miller_rabin.rs -o $(BUILD_DIR)/mr_rust_test
	./$(BUILD_DIR)/mr_rust_test

test-matrix: $(BUILD_DIR)
	@echo ">>> Testing Matrix multiplication implementations..."
	$(PYTHON) algorithms/01_python/math/strassen.py
	$(CC) -O3 algorithms/02_c/math/matmul_tiled.c -o $(BUILD_DIR)/matmul_c_test
	./$(BUILD_DIR)/matmul_c_test
	$(FC) -O3 algorithms/24_fortran/math/matmul_blocked.f90 -o $(BUILD_DIR)/matmul_f90_test
	./$(BUILD_DIR)/matmul_f90_test

test-scc: $(BUILD_DIR)
	@echo ">>> Testing Strongly Connected Components implementations..."
	$(PYTHON) algorithms/01_python/graphs/kosaraju.py
	$(CXX) -O3 algorithms/03_cpp/graphs/kosaraju.cpp -o $(BUILD_DIR)/scc_cpp_test
	./$(BUILD_DIR)/scc_cpp_test
	$(GO) run algorithms/11_golang/graphs/kosaraju.go

test-astar: $(BUILD_DIR)
	@echo ">>> Testing A* Shortest Path implementations..."
	$(PYTHON) algorithms/01_python/graphs/a_star.py
	$(CXX) -O3 algorithms/03_cpp/graphs/a_star.cpp -o $(BUILD_DIR)/astar_cpp_test
	./$(BUILD_DIR)/astar_cpp_test
	$(RUSTC) -O algorithms/09_rust/graphs/a_star.rs -o $(BUILD_DIR)/astar_rust_test
	./$(BUILD_DIR)/astar_rust_test
	$(GO) run algorithms/11_golang/graphs/a_star.go
	javac -d $(BUILD_DIR) algorithms/04_java/graphs/AStarGrid.java
	java -cp $(BUILD_DIR) AStarGrid

test-kmp: $(BUILD_DIR)
	@echo ">>> Testing Knuth-Morris-Pratt implementations..."
	$(PYTHON) algorithms/01_python/strings/kmp_full.py
	$(CC) -O3 algorithms/02_c/strings/kmp_full.c -o $(BUILD_DIR)/kmp_c_test
	./$(BUILD_DIR)/kmp_c_test
	$(CXX) -O3 algorithms/03_cpp/strings/kmp_full.cpp -o $(BUILD_DIR)/kmp_cpp_test
	./$(BUILD_DIR)/kmp_cpp_test
	$(RUSTC) -O algorithms/09_rust/strings/kmp_full.rs -o $(BUILD_DIR)/kmp_rust_test
	./$(BUILD_DIR)/kmp_rust_test
	$(GO) run algorithms/11_golang/strings/kmp_full.go
	javac -d $(BUILD_DIR) algorithms/04_java/strings/KMPFull.java
	java -cp $(BUILD_DIR) KMPFull

test-convexhull: $(BUILD_DIR)
	@echo ">>> Testing Convex Hull implementations..."
	$(PYTHON) algorithms/01_python/graphs/convex_hull.py
	$(CXX) -O3 algorithms/03_cpp/graphs/convex_hull.cpp -o $(BUILD_DIR)/ch_cpp_test
	./$(BUILD_DIR)/ch_cpp_test
	$(RUSTC) -O algorithms/09_rust/graphs/convex_hull.rs -o $(BUILD_DIR)/ch_rust_test
	./$(BUILD_DIR)/ch_rust_test
	$(GO) run algorithms/11_golang/graphs/convex_hull.go

test-huffman: $(BUILD_DIR)
	@echo ">>> Testing Huffman Coding implementations..."
	$(PYTHON) algorithms/01_python/strings/huffman.py
	$(CXX) -O3 algorithms/03_cpp/strings/huffman.cpp -o $(BUILD_DIR)/huffman_cpp_test
	./$(BUILD_DIR)/huffman_cpp_test
	$(RUSTC) -O algorithms/09_rust/strings/huffman.rs -o $(BUILD_DIR)/huffman_rust_test
	./$(BUILD_DIR)/huffman_rust_test
	javac -d $(BUILD_DIR) algorithms/04_java/strings/Huffman.java
	java -cp $(BUILD_DIR) Huffman

test-toposort: $(BUILD_DIR)
	@echo ">>> Testing Topological Sort implementations..."
	$(PYTHON) algorithms/01_python/graphs/topological_sort.py
	$(CXX) -O3 algorithms/03_cpp/graphs/topological_sort.cpp -o $(BUILD_DIR)/toposort_cpp_test
	./$(BUILD_DIR)/toposort_cpp_test
	$(RUSTC) -O algorithms/09_rust/graphs/topological_sort.rs -o $(BUILD_DIR)/toposort_rust_test
	./$(BUILD_DIR)/toposort_rust_test
	$(GO) run algorithms/11_golang/graphs/topological_sort.go

# --- Architectures ---

test-architectures: $(BUILD_DIR)
	@echo ">>> Testing Architectures and Concurrency Patterns..."
	javac -d $(BUILD_DIR) architectures/java_patterns/ObserverPattern.java
	java -cp $(BUILD_DIR) ObserverPattern
	javac -d $(BUILD_DIR) architectures/java_patterns/BuilderPattern.java
	java -cp $(BUILD_DIR) BuilderPattern
	$(GO) run architectures/concurrency_patterns/actor_system.go
	$(RUSTC) -O architectures/concurrency_patterns/worker_pool.rs -o $(BUILD_DIR)/wp_rust_test
	./$(BUILD_DIR)/wp_rust_test
	@echo ">>> Testing additional design-pattern families (Python)..."
	@for f in $$(find architectures/data_patterns architectures/integration_patterns architectures/resilience_patterns architectures/microservices_patterns architectures/distributed_patterns architectures/functional_patterns -name '*.py' | sort); do $(PYTHON) $$f >/dev/null || { echo "FAIL $$f"; exit 1; }; done
	@echo "Design-pattern families verified."

# --- Sparse / less common languages ---

test-sparse:
	@echo ">>> Testing sparse language implementations..."
	$(PYTHON) algorithms/01_python/math/fft.py
	-$(GO) run algorithms/11_golang/graphs/kosaraju.go 2>/dev/null || echo "(Go sparse test: require go runtime)"

# --- Competitive Programming toolkit ---

test-dsu: $(BUILD_DIR)
	@echo ">>> Testing Disjoint Set Union (Union-Find)..."
	$(PYTHON) algorithms/01_python/data_structures/dsu.py
	$(CC) -O2 algorithms/02_c/data_structures/dsu.c -o $(BUILD_DIR)/dsu_c
	./$(BUILD_DIR)/dsu_c
	$(CXX) -O2 algorithms/03_cpp/data_structures/dsu.cpp -o $(BUILD_DIR)/dsu_cpp
	./$(BUILD_DIR)/dsu_cpp
	javac -d $(BUILD_DIR) algorithms/04_java/data_structures/DSU.java && java -cp $(BUILD_DIR) DSU
	$(GO) run algorithms/11_golang/data_structures/dsu.go
	$(RUSTC) -O algorithms/09_rust/data_structures/dsu.rs -o $(BUILD_DIR)/dsu_rs && ./$(BUILD_DIR)/dsu_rs

test-binary-search: $(BUILD_DIR)
	@echo ">>> Testing Binary Search (lower/upper bound)..."
	$(PYTHON) algorithms/01_python/searching/binary_search.py
	$(CXX) -O2 algorithms/03_cpp/searching/binary_search.cpp -o $(BUILD_DIR)/bs_cpp
	./$(BUILD_DIR)/bs_cpp
	javac -d $(BUILD_DIR) algorithms/04_java/searching/BinarySearch.java && java -cp $(BUILD_DIR) BinarySearch
	$(GO) run algorithms/11_golang/searching/binary_search.go
	$(RUSTC) -O algorithms/09_rust/searching/binary_search.rs -o $(BUILD_DIR)/bs_rs && ./$(BUILD_DIR)/bs_rs

test-dp-advanced:
	@echo ">>> Testing Advanced Dynamic Programming (Kadane/LIS/MatrixChain/LPS)..."
	$(PYTHON) algorithms/01_python/dp/kadane.py
	$(PYTHON) algorithms/01_python/dp/lis.py
	$(PYTHON) algorithms/01_python/dp/matrix_chain.py
	$(PYTHON) algorithms/01_python/dp/longest_palindromic_subsequence.py
	$(CXX) -O2 algorithms/03_cpp/dp/lis.cpp -o $(BUILD_DIR)/lis_cpp && ./$(BUILD_DIR)/lis_cpp
	$(CXX) -O2 algorithms/03_cpp/dp/kadane.cpp -o $(BUILD_DIR)/kad_cpp && ./$(BUILD_DIR)/kad_cpp
	$(GO) run algorithms/11_golang/dp/lis.go
	$(RUSTC) -O algorithms/09_rust/dp/lis.rs -o $(BUILD_DIR)/lis_rs && ./$(BUILD_DIR)/lis_rs

test-number-theory:
	@echo ">>> Testing Modular Arithmetic & Number Theory..."
	$(PYTHON) algorithms/01_python/math/mod_inverse.py
	$(PYTHON) algorithms/01_python/math/ncr.py
	$(PYTHON) algorithms/01_python/math/crt.py
	$(PYTHON) algorithms/01_python/math/euler_totient.py
	$(CXX) -O2 algorithms/03_cpp/math/crt.cpp -o $(BUILD_DIR)/crt_cpp && ./$(BUILD_DIR)/crt_cpp
	$(CXX) -O2 algorithms/03_cpp/math/ncr.cpp -o $(BUILD_DIR)/ncr_cpp && ./$(BUILD_DIR)/ncr_cpp
	$(GO) run algorithms/11_golang/math/mod_inverse.go
	$(RUSTC) -O algorithms/09_rust/math/mod_inverse.rs -o $(BUILD_DIR)/mi_rs && ./$(BUILD_DIR)/mi_rs

test-strings-advanced:
	@echo ">>> Testing Advanced String Algorithms (Z/Mancher)..."
	$(PYTHON) algorithms/01_python/strings/z_algorithm.py
	$(PYTHON) algorithms/01_python/strings/manacher.py
	$(CXX) -O2 algorithms/03_cpp/strings/manacher.cpp -o $(BUILD_DIR)/man_cpp && ./$(BUILD_DIR)/man_cpp
	$(GO) run algorithms/11_golang/strings/z_algorithm.go
	$(RUSTC) -O algorithms/09_rust/strings/z_algorithm.rs -o $(BUILD_DIR)/z_rs && ./$(BUILD_DIR)/z_rs

test-graphs-advanced: $(BUILD_DIR)
	@echo ">>> Testing Advanced Graph Algorithms..."
	$(PYTHON) algorithms/01_python/graphs/max_flow_dinic.py
	$(PYTHON) algorithms/01_python/graphs/lca_binary_lifting.py
	$(PYTHON) algorithms/01_python/graphs/bipartite_check.py
	$(PYTHON) algorithms/01_python/graphs/kahn_topological_sort.py
	$(PYTHON) algorithms/01_python/graphs/bridges_articulation.py
	$(CXX) -O2 algorithms/03_cpp/graphs/max_flow_dinic.cpp -o $(BUILD_DIR)/dinic_cpp && ./$(BUILD_DIR)/dinic_cpp
	$(CXX) -O2 algorithms/03_cpp/graphs/lca_binary_lifting.cpp -o $(BUILD_DIR)/lca_cpp && ./$(BUILD_DIR)/lca_cpp
	$(GO) run algorithms/11_golang/graphs/max_flow_dinic.go
	$(RUSTC) -O algorithms/09_rust/graphs/lca_binary_lifting.rs -o $(BUILD_DIR)/lca_rs && ./$(BUILD_DIR)/lca_rs

test-techniques:
	@echo ">>> Testing Core CP Techniques..."
	$(PYTHON) algorithms/01_python/techniques/two_pointers.py
	$(PYTHON) algorithms/01_python/techniques/sliding_window.py
	$(PYTHON) algorithms/01_python/techniques/prefix_sum.py
	$(PYTHON) algorithms/01_python/techniques/backtracking.py
	$(PYTHON) algorithms/01_python/techniques/bit_manipulation.py
	$(GO) run algorithms/11_golang/techniques/sliding_window.go
	$(RUSTC) -O algorithms/09_rust/techniques/two_pointers.rs -o $(BUILD_DIR)/tp_rs && ./$(BUILD_DIR)/tp_rs

test-datastructures: $(BUILD_DIR)
	@echo ">>> Testing Advanced Data Structures..."
	$(PYTHON) algorithms/01_python/data_structures/sparse_table.py
	$(PYTHON) algorithms/01_python/data_structures/segment_tree_lazy.py
	$(PYTHON) algorithms/01_python/data_structures/monotonic_stack.py
	$(CXX) -O2 algorithms/03_cpp/data_structures/segment_tree_lazy.cpp -o $(BUILD_DIR)/stl_cpp && ./$(BUILD_DIR)/stl_cpp
	$(GO) run algorithms/11_golang/data_structures/sparse_table.go
	$(RUSTC) -O algorithms/09_rust/data_structures/segment_tree_lazy.rs -o $(BUILD_DIR)/stl_rs && ./$(BUILD_DIR)/stl_rs

test-competitive: test-dsu test-binary-search test-dp-advanced test-number-theory test-strings-advanced test-graphs-advanced test-techniques test-datastructures
	@echo ""
	@echo "COMPETITIVE PROGRAMMING TOOLKIT VERIFIED SUCCESSFULLY!"

# --- GPU, low-level and web modules ---

test-asm: $(BUILD_DIR)
	@echo ">>> Assembling and running x86-64 assembly examples..."
	@for f in algorithms/27_assembly/x86_64/*.s; do \
		base=$$(basename $$f .s); \
		$(AS) --64 $$f -o $(BUILD_DIR)/$$base.o || exit 1; \
		$(LD) $(BUILD_DIR)/$$base.o -o $(BUILD_DIR)/$$base || exit 1; \
	done
	@$(BUILD_DIR)/hello_world > /dev/null
	@$(BUILD_DIR)/exit_42; test $$? -eq 42 || { echo "exit_42 failed"; exit 1; }
	@$(BUILD_DIR)/fibonacci; test $$? -eq 55 || { echo "fibonacci failed"; exit 1; }
	@$(BUILD_DIR)/gcd; test $$? -eq 12 || { echo "gcd failed"; exit 1; }
	@$(BUILD_DIR)/bubble_sort; test $$? -eq 1 || { echo "bubble_sort failed"; exit 1; }
	@echo "x86-64 assembly verified."
	@for f in algorithms/27_assembly/arm64/*.s; do clang --target=aarch64-linux-gnu -c $$f -o $(BUILD_DIR)/$$(basename $$f .s).a64.o || exit 1; done
	@for f in algorithms/27_assembly/riscv64/*.s; do clang --target=riscv64-linux-gnu -c $$f -o $(BUILD_DIR)/$$(basename $$f .s).rv.o || exit 1; done
	@echo "AArch64 and RISC-V assembly verified."

test-llvm-ir:
	@echo ">>> Verifying generated LLVM IR..."
	@command -v opt >/dev/null 2>&1 || { echo "opt not found; skipping LLVM IR verification."; exit 0; }
	@for f in algorithms/30_llvm_ir/*/*.ll; do opt -passes=verify -disable-output $$f || exit 1; done
	@echo "LLVM IR verified."

test-wasm:
	@echo ">>> Validating WebAssembly text modules..."
	@python3 -c "import wasmtime" 2>/dev/null || { echo "wasmtime python package not found; skipping."; exit 0; }
	@python3 -c "import glob, wasmtime; [wasmtime.wat2wasm(open(f).read()) for f in glob.glob('algorithms/31_wasm/*.wat')]; print('WebAssembly modules validated.')"

test-web:
	@echo ">>> Validating web assets..."
	@python3 -c "import glob, json; [json.load(open(f)) for f in glob.glob('web/json/*.json')]; [json.loads(l) for f in glob.glob('web/json/*.jsonl') for l in open(f) if l.strip()]; print('JSON validated.')"
	@python3 -c "import glob, xml.etree.ElementTree as ET; [ET.parse(f) for f in glob.glob('web/xml/*')]; print('XML validated.')"
	@if command -v sass >/dev/null 2>&1; then sass --no-source-map web/scss/main.scss $(BUILD_DIR)/web.css && echo "Sass compiled."; else echo "sass not found; skipping Sass."; fi

test-cuda:
	@echo ">>> Testing NVIDIA CUDA samples..."
	@if command -v nvcc >/dev/null 2>&1; then \
		nvcc -arch=sm_90 -I algorithms/26_cuda/Common algorithms/26_cuda/cpp/0_Introduction/vectorAdd/vectorAdd.cu -o $(BUILD_DIR)/cuda_vectorAdd && echo "CUDA sample compiled."; \
	else \
		echo "nvcc not found; skipping CUDA build (sources are reference-only)."; \
	fi

test-devops:
	@echo ">>> Validating DevOps configuration..."
	@python3 -c "import glob, yaml; fs=glob.glob('devops/**/*.yml', recursive=True); [list(yaml.safe_load_all(open(f))) for f in fs if '/helm/templates/' not in f]; print('DevOps YAML validated (%d files).' % len(fs))"
	@for f in devops/scripts/*.sh; do bash -n "$$f" || exit 1; done
	@echo "DevOps shell scripts validated."

test-interview: $(BUILD_DIR)
	@echo ">>> Running interview-preparation self-checks..."
	@for f in $$(find interview_prep -name '*.py' | sort); do timeout 60 $(PYTHON) $$f >/dev/null || { echo "FAIL $$f"; exit 1; }; done
	@echo "Interview Python checks passed."
	@if command -v g++ >/dev/null 2>&1; then \
		g++ -std=c++20 interview_prep/cpp/stl_from_scratch/test_all.cpp -o $(BUILD_DIR)/interview_stl || exit 1; \
		$(BUILD_DIR)/interview_stl || exit 1; \
		g++ -std=c++20 -pthread interview_prep/concurrency/thread_pool.cpp -o $(BUILD_DIR)/interview_thread_pool || exit 1; \
		$(BUILD_DIR)/interview_thread_pool || exit 1; \
		g++ -std=c++20 -fcoroutines interview_prep/deep_dives/01_cpp20_big_four/coroutine_generator.cpp -o $(BUILD_DIR)/dd_coro || exit 1; \
		$(BUILD_DIR)/dd_coro || exit 1; \
		g++ -std=c++20 interview_prep/deep_dives/14_reinventing_the_wheel/test_suite.cpp -o $(BUILD_DIR)/dd_wheel || exit 1; \
		$(BUILD_DIR)/dd_wheel || exit 1; \
		echo "Interview C++ checks passed."; \
	else echo "g++ not found; skipping C++ checks."; fi

test-formal-physics:
	@echo ">>> Verifying formal physics (Lean 4 / Mathlib)..."
	@if command -v lake >/dev/null 2>&1 && [ -d formal_physics/.lake/packages/mathlib ]; then \
		cd formal_physics && lake build; \
	else echo "lake/Mathlib not available locally; run formal_physics/scripts/verify.sh."; fi

# --- Aggregate targets ---

test-algorithms: test-fft test-dijkstra test-primality test-matrix test-scc test-astar test-kmp test-convexhull test-huffman test-toposort
	@echo ""
	@echo "ALGORITHM SUITES VERIFIED SUCCESSFULLY!"

test: test-python test-c test-cpp test-java test-rust test-fortran test-js test-go test-scripts test-algorithms test-competitive test-architectures test-asm test-llvm-ir test-wasm test-web test-cuda test-devops test-interview
	@echo ""
	@echo "================================================================="
	@echo "ALL REPOSITORY TEST SUITES EXECUTED AND VERIFIED SUCCESSFULLY!"
	@echo "================================================================="

clean:
	rm -rf $(BUILD_DIR)