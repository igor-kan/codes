#include "interface.hpp"
#include <cassert>

int main() {
    using namespace codes_link_cut_tree_splay;
    LinkCutTree lct(6);
    for (int i = 0; i < 6; ++i) lct.set_value(i, (i + 1) * 10);
    assert(lct.link(0, 1));
    assert(lct.link(1, 2));
    assert(lct.link(2, 3));
    assert(lct.link(2, 4));
    assert(!lct.link(0, 3));
    assert(lct.query_path_sum(0, 4) == 10 + 20 + 30 + 50);
    assert(lct.query_path_max(0, 3) == 40);
    assert(lct.cut(1, 2));
    assert(!lct.connected(0, 4));
    assert(lct.link(1, 5));
    assert(lct.query_path_sum(0, 5) == 10 + 20 + 60);
    verify_lct_invariants(lct);
    return 0;
}
