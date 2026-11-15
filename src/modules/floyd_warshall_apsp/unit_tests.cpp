#include "interface.hpp"
#include <cassert>
#include <cmath>
#include <limits>

int main() {
    using namespace codes_floyd_warshall_apsp;
    const double INF = std::numeric_limits<double>::infinity();
    // 4-vertex directed graph with negative edge weights, zero negative cycles
    std::vector<double> w = {
        0,   3,  8, -4,
        INF, 0, INF, 5,
        INF, 4,  0, INF,
        6, INF, -5, 0
    };
    auto r = solve_apsp(4, w);
    assert(!r.has_negative_cycle);
    // 0->3 (-4) -> 2 (-5) = -9; 0->3->2->1 = -5
    assert(std::abs(r.dist[0 * 4 + 2] - (-9.0)) < 1e-9);
    assert(std::abs(r.dist[0 * 4 + 1] - (-5.0)) < 1e-9);
    assert((reconstruct_path(r, 0, 1) == std::vector<int>{0, 3, 2, 1}));
    assert(verify_triangle_inequality(r) == Status::Ok);
    return 0;
}
