#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_suffix_automaton_lcs;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    SuffixAutomatonLcs sam("abcdefgh");
    assert(sam.count_distinct_substrings() == 36);
    assert(sam.longest_common_substring("xyzcdefg") == 5);
    return 0;
}
