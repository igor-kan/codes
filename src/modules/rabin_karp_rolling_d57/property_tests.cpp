#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_rabin_karp_rolling_d57;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    std::string t = "mississippi", p = "ssi";
    for (int idx : rabin_karp_search(t, p)) assert(t.substr(idx, p.size()) == p);
    return 0;
}
