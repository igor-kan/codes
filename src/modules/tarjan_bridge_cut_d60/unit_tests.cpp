#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_tarjan_bridge_cut_d60;
    validate_problem_size(1);
    std::vector<GraphEdge> es = {{0,1},{1,2},{2,0},{1,3},{3,4},{4,5},{5,3}};
    auto r = find_bridges_and_cuts(6, es);
    assert(r.bridges.size() == 1 && r.bridges[0].u == 1 && r.bridges[0].v == 3);
    assert(r.cut_vertices.size() == 2);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
