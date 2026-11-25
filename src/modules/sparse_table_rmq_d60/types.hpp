#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_sparse_table_rmq_d60 {
struct RmqRange {
    int l;
    int r;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "sparse_table_rmq_d60";
    int version = 1;
};
} // namespace codes_sparse_table_rmq_d60
