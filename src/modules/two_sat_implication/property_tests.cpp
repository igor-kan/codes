#include "interface.hpp"
#include <cassert>

int main() {
    using namespace codes_two_sat_implication;
    std::vector<Clause2> c1 = {{0,false,1,false},{0,true,2,false},{1,true,2,true}};
    std::vector<Clause2> c2 = {{0,false,0,false},{0,true,0,true}};
    auto res = parallel_solve_instances({{3, c1}, {2, c2}});
    assert(res[0].satisfiable);
    assert(!res[1].satisfiable);
    verify_sat_witness(3, c1, res[0]);
    return 0;
}
