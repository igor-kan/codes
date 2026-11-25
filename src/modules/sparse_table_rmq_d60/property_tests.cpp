#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_sparse_table_rmq_d60;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    std::vector<std::int64_t> a = {14, 9, 22, 4, 17, 6, 11, 2, 19};
    SparseTableRmq st(a);
    for (int l = 0; l < 9; ++l) {
        std::int64_t mn = a[l];
        for (int r = l; r < 9; ++r) {
            mn = std::min(mn, a[r]);
            assert(st.query(l, r) == mn);
        }
    }
    return 0;
}
