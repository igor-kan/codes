#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_aho_kmp_failure_automaton;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    auto s = scan_ac_dfa({"ab", "aba", "ba"}, "ababa");
    assert(s.matches == 6);
    return 0;
}
