#include "interface.hpp"
#include <cassert>

int main() {
    using namespace codes_kosaraju_two_pass_scc;
    std::vector<std::vector<std::size_t>> g(6);
    g[0] = {1}; g[1] = {2}; g[2] = {0, 3}; // SCC {0,1,2}
    g[3] = {4}; g[4] = {5}; g[5] = {3};    // SCC {3,4,5}
    auto res = find_scc(6, g);
    assert(res.num_components == 2);
    assert(res.comp_id[0] == res.comp_id[1] && res.comp_id[1] == res.comp_id[2]);
    assert(res.comp_id[3] == res.comp_id[4] && res.comp_id[4] == res.comp_id[5]);
    assert(res.comp_id[0] < res.comp_id[3]);
    assert(verify_condensation_dag(6, g, res) == Status::Ok);
    return 0;
}
