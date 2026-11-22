#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_bellman_ford_spfa_d57 {
struct DirWeightedEdge {
    int u = 0;
    int v = 0;
    long long w = 0;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "bellman_ford_spfa_d57";
    int version = 1;
};
} // namespace codes_bellman_ford_spfa_d57
