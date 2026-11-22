#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_bellman_ford_spfa_d57;
    validate_problem_size(1);
    std::vector<DirWeightedEdge> es = {{0, 1, 5}, {0, 2, 4}, {1, 3, -3}, {2, 1, -2}, {2, 3, 4}};
    auto [neg, dist] = bellman_ford_solve(4, 0, es);
    assert(!neg && dist[1] == 2 && dist[3] == -1);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
