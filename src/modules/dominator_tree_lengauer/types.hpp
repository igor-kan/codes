#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_dominator_tree_lengauer {
struct CfgGraph {
    int n = 0;
    std::vector<std::vector<int>> adj;
    std::vector<std::vector<int>> radj;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "dominator_tree_lengauer";
    int version = 1;
};
} // namespace codes_dominator_tree_lengauer
