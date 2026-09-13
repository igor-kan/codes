# ==============================================================================
# Computational Polyglot Algorithms: Master Build & Verification Harness
# ==============================================================================

CC ?= gcc
CXX ?= g++
FC = gfortran
PYTHON ?= python3
NODE ?= node
RUSTC ?= rustc
GO ?= go
BUILD_DIR = build

.PHONY: all test test-python test-c test-cpp test-java test-lua test-rust test-fortran test-js test-go test-quarto clean help

all: test

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

help:
	@echo "Computational Polyglot Algorithms Build Matrix"
	@echo "Available test targets:"
	@echo "  make test-python    Run Python RK45 and DSU suites"
	@echo "  make test-c         Compile and execute C MurmurHash3"
	@echo "  make test-cpp       Compile and execute C++ LRU Cache"
	@echo "  make test-rust      Compile and execute Rust SPSC RingBuffer"
	@echo "  make test-fortran   Compile and execute Fortran Conjugate Gradient"
	@echo "  make test-js        Execute JavaScript concurrency pipeline"
	@echo "  make test-go        Execute Golang worker pool"
	@echo "  make test-quarto    Execute all Quarto website extracted algorithms"
	@echo "  make test           Run all available local tests"

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
	@echo ">>> Compiling and Testing Fortran Conjugate Gradient Solver..."
	$(FC) -O3 languages/24_fortran/conjugate_gradient.f90 -o $(BUILD_DIR)/cg_test
	./$(BUILD_DIR)/cg_test

test-js:
	@echo ">>> Executing JavaScript Asynchronous Pipeline..."
	$(NODE) languages/06_javascript/async_pipeline.js

test-go:
	@echo ">>> Executing Golang Worker Pool..."
	$(GO) run languages/11_golang/worker_pool.go

test-quarto:
	@echo ">>> Testing Quarto Website Mathematical & Physical Algorithms..."
	$(PYTHON) quarto_website_code/mathematics/euclidean_algorithms.py
	$(PYTHON) quarto_website_code/mathematics/finite_geometry_fano.py
	$(PYTHON) quarto_website_code/mathematics/multilinear_algebra.py
	$(PYTHON) quarto_website_code/mathematics/perfect_numbers_factorization.py
	$(PYTHON) quarto_website_code/physics/curvilinear_tensors.py
	$(PYTHON) quarto_website_code/physics/rigid_body_inertia.py
	$(PYTHON) quarto_website_code/finance/corporate_valuation_dcf.py
	$(PYTHON) quarto_website_code/computer_science/k4_planar_graph.py

test: test-python test-c test-cpp test-java test-lua test-rust test-fortran test-js test-go test-quarto
	@echo ""
	@echo "================================================================="
	@echo "ALL POLYGLOT TEST SUITES EXECUTED AND VERIFIED SUCCESSFULLY!"
	@echo "================================================================="

clean:
	rm -rf $(BUILD_DIR)
