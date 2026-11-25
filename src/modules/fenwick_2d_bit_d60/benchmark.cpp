#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_fenwick_2d_bit_d60;
    Fenwick2D bit(32, 32);
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        bit.add(iter & 31, (iter * 7) & 31, 1);
    sink = sink + bit.rect_sum(4, 4, 24, 24);
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "fenwick_2d_bit_d60 us=" << us << " sink=" << sink << "\n";
    return 0;
}
