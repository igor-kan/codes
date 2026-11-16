#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_min_cost_max_flow_spfa {
struct FlowArc {
    std::size_t from = 0;
    std::size_t to = 0;
    int64_t cap = 0;
    int64_t cost = 0;
};

struct FlowSolution {
    int64_t total_flow = 0;
    int64_t total_cost = 0;
    std::vector<int64_t> arc_flows;
};
} // namespace codes_min_cost_max_flow_spfa
