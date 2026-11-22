#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_edmonds_karp_flow_d57 {
struct FlowEdgeSpec {
    int u = 0;
    int v = 0;
    long long cap = 0;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "edmonds_karp_flow_d57";
    int version = 1;
};
} // namespace codes_edmonds_karp_flow_d57
