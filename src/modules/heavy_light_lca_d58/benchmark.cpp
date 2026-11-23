#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_heavy_light_lca_d58;
    BinaryLiftLca b_bl(5, 0, {{0,1},{1,2},{2,3},{3,4}});
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        sink += b_bl.dist(1, 4);
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "heavy_light_lca_d58 us=" << us << " sink=" << sink << "\n";
    return 0;
}
