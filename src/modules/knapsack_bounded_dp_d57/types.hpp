#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_knapsack_bounded_dp_d57 {
struct BoundedBundle {
    int weight = 0;
    long long value = 0;
    int count = 0;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "knapsack_bounded_dp_d57";
    int version = 1;
};
} // namespace codes_knapsack_bounded_dp_d57
