#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_edmonds_karp_flow_d57;
    std::vector<FlowEdgeSpec> b_es = {{0,1,8},{0,2,6},{1,3,5},{2,3,9}};
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        sink += edmonds_karp_maxflow(4, 0, 3, b_es);
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "edmonds_karp_flow_d57 us=" << us << " sink=" << sink << "\n";
    return 0;
}
