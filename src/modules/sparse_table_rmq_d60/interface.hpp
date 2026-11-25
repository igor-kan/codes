#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_sparse_table_rmq_d60 {
class SparseTableRmq {
    int n_;
    std::vector<int> lg_;
    std::vector<std::vector<std::int64_t>> st_;
public:
    explicit SparseTableRmq(const std::vector<std::int64_t>& vals);
    std::int64_t query(int l, int r) const;
};

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_sparse_table_rmq_d60
