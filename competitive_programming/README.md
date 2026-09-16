# Competitive Programming Solutions

Original, self-contained solutions to classic Codeforces and LeetCode
problems, organised by platform and language. Every file carries an inline
self-test, so it can be executed directly to verify correctness.

## Layout

```
competitive_programming/
├── codeforces/
│   ├── 01_python/       # 20 classic problems (4A, 1A, 71A, 158A, ...)
│   ├── 04_java/
│   ├── 06_javascript/
│   ├── 07_typescript/
│   ├── 09_rust/
│   └── 11_golang/
└── leetcode/
    ├── 01_python/       # 20 problems (7, 9, 13, 14, 26, ... 1480)
    ├── 03_cpp/
    ├── 06_javascript/
    ├── 07_typescript/
    ├── 09_rust/
    └── 11_golang/
```

All solutions are written from scratch; none are copied from external
solution archives. Problems are referenced by their public number and slug
only, which keeps the repository free of third-party problem statements.

## Running a solution

Each file is standalone. For example:

```bash
python3 competitive_programming/codeforces/01_python/4a_watermelon.py
node competitive_programming/leetcode/06_javascript/7_reverse_integer.js
go run competitive_programming/leetcode/11_golang/704_binary_search.go
javac -d /tmp/out competitive_programming/codeforces/04_java/Watermelon.java
java -ea -cp /tmp/out Watermelon
```

A solution passes when it prints its `... ok` line and exits with status 0.
