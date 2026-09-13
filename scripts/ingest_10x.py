import os
import shutil
import sys

DEST_BASE = "/home/igorkan/repos/codes"
SRC_BASE = "/tmp/expansion_sources_10x"

# Filter settings
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB
EXCLUDED_EXTS = {
    ".o", ".a", ".so", ".dylib", ".dll", ".exe", ".bin",
    ".jar", ".war", ".ear", ".class",
    ".tar", ".gz", ".zip", ".bz2", ".xz", ".7z",
    ".png", ".jpg", ".jpeg", ".gif", ".ico", ".svg", ".bmp", ".webp",
    ".pdf", ".mp4", ".mov", ".avi", ".wasm", ".pyc", ".pyo"
}
EXCLUDED_DIRS = {".git", ".github", ".vscode", "build", "dist", "target", "node_modules"}

def copy_tree_filtered(src, dst):
    if not os.path.exists(src):
        print(f"Warning: source does not exist: {src}")
        return 0, 0
    os.makedirs(dst, exist_ok=True)
    total_bytes = 0
    total_files = 0
    for root, dirs, files in os.walk(src):
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS and not d.startswith(".")]
        rel_root = os.path.relpath(root, src)
        dest_dir = os.path.join(dst, rel_root) if rel_root != "." else dst
        os.makedirs(dest_dir, exist_ok=True)
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in EXCLUDED_EXTS:
                continue
            fp = os.path.join(root, f)
            try:
                if os.path.islink(fp):
                    continue
                sz = os.path.getsize(fp)
                if sz > MAX_FILE_SIZE or sz == 0:
                    continue
                dfp = os.path.join(dest_dir, f)
                shutil.copy2(fp, dfp)
                total_bytes += sz
                total_files += 1
            except Exception:
                pass
    return total_bytes, total_files

