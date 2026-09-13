# ==============================================================================
# Code & Scripts Repository: Master Build & Verification Harness
# ==============================================================================

CC ?= gcc
CXX ?= g++
FC = gfortran
PYTHON ?= python3
NODE ?= node
RUSTC ?= rustc
GO ?= go
BUILD_DIR = build

.PHONY: all test clean help \
	test-python test-c test-cpp test-java test-lua test-rust test-fortran test-js test-go test-scripts \
	test-fft test-dijkstra test-primality test-matrix test-scc \
	test-astar test-kmp test-convexhull test-huffman test-toposort test-architectures \
	test-algorithms

all: test

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

help:
	@echo "Repository Build & Execution Matrix"
	@echo "Available test targets:"
	@echo "  make test-python        Run Python scripts"
	@echo "  make test-c             Compile and execute C routines"
	@echo "  make test-cpp           Compile and execute C++ routines"
	@echo "  make test-java          Compile and execute Java routines"
	@echo "  make test-lua           Execute Lua coroutine scripts"
	@echo "  make test-rust          Compile and execute Rust routines"
	@echo "  make test-fortran       Compile and execute Fortran routines"
	@echo "  make test-js            Execute JavaScript routines"
	@echo "  make test-go            Execute Golang routines"
	@echo "  make test-scripts       Execute computational Python scripts"
	@echo "  make test-astar         Execute A* Search pathfinding suite"
	@echo "  make test-kmp           Execute Knuth-Morris-Pratt string search suite"
	@echo "  make test-convexhull    Execute 2D Convex Hull geometric suite"
	@echo "  make test-huffman       Execute Huffman Data Compression suite"
	@echo "  make test-toposort      Execute DAG Topological Sorting suite"
	@echo "  make test-architectures Execute design pattern and concurrency suites"
	@echo "  make test-algorithms   Execute all core algorithm benchmark suites"
	@echo "  make test               Run full regression verification"

test-python:
	@echo ">>> Testing Python Algorithms..."
	$(PYTHON) languages/01_python/rk45_adaptive.py
	$(PYTHON) languages/01_python/disjoint_set.py

test-c: $(BUILD_DIR)
	@echo ">>> Compiling and Testing C MurmurHash3..."
	$(CC) -O3 -Wall -Wextra languages/02_c/murmurhash3.c -o $(BUILD_DIR)/murmurhash3_test
	./$(BUILD_DIR)/murmurhash3_test

test-cpp: $(BUILD_DIR)
	@echo ">>> Compiling and Testing C++ LRU Cache..."
	$(CXX) -x c++ -DCOMPILE_TEST_MAIN -O3 -std=c++17 -Wall languages/03_cpp/lru_cache.hpp -o $(BUILD_DIR)/lru_test
	./$(BUILD_DIR)/lru_test

test-java: $(BUILD_DIR)
	@echo ">>> Compiling and Testing Java Trie..."
	javac -d $(BUILD_DIR) languages/04_java/Trie.java
	java -cp $(BUILD_DIR) Trie

test-lua:
	@echo ">>> Testing Lua Cooperative Coroutine Scheduler..."
	lua languages/19_lua/coroutine_scheduler.lua

test-rust: $(BUILD_DIR)
	@echo ">>> Compiling and Testing Rust SPSC Ring Buffer..."
	$(RUSTC) -O languages/09_rust/ring_buffer.rs -o $(BUILD_DIR)/ring_buffer_test
	./$(BUILD_DIR)/ring_buffer_test

test-fortran: $(BUILD_DIR)
	@echo ">>> Compiling and Testing Fortran Numerical Solvers..."
	$(FC) -O3 languages/24_fortran/conjugate_gradient.f90 -o $(BUILD_DIR)/cg_test
	./$(BUILD_DIR)/cg_test
	$(FC) -O3 languages/24_fortran/lu_factorization.f90 -o $(BUILD_DIR)/lu_test
	./$(BUILD_DIR)/lu_test

test-js:
	@echo ">>> Executing JavaScript Asynchronous Pipeline..."
	$(NODE) languages/06_javascript/async_pipeline.js

