#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_bellman_ford_spfa;
    std::vector<std::vector<Edge>> g(5);
    g[0].push_back({1, 6}); g[0].push_back({2, 7});
    g[1].push_back({3, 5}); g[1].push_back({4, -4});
    g[2].push_back({3, -3}); g[3].push_back({1, -2});
    g[4].push_back({3, 7});
    auto r1 = solve_bellman_ford(5, g, 0);
    auto r2 = solve_spfa(5, g, 0);
    auto r3 = solve_spfa_slf(5, g, 0);
    assert(!r1.negative_cycle && r1.dist == r2.dist && r2.dist == r3.dist);
    assert(std::abs(r1.dist[1] - 2.0) < 1e-9 && std::abs(r1.dist[4] - (-2.0)) < 1e-9);
    assert(verify_optimality(g, r1) == Status::Ok);
    return 0;
}
