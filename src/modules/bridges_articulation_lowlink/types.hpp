#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_bridges_articulation_lowlink {
struct UndirectedEdge {
    std::size_t u = 0;
    std::size_t v = 0;
};

struct CutReport {
    std::vector<std::size_t> bridge_edge_ids;
    std::vector<std::size_t> articulation_vertices;
};
} // namespace codes_bridges_articulation_lowlink
