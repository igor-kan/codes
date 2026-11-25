#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_sparse_table_rmq_d60;
    validate_problem_size(1);
    SparseTableRmq st({5, 2, 8, 1, 9, 3, 7});
    assert(st.query(0, 2) == 2);
    assert(st.query(2, 6) == 1);
    assert(st.query(4, 6) == 3);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
