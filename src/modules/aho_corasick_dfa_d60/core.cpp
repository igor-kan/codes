#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_aho_corasick_dfa_d60 {

static AcNode make_ac_node() {
    AcNode nd;
    for (int i = 0; i < 26; ++i) nd.next[i] = -1;
    nd.fail = 0;
    nd.out_cnt = 0;
    return nd;
}
AhoCorasick::AhoCorasick() : nodes_(1, make_ac_node()), built_(false) {}
void AhoCorasick::add_pattern(const std::string& pat) {
    int cur = 0;
    for (char ch : pat) {
        int c = ch - 'a';
        if (c < 0 || c >= 26) continue;
        if (nodes_[cur].next[c] == -1) {
            nodes_[cur].next[c] = static_cast<int>(nodes_.size());
            nodes_.push_back(make_ac_node());
        }
        cur = nodes_[cur].next[c];
    }
    nodes_[cur].out_cnt += 1;
}
void AhoCorasick::build() {
    std::queue<int> q;
    for (int c = 0; c < 26; ++c) {
        if (nodes_[0].next[c] != -1) {
            q.push(nodes_[0].next[c]);
        } else {
            nodes_[0].next[c] = 0;
        }
    }
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        nodes_[u].out_cnt += nodes_[nodes_[u].fail].out_cnt;
        for (int c = 0; c < 26; ++c) {
            int v = nodes_[u].next[c];
            if (v != -1) {
                nodes_[v].fail = nodes_[nodes_[u].fail].next[c];
                q.push(v);
            } else {
                nodes_[u].next[c] = nodes_[nodes_[u].fail].next[c];
            }
        }
    }
    built_ = true;
}
int AhoCorasick::count_matches(const std::string& text) const {
    if (!built_) return -1;
    int cur = 0, total = 0;
    for (char ch : text) {
        int c = ch - 'a';
        if (c < 0 || c >= 26) {
            cur = 0;
            continue;
        }
        cur = nodes_[cur].next[c];
        total += nodes_[cur].out_cnt;
    }
    return total;
}

} // namespace codes_aho_corasick_dfa_d60
