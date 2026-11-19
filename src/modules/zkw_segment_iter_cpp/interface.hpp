#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_zkw_segment_iter_cpp {
class ZkwSegTree {
public:
    explicit ZkwSegTree(int n);
    void point_set(int idx, std::int64_t val);
    std::int64_t range_sum(int l, int r) const;
private:
    int base_;
    std::vector<std::int64_t> tree_;
};

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_zkw_segment_iter_cpp
