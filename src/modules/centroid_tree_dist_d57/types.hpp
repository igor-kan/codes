#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_centroid_tree_dist_d57 {
struct TreeExtent {
    int diameter = 0;
    int radius = 0;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "centroid_tree_dist_d57";
    int version = 1;
};
} // namespace codes_centroid_tree_dist_d57
