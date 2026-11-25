#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_aho_corasick_dfa_d60;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    AhoCorasick ac;
    ac.add_pattern("aba");
    ac.add_pattern("ba");
    ac.build();
    assert(ac.count_matches("ababa") == 4);
    return 0;
}
