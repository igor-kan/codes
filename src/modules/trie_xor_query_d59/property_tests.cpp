#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_trie_xor_query_d59;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    XorTrie tr;
    std::vector<unsigned> xs = {12u, 7u, 19u, 33u};
    for (unsigned v : xs) tr.insert(v);
    unsigned brute = 0;
    for (unsigned v : xs) brute = std::max(brute, v ^ 15u);
    assert(tr.max_xor(15u) == brute);
    return 0;
}
