#include "interface.hpp"
#include <cassert>

int main() {
    using namespace codes_kosaraju_two_pass_scc;
    // Complete DAG must yield n singleton SCCs in exact topological order
    std::vector<std::vector<std::size_t>> dag(12);
    for (std::size_t u = 0; u < 12; ++u) for (std::size_t v = u + 1; v < 12; ++v) dag[u].push_back(v);
    auto r = find_scc(12, dag);
    assert(r.num_components == 12);
    assert(verify_condensation_dag(12, dag, r) == Status::Ok);
    return 0;
}
