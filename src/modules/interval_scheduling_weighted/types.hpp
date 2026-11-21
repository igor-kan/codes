#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_interval_scheduling_weighted {
struct WeightedJob {
    long long start = 0;
    long long end = 0;
    long long weight = 0;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "interval_scheduling_weighted";
    int version = 1;
};
} // namespace codes_interval_scheduling_weighted
