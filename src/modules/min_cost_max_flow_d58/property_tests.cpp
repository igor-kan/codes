#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_min_cost_max_flow_d58;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    std::vector<CostArc> par = {{0,1,1,10},{0,2,1,2},{1,3,1,10},{2,3,1,2}};
    auto [fl, cs] = min_cost_max_flow(4, 0, 3, par);
    assert(fl == 2 && cs == 24);
    return 0;
}
