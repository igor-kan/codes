#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_trie_xor_query_d59 {

XorTrie::XorTrie() : nodes_(1) {}

void XorTrie::insert(unsigned int val) {
    int cur = 0;
    for (int b = 30; b >= 0; --b) {
        int bit = (val >> b) & 1u;
        if (nodes_[cur].child[bit] == -1) {
            nodes_[cur].child[bit] = static_cast<int>(nodes_.size());
            nodes_.emplace_back();
        }
        cur = nodes_[cur].child[bit];
    }
}

unsigned int XorTrie::max_xor(unsigned int q) const {
    if (nodes_.size() <= 1) return 0;
    int cur = 0;
    unsigned int res = 0;
    for (int b = 30; b >= 0; --b) {
        int bit = (q >> b) & 1u;
        int want = 1 ^ bit;
        if (nodes_[cur].child[want] != -1) {
            res |= (1u << b);
            cur = nodes_[cur].child[want];
        } else {
            cur = nodes_[cur].child[bit];
        }
    }
    return res;
}

} // namespace codes_trie_xor_query_d59
