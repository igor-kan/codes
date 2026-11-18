#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_persistent_treap_split;
    validate_problem_size(1);
    PersistentTreap pt;
    int r0 = -1;
    for (int i = 1; i <= 5; ++i) r0 = pt.merge(r0, pt.new_node(i * 10, static_cast<std::uint32_t>(i * 2654435761u)));
    auto [a, b] = pt.split(r0, 2);
    int r1 = pt.merge(a, pt.merge(pt.new_node(99, 1234567u), b));
    assert(pt.range_sum(r0, 0, 4) == 150);
    assert(pt.range_sum(r1, 0, 5) == 249);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
