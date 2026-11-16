#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_sparse_table_rmq_o1 {
SparseTable build_sparse_table(const std::vector<int64_t>& arr);
int64_t query_rmq_o1(const SparseTable& tab, std::size_t l, std::size_t r);
Status validate_query(const SparseTable& tab, std::size_t l, std::size_t r);
std::vector<int64_t> batch_query_rmq(const SparseTable& tab, const std::vector<std::pair<std::size_t, std::size_t>>& queries);
Status verify_table_invariants(const SparseTable& tab, const std::vector<int64_t>& arr);
} // namespace codes_sparse_table_rmq_o1
