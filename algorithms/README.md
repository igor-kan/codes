# Algorithms Reference Library

Polyglot algorithm implementations across **25 canonical languages** — a comprehensive competitive-programming (LeetCode/Codeforces) toolkit plus foundational algorithms — extended with GPU and low-level tiers: **CUDA, assembly, PTX, SASS, LLVM IR and WebAssembly**. Each language directory contains standalone implementations organized by category.

## Coverage Matrix

_Auto-generated coverage: ✓ = implementation present._

### Sorting

| Algorithm | Py | C | C++ | Java | C# | JS | TS | R | Rust | SQL | Go | PHP | Swift | Julia | Ruby | Kotlin | MATLAB | OCaml | Lua | Lisp | Scala | Haskell | Elixir | Fortran | Lean4 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bubble Sort | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| Insertion Sort | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ |
| Selection Sort | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |
| Merge Sort | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| Quick Sort | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ |  |  | ✓ | ✓ |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| Heap Sort | ✓ | ✓ | ✓ | ✓ |  |  |  |  | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Counting Sort | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |
| Radix Sort | ✓ | ✓ | ✓ | ✓ |  |  |  |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Shell Sort | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Bucket Sort | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### Searching

| Algorithm | Py | C | C++ | Java | C# | JS | TS | R | Rust | SQL | Go | PHP | Swift | Julia | Ruby | Kotlin | MATLAB | OCaml | Lua | Lisp | Scala | Haskell | Elixir | Fortran | Lean4 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Binary Search | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |
| Ternary Search | ✓ | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### Techniques

| Algorithm | Py | C | C++ | Java | C# | JS | TS | R | Rust | SQL | Go | PHP | Swift | Julia | Ruby | Kotlin | MATLAB | OCaml | Lua | Lisp | Scala | Haskell | Elixir | Fortran | Lean4 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Two Pointers | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Sliding Window | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Prefix Sum | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Backtracking | ✓ |  | ✓ | ✓ |  | ✓ |  |  | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Bit Manipulation | ✓ |  | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### Graphs

| Algorithm | Py | C | C++ | Java | C# | JS | TS | R | Rust | SQL | Go | PHP | Swift | Julia | Ruby | Kotlin | MATLAB | OCaml | Lua | Lisp | Scala | Haskell | Elixir | Fortran | Lean4 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BFS | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| DFS | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Dijkstra | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ |  | ✓ | ✓ |  |  | ✓ |  |  |  |  |  |  |  |  |  |  |
| A* | ✓ |  | ✓ | ✓ |  |  |  |  | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Bellman-Ford | ✓ | ✓ | ✓ | ✓ |  |  |  |  | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Floyd-Warshall | ✓ | ✓ | ✓ | ✓ |  |  |  |  | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Prim (MST) | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Kruskal (MST) | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Topological Sort | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Kahn Topo Sort | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Kosaraju SCC | ✓ |  | ✓ |  |  |  |  |  |  |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Tarjan SCC | ✓ |  |  |  |  |  |  |  |  |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Bipartite Check | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Cycle Detection | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Bridges/Articulation | ✓ | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Eulerian Path | ✓ | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Max Flow (Dinic) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| LCA (Binary Lifting) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Convex Hull | ✓ |  | ✓ |  |  |  |  |  | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### Dynamic Programming

| Algorithm | Py | C | C++ | Java | C# | JS | TS | R | Rust | SQL | Go | PHP | Swift | Julia | Ruby | Kotlin | MATLAB | OCaml | Lua | Lisp | Scala | Haskell | Elixir | Fortran | Lean4 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LCS | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |
| Knapsack | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ |  | ✓ |  |  |  |  |  |  |  | ✓ |  |  |  |  | ✓ |  |
| Edit Distance | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Levenshtein |  |  |  |  |  |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Coin Change | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Kadane (Max Subarray) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |
| LIS | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |
| Matrix Chain | ✓ |  | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Longest Palindromic Subseq | ✓ | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### Strings

| Algorithm | Py | C | C++ | Java | C# | JS | TS | R | Rust | SQL | Go | PHP | Swift | Julia | Ruby | Kotlin | MATLAB | OCaml | Lua | Lisp | Scala | Haskell | Elixir | Fortran | Lean4 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| KMP | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |  |  |  |
| Rabin-Karp | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Z-Algorithm | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |
| Manacher | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |
| Huffman | ✓ |  | ✓ | ✓ |  |  |  |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### Data Structures

| Algorithm | Py | C | C++ | Java | C# | JS | TS | R | Rust | SQL | Go | PHP | Swift | Julia | Ruby | Kotlin | MATLAB | OCaml | Lua | Lisp | Scala | Haskell | Elixir | Fortran | Lean4 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DSU (Union-Find) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |
| Trie | ✓ |  |  |  | ✓ |  |  |  | ✓ |  | ✓ | ✓ | ✓ |  |  | ✓ |  |  |  |  |  |  |  |  |  |
| Fenwick Tree | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Segment Tree | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Segment Tree (Lazy) | ✓ |  | ✓ | ✓ |  |  |  |  | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Sparse Table | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |  | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Monotonic Stack | ✓ | ✓ | ✓ | ✓ |  |  |  |  | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Monotonic Queue | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| LRU Cache | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Skip List | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Bloom Filter |  |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Linked List |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Stack | ✓ | ✓ | ✓ | ✓ |  |  |  |  | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Queue | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| BST |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### Math / Number Theory

