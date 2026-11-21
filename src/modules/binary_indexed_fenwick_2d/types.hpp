#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_binary_indexed_fenwick_2d {
struct RectBounds {
    int r1 = 0;
    int c1 = 0;
    int r2 = 0;
    int c2 = 0;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "binary_indexed_fenwick_2d";
    int version = 1;
};
} // namespace codes_binary_indexed_fenwick_2d
