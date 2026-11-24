#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_dsu_bipartite_parity_d59;
    BipartiteDsu b_dsu(8);
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        b_dsu.add_edge(0, 1); sink += b_dsu.is_bipartite() ? 1 : 0;
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "dsu_bipartite_parity_d59 us=" << us << " sink=" << sink << "\n";
    return 0;
}
