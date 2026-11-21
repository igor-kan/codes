#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_sliding_window_deque_extrema {

std::vector<long long> sliding_window_max(const std::vector<long long>& xs, int k) {
    if (k <= 0 || k > static_cast<int>(xs.size())) throw std::invalid_argument("invalid window size");
    std::deque<int> dq;
    std::vector<long long> out;
    out.reserve(xs.size() - k + 1);
    for (int i = 0; i < static_cast<int>(xs.size()); ++i) {
        if (!dq.empty() && dq.front() <= i - k) dq.pop_front();
        while (!dq.empty() && xs[dq.back()] <= xs[i]) dq.pop_back();
        dq.push_back(i);
        if (i >= k - 1) out.push_back(xs[dq.front()]);
    }
    return out;
}

std::vector<long long> sliding_window_min(const std::vector<long long>& xs, int k) {
    if (k <= 0 || k > static_cast<int>(xs.size())) throw std::invalid_argument("invalid window size");
    std::deque<int> dq;
    std::vector<long long> out;
    out.reserve(xs.size() - k + 1);
    for (int i = 0; i < static_cast<int>(xs.size()); ++i) {
        if (!dq.empty() && dq.front() <= i - k) dq.pop_front();
        while (!dq.empty() && xs[dq.back()] >= xs[i]) dq.pop_back();
        dq.push_back(i);
        if (i >= k - 1) out.push_back(xs[dq.front()]);
    }
    return out;
}

} // namespace codes_sliding_window_deque_extrema
