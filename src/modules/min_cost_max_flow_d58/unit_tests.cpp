#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_min_cost_max_flow_d58;
    validate_problem_size(1);
    std::vector<CostArc> arcs = {{0,1,2,1},{0,2,2,5},{1,3,1,2},{1,2,1,1},{2,3,3,2}};
    auto [fl, cs] = min_cost_max_flow(4, 0, 3, arcs);
    assert(fl == 4 && cs == 21);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
