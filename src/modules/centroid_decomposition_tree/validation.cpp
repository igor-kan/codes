#include "interface.hpp"

namespace codes_centroid_decomposition_tree {
void validate_tree(int n, const std::vector<std::pair<int, int>>& edges) {
    if (n <= 0 || static_cast<int>(edges.size()) != n - 1) {
        throw std::invalid_argument("Centroid decomposition requires n > 0 and n - 1 edges");
    }
    for (const auto& e : edges) {
        if (e.first < 0 || e.first >= n || e.second < 0 || e.second >= n || e.first == e.second) {
            throw std::out_of_range("invalid tree edge");
        }
    }
}
} // namespace codes_centroid_decomposition_tree
