#include "interface.hpp"

namespace codes_sparse_table_rmq_o1 {
Status validate_query(const SparseTable& tab, std::size_t l, std::size_t r) {
    if (tab.n == 0) return Status::NullOrEmpty;
    if (l > r || r >= tab.n) return Status::OutOfBounds;
    return Status::Ok;
}
} // namespace codes_sparse_table_rmq_o1
