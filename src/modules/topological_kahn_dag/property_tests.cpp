#include "interface.hpp"
#include <cassert>

int main() {
    using namespace codes_topological_kahn_dag;
    std::vector<std::vector<std::size_t>> chain(50);
    for (std::size_t i = 0; i < 49; ++i) chain[i].push_back(i + 1);
    auto r = kahn_sort(50, chain);
    assert(r.is_dag && verify_topological_order(50, chain, r) == Status::Ok);
    return 0;
}
