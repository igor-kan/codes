#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_ahocorasick_automaton_d56;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    std::vector<std::string> p1 = {"ab", "bc", "bab", "d"};
    std::vector<std::string> p2 = {"d", "bab", "bc", "ab"};
    assert(ac_count_matches(p1, "babcd") == ac_count_matches(p2, "babcd"));
    return 0;
}
