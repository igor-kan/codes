#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_zkw_range_sum_d59 {
class ZkwSumTree {
public:
    explicit ZkwSumTree(int n);
    void add(int idx, long long delta);
    long long sum(int l, int r) const;
private:
    int n_;
    std::vector<long long> t_;
};

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_zkw_range_sum_d59
