#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_centroid_decomposition_tree {
struct CentroidResult {
    std::vector<int> centroid_parent;
    std::vector<int> depth;
    std::vector<std::vector<std::pair<int, int>>> ancestors;
};
} // namespace codes_centroid_decomposition_tree
