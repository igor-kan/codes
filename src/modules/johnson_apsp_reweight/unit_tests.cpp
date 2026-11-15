#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_johnson_apsp_reweight;
    std::vector<std::vector<WEdge>> g(4);
    g[0].push_back({1, 3}); g[0].push_back({3, -4});
    g[1].push_back({3, 5});
    g[2].push_back({1, 4});
    g[3].push_back({0, 6}); g[3].push_back({2, -5});
    auto r = solve_johnson(4, g);
    assert(!r.has_negative_cycle);
    assert(validate_reweighting(g, r.potentials) == Status::Ok);
    assert(verify_matrix_invariants(r) == Status::Ok);
    assert(std::abs(r.dist[0][2] - (-9.0)) < 1e-9);
    assert(std::abs(r.dist[0][1] - (-5.0)) < 1e-9);
    return 0;
}
