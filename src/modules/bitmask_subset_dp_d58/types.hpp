#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_bitmask_subset_dp_d58 {
struct AssignDim {
    int n = 0;
    long long min_cost = 0;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "bitmask_subset_dp_d58";
    int version = 1;
};
} // namespace codes_bitmask_subset_dp_d58
