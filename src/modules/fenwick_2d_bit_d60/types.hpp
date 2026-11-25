#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_fenwick_2d_bit_d60 {
struct GridPoint {
    int r;
    int c;
    std::int64_t delta;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "fenwick_2d_bit_d60";
    int version = 1;
};
} // namespace codes_fenwick_2d_bit_d60
