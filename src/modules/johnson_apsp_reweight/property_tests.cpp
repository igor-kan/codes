#include "interface.hpp"
#include <cassert>

int main() {
    using namespace codes_johnson_apsp_reweight;
    std::vector<std::vector<WEdge>> g(3);
    g[0].push_back({1, 2}); g[1].push_back({2, -5}); g[2].push_back({0, 1});
    auto r = solve_johnson(3, g);
    assert(r.has_negative_cycle);
    return 0;
}
