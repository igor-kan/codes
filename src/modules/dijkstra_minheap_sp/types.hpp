#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_dijkstra_minheap_sp {
struct WeightedEdge {
    int to = 0;
    long long weight = 0;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "dijkstra_minheap_sp";
    int version = 1;
};
} // namespace codes_dijkstra_minheap_sp
