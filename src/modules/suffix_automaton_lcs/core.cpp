#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_suffix_automaton_lcs {

SuffixAutomatonLcs::SuffixAutomatonLcs(const std::string& s) {
    st_.emplace_back();
    for (char ch : s) extend(ch - 'a');
}

void SuffixAutomatonLcs::extend(int c) {
    int cur = static_cast<int>(st_.size());
    st_.emplace_back();
    st_[cur].len = st_[last_].len + 1;
    int p = last_;
    while (p != -1 && st_[p].next[c] == -1) {
        st_[p].next[c] = cur;
        p = st_[p].link;
    }
    if (p == -1) {
        st_[cur].link = 0;
    } else {
        int q = st_[p].next[c];
        if (st_[p].len + 1 == st_[q].len) {
            st_[cur].link = q;
        } else {
            int clone = static_cast<int>(st_.size());
            st_.push_back(st_[q]);
            st_[clone].len = st_[p].len + 1;
            while (p != -1 && st_[p].next[c] == q) {
                st_[p].next[c] = clone;
                p = st_[p].link;
            }
            st_[q].link = st_[cur].link = clone;
        }
    }
    last_ = cur;
}

std::int64_t SuffixAutomatonLcs::count_distinct_substrings() const {
    std::int64_t total = 0;
    for (std::size_t i = 1; i < st_.size(); ++i) {
        total += st_[i].len - st_[st_[i].link].len;
    }
    return total;
}

int SuffixAutomatonLcs::longest_common_substring(const std::string& t) const {
    int v = 0, l = 0, best = 0;
    for (char ch : t) {
        int c = ch - 'a';
        while (v != 0 && st_[v].next[c] == -1) {
            v = st_[v].link;
            l = st_[v].len;
        }
        if (st_[v].next[c] != -1) {
            v = st_[v].next[c];
            ++l;
        }
        if (l > best) best = l;
    }
    return best;
}

} // namespace codes_suffix_automaton_lcs
