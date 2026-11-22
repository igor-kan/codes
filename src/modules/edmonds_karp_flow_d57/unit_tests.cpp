#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_edmonds_karp_flow_d57;
    validate_problem_size(1);
    std::vector<FlowEdgeSpec> es = {{0,1,16},{0,2,13},{1,2,10},{2,1,4},{1,3,12},{2,4,14},{3,2,9},{3,5,20},{4,3,7},{4,5,4}};
    assert(edmonds_karp_maxflow(6, 0, 5, es) == 23);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
