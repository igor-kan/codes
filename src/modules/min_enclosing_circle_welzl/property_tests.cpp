#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_min_enclosing_circle_welzl;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    auto d = minimum_enclosing_disk({{-3, 0}, {3, 0}, {0, 1}});
    assert(std::fabs(d.r - 3.0) < 1e-9);
    return 0;
}
