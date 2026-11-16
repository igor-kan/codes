#include "interface.hpp"
#include <algorithm>

namespace codes_longest_increasing_subseq_patience {
LisResult compute_lis_patience(const std::vector<int64_t>& seq) {
    LisResult out;
    if (seq.empty()) return out;
    const std::size_t n = seq.size();
    std::vector<int64_t> tail_vals;
    std::vector<std::size_t> tail_idx;
    std::vector<std::size_t> prev(n, n);
    for (std::size_t i = 0; i < n; ++i) {
        auto it = std::lower_bound(tail_vals.begin(), tail_vals.end(), seq[i]);
        std::size_t pos = static_cast<std::size_t>(it - tail_vals.begin());
        if (pos == tail_vals.size()) {
            tail_vals.push_back(seq[i]);
            tail_idx.push_back(i);
        } else {
            tail_vals[pos] = seq[i];
            tail_idx[pos] = i;
        }
        if (pos > 0) prev[i] = tail_idx[pos - 1];
    }
    std::size_t cur = tail_idx.back();
    while (cur != n) {
        out.indices.push_back(cur);
        out.values.push_back(seq[cur]);
        cur = prev[cur];
    }
    std::reverse(out.indices.begin(), out.indices.end());
    std::reverse(out.values.begin(), out.values.end());
    return out;
}
} // namespace codes_longest_increasing_subseq_patience
