#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_tarjan_bridge_cut_d60 {
struct GraphEdge {
    int u;
    int v;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "tarjan_bridge_cut_d60";
    int version = 1;
};
} // namespace codes_tarjan_bridge_cut_d60
