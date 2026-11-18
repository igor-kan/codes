#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_directed_mst_chu_liu;
    validate_problem_size(1);
    std::vector<DirEdge> es = {{0,1,10},{0,2,20},{1,2,2},{2,1,3},{1,3,15},{2,3,4}};
    assert(edmonds_directed_mst(4, 0, es) == 16);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
