#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_rolling_median_multiset_d58 {
struct WindowMedianSpec {
    int k = 3;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "rolling_median_multiset_d58";
    int version = 1;
};
} // namespace codes_rolling_median_multiset_d58