| Algorithm | Py | C | C++ | Java | C# | JS | TS | R | Rust | SQL | Go | PHP | Swift | Julia | Ruby | Kotlin | MATLAB | OCaml | Lua | Lisp | Scala | Haskell | Elixir | Fortran | Lean4 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GCD / LCM | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Sieve of Eratosthenes | ✓ | ✓ |  |  | ✓ | ✓ |  | ✓ | ✓ |  | ✓ | ✓ |  | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |
| Fast Power | ✓ |  |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| FFT | ✓ |  | ✓ |  |  |  |  |  | ✓ |  |  |  |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| Matrix Multiplication | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ✓ |  |
| Miller-Rabin | ✓ | ✓ |  |  |  |  |  |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Modular Inverse | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| nCr mod p | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Euler Totient | ✓ | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| CRT | ✓ | ✓ | ✓ | ✓ |  |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Fibonacci |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ✓ |

### Cryptography

| Algorithm | Py | C | C++ | Java | C# | JS | TS | R | Rust | SQL | Go | PHP | Swift | Julia | Ruby | Kotlin | MATLAB | OCaml | Lua | Lisp | Scala | Haskell | Elixir | Fortran | Lean4 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Caesar Cipher | ✓ |  |  |  |  |  |  |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Vigenere |  |  |  |  |  |  |  |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### Machine Learning

| Algorithm | Py | C | C++ | Java | C# | JS | TS | R | Rust | SQL | Go | PHP | Swift | Julia | Ruby | Kotlin | MATLAB | OCaml | Lua | Lisp | Scala | Haskell | Elixir | Fortran | Lean4 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| K-Means | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Linear Regression | ✓ |  |  |  |  |  |  |  |  |  |  |  |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |

## Additional Algorithm Coverage

A second wave of algorithms was added across the major languages (and a new
`geometry/` category). The table lists where each is implemented.

| Algorithm | Languages |
|:---|:---|
| Max heap | Python, C, C++, Java, C#, JavaScript, TypeScript, Rust, Go, PHP, Julia, Ruby, Kotlin, Lua, Swift |
| Circular buffer | Python, C, C++, Java, C#, JavaScript, TypeScript, Rust, Go |
| Boyer-Moore search | Python, C, C++, Java, C#, JavaScript, TypeScript, Rust, Go, PHP, Julia, Ruby, Kotlin, Lua, Swift |
| Catalan numbers | Python, C, C++, Java, C#, JavaScript, TypeScript, Rust, Go, PHP, Julia, Ruby, Kotlin, Lua, Swift |
| Egg dropping | Python, C, C++, Java, C#, JavaScript, TypeScript, Rust, Go |
| Matrix exponentiation | Python, C, C++, Java, C#, JavaScript, TypeScript, Rust, Go |
| Gaussian elimination | Python, C, C++, Java, C#, JavaScript, TypeScript, Rust, Go |
| Point in polygon | Python, C, C++, Java, C#, JavaScript, TypeScript, Rust, Go |
| Closest pair of points | Python, C, C++, Java, C#, JavaScript, TypeScript, Rust, Go |
| Base64 codec | Python, C, C++, Java, C#, JavaScript, TypeScript, Rust, Go |
| Treap | Python, C++ |
| Splay tree | Python |
| Aho-Corasick | Python, C++ |
| Suffix array | Python |

Related suites: foundational gaps across all 25 languages are tracked by the
coverage matrix above; the new `geometry/` category holds the computational
geometry implementations.

## Language Directory Navigation

| # | Directory | Language | Files |
|---|-----------|----------|-------|
| 1 | `01_python/` | Python | 172 |
| 2 | `02_c/` | C | 66 |
| 3 | `03_cpp/` | C++ | 77 |
| 4 | `04_java/` | Java | 63 |
| 5 | `05_csharp/` | C# | 44 |
| 6 | `06_javascript/` | JavaScript | 45 |
| 7 | `07_typescript/` | TypeScript | 36 |
| 8 | `08_r/` | R | 32 |
| 9 | `09_rust/` | Rust | 62 |
| 10 | `10_sql/` | SQL | 6 |
| 11 | `11_golang/` | Go | 60 |
| 12 | `12_php/` | PHP | 21 |
| 13 | `13_swift/` | Swift | 19 |
| 14 | `14_julia/` | Julia | 21 |
| 15 | `15_ruby/` | Ruby | 21 |
| 16 | `16_kotlin/` | Kotlin | 19 |
| 17 | `17_matlab/` | MATLAB | 6 |
| 18 | `18_ocaml/` | OCaml | 15 |
| 19 | `19_lua/` | Lua | 20 |
| 20 | `20_lisp/` | Common Lisp | 16 |
| 21 | `21_scala/` | Scala | 16 |
| 22 | `22_haskell/` | Haskell | 16 |
| 23 | `23_elixir/` | Elixir | 15 |
| 24 | `24_fortran/` | Fortran | 7 |
| 25 | `25_lean4/` | Lean 4 | 5 |
| 26 | `26_cuda/` | CUDA | 668 |
| 27 | `27_assembly/` | Assembly (x86-64/AArch64/RISC-V) | 39 |
| 28 | `28_ptx/` | PTX | 20 |
| 29 | `29_sass/` | SASS | 9 |
| 30 | `30_llvm_ir/` | LLVM IR | 47 |
| 31 | `31_wasm/` | WebAssembly (WAT) | 18 |

## Testing

```bash
make test-competitive   # DSU, binary search, DP, number theory, graphs, techniques
make test-algorithms    # classic polyglot suites (FFT, Dijkstra, A*, KMP, ...)
make test               # full regression (all languages + scripts + architectures)
```
