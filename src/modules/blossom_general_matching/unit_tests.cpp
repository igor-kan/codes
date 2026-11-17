#include "interface.hpp"
#include <cassert>

int main() {
    using namespace codes_blossom_general_matching;
    // Triangle + tail + odd pentagon: cannot be matched without blossom shrinking
    std::vector<std::pair<int, int>> edges = {
        {0,1},{1,2},{2,3},{3,4},{4,0},{1,5}
    };
    auto res = edmonds_blossom_matching(6, edges);
    verify_matching_invariants(6, edges, res);
    assert(res.pairs == 3);
    return 0;
}
