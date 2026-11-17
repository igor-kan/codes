#include "interface.hpp"

namespace codes_blossom_general_matching {
void validate_matching_input(int n, const std::vector<std::pair<int, int>>& edges) {
    if (n <= 0) throw std::invalid_argument("vertex count must be positive");
    for (const auto& e : edges) {
        if (e.first < 0 || e.first >= n || e.second < 0 || e.second >= n || e.first == e.second) {
            throw std::out_of_range("invalid undirected matching edge");
        }
    }
}
} // namespace codes_blossom_general_matching
