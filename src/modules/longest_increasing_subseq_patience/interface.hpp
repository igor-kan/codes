#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_longest_increasing_subseq_patience {
LisResult compute_lis_patience(const std::vector<int64_t>& seq);
Status validate_sequence(const std::vector<int64_t>& seq);
std::size_t compute_lis_length_fast(const std::vector<int64_t>& seq);
std::vector<LisResult> batch_lis(const std::vector<std::vector<int64_t>>& seqs);
Status verify_lis_invariants(const std::vector<int64_t>& seq, const LisResult& res);
} // namespace codes_longest_increasing_subseq_patience
