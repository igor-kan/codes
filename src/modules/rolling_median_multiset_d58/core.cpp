#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_rolling_median_multiset_d58 {

std::vector<long long> sliding_window_medians(const std::vector<long long>& xs, int k) {
    if (k <= 0 || k > static_cast<int>(xs.size())) throw std::invalid_argument("bad k");
    std::vector<long long> out;
    std::vector<long long> win(k);
    for (int i = 0; i <= static_cast<int>(xs.size()) - k; ++i) {
        for (int j = 0; j < k; ++j) win[j] = xs[i + j];
        std::nth_element(win.begin(), win.begin() + (k - 1) / 2, win.end());
        out.push_back(win[(k - 1) / 2]);
    }
    return out;
}

} // namespace codes_rolling_median_multiset_d58
