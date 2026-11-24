#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_dsu_bipartite_parity_d59 {
struct ParityEdge {
    int u = 0;
    int v = 0;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "dsu_bipartite_parity_d59";
    int version = 1;
};
} // namespace codes_dsu_bipartite_parity_d59
