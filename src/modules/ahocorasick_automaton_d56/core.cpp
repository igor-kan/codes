#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_ahocorasick_automaton_d56 {

int ac_count_matches(const std::vector<std::string>& patterns, const std::string& text) {
    auto hits = ac_per_pattern_hits(patterns, text);
    int total = 0;
    for (int h : hits) total += h;
    return total;
}

std::vector<int> ac_per_pattern_hits(const std::vector<std::string>& patterns, const std::string& text) {
    struct Node {
        int next[26];
        int fail = 0;
        std::vector<int> out;
        Node() { for (int i = 0; i < 26; ++i) next[i] = -1; }
    };
    std::vector<Node> trie(1);
    for (int pid = 0; pid < static_cast<int>(patterns.size()); ++pid) {
        int cur = 0;
        for (char ch : patterns[pid]) {
            if (ch < 'a' || ch > 'z') throw std::invalid_argument("lowercase ascii only");
            int c = ch - 'a';
            if (trie[cur].next[c] < 0) {
                trie[cur].next[c] = static_cast<int>(trie.size());
                trie.emplace_back();
            }
            cur = trie[cur].next[c];
        }
        trie[cur].out.push_back(pid);
    }
    std::vector<int> q;
    for (int c = 0; c < 26; ++c) {
        int nxt = trie[0].next[c];
        if (nxt >= 0) {
            trie[nxt].fail = 0;
            q.push_back(nxt);
        } else {
            trie[0].next[c] = 0;
        }
    }
    for (std::size_t qi = 0; qi < q.size(); ++qi) {
        int u = q[qi];
        for (int c = 0; c < 26; ++c) {
            int v = trie[u].next[c];
            if (v >= 0) {
                int f = trie[trie[u].fail].next[c];
                trie[v].fail = f;
                for (int pid : trie[f].out) trie[v].out.push_back(pid);
                q.push_back(v);
            } else {
                trie[u].next[c] = trie[trie[u].fail].next[c];
            }
        }
    }
    std::vector<int> hits(patterns.size(), 0);
    int cur = 0;
    for (char ch : text) {
        if (ch < 'a' || ch > 'z') {
            cur = 0;
            continue;
        }
        cur = trie[cur].next[ch - 'a'];
        for (int pid : trie[cur].out) ++hits[pid];
    }
    return hits;
}

} // namespace codes_ahocorasick_automaton_d56
