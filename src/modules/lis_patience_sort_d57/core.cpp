#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_lis_patience_sort_d57 {

int patience_lis_length(const std::vector<long long>& xs) {
    std::vector<long long> tails;
    tails.reserve(xs.size());
    for (long long x : xs) {
        auto it = std::lower_bound(tails.begin(), tails.end(), x);
        if (it == tails.end()) tails.push_back(x);
        else *it = x;
    }
    return static_cast<int>(tails.size());
}

} // namespace codes_lis_patience_sort_d57
