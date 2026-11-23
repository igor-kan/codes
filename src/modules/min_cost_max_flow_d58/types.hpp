#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_min_cost_max_flow_d58 {
struct CostArc {
    int u = 0;
    int v = 0;
    long long cap = 0;
    long long cost = 0;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "min_cost_max_flow_d58";
    int version = 1;
};
} // namespace codes_min_cost_max_flow_d58
