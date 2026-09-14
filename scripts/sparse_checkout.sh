#!/usr/bin/env bash
# ==============================================================================
# Sparse Checkout Manager for codes Repository
# Keeps local disk footprint minimal (< 50 MB) while 3.0+ GB is safely stored on GitHub.
# ==============================================================================
set -e

CORE_PATHS=(
  "algorithms"
  "architectures/concurrency_patterns"
  "architectures/cpp_patterns"
  "architectures/distributed_patterns"
  "architectures/go_patterns"
  "architectures/java_patterns"
  "architectures/python_patterns"
  "architectures/rust_patterns"
  "architectures/typescript_patterns"
  "databases"
  "devops"
  "scripts"
  "web"
)

show_help() {
  echo "Usage: ./scripts/sparse_checkout.sh <command> [arguments]"
  echo ""
  echo "Commands:"
  echo "  minimal               Reset to minimal local footprint (< 50 MB: core algorithms, docs, scripts)"
  echo "  status                Display currently checked out sparse paths and local directory size"
  echo "  add <path>            Check out a specific language, library, or directory to local disk"
  echo "  remove <path>         Remove a directory from local disk (preserves code safely on GitHub)"
  echo "  all                   Check out the entire 3.0 GB repository locally"
  echo "  list                  List available language modules and packages"
  echo ""
  echo "Examples:"
  echo "  ./scripts/sparse_checkout.sh minimal"
  echo "  ./scripts/sparse_checkout.sh add languages/01_python"
  echo "  ./scripts/sparse_checkout.sh add languages/02_c/linux_kernel"
  echo "  ./scripts/sparse_checkout.sh remove languages/02_c/linux_kernel"
}

cmd_minimal() {
  echo "==> Configuring minimal sparse checkout (< 50 MB local footprint)..."
  git sparse-checkout init --cone
  git sparse-checkout set "${CORE_PATHS[@]}"
  echo "==> Done. Local working tree contains only core algorithms, architectures, scripts, and documentation."
  cmd_status
}

cmd_status() {
  echo "==> Current sparse checkout directories:"
  if git sparse-checkout list 2>/dev/null; then
    :
  else
    echo "  (sparse-checkout is not currently active - full repository is checked out locally)"
  fi
  echo ""
  echo "==> Local disk usage (excluding .git/):"
  du -sh --exclude=".git" . 2>/dev/null || du -sh .
}

cmd_add() {
  if [ -z "$1" ]; then
    echo "Error: missing path argument."
    echo "Usage: ./scripts/sparse_checkout.sh add <path>"
    exit 1
  fi
  echo "==> Checking out $1 locally..."
  git sparse-checkout add "$1"
  echo "==> Added $1 to local disk."
  cmd_status
}

cmd_remove() {
  if [ -z "$1" ]; then
    echo "Error: missing path argument."
    echo "Usage: ./scripts/sparse_checkout.sh remove <path>"
    exit 1
  fi
  echo "==> Removing $1 from local disk (retaining on GitHub)..."
  current_paths=$(git sparse-checkout list | grep -v "^$1$")
  git sparse-checkout set $current_paths
  echo "==> Removed $1."
  cmd_status
}

cmd_all() {
  echo "==> Disabling sparse checkout (checking out all 3.0 GB locally)..."
  git sparse-checkout disable
  echo "==> Full repository checked out."
  cmd_status
}

cmd_list() {
  echo "==> Available Language Modules in Repository:"
  echo "  languages/01_python       (SciPy, AstroPy, CPython Lib, SymPy, scikit-learn)"
  echo "  languages/02_c            (Linux Kernel, FreeBSD, PostgreSQL, SQLite, curl, GCC Optimizer)"
  echo "  languages/03_cpp          (LLVM, Clang, LLD, DuckDB, ClickHouse, V8, PyTorch, TensorFlow, Zig)"
  echo "  languages/04_java         (OpenJDK java.base, Apache Kafka, Apache Flink, Guava)"
  echo "  languages/05_csharp       (.NET Base Class Library - BCL)"
  echo "  languages/06_javascript   (Node.js Core, Lodash, D3)"
  echo "  languages/07_typescript   (TypeScript Compiler, RxJS)"
  echo "  languages/08_r            (R Core Engine & Standard Packages)"
  echo "  languages/09_rust         (Rust Std, Rustc Compiler, Tokio, Ripgrep)"
  echo "  languages/10_sql          (Pagila, dbt Models)"
  echo "  languages/11_golang       (Go Std, Kubernetes Core & Client, etcd Raft)"
  echo "  languages/12_php          (PHP Zend Engine, Standard Extensions)"
  echo "  languages/13_swift        (Swift Stdlib, Swift Compiler & SIL Optimizer)"
  echo "  languages/14_julia        (Julia Stdlib & Runtime, OrdinaryDiffEq, Distributions)"
  echo "  languages/15_ruby         (Ruby Stdlib, Core C Extensions)"
  echo "  languages/16_kotlin       (Kotlin Stdlib)"
  echo "  languages/17_matlab       (MATLAB/Octave Algorithms)"
  echo "  languages/18_ocaml        (OCaml Stdlib, Parsing Subsystem)"
  echo "  languages/19_lua          (Lua Core Interpreter & VM)"
  echo "  languages/20_lisp         (Clojure Stdlib, Common Lisp Algorithms, AIMA)"
  echo "  languages/21_scala        (Apache Spark Core, SQL, MLlib, Streaming, GraphX, Cats)"
  echo "  languages/22_haskell      (GHC Compiler, Base Library, Containers)"
  echo "  languages/23_elixir       (Elixir Stdlib)"
  echo "  languages/24_fortran      (Fortran-lang Stdlib, BLAS)"
  echo "  languages/25_lean4        (Lean 4 Mathlib Formal Mathematics)"
  echo "  algorithms/26_cuda        (NVIDIA CUDA Samples)"
  echo "  algorithms/27_assembly    (x86-64 / AArch64 / RISC-V assembly)"
  echo "  algorithms/28_ptx         (PTX kernels)"
  echo "  algorithms/29_sass        (SASS disassembly reference)"
  echo "  algorithms/30_llvm_ir     (LLVM IR)"
  echo "  algorithms/31_wasm        (WebAssembly text)"
  echo "  web                       (HTML, CSS, Sass, Tailwind, JS/TS, React, Vue, JSON, XML, GraphQL)"
  echo "  databases                 (Cypher, Gremlin, SPARQL, MongoDB, Cassandra, Redis, Elasticsearch)"
  echo "  devops                    (CI/CD, Docker, Kubernetes, Terraform, Ansible, Helm, monitoring)"
  echo "  architectures/dart_systems (Dart SDK Packages & Core Libraries)"
}

case "$1" in
  minimal)
    cmd_minimal
    ;;
  status)
    cmd_status
    ;;
  add)
    cmd_add "$2"
    ;;
  remove)
    cmd_remove "$2"
    ;;
  all)
    cmd_all
    ;;
  list)
    cmd_list
    ;;
  *)
    show_help
    ;;
esac
