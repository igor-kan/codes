#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_dinic_scaling_maxflow;
    int n = 4;
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        ScalingDinic g(n); g.add_edge(0,1,10); g.add_edge(1,3,10); sink += g.max_flow(0,3);
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "dinic_scaling_maxflow us=" << us << " sink=" << sink << "\n";
    return 0;
}
