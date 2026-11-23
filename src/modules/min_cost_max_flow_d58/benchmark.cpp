#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_min_cost_max_flow_d58;
    std::vector<CostArc> barcs = {{0,1,3,2},{1,2,2,4}};
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        sink += min_cost_max_flow(3, 0, 2, barcs).second;
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "min_cost_max_flow_d58 us=" << us << " sink=" << sink << "\n";
    return 0;
}
