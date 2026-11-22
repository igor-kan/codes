#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_rabin_karp_rolling_d57 {

std::vector<int> rabin_karp_search(const std::string& text, const std::string& pat) {
    if (pat.empty()) throw std::invalid_argument("empty pattern");
    int n = static_cast<int>(text.size()), m = static_cast<int>(pat.size());
    std::vector<int> hits;
    if (m > n) return hits;
    const long long M1 = 1000000007LL, M2 = 1000000009LL;
    const long long B1 = 313LL, B2 = 317LL;
    long long p1 = 1, p2 = 1;
    for (int i = 0; i < m - 1; ++i) { p1 = (p1 * B1) % M1; p2 = (p2 * B2) % M2; }
    long long ph1 = 0, ph2 = 0, th1 = 0, th2 = 0;
    for (int i = 0; i < m; ++i) {
        unsigned char pc = static_cast<unsigned char>(pat[i]);
        unsigned char tc = static_cast<unsigned char>(text[i]);
        ph1 = (ph1 * B1 + pc) % M1; ph2 = (ph2 * B2 + pc) % M2;
        th1 = (th1 * B1 + tc) % M1; th2 = (th2 * B2 + tc) % M2;
    }
    for (int i = 0; i <= n - m; ++i) {
        if (th1 == ph1 && th2 == ph2 && text.compare(i, m, pat) == 0) hits.push_back(i);
        if (i < n - m) {
            unsigned char outc = static_cast<unsigned char>(text[i]);
            unsigned char inc = static_cast<unsigned char>(text[i + m]);
            th1 = ((th1 - outc * p1 % M1 + M1) * B1 + inc) % M1;
            th2 = ((th2 - outc * p2 % M2 + M2) * B2 + inc) % M2;
        }
    }
    return hits;
}

} // namespace codes_rabin_karp_rolling_d57
