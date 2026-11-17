#include "interface.hpp"
#include <cassert>

int main() {
    using namespace codes_blossom_general_matching;
    std::vector<std::pair<int, int>> c5 = {{0,1},{1,2},{2,3},{3,4},{4,0}};
    std::vector<std::pair<int, int>> k6;
    for (int i = 0; i < 6; ++i)
        for (int j = i + 1; j < 6; ++j) k6.emplace_back(i, j);
    auto out = parallel_matching_batch({{5, c5}, {6, k6}});
    assert(out[0].pairs == 2);
    assert(out[1].pairs == 3);
    verify_matching_invariants(5, c5, out[0]);
    verify_matching_invariants(6, k6, out[1]);
    return 0;
}
