#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_dsu_bipartite_parity_d59;
    validate_problem_size(1);
    BipartiteDsu dsu(4);
    assert(dsu.add_edge(0, 1) && dsu.add_edge(1, 2) && dsu.add_edge(2, 3) && dsu.add_edge(3, 0));
    assert(!dsu.add_edge(0, 2));
    verify_module_postcondition(true, "unit ok");
    return 0;
}
