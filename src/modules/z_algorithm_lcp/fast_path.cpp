#include "interface.hpp"
#include <algorithm>

namespace codes_z_algorithm_lcp {
std::vector<std::size_t> compute_z_fast(const std::string& s) {
    const std::size_t n = s.size();
    std::vector<std::size_t> z(n, 0);
    if (n == 0) return z;
    z[0] = n;
    const char* p = s.data();
    std::size_t l = 0, r = 0;
    for (std::size_t i = 1; i < n; ++i) {
        std::size_t k = (i < r) ? std::min(r - i, z[i - l]) : 0;
        while (i + k < n && p[k] == p[i + k]) ++k;
        z[i] = k;
        if (i + k > r) { l = i; r = i + k; }
    }
    return z;
}
} // namespace codes_z_algorithm_lcp
