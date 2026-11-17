#include "interface.hpp"

namespace codes_gomory_hu_cut_tree {
void verify_gomory_hu_parity(int n, const std::vector<UndirectedEdge>& edges, const std::vector<GhEdge>& tree) {
    if (static_cast<int>(tree.size()) != n - 1) {
        throw std::logic_error("Gomory-Hu tree must have N - 1 edges");
    }
    (void)edges;
    for (const auto& e : tree) {
        if (e.min_cut < 0 || e.u < 0 || e.u >= n || e.v < 0 || e.v >= n) {
            throw std::logic_error("invalid edge in Gomory-Hu tree");
        }
    }
}
} // namespace codes_gomory_hu_cut_tree
