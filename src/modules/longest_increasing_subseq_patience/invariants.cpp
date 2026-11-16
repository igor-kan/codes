#include "interface.hpp"
#include <algorithm>

namespace codes_longest_increasing_subseq_patience {
Status verify_lis_invariants(const std::vector<int64_t>& seq, const LisResult& res) {
    if (seq.empty()) return res.indices.empty() ? Status::Ok : Status::InvariantViolation;
    if (res.indices.size() != res.values.size() || res.indices.empty()) return Status::InvariantViolation;
    for (std::size_t i = 0; i < res.indices.size(); ++i) {
        if (res.indices[i] >= seq.size() || seq[res.indices[i]] != res.values[i]) return Status::InvariantViolation;
        if (i > 0 && (res.indices[i] <= res.indices[i - 1] || res.values[i] <= res.values[i - 1])) {
            return Status::InvariantViolation;
        }
    }
    std::vector<std::size_t> dp(seq.size(), 1);
    std::size_t best = 1;
    for (std::size_t i = 0; i < seq.size(); ++i) {
        for (std::size_t j = 0; j < i; ++j) {
            if (seq[j] < seq[i]) dp[i] = std::max(dp[i], dp[j] + 1);
        }
        best = std::max(best, dp[i]);
    }
    if (best != res.indices.size()) return Status::InvariantViolation;
    return Status::Ok;
}
} // namespace codes_longest_increasing_subseq_patience
