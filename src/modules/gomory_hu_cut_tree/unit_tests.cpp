#include "interface.hpp"
#include <cassert>

int main() {
    using namespace codes_gomory_hu_cut_tree;
    std::vector<UndirectedEdge> edges = {
        {0, 1, 10}, {0, 2, 6}, {1, 2, 5}, {1, 3, 4}, {2, 3, 8}, {3, 4, 2}
    };
    auto tree = build_gomory_hu_tree(5, edges);
    verify_gomory_hu_parity(5, edges, tree);
    assert(query_pair_min_cut(5, tree, 0, 4) == 2);
    assert(query_pair_min_cut(5, tree, 0, 3) == 12);
    assert(query_pair_min_cut(5, tree, 1, 2) == 15);
    return 0;
}
