#include "interface.hpp"
#include <algorithm>

namespace codes_z_algorithm_lcp {
std::vector<std::size_t> compute_z_array(const std::string& s) {
    const std::size_t n = s.size();
    std::vector<std::size_t> z(n, 0);
    if (n == 0) return z;
    z[0] = n;
    std::size_t l = 0, r = 0;
    for (std::size_t i = 1; i < n; ++i) {
        if (i < r) {
            z[i] = std::min(r - i, z[i - l]);
        }
        while (i + z[i] < n && s[z[i]] == s[i + z[i]]) {
            ++z[i];
        }
        if (i + z[i] > r) {
            l = i;
            r = i + z[i];
        }
    }
    return z;
}

std::vector<std::size_t> find_matches(const std::string& text, const std::string& pattern) {
    std::vector<std::size_t> matches;
    if (pattern.empty() || text.size() < pattern.size()) return matches;
    std::string sep;
    sep.reserve(pattern.size() + 1 + text.size());
    sep.append(pattern);
    sep.push_back('\x01');
    sep.append(text);
    const auto z = compute_z_array(sep);
    const std::size_t plen = pattern.size();
    for (std::size_t i = plen + 1; i < sep.size(); ++i) {
        if (z[i] == plen) matches.push_back(i - plen - 1);
    }
    return matches;
}
} // namespace codes_z_algorithm_lcp
