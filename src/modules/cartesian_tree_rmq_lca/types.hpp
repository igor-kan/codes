#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_cartesian_tree_rmq_lca {
struct CartesianNode {
    int parent = -1;
    int left = -1;
    int right = -1;
    std::int64_t val = 0;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "cartesian_tree_rmq_lca";
    int version = 1;
};
} // namespace codes_cartesian_tree_rmq_lca
