#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_manacher_palindrome_radii {

std::string manacher_longest_palindrome(const std::string& s) {
    if (s.empty()) return "";
    int m = static_cast<int>(s.size()) * 2 + 1;
    std::vector<int> p(m, 0);
    auto char_at = [&](int idx) -> char {
        return (idx & 1) ? s[idx >> 1] : '';
    };
    int center = 0;
    int right = 0;
    int best_center = 0;
    int best_rad = 0;
    for (int i = 0; i < m; ++i) {
        int mirror = 2 * center - i;
        if (i < right) p[i] = std::min(right - i, p[mirror]);
        while (i - p[i] - 1 >= 0 && i + p[i] + 1 < m && char_at(i - p[i] - 1) == char_at(i + p[i] + 1)) {
            ++p[i];
        }
        if (i + p[i] > right) {
            center = i;
            right = i + p[i];
        }
        if (p[i] > best_rad) {
            best_rad = p[i];
            best_center = i;
        }
    }
    int start = (best_center - best_rad) / 2;
    return s.substr(start, best_rad);
}

} // namespace codes_manacher_palindrome_radii
