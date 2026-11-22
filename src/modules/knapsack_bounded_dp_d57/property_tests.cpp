#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_knapsack_bounded_dp_d57;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    std::vector<BoundedBundle> its = {{2, 10, 5}};
    assert(bounded_knapsack_max(5, its) <= bounded_knapsack_max(7, its));
    assert(bounded_knapsack_max(7, its) == 30);
    return 0;
}
