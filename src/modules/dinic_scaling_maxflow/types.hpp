#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_dinic_scaling_maxflow {
struct FlowEdge {
    int to;
    int rev;
    std::int64_t cap;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "dinic_scaling_maxflow";
    int version = 1;
};
} // namespace codes_dinic_scaling_maxflow
