#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_bellman_ford_spfa_d57;
    std::vector<DirWeightedEdge> b_es = {{0, 1, 3}, {1, 2, -1}, {2, 3, 2}};
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        sink += bellman_ford_solve(4, 0, b_es).second[3];
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "bellman_ford_spfa_d57 us=" << us << " sink=" << sink << "\n";
    return 0;
}
