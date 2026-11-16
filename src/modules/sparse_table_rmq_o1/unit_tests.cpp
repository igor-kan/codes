#include "interface.hpp"
#include <cassert>

int main() {
    using namespace codes_sparse_table_rmq_o1;
    std::vector<int64_t> a = {7, 2, 3, 0, 5, 10, 3, 12, 18, -4, 9};
    auto tab = build_sparse_table(a);
    assert(query_rmq_o1(tab, 0, 4) == 0);
    assert(query_rmq_o1(tab, 4, 7) == 3);
    assert(query_rmq_o1(tab, 0, 10) == -4);
    assert(verify_table_invariants(tab, a) == Status::Ok);
    return 0;
}
