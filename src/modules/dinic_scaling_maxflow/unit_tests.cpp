#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_dinic_scaling_maxflow;
    validate_problem_size(1);
    ScalingDinic g(4);
    g.add_edge(0, 1, 1000); g.add_edge(0, 2, 1000);
    g.add_edge(1, 2, 1);    g.add_edge(1, 3, 1000);
    g.add_edge(2, 3, 1000);
    assert(g.max_flow(0, 3) == 2000);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