mappings = [
    # (source_rel_path, dest_rel_path, description)
    # Python
    ("scipy", "languages/01_python/scipy", "SciPy scientific algorithms"),
    ("astropy", "languages/01_python/astropy", "AstroPy astronomy algorithms"),
    ("cpython/Lib", "languages/01_python/cpython_lib", "CPython standard library"),
    # C
    ("linux_core", "languages/02_c/linux_kernel", "Linux kernel core (mm, crypto, fs, net)"),
    ("freebsd/sys", "languages/02_c/freebsd_sys", "FreeBSD kernel and subsystems"),
    ("postgres/src", "languages/02_c/postgres", "PostgreSQL database engine"),
    ("sqlite_core/src", "languages/02_c/sqlite", "SQLite relational database engine"),
    ("curl_core/lib", "languages/02_c/curl", "libcurl network protocols engine"),
    ("cpython/Python", "languages/02_c/cpython_vm", "CPython bytecode interpreter"),
    ("cpython/Objects", "languages/02_c/cpython_objects", "CPython object implementations"),
    ("gcc_core/gcc", "languages/02_c/gcc_optimizer", "GCC compiler tree-ssa & optimizer"),
    # C++
    ("llvm_core/llvm", "languages/03_cpp/llvm", "LLVM core optimizer and code generator"),
    ("llvm_core/clang", "languages/03_cpp/clang", "Clang C/C++ AST and parser"),
    ("llvm_core/lld", "languages/03_cpp/lld", "LLD high-performance linker"),
    ("duckdb/src", "languages/03_cpp/duckdb", "DuckDB vectorized analytical database"),
    ("clickhouse_core/src", "languages/03_cpp/clickhouse", "ClickHouse analytical DBMS engine"),
    ("pytorch/aten", "languages/03_cpp/pytorch_aten", "PyTorch ATen tensor operations"),
    ("pytorch/c10", "languages/03_cpp/pytorch_c10", "PyTorch C10 core primitives"),
    ("zig/lib/std", "languages/03_cpp/zig_std", "Zig standard library"),
    ("v8_core/src", "languages/03_cpp/v8_engine", "V8 JavaScript & WebAssembly engine"),
    ("tensorflow_core/tensorflow", "languages/03_cpp/tensorflow_core", "TensorFlow machine learning core"),
    # Java
    ("openjdk/src/java.base", "languages/04_java/openjdk_base", "OpenJDK java.base runtime & collections"),
    ("kafka_core", "languages/04_java/kafka", "Apache Kafka distributed log & clients"),
    ("flink_core", "languages/04_java/flink", "Apache Flink stream processing runtime"),
    # C#
    ("dotnet_libraries/src/libraries", "languages/05_csharp/dotnet_bcl", ".NET Base Class Library (BCL)"),
    # JavaScript
    ("nodejs_core/lib", "languages/06_javascript/nodejs_lib", "Node.js core JavaScript modules"),
    # TypeScript
    ("ms_typescript/src", "languages/07_typescript/compiler", "TypeScript compiler and typechecker"),
    # R
    ("r_source/src", "languages/08_r/r_core", "R interpreter and standard package sources"),
    # Rust
    ("rust_std/library", "languages/09_rust/library", "Rust standard library (core, alloc, std)"),
    ("rust_std/compiler", "languages/09_rust/compiler", "Rustc compiler internals"),
    # Go
    ("go_std/src", "languages/11_golang/std", "Go standard library & runtime"),
    ("kubernetes/pkg", "languages/11_golang/kubernetes_pkg", "Kubernetes cluster architecture"),
    ("kubernetes/staging", "languages/11_golang/kubernetes_client", "Kubernetes client-go & staging"),
    # PHP
    ("php_core/Zend", "languages/12_php/zend_engine", "PHP Zend virtual machine"),
    ("php_core/ext", "languages/12_php/extensions", "PHP standard extensions"),
    # Swift
    ("swift/stdlib", "languages/13_swift/stdlib", "Swift standard library"),
    ("swift/lib", "languages/13_swift/lib", "Swift compiler & SIL optimizer"),
    # Julia
    ("julia_std/stdlib", "languages/14_julia/stdlib", "Julia standard library"),
    ("julia_std/src", "languages/14_julia/src", "Julia runtime and numerical engine"),
    # Ruby
    ("ruby_core/lib", "languages/15_ruby/stdlib", "Ruby standard library"),
    ("ruby_core/ext", "languages/15_ruby/ext", "Ruby core C extensions"),
    # Kotlin
    ("kotlin_stdlib/libraries/stdlib", "languages/16_kotlin/stdlib", "Kotlin standard library"),
    # OCaml
    ("ocaml_std/stdlib", "languages/18_ocaml/stdlib", "OCaml standard library"),
    ("ocaml_std/parsing", "languages/18_ocaml/parsing", "OCaml lexer and parser"),
    # Lua
    ("lua_core", "languages/19_lua/lua_core", "Lua interpreter, VM and garbage collector"),
    # Lisp / Clojure
    ("clojure_std/src/clj", "languages/20_lisp/clojure_std", "Clojure standard library"),
    # Scala
    ("spark_core", "languages/21_scala/spark", "Apache Spark distributed engine"),
    # Haskell
    ("ghc/compiler", "languages/22_haskell/ghc_compiler", "Glasgow Haskell Compiler"),
    ("ghc/libraries/base", "languages/22_haskell/base_lib", "Haskell base library"),
    # Elixir
    ("elixir_std/lib/elixir", "languages/23_elixir/std", "Elixir standard library"),
    # Lean 4
    ("mathlib4/Mathlib", "languages/25_lean4/mathlib4", "Lean 4 Mathlib formal mathematics"),
    # Dart Systems
    ("dart_sdk/pkg", "architectures/dart_systems/pkg", "Dart SDK core packages"),
    ("dart_sdk/sdk/lib", "architectures/dart_systems/lib", "Dart SDK core libraries")
]

grand_total_bytes = 0
grand_total_files = 0

for src_rel, dst_rel, desc in mappings:
    src_full = os.path.join(SRC_BASE, src_rel)
    dst_full = os.path.join(DEST_BASE, dst_rel)
    if not os.path.exists(src_full):
        print(f"Skipping missing source: {src_full}")
        continue
    print(f"Ingesting {desc} ({src_rel} -> {dst_rel})...", flush=True)
    b, f = copy_tree_filtered(src_full, dst_full)
    grand_total_bytes += b
    grand_total_files += f
    print(f"  Copied {f} files, {b / (1024*1024):.2f} MB", flush=True)

print("=" * 60, flush=True)
print(f"Grand Total Ingested: {grand_total_files} files, {grand_total_bytes / (1024*1024):.2f} MB ({grand_total_bytes / (1024*1024*1024):.3f} GB)", flush=True)
