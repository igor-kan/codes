#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_stochastic_universal_sampl;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    std::vector<double> w = {0.25, 0.25, 0.25, 0.25};
    VoseAliasSampler vs(w);
    assert(vs.sample_one(2, 0.1) == 2);
    return 0;
}
