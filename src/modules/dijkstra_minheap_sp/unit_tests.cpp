#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_dijkstra_minheap_sp;
    validate_problem_size(1);
    std::vector<std::vector<std::pair<int, long long>>> g(4);
    g[0] = {{1, 4}, {2, 1}};
    g[2] = {{1, 2}, {3, 5}};
    g[1] = {{3, 1}};
    auto d = dijkstra_distances(4, 0, g);
    assert(d[0] == 0 && d[1] == 3 && d[2] == 1 && d[3] == 4);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
