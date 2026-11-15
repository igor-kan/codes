#include "interface.hpp"
#include <cassert>

int main() {
    using namespace codes_bellman_ford_spfa;
    std::vector<std::vector<Edge>> cyc(3);
    cyc[0].push_back({1, 1}); cyc[1].push_back({2, -2}); cyc[2].push_back({0, -1});
    assert(solve_bellman_ford(3, cyc, 0).negative_cycle);
    assert(solve_spfa(3, cyc, 0).negative_cycle);
    return 0;
}
