#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_zkw_segment_iter_cpp;
    validate_problem_size(1);
    ZkwSegTree st(6);
    for (int i = 0; i < 6; ++i) st.point_set(i, (i + 1) * 10);
    assert(st.range_sum(1, 4) == 140 && st.range_sum(0, 5) == 210);
    st.point_set(2, 100);
    assert(st.range_sum(1, 4) == 210);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
