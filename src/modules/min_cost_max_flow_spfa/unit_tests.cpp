#include "interface.hpp"
#include <cassert>

int main() {
    using namespace codes_min_cost_max_flow_spfa;
    std::vector<FlowArc> arcs = {
        {0, 1, 2, 1}, {0, 2, 2, 5}, {1, 2, 1, 1}, {1, 3, 1, 4}, {2, 3, 3, 1}
    };
    auto r1 = solve_mcmf_spfa(4, 0, 3, arcs);
    auto r2 = solve_mcmf_potentials(4, 0, 3, arcs);
    assert(r1.total_flow == 4 && r2.total_flow == 4);
    assert(r1.total_cost == r2.total_cost && r1.total_cost == 20);
    assert(verify_flow_invariants(4, 0, 3, arcs, r1) == Status::Ok);
    assert(verify_flow_invariants(4, 0, 3, arcs, r2) == Status::Ok);
    return 0;
}
