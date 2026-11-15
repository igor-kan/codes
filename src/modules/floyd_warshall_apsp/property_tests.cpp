#include "interface.hpp"
#include <cassert>
#include <cmath>
#include <limits>

int main() {
    using namespace codes_floyd_warshall_apsp;
    const double INF = std::numeric_limits<double>::infinity();
    std::vector<double> cyc = {0, 1, INF, INF, 0, -2, -1, INF, 0}; // 0->1->2->0 = -2 cycle!
    auto r = solve_apsp(3, cyc);
    assert(r.has_negative_cycle);
    std::vector<double> pos = {0, 2, 9, 4, 0, 1, 7, 3, 0};
    auto rp = solve_apsp(3, pos);
    auto rf = solve_apsp_blocked(3, pos);
    assert(rp.dist == rf.dist && batch_verify_paths(rp) == Status::Ok);
    return 0;
}
