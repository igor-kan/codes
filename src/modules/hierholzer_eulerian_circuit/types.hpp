#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_hierholzer_eulerian_circuit {
struct DirectedEdge {
    std::size_t u = 0;
    std::size_t v = 0;
};

struct EulerResult {
    bool valid = false;
    std::vector<std::size_t> vertices;
    std::vector<std::size_t> edge_ids;
};
} // namespace codes_hierholzer_eulerian_circuit
