#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_dinic_max_flow_d60 {
struct FlowEdge {
    int to;
    int rev;
    std::int64_t cap;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "dinic_max_flow_d60";
    int version = 1;
};
} // namespace codes_dinic_max_flow_d60
