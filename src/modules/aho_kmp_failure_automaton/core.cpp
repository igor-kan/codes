#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_aho_kmp_failure_automaton {

DfaMatchSummary scan_ac_dfa(const std::vector<std::string>& pats, const std::string& text) {
    struct Node { int nxt[26]; int fail = 0; int out = 0; Node() { std::fill(std::begin(nxt), std::end(nxt), -1); } };
    std::vector<Node> tr(1);
    for (const auto& p : pats) {
        int u = 0;
        for (char ch : p) {
            int c = ch - 'a';
            if (tr[u].nxt[c] == -1) { tr[u].nxt[c] = static_cast<int>(tr.size()); tr.emplace_back(); }
            u = tr[u].nxt[c];
        }
        ++tr[u].out;
    }
    std::queue<int> q;
    for (int c = 0; c < 26; ++c) {
        if (tr[0].nxt[c] != -1) q.push(tr[0].nxt[c]);
        else tr[0].nxt[c] = 0;
    }
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int c = 0; c < 26; ++c) {
            int v = tr[u].nxt[c];
            if (v != -1) {
                tr[v].fail = tr[tr[u].fail].nxt[c];
                tr[v].out += tr[tr[v].fail].out;
                q.push(v);
            } else {
                tr[u].nxt[c] = tr[tr[u].fail].nxt[c];
            }
        }
    }
    int cur = 0; std::int64_t hits = 0;
    for (char ch : text) { cur = tr[cur].nxt[ch - 'a']; hits += tr[cur].out; }
    return {static_cast<int>(tr.size()), hits};
}

} // namespace codes_aho_kmp_failure_automaton