test-go:
	@echo ">>> Executing Golang Worker Pool..."
	$(GO) run languages/11_golang/worker_pool.go

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

test-fft: $(BUILD_DIR)
	@echo ">>> Testing Fast Fourier Transform implementations..."
	$(PYTHON) algorithms/fast_fourier_transform/fft.py
	$(CXX) -O3 algorithms/fast_fourier_transform/fft.cpp -o $(BUILD_DIR)/fft_cpp_test
	./$(BUILD_DIR)/fft_cpp_test
	$(RUSTC) -O algorithms/fast_fourier_transform/fft.rs -o $(BUILD_DIR)/fft_rust_test
	./$(BUILD_DIR)/fft_rust_test

test-dijkstra: $(BUILD_DIR)
	@echo ">>> Testing Dijkstra shortest path implementations..."
	$(PYTHON) algorithms/dijkstra_shortest_path/dijkstra.py
	$(CXX) -O3 algorithms/dijkstra_shortest_path/dijkstra.cpp -o $(BUILD_DIR)/dijkstra_cpp_test
	./$(BUILD_DIR)/dijkstra_cpp_test
	$(GO) run algorithms/dijkstra_shortest_path/dijkstra.go
	$(RUSTC) -O algorithms/dijkstra_shortest_path/dijkstra.rs -o $(BUILD_DIR)/dijkstra_rust_test
	./$(BUILD_DIR)/dijkstra_rust_test
	javac -d $(BUILD_DIR) algorithms/dijkstra_shortest_path/Dijkstra.java
	java -cp $(BUILD_DIR) Dijkstra

test-primality: $(BUILD_DIR)
	@echo ">>> Testing Primality and Factorization implementations..."
	$(PYTHON) algorithms/primality_factorization/miller_rabin.py
	$(CC) -O3 algorithms/primality_factorization/miller_rabin.c -o $(BUILD_DIR)/mr_c_test
	./$(BUILD_DIR)/mr_c_test
	$(RUSTC) -O algorithms/primality_factorization/miller_rabin.rs -o $(BUILD_DIR)/mr_rust_test
	./$(BUILD_DIR)/mr_rust_test

test-matrix: $(BUILD_DIR)
	@echo ">>> Testing Matrix multiplication implementations..."
	$(PYTHON) algorithms/matrix_multiplication/strassen.py
	$(CC) -O3 algorithms/matrix_multiplication/matmul_tiled.c -o $(BUILD_DIR)/matmul_c_test
	./$(BUILD_DIR)/matmul_c_test
	$(FC) -O3 algorithms/matrix_multiplication/matmul_blocked.f90 -o $(BUILD_DIR)/matmul_f90_test
	./$(BUILD_DIR)/matmul_f90_test

test-scc: $(BUILD_DIR)
	@echo ">>> Testing Strongly Connected Components implementations..."
	$(PYTHON) algorithms/strongly_connected_components/kosaraju.py
	$(CXX) -O3 algorithms/strongly_connected_components/kosaraju.cpp -o $(BUILD_DIR)/scc_cpp_test
	./$(BUILD_DIR)/scc_cpp_test
	$(GO) run algorithms/strongly_connected_components/kosaraju.go

test-astar: $(BUILD_DIR)
	@echo ">>> Testing A* Shortest Path implementations..."
	$(PYTHON) algorithms/a_star_pathfinding/a_star.py
	$(CXX) -O3 algorithms/a_star_pathfinding/a_star.cpp -o $(BUILD_DIR)/astar_cpp_test
	./$(BUILD_DIR)/astar_cpp_test
	$(RUSTC) -O algorithms/a_star_pathfinding/a_star.rs -o $(BUILD_DIR)/astar_rust_test
	./$(BUILD_DIR)/astar_rust_test
	$(GO) run algorithms/a_star_pathfinding/a_star.go
	javac -d $(BUILD_DIR) algorithms/a_star_pathfinding/AStar.java
	java -cp $(BUILD_DIR) AStar

