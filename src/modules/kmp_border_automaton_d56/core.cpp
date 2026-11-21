#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_kmp_border_automaton_d56 {

std::vector<int> kmp_prefix_function(const std::string& pat) {
    int n = static_cast<int>(pat.size());
    std::vector<int> pi(n, 0);
    for (int i = 1; i < n; ++i) {
        int j = pi[i - 1];
        while (j > 0 && pat[i] != pat[j]) j = pi[j - 1];
        if (pat[i] == pat[j]) ++j;
        pi[i] = j;
    }
    return pi;
}

std::vector<int> kmp_find_all(const std::string& text, const std::string& pat) {
    if (pat.empty()) throw std::invalid_argument("empty pattern");
    auto pi = kmp_prefix_function(pat);
    std::vector<int> hits;
    int j = 0;
    int m = static_cast<int>(pat.size());
    for (int i = 0; i < static_cast<int>(text.size()); ++i) {
        while (j > 0 && text[i] != pat[j]) j = pi[j - 1];
        if (text[i] == pat[j]) ++j;
        if (j == m) {
            hits.push_back(i - m + 1);
            j = pi[j - 1];
        }
    }
    return hits;
}

} // namespace codes_kmp_border_automaton_d56
