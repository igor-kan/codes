#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_sparse_table_rmq_o1 {
struct SparseTable {
    std::size_t n = 0;
    std::vector<std::size_t> lg2;
    std::vector<std::vector<int64_t>> st;
};
} // namespace codes_sparse_table_rmq_o1
