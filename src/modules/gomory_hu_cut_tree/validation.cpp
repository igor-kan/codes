#include "interface.hpp"

namespace codes_gomory_hu_cut_tree {
void validate_graph(int n, const std::vector<UndirectedEdge>& edges) {
    if (n <= 0) throw std::invalid_argument("vertex count must be positive");
    for (const auto& e : edges) {
        if (e.u < 0 || e.u >= n || e.v < 0 || e.v >= n || e.cap < 0) {
            throw std::out_of_range("invalid undirected capacity edge");
        }
    }
}
} // namespace codes_gomory_hu_cut_tree
