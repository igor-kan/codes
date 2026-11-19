#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_stoer_wagner_global_mincut;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    std::vector<std::vector<std::int64_t>> g = {
        {0, 10, 10, 0}, {10, 0, 10, 1}, {10, 10, 0, 0}, {0, 1, 0, 0}
    };
    assert(stoer_wagner_mincut(4, g).weight == 1);
    return 0;
}
