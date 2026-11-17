#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_gomory_hu_cut_tree {
struct UndirectedEdge {
    int u;
    int v;
    std::int64_t cap;
};

struct GhEdge {
    int u;
    int v;
    std::int64_t min_cut;
};
} // namespace codes_gomory_hu_cut_tree
