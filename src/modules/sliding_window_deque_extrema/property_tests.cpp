#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_sliding_window_deque_extrema;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    std::vector<long long> ys = {4, -2, 8, 1, 9, -5, 6};
    auto mx = sliding_window_max(ys, 3);
    auto mn = sliding_window_min(ys, 3);
    assert(mx.size() == mn.size());
    for (std::size_t i = 0; i < mx.size(); ++i) assert(mx[i] >= mn[i]);
    return 0;
}
