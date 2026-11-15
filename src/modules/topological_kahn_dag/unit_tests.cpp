#include "interface.hpp"
#include <cassert>

int main() {
    using namespace codes_topological_kahn_dag;
    std::vector<std::vector<std::size_t>> g(4);
    g[3] = {1}; g[2] = {0}; g[1] = {0};
    auto r = kahn_lex_min(4, g);
    assert(r.is_dag);
    assert((r.order == std::vector<std::size_t>{2, 3, 1, 0}));
    assert(verify_topological_order(4, g, r) == Status::Ok);
    g[0].push_back(3); // Introduce cycle 3->1->0->3
    assert(!kahn_sort(4, g).is_dag);
    return 0;
}
