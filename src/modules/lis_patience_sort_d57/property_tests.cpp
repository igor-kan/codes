#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_lis_patience_sort_d57;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    std::vector<long long> inc = {1, 2, 3, 4, 5, 6};
    std::vector<long long> rev(inc.rbegin(), inc.rend());
    assert(patience_lis_length(inc) == 6 && patience_lis_length(rev) == 1);
    return 0;
}
