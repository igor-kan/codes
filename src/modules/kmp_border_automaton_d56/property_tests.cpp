#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_kmp_border_automaton_d56;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    std::string txt = "aaabaaaab";
    std::string pat = "aa";
    auto hits = kmp_find_all(txt, pat);
    for (int pos : hits) assert(txt.substr(pos, pat.size()) == pat);
    return 0;
}
