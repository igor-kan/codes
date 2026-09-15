# Interview Preparation

A study and practice vault for software-engineering interviews, organized around
a ~8-week plan that runs algorithm practice concurrently with systems topics.
Every item is small and runnable (or a focused note) so it can be reviewed
quickly and committed independently.

## Roadmap

| Track | Budget | Focus | Directory |
|:---|:---|:---|:---|
| Algorithms | 1:46 | LeetCode patterns, ~1900 contest rating, daily practice | `algorithms/` |
| C++ | 2:10 | *A Tour of C++*, *Effective C++*, *Effective Modern C++*, 100 questions, STL from scratch | `cpp/` |
| Concurrency | 4:30 | *C++ Concurrency in Action* (1 month) | `concurrency/` |
| Python | 4:50 | *Fluent Python* | `python/` |
| Computer Networking | 5:10 | *Computer Networking: A Top-Down Approach*, Ch. 1-5 (2 months) | `networking/` |
| Operating Systems | 5:46 | *Operating Systems: Three Easy Pieces*: virtualization + concurrency | `operating_systems/` |
| Computer Architecture | 6:20 | Caches, branch prediction, memory hierarchy | `computer_architecture/` |
| System Design | 6:45 | Low-level/high-throughput design, DDIA, Alex Xu (3 months) | `system_design/` |
| Behavioral | 7:38 | STAR stories for team trust (3 days) | `behavioral/` |
| Math & Statistics | 7:58 | Probability/statistics, the "Green Book" (optional, ~10%) | `math_stats/` |

The times are cumulative offsets in the original plan; a sensible schedule runs
algorithms every day while one systems topic is in focus.

## Layout

```
interview_prep/
├── algorithms/            LeetCode patterns: arrays, strings, linked lists, trees,
│                          graphs, DP, heap/trie/bit, techniques
├── cpp/
│   ├── stl_from_scratch/  my_vector, my_string, my_shared_ptr, my_optional, ...
│   ├── tour/              A Tour of C++ examples
│   ├── effective/         Effective C++ / Effective Modern C++ examples
│   └── questions/         100 interview questions + answer programs
├── concurrency/           C++ Concurrency in Action: threads, locks, atomics,
│                          lock-free structures, futures, thread pools
├── python/                Fluent Python: data model, generators, decorators,
│                          descriptors, metaclasses, asyncio
├── networking/            Top-down Ch. 1-5: apps, transport, network, link, sockets
├── operating_systems/     OSTEP: virtualization, memory, concurrency, persistence
├── computer_architecture/ caches, branch prediction, memory hierarchy, pipelining
├── system_design/         fundamentals, low-level, DDIA notes, worked designs
├── behavioral/            STAR method, story banks, question bank
├── math_stats/            probability, statistics, linear algebra, Monte Carlo
└── deep_dives/            numbered deep dives (C++20, STL, smart pointers,
                           reimplementation, networking 15-19, OS 20-31)
```

## Deep dives

`deep_dives/` contains focused, numbered treatments of the C++20 Big Four, STL
internals, smart pointers, reimplementing the standard library, and the full
networking and operating-systems syllabi. See
[`deep_dives/README.md`](deep_dives/README.md) for the topic index.

## How to use

```bash
# Run a Python practice file (each has self-checks)
python3 algorithms/arrays/two_sum.py

# Build and run the from-scratch STL test suite
g++ -std=c++20 cpp/stl_from_scratch/test_all.cpp -o /tmp/stl && /tmp/stl

# Build a concurrency example
g++ -std=c++20 -pthread concurrency/thread_pool.cpp -o /tmp/tp && /tmp/tp
```

## Method

- **Algorithms:** learn the pattern, implement from scratch, then time yourself on
  a new variant. Keep a mistake log and revisit spaced-repetition style.
- **C++:** reproduce STL components to internalize move semantics, RAII and
  templates; then map each *Effective* item to a code example.
- **Concurrency:** reason about every example under the C++ memory model, and
  verify with ThreadSanitizer (`-fsanitize=thread`).
- **Systems:** connect book chapters to back-of-envelope estimates and to the
  worked designs in `system_design/designs/`.
- **Behavioral:** maintain 6-8 STAR stories that can be remixed across prompts.