test-kmp: $(BUILD_DIR)
	@echo ">>> Testing Knuth-Morris-Pratt implementations..."
	$(PYTHON) algorithms/knuth_morris_pratt/kmp.py
	$(CC) -O3 algorithms/knuth_morris_pratt/kmp.c -o $(BUILD_DIR)/kmp_c_test
	./$(BUILD_DIR)/kmp_c_test
	$(CXX) -O3 algorithms/knuth_morris_pratt/kmp.cpp -o $(BUILD_DIR)/kmp_cpp_test
	./$(BUILD_DIR)/kmp_cpp_test
	$(RUSTC) -O algorithms/knuth_morris_pratt/kmp.rs -o $(BUILD_DIR)/kmp_rust_test
	./$(BUILD_DIR)/kmp_rust_test
	$(GO) run algorithms/knuth_morris_pratt/kmp.go
	javac -d $(BUILD_DIR) algorithms/knuth_morris_pratt/KMP.java
	java -cp $(BUILD_DIR) KMP

test-convexhull: $(BUILD_DIR)
	@echo ">>> Testing Convex Hull implementations..."
	$(PYTHON) algorithms/convex_hull/convex_hull.py
	$(CXX) -O3 algorithms/convex_hull/convex_hull.cpp -o $(BUILD_DIR)/ch_cpp_test
	./$(BUILD_DIR)/ch_cpp_test
	$(RUSTC) -O algorithms/convex_hull/convex_hull.rs -o $(BUILD_DIR)/ch_rust_test
	./$(BUILD_DIR)/ch_rust_test
	$(GO) run algorithms/convex_hull/convex_hull.go

test-huffman: $(BUILD_DIR)
	@echo ">>> Testing Huffman Coding implementations..."
	$(PYTHON) algorithms/huffman_coding/huffman.py
	$(CXX) -O3 algorithms/huffman_coding/huffman.cpp -o $(BUILD_DIR)/huffman_cpp_test
	./$(BUILD_DIR)/huffman_cpp_test
	$(RUSTC) -O algorithms/huffman_coding/huffman.rs -o $(BUILD_DIR)/huffman_rust_test
	./$(BUILD_DIR)/huffman_rust_test
	javac -d $(BUILD_DIR) algorithms/huffman_coding/Huffman.java
	java -cp $(BUILD_DIR) Huffman

test-toposort: $(BUILD_DIR)
	@echo ">>> Testing Topological Sort implementations..."
	$(PYTHON) algorithms/topological_sort/topological_sort.py
	$(CXX) -O3 algorithms/topological_sort/topological_sort.cpp -o $(BUILD_DIR)/toposort_cpp_test
	./$(BUILD_DIR)/toposort_cpp_test
	$(RUSTC) -O algorithms/topological_sort/topological_sort.rs -o $(BUILD_DIR)/toposort_rust_test
	./$(BUILD_DIR)/toposort_rust_test
	$(GO) run algorithms/topological_sort/topological_sort.go

test-architectures: $(BUILD_DIR)
	@echo ">>> Testing Architectures and Concurrency Patterns..."
	javac -d $(BUILD_DIR) architectures/java_patterns/ObserverPattern.java
	java -cp $(BUILD_DIR) ObserverPattern
	javac -d $(BUILD_DIR) architectures/java_patterns/BuilderPattern.java
	java -cp $(BUILD_DIR) BuilderPattern
	$(GO) run architectures/concurrency_patterns/actor_system.go
	$(RUSTC) -O architectures/concurrency_patterns/worker_pool.rs -o $(BUILD_DIR)/wp_rust_test
	./$(BUILD_DIR)/wp_rust_test

test-algorithms: test-fft test-dijkstra test-primality test-matrix test-scc test-astar test-kmp test-convexhull test-huffman test-toposort

test: test-python test-c test-cpp test-java test-lua test-rust test-fortran test-js test-go test-scripts test-algorithms test-architectures
	@echo ""
	@echo "================================================================="
	@echo "ALL REPOSITORY TEST SUITES EXECUTED AND VERIFIED SUCCESSFULLY!"
	@echo "================================================================="

clean:
	rm -rf $(BUILD_DIR)
