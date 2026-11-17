#include "interface.hpp"
#include <cassert>

int main() {
    using namespace codes_gomory_hu_cut_tree;
    std::vector<UndirectedEdge> k4 = {
        {0,1,3}, {0,2,3}, {0,3,3}, {1,2,3}, {1,3,3}, {2,3,3}
    };
    auto cuts = parallel_cut_queries(4, k4, {{0,1},{1,3},{2,3},{0,2}});
    for (auto c : cuts) assert(c == 9);
    auto tree = build_gomory_hu_tree(4, k4);
    auto mat = fast_all_pairs_cuts(4, tree);
    assert(mat[0 * 4 + 3] == 9);
    return 0;
}
