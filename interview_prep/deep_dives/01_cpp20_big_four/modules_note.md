# C++20 Modules

Modules replace textual `#include` with compiled interfaces, removing macro
leakage, improving build times, and giving a stable ABI boundary for templates.

## Module units

- **Primary module interface:** `export module math;`
- **Partition:** `export module math:geometry;` imported with
  `import :geometry;`
- **Implementation unit:** `module math;` (no export).
- **Header unit:** `import <vector>;` or `import "legacy.hpp";`.

## Exports and imports

```cpp
// math.ixx
export module math;
export int add(int a, int b) { return a + b; }
export namespace trig { double sin_deg(double d); }
```

```cpp
// main.cpp
import math;
import <iostream>;
int main() { std::cout << add(2, 3) << '\n'; }
```

## Build notes

- GCC: `g++ -std=c++20 -fmodules-ts -x c++ math.ixx -c` then link.
- Clang/CMake: `CMAKE_CXX_SCAN_FOR_MODULES`.
- Modules are not yet universally supported; the `modules/` files here are
  reference examples (`-fsyntax-only` may be required on older toolchains).

See `modules/math.ixx` and `modules/main.cpp`.
