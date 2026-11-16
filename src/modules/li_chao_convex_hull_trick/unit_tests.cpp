#include "interface.hpp"
#include <cassert>

int main() {
    using namespace codes_li_chao_convex_hull_trick;
    auto t = make_lichao_tree(-100, 100);
    assert(insert_line(t, {2, 10}) == Status::Ok);
    assert(insert_line(t, {-3, 25}) == Status::Ok);
    assert(insert_line(t, {0, 12}) == Status::Ok);
    assert(query_min(t, -10) == -10);
    assert(query_min(t, 0) == 10);
    assert(query_min(t, 10) == -5);
    assert(verify_lichao_oracle(t, {-50, -10, 0, 5, 10, 50}) == Status::Ok);
    return 0;
}
