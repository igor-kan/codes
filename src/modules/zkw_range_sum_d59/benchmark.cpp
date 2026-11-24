#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_zkw_range_sum_d59;
    ZkwSumTree b_z(16); for (int i = 0; i < 16; ++i) b_z.add(i, 2);
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        sink += b_z.sum(2, 13);
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "zkw_range_sum_d59 us=" << us << " sink=" << sink << "\n";
    return 0;
}
